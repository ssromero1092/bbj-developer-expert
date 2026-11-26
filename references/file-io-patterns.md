# File I/O Patterns

Patrones de manejo de archivos en BBj observados en codigo real.

## Puntos de analisis
- OPEN/CLOSE y control de canales.
- READ/WRITE/EXTRACT/FIND y manejo de errores.
- Bloqueos, concurrencia y tiempos (si aplica).

## Ficha
| Patron | Programa | Riesgo | Buen uso | Confianza |
|---|---|---|---|---|
| PENDIENTE | PENDIENTE | PENDIENTE | PENDIENTE | pendiente |

## Patron: listado externo guardado en MKEYED (verificado)
- Un servicio lento se consulta una vez y su resultado se guarda; la pantalla lee del archivo.
- Registro de ancho fijo (600 bytes) con claves 0, 1 y 2. Si cambia la estructura, **el archivo debe borrarse y recrearse**.
- **Upsert que respeta lo local:** actualizar campos del servicio externo, conservar los campos grabados localmente (marca, folio, usuario, fecha de integracion).
- **Reconciliar** contra el archivo "verdad" (adquisiciones): si el documento ya no existe, bajar la marca.
- Un modulo concentra todo el acceso al archivo (operaciones numeradas) y las pantallas no lo abren.
- Todo `READ` de un registro del archivo debe usar la **misma lista de campos** que el `WRITE`. Al agregar un campo, actualizar todos los `READ`/`WRITE` (en el caso real, 22 campos).
- Orden de salida: el orden del archivo es el de la clave. Ordenar para el usuario se hace en la grilla, no en el acceso a datos.

## Patron: archivos con sufijo de anio
`OPEN (ch,ERR=lbl)"MAECOST."+AP$` con `AP$="26"`. Si no abre, el canal queda en 0 y la salida muestra solo el codigo. Los nombres (cuenta, centro, item) se leen aparte y se agregan como campos extra a la linea.
