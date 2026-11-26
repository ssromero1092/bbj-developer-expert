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

## Convenciones pendientes de confirmar
| Tema | Hipotesis | Que falta confirmar |
|---|---|---|
| Nomenclatura de variables BBj | pendiente | Mas programas de referencia |
