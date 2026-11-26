# Integracion de compras con un ERP externo (caso Defontana)

Caso real documentado a partir de un proyecto de produccion. Los nombres de proveedores, RUT, URLs y credenciales se omiten a proposito. Los nombres de programas (`CON214`, `ADQ160`, `defcomp`) se conservan como ejemplos de estructura.

Complementa a `sales-integration-defontana.md` (factura de venta). Aqui el flujo es de **lectura**: se traen las compras del ERP externo y se ingresan, una a una, al sistema de adquisiciones.

## Idea central: el listado vive en un archivo local
El servicio externo tarda entre 15 y 20 segundos por consulta. En vez de consultarlo cada vez que se abre un mes, el listado se guarda en un archivo MKEYED y la pantalla lo lee de ahi. Un boton "Actualizar" lo refresca. El servicio externo solo se consulta cuando falta un dato.

| Antes | Despues |
|---|---|
| Cada mes elegido consultaba al servicio externo | El mes sale del archivo local, sin espera |
| Sin conexion no se veia nada | Lo ya guardado se ve igual |
| El listado no recordaba que estaba ingresado | Cada compra lleva una marca de integracion, folio y mes |

## Arquitectura en tres capas
```
Pantalla (CON214)  ->  CALL defcomp.bbj, op N  ->  archivo MKEYED local (ADQEDEF)
        |                                              ^
        +-> consulta_*.bbj -> DAIRE_ERP.bbj -> servicio Node -> ERP externo
```
- **Una sola rutina concentra el acceso al archivo** (`defcomp.bbj`, con operaciones numeradas). Las pantallas no abren el archivo directamente.
- **Las consultas externas van aparte** (`consulta_compras.bbj`, `consulta_detalle_compra.bbj`, `consulta_pdf_compra.bbj`), con un interruptor de prueba (`STBL("!MOCK_COMPRAS")="1"`) que responde datos locales sin llamar al servicio.

## Operaciones del programa de acceso (patron "una rutina, N operaciones")
Firma: `CALL "defcomp.bbj",1,OP,DIRECTORIO$,REGS!,MARCAS!,IDX,ESTADO_API,MENSAJE_API$,DET$`.

| Op | Funcion |
|---|---|
| 1 | Sincroniza un mes: alta o actualizacion, sin pisar lo ya integrado |
| 3 | Guarda el detalle consultado al ERP y marca "detalle = S" |
| 4 | Verifica contra el archivo de adquisiciones y marca integrada |
| 5 | Crea el proveedor si no existe, sin pantallas |
| 6 | Desmarca al eliminar el documento (vuelve a pendiente) |
| 7 | Lista un mes desde el archivo, con folio y mes contable |
| 8 | Detalle local del documento ya ingresado, con nombres de cuenta, centro e item |
| 9 | Estado para ingresar: detalle S/N, proveedor E/N, clave y importes guardados |

Convenciones: `ESTADO_API=0` es exito; `MENSAJE_API$` lleva el resultado como texto separado por `CHR(9)`; el cierre es `IF TCB(13) THEN EXIT ELSE RELEASE`.

## Clave compuesta y reconciliacion
- Clave principal de 27 caracteres: `AAAAMM + RUT(9) + TIPO(2) + NUMERO(10)`. Clave 1 = `RUT + TIPO + NUMERO` (para buscar sin conocer el mes). Clave 2 = marca + clave principal.
- El archivo de adquisiciones usa otra clave (RUT + tipo + **ultimos 7** digitos del numero) y guarda el numero completo aparte. Por eso el cruce se hace por clave de 18 mas verificacion del numero completo.
- **Regla de oro del upsert:** al actualizar desde el ERP se agregan las compras nuevas y se actualizan las existentes, pero **nunca se pisa** lo grabado localmente (marca de integrado, folio, mes contable).
- Tipos sin equivalencia se guardan igual para mostrarlos, pero no se pueden ingresar.

## Flujo de ingreso
1. Op 9: ¿detalle guardado? ¿proveedor existe?
2. Solo si falta alguno: consultar el detalle al ERP (con loader) y guardarlo (op 3).
3. Si el proveedor no existe, crearlo (op 5).
4. Abrir la pantalla de adquisiciones pasando por `CALL` la **clave + anio** (`LLAMADA$`). La pantalla precarga proveedor, tipo, numero y fechas **pasando por las mismas validaciones de siempre** (no se escribe directo en los archivos).
5. Antes de grabar, **cuadratura** contra el ERP con tolerancia de $2; si no cuadra se muestra la diferencia y se deja decidir.
6. Al grabar o eliminar, la pantalla se cierra y devuelve el control; la pantalla padre relee el mes y repinta.

### Si el ERP no responde
Lo que ya esta guardado sigue funcionando. Si falta el detalle, se pregunta si se ingresa igual: vencimiento = emision, cuadratura solo por total, proveedor nuevo con RUT y razon social. El detalle **no** se marca como guardado, para reintentar despues.

## Hallazgos de datos (verificados)
- El total de una nota de credito llega como texto con signo menos; al sumar, las notas restan.
- Otros impuestos no vienen por separado: `total - neto - exento - IVA`.
- Facturas exentas traen la lista de impuestos vacia: proteger los bucles contra listas vacias.
- Maestros anuales: archivos con sufijo de anio (`MAECOST.26`). El anio se pasa de la pantalla padre a la hija, y la hija **no lo deja cambiar**.
- Un RUT puede venir vacio en el listado y estar solo en el detalle.
