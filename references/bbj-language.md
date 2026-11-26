# BBj Language Notes

Resumen operativo del lenguaje BBj basado en evidencia local y verificacion externa.

## Que documentar aqui
- Instrucciones BBj observadas en programas reales.
- Patrones de flujo (GOSUB, labels, RETURN, etc.) cuando aparezcan.
- Convenciones de tipos, conversiones y formatos detectadas.

## Formato de evidencia
| Tema | Evidencia en programa | Explicacion | Confianza |
|---|---|---|---|
| PENDIENTE | PENDIENTE | PENDIENTE | pendiente |

## Limites
No inventar sintaxis ni funciones BBj no verificadas.

## Reglas verificadas en produccion (proyecto de compras, 2026-11)
Cada una se comprobo con el programa corriendo en el servidor del usuario. Las marcadas *(sin verificar)* no.

| Tema | Regla | Evidencia |
|---|---|---|
| Condicional | `IF cond THEN a; b` hace **condicional tambien a `b`**. Para un `ELSE` claro, partir en lineas numeradas distintas. | CON214 7120-7170, ADQ160 5407-5409 |
| Bucle FOR | El cuerpo se ejecuta **una vez aunque el limite este superado**. Proteger con `IF N=0 THEN ...` antes. | defcomp op 7, op 8 |
| SETERR | Salta como un GOTO: **no vuelve** a la rutina que fallo. No usar `RETURN` tras un error atrapado con SETERR. | consulta_detalle_compra, error ERR=27 |
| ENTER | `ENTER ...,ERR=*next` absorbe parametros de mas: permite llamar con firmas ampliadas sin romper llamadores antiguos. | ADQ160 0007 (`LLAMADA`, `LLAMADA$`) |
| CALL a programas ajenos | **No poner `ERR=` al final** de un `CALL` a un programa que no es tuyo: oculta errores reales. | CALL "GDIGVE" (regla del usuario) |
| STBL | `STBL("!VAR")` comparte variables entre programas; se usa para interruptores de prueba. | consulta_compras 3016 |
| Directivas de lista | Vaciar un `LISTBUTTON` es `'LISTCLR'(id)`, **no** `LISTCLEAR`. Agregar: `'LISTADD'(id,-1,texto)`. Seleccionar: `'LISTSEL'(id,n)`. | GPERIODO 0040-0055 |
| Mascaras | Usar una mascara de `STR(x:M$)` sin haberla definido da **ERROR=43 (Mask is empty)**. Definirla al iniciar. | CON214 0009 |
| Listas Java | `new java.util.ArrayList()`; `get()`, `add()`, `size()`. | CON214 6014 |
| Grilla ordenable | `Grid!.setAllColumnsUserSortable(1,ERR=*NEXT)` activa el orden por clic en el encabezado. Apagarlo con `(0)` **no deshace** un orden ya aplicado. *(la firma no esta documentada; se probo en produccion)* | CON214 0020, 6037 |
| Eventos de grilla | `BBjGrid` **no tiene evento de clic en el encabezado**. `ON_GRID_MOUSE_DOWN` solo dispara en filas. | Log de produccion + documentacion BASIS |

## Cuando se ordena una grilla
Al ordenar por columna, la **posicion de la fila deja de coincidir** con la del arreglo en memoria. No usar `getRow()` como indice: buscar el registro por una clave (por ejemplo RUT + tipo + numero) leida de la propia fila.
