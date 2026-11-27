# Source Program Catalog

Inventario de programas BBj/.arc proporcionados por el usuario.

## Estado
- No agregar programas inventados.
- Conservar exactamente nombre y ruta entregados por el usuario.
- Marcar deducciones como deduccion.

## Tabla de inventario
| ID | Nombre archivo | Ruta proporcionada | Sistema/Modulo | Disponibilidad | Estado analisis | Temas detectados | Descripcion (fuente) | Observaciones |
|---|---|---|---|---|---|---|---|---|
| PRG-001 | CON214.bbj + con214.arc | pgms/, brc/esp/ | Compras / libro de compras | disponible | analizado | listado en grilla, orden por columna, totales, detalle, botones con icono | Pantalla del libro de compras de un ERP externo | Ver references/purchases-integration-defontana.md |
| PRG-002 | defcomp.bbj | api/ | Compras / acceso al archivo local | disponible | analizado | 9 operaciones, upsert, reconciliacion | Unico acceso al archivo MKEYED de compras | CALL con firma fija |
| PRG-003 | ADQ160.bbj + adq160.arc | pgms/, brc/esp/ | Adquisiciones | disponible | parcial | precarga, cuadratura, cierre al grabar | Recepcion de documentos sin ordenes de compra | Se llama desde CON214 con clave + anio |
| PRG-004 | consulta_compras.bbj, consulta_detalle_compra.bbj, consulta_pdf_compra.bbj | api/ | Compras / consultas al servicio externo | disponible | analizado | HTTP, JSON anidado, interruptor de prueba | Solo lectura | Usa DAIRE_ERP.bbj |
| PRG-005 | GPERIODO.bbj | publicos/ | Comun | disponible | analizado | seleccion de periodo y apertura anual | Devuelve PERIODO$=AAAA y APERTURA$=.AA | Su formato se uso para fijar el anio desde otra pantalla |
| PRG-006 | MAE330.bbj (metacaracter) -> MAE330.bbj + mae330.arc (grafico) | metacaracter/pgms/, pgms/, brc/esp/ (repo privado del proyecto) | Cliente A / mantencion de dosificacion de productos | disponible | convertido y probado en servidor (OK) | mantenedor simple, copia entre agricolas, actualizar objetivo, listado/Excel | Primer programa convertido de metacaracter a grafico | Ver references/metacaracter-to-graphic-simple.md |
| PRG-007 | MAE420.bbj + mae420.arc | pgms/, brc/esp/ | Cliente A / maestro de precios de lista | disponible | analizado | patron grafico de mantenedor simple (EVENTOS, MENU_SUPERIOR, ayudas, colores) | Programa grafico de referencia entregado por el usuario | Usa Translator: NO se copia ese punto |
| PRG-008 | MAE340.bbj (metacaracter) -> MAE340.bbj + mae340.arc (grafico) | metacaracter/pgms/, pgms/, brc/esp/ (repo privado del proyecto) | Cliente A / distribucion de unidades de fertilizantes | disponible | convertido, sin probar en servidor | mantenedor simple de 10 valores numericos, sin periodo, listado + Excel nuevo | Segunda conversion de metacaracter a grafico | Ver references/metacaracter-to-graphic-simple.md |

## Valores sugeridos
- Disponibilidad: disponible, pendiente, parcial.
- Estado analisis: no iniciado, en analisis, analizado, requiere confirmacion.
