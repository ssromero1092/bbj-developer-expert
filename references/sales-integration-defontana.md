# Integración DAIRE -> Defontana (factura de venta)

Fuentes: `daire\metacaracter\pgms\PRO240.bbj`, `daire\api\integracion.bbj`, `daire\api\DAIRE_ERP.bbj`, `daire\api\DAIRE_ERP_LOGIN.bbj`.
BBj **no habla con Defontana directo**: llama a un intermediario Node (`https://<host-del-servicio>/integracion/api/...`) que presumiblemente reenvía a Defontana. El contrato real del Node no está en estos archivos.

## Flujo
```
PRO240 (opción F -> E, 3600)
  3607  ESCAPE; IF SW_INTEGRACION_API=1 THEN 3640     (SW=1 solo si CODUSU$="0000", línea 0058)
  3640  GOSUB 9500
  9500  CALL "integracion.bbj",1,CLAVE$,APER$,NODOEMP$,TOKEN_API$,ESTADO_API,MENSAJE_API$
          solo procesa tipo 01 y 11 (9520)
integracion.bbj
  1000  lee VTAEFAC (encabezado) y MAEANAL (cliente)
  2000  arma payload JSON (detalle desde VTAGFAC, nombre producto desde MAELIST)
  0100  CALL "DAIRE_ERP.bbj",1,NF=1,payload_json$,data_api!,TOKEN_API$,statusCode,...
DAIRE_ERP.bbj
  si no hay token -> CALL "DAIRE_ERP_LOGIN.bbj"
  POST {base}/integracion/api/defontana/factura   headers: Dbname, Authorization: Bearer
DAIRE_ERP_LOGIN.bbj
  POST {base}/integracion/api/auth/login   body {username,password,numero_unico}
  token en data.token o token (org.json.JSONObject)
Vuelta: statusCode -> ESTADO_API ; body -> MENSAJE_API$ ; PRO240 3643-3645 marca ESTADO$="3" y VTATSII
```

## Códigos internos de integracion.bbj
| ESTADO_API | Significado |
|---|---|
| 996 | falló la llamada a DAIRE_ERP (8900) |
| 997 | factura sin detalle en VTAGFAC |
| 998 | factura no existe en VTAEFAC |
| 999 | cliente sin RUT o RUT inválido |
| otro | HTTP statusCode devuelto por el Node |

## Mapeo de campos
- Clave de factura: `CLAVE$` = empresa(2)+tipo(2)+folio(10) = 14 chars. `TIPO_DOC$=CLAVE$(3,2)`; tipo `11` se envía como `codigo_lh_tipo "08"` (1050).
- `numero_lh` = `CLAVE$` completa sin espacios (14 chars), no el folio de 10 dígitos. *Confirmar con el contrato del Node.*
- VTAEFAC (orden de lectura 1010 = orden de escritura PRO240 1410): clave, rut, fecha emisión, fecha venc., descuento, pago-ref, neto, exento, iva, total, condición pago, iva$, marca, tramo, ruta, bodega, saldo, estado, destino, moneda, sucursal, dólar, operador, caja, lista, clave NC, voucher, obs.
- VTAGFAC (2130 = PRO240 1520): clave+item, cantidad, producto, precio, fecha, centro, % dto, medida, retiro, fruta, cuenta, ítem.
- MAEANAL (1030): rut, nombre, dirección, ciudad, fono, rut válido, comuna, correo, atención, giro.
- Constantes enviadas: `vendedor/referencia/bodega/sucursal = null`, `flete/ila/impuesto_adicional/descuento = 0`, `es_servicio=false`, unidad vacía -> `"0303"`.
- RUT: se quitan puntos y guion y se reinserta guion antes del último dígito (3300).

## Hallazgos conocidos (revisión inicial)
Severidad según lectura estática; ninguno se ejecutó contra el servidor.

**Bloqueantes**
1. `PRO240 3643`: `IF ESTADO_API<>0` trata cualquier HTTP 200/201 como error; `integracion 0110` hace `ESTADO_API=statusCode`. En éxito nunca se marca `ESTADO$="3"` ni `VTATSII`.
2. `ESCAPE` activos: `PRO240 3607`, `integracion 0100, 1010, 2220`, `DAIRE_ERP` en `postFacturaVentaDefontana` (dos veces).
3. `integracion 3500`: escape JSON con `"\\\\"`/`"\\\""` (BBj no interpreta `\`) y `WHILE POS(CHR(92)/CHR(34)=ESC$)`: bucle infinito si un campo contiene `"` o `\`.
4. `integracion 2070`: `GOSUB 3200` sin asignar `NUM_IN` (y `TOTAL_NETO$` no se usa) -> variable sin inicializar.

**Altos**
5. `PRO240 9510/9520` retornan sin asignar `ESTADO_API`; 3643 lo evalúa -> error por variable no asignada para tipos distintos de 01/11.
6. Las ediciones de dirección/ciudad/mail/giro/comuna de PRO240 (3200-3570) y el modo "por observación" (OPCION=2) se pierden en la ruta API: `integracion` relee MAEANAL y no recibe `MATANA$` ni `OPCION`.
7. Credenciales y URL en el código (`DAIRE_ERP cargarConfigNode`, defaults de `DAIRE_ERP_LOGIN`): un usuario y una clave fijos (no se reproducen aqui). Además `logCurlRequest` imprime el Bearer y el payload completo.
8. Sin control de reenvío: no se revisa `ESTADO$="3"` antes de enviar; el usuario puede disparar dos veces.
9. Canales `VTAEFAC/VTAGFAC/MAEANAL/MAELIST` no se cierran en rutas de error (`GOTO 9000` salta el 0130).

**Medios / bajos**
10. Token se pide por cada factura (no se cachea) y no hay reintento ante 401. Mismatch `TOKEN_API$` ($) vs `token!` (!).
11. Respuesta del Node no se parsea: no se guarda folio/ID Defontana ni se valida `estado:false` con HTTP 200. PRO240 no muestra `MENSAJE_API$` al usuario.
12. Sin timeout explícito; la pantalla queda bloqueada si el Node no responde. *(verificar API de BBWebClient)*
13. Descuentos (`DESCUE`, `PORCDES$`) no viajan; `descuento:0` fijo. Tipos 04/12/18 redondean con `-0.5` en PRO240 pero la integración solo cubre 11.
14. Codificación: acentos/ñ en `setContent(String)` pueden depender del charset por defecto de la JVM. *(verificar)*
15. `PRINT "DEBUG_RUT_*"` (2050, 2052, 3340, 3430, 3450) y `DEBUG_NODE_*` en pantalla de caracteres.
16. Compuerta de pruebas hardcodeada (`CODUSU$="0000"`); definir bandera de ambiente antes de producción.

## Pendiente de confirmar con el usuario
- Contrato JSON exacto que espera el Node (¿`numero_lh` es 14 chars o el folio?, ¿qué devuelve en éxito?).
- Versión de BBj del servidor y si PRO240 corre en caracteres o GUI.
- ¿Defontana calcula el IVA (no se envía `TIVA`)?
