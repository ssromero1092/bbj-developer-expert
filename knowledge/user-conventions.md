# User Conventions

Registrar solo convenciones confirmadas por el usuario o con evidencia suficiente.

## Convenciones confirmadas
| Convencion | Estado | Evidencia | Fuente |
|---|---|---|---|
| REVIEW FIRST antes de implementar | confirmada | Requisito explicito del usuario | Conversacion |
| En BBj con lineas numeradas, usar numeracion interna como referencia principal y conservar orden/correlacion | confirmada | Requisito explicito del usuario | Conversacion |
| Para cambios de campos con ayuda de maestro, analizar .arc + .bbj + formato/layout del archivo antes de proponer implementacion | confirmada | Requisito explicito del usuario | Conversacion |

| Editar solo la copia de trabajo; la copia en uso solo se lee y compara | confirmada | Regla permanente del usuario | Conversacion |
| `git commit` y `git push` solo cuando el usuario lo pide; un commit para programas y otro para documentacion | confirmada | Practica constante del usuario | Conversacion |
| No poner `ERR=` al final de un `CALL` a un programa ajeno | confirmada | El usuario lo quito de `CALL "GDIGVE"` | Conversacion |
| Textos propios en ASCII; archivos `.bbj` ASCII con fin de linea LF | confirmada | Regla del usuario | Conversacion |
| Los repositorios con datos del cliente son privados y deben seguir siendolo | confirmada | Regla del usuario | Conversacion |
| Documentar cada cambio en una bitacora del proyecto, marcando lo "sin verificar" | confirmada | Practica constante | Conversacion |
| No usar `BBTranslator`/`getTranslation`: deprecado y no funciona en ningun sistema BBj de la empresa; mensajes con texto directo | confirmada | Dicho por el usuario (2026-11-26) | Conversacion |
| Conversion metacaracter a grafico: editar solo `pgms/` (copia de `metacaracter/pgms/`), crear `brc/esp/x.arc`, conservar la logica y seguir el patron visual de un programa grafico de referencia | confirmada | Requerimiento del usuario (MAE330) | Conversacion |
| En el `.arc` las etiquetas llevan solo el nombre del campo, sin numeros ("1.", "2.") | confirmada | Pedido del usuario | Conversacion |
| En un mantenedor, el ultimo campo (y cualquier campo si el registro ya existe) llama a la rutina de grabar al dar Enter | confirmada | Pedido del usuario | Conversacion |
| Usar la misma ayuda (GZOOM/GZOOMLH/GZOOM2) que usa el programa original | confirmada | Pedido del usuario | Conversacion |
| Botones de acciones extra (copiar, actualizar) con icono `.bmp` propio (`COPIAR.bmp`, `ACTUALIZA.bmp`) | confirmada | Pedido del usuario | Conversacion |
| Rutas de prueba en PC local dentro de un programa (p. ej. una ruta de maestros con unidad y carpeta fijas) se dejan como estan | confirmada | Respuesta del usuario | Conversacion |
| El Excel de un programa convertido se genera con el patron GEXCEL del programa de referencia (temporal MKEYED + `GEXCEL.bbj`), no con texto y tabulaciones; se cierra el PRN antes de generar y se abre el Excel al terminar | confirmada | Pedido del usuario, probado en servidor | Conversacion |

## Convenciones pendientes de confirmar
| Tema | Hipotesis | Que falta confirmar |
|---|---|---|
| Nomenclatura de variables BBj | pendiente | Mas programas de referencia |
