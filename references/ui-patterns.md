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
