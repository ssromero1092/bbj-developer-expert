# UI Patterns (.arc y programas graficos)

Patrones de UI para programas BBj con formularios/controles .arc.

## Analizar
- Controles, IDs y disposicion.
- Relacion entre .bbj y .arc.
- Eventos, validaciones y navegacion.
- Convenciones de etiquetas y ayudas.

## Patron: campo con ayuda de maestro
Checklist minimo:
- Edit + ToolButton asociados (IDs y orden visual).
- Callback de ambos controles en .bbj.
- Rutina de ayuda (GZOOM/GZOOMWD/GZOOMLH o equivalente).
- Transformacion del valor retornado por ayuda.
- Validacion final (READ/FIND al maestro y setText de descripcion).
- Comportamiento de foco y habilitacion/deshabilitacion.

## Evidencia recomendada
- ID en .arc.
- Bloque callback en .bbj.
- Bloque CASE del evento y rutina de maestro asociada.

## Registro
| Pantalla | Programa BBj relacionado | Patron UI | Evidencia | Observaciones |
|---|---|---|---|---|
| PENDIENTE | PENDIENTE | PENDIENTE | PENDIENTE | PENDIENTE |

## Patrones de programas graficos que se llaman entre si (verificados)

### Ventana invisible hasta estar lista
- En el `.arc`, `INVISIBLE` como **primera propiedad** de `WINDOW`; en el codigo, `Window!.setVisible(1)` al terminar de armar la pantalla. Evita ver como se dibujan los controles.
- Loader de la aplicacion: `barraprogreso!=BBjAPI().getGroupNamespace()`; `setValue("barraprogreso",0)` lo enciende y `1` lo apaga. Apagarlo siempre despues del `CALL`, tambien en las rutas de error.

### Contextos al llamar una pantalla desde otra
- Cada ventana tiene su contexto, pero `SysGui!` es el mismo objeto. Si se abre una pantalla hija con `CALL`, **no cambiar el contexto antes**; guardar el propio (`CTX_PROPIO`) y restaurarlo al volver con `sysgui!.setContext(...)` y `PRINT(GUI)'CONTEXT'(...)`.
- Errores vistos: `ERROR=17 No control with id 203 in context 0` (contexto cambiado antes del CALL) y `No window with context 1` (contexto no restaurado al volver).
- El contexto se lee del texto de la ventana (`STR(Window!)` contiene `context=N`).

### Pantalla hija con valores fijados por el padre
Pasar datos por el parametro de `ENTER` (`LLAMADA$`): clave + anio. La hija rellena y **bloquea** el combo del anio (`'LISTCLR'`, `'LISTADD'`, `'LISTSEL'`, `'DISABLE'`), sin pedirlo. Desde el menu (sin parametro) funciona como antes.

### Dos grillas en lugar de una
Si una misma grilla sirve para un listado ordenable y para un detalle, el orden del listado desarma el detalle. Solucion: una **segunda grilla oculta** (otro id) para el detalle, y una variable que apunte a la grilla activa. Asi las rutinas que dibujan el detalle no cambian.
- En el `.arc`, el id de `COLUMNHEAD` debe ser **unico por grilla**. Duplicarlo da `ERROR=29 (Duplicate ID)`.

### Totales fuera de la grilla
Poner la fila de totales dentro de la grilla la mezcla con el orden por columna. Mostrar los totales en un `STATICTEXT` aparte, actualizado con `PRINT(GUI)'TITLE'(id,texto)`.

### Iconos de botones de menu
`img=SysGui!.getImageManager().loadImageFromFile("NOMBRE.bmp")` y `boton!.setImage(img!)`. Si el nombre no coincide exactamente con el archivo del servidor, el boton queda sin icono, sin error.
