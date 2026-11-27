# Knowledge Change Log

Bitacora de actualizaciones de la skill y su base de conocimiento.

## Entradas
| Fecha | Archivo | Cambio | Motivo | Fuente/Programa | Aprobado por usuario |
|---|---|---|---|---|---|
| 2026-11-02 | Estructura inicial de skill | Creacion de base bbj-developer-expert | Inicializacion | Requerimiento del usuario | si |
| 2026-11-02 | SKILL.md, references/program-structure.md, knowledge/user-conventions.md | Regla de numeracion interna BBj como referencia principal y preservacion de correlacion | Solicitud explicita del usuario | Conversacion | si |
| 2026-11-02 | workflows/implement-approved-change.md, workflows/review-changes.md | Mini-checklist obligatoria para validar orden/correlacion de lineas BBj y referencias GOTO/GOSUB | Solicitud explicita del usuario | Conversacion | si |
| 2026-11-02 | SKILL.md, workflows/analyze-existing-program.md, workflows/propose-change.md, references/ui-patterns.md, references/bbj-database.md, knowledge/user-conventions.md, references/unresolved-questions.md | Regla especial para campos con ayuda de maestro (GZOOM) y requisito de layout de archivo legible | Solicitud explicita del usuario | Conversacion | si |
| 2026-11-26 | references/bbj-language.md, ui-patterns.md, file-io-patterns.md, error-handling.md | Reglas BBj, patrones de pantallas graficas, archivo local con upsert y tabla de errores vistos | Proyecto de compras con un ERP externo, probado en produccion | CON214, defcomp, ADQ160 | si |
| 2026-11-26 | references/purchases-integration-defontana.md, sales-integration-defontana.md, bbj-pitfalls.md | Documentos de integracion de compras y ventas (sin credenciales ni URL) y trampas de BBj | Conocimiento acumulado en la copia local de la skill | Proyecto del usuario | si |
| 2026-11-26 | tools/check_bbj_numbering.py, workflows/verify-numbering-and-copies.md | Verificador de numeracion y regla de dos copias | Evito errores repetidos de numeracion y de saltos | Proyecto de compras | si |
| 2026-11-26 | knowledge/user-conventions.md, source-program-catalog.md, discovered-patterns.md, verified-capabilities.md, SKILL.md, README.md | Convenciones confirmadas, catalogo, patrones y capacidades verificadas | Cierre del proyecto de compras | Proyecto de compras | si |
| 2026-11-26 | workflows/convert-metacaracter-to-graphic.md, references/metacaracter-to-graphic-simple.md, SKILL.md, README.md, CHANGELOG.md | Flujo y receta para convertir metacaracter a grafico (mantenedor simple) | Primera conversion hecha: MAE330 (primer cliente) (sin probar en servidor) | Conversacion, MAE330 y MAE420 | si |
| 2026-11-26 | knowledge/user-conventions.md, source-program-catalog.md, discovered-patterns.md, verified-capabilities.md | Convenciones (sin Translator, etiquetas sin numeros, grabar al Enter...), catalogo, patrones y capacidades sin verificar | Decisiones del usuario durante la conversion de MAE330 | Conversacion | si |
| 2026-11-26 | references/metacaracter-to-graphic-simple.md, knowledge/discovered-patterns.md, verified-capabilities.md, source-program-catalog.md | Lo que estaba "sin verificar" pasa a probado en servidor | El usuario probo MAE330 en el servidor y todo funciona OK | Conversacion | si |
| 2026-11-26 | references/metacaracter-to-graphic-simple.md, CHANGELOG.md, knowledge/discovered-patterns.md, verified-capabilities.md, user-conventions.md | Patron de Excel con GEXCEL.bbj (temporal, GEXCEL, apertura) y trampas asociadas | El usuario pidio rehacer el Excel de MAE330 con la logica de un programa de referencia y lo probo en el servidor | Conversacion, MAE330 | si |

## Regla
No reemplazar conocimiento previo sin registrar motivo y evidencia.
