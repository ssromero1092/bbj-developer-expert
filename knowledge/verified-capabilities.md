# Verified BBj Capabilities

Caracteristicas BBj verificadas por documentacion oficial BASIS o por evidencia reproducible.

## Registro
| Capacidad | Version BBj | Estado verificacion | Fuente | Notas |
|---|---|---|---|---|
| Integracion con clases Java via use/declare | 20+ (pendiente confirmar detalle) | observada en codigo | Programas de referencia del usuario | Verificar documentacion oficial por version |

| `setAllColumnsUserSortable(1)` en una grilla | 22.14 | probada en produccion | Servidor del usuario | La documentacion solo lo muestra en un ejemplo, sin firma. Apagar con (0) no deshace el orden aplicado |
| `ON_GRID_MOUSE_DOWN` / `ON_GRID_SELECT_COLUMN` | 22.14 | probada en produccion | Logs del usuario | Disparan en filas, **no** en el encabezado |
| `'LISTCLR'` para vaciar un `LISTBUTTON` | 22.14 | codigo del usuario | GPERIODO.bbj 0040 | `LISTCLEAR` no se uso |
| `java.util.ArrayList`/`TreeMap` desde BBj | 22.14 | probada en produccion | CON214, defcomp | `new java.util.ArrayList()`, `get`, `add`, `size` |
| Ventana `INVISIBLE` en `.arc` + `setVisible(1)` | 22.14 | probada en produccion | con214.arc, adq160.arc | Evita ver como se dibuja la pantalla |
| `Window!.getControl(n).setVisible(0/1)` para mostrar u ocultar un panel de controles | 22.14 | probada en servidor | MAE330 8000-9240 | Panel de copia en la misma ventana, funciona |
| `GZOOMLH.bbj` con MAEPROD en pantalla grafica | 22.14 | probada en servidor | ADQ160 2821, MAE330 0915 | Funciona en MAE330 |
| `BBTranslator` / `getTranslation` | - | **no funciona** (deprecado) | Dicho por el usuario | No usar en ningun programa |

## Politica
- No promover una hipotesis a capacidad verificada sin fuente confiable.
- Distinguir claramente evidencia de codigo vs documentacion oficial.
