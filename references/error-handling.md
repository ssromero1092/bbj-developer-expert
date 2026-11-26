# Error Handling Patterns

Documentar manejo de errores en BBj (seterr, err, errmes, sqlerr, rutas de escape, etc.).

## Registro
- Patron:
- Programa fuente:
- Seccion/rutina:
- Escenario que cubre:
- Riesgos si se altera:
- Confianza:

## Observacion inicial
En referencias vistas aparecen rutinas de error que retornan JSON en servlets y controlan errores de I/O/SQL.

## Errores vistos en un proyecto real (compras, 2026-11) y su causa
| Sintoma | Causa | Arreglo |
|---|---|---|
| ERROR=17 `No control with id N in context 0` | Contexto de ventana cambiado antes de un `CALL` a otra pantalla | No tocar el contexto antes del CALL; guardar y restaurar |
| ERROR=29 `Duplicate ID` al crear una ventana | Id de `COLUMNHEAD` repetido en el `.arc` | Id unico por grilla |
| ERROR=43 `Mask is empty` | Mascara de `STR(x:M$)` sin definir | Definir al inicio |
| ERR=27 al mostrar una factura exenta | Lista de impuestos vacia + `RETURN` desde una rutina atrapada por `SETERR` | Guardas contra listas vacias y `GOTO` al cierre |
| La clave llegaba mas larga de lo esperado y la pantalla hija la descartaba | Una operacion devolvia mas campos y se tomaba "todo lo que sigue" | Cortar en el primer separador `CHR(9)` |
| Un aviso no salia | Un `GOTO` previo saltaba por encima del punto de aviso | Colocar el aviso en un punto por el que siempre se pasa |
| Salto a numero de linea inexistente tras limpiar | Se borro una linea que era destino de `DOM=`/`ERR=` | Verificar destinos antes de borrar |

## Al limpiar trazas de depuracion
Una traza (`println`) puede ser **destino de un `DOM=` o `ERR=`**. Antes de borrarla, buscar saltos a su numero; si existe, dejar la linea como `REM`.
