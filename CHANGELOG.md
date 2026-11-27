# Changelog

## [0.3.0] - 2026-11-26
### Added
- `workflows/convert-metacaracter-to-graphic.md`: flujo para convertir programas de metacaracter a grafico, con los 3 tipos de pantalla (simple, complejo, informes) y las reglas acordadas.
- `references/metacaracter-to-graphic-simple.md`: receta del mantenedor simple (equivalencias, esqueleto de MAE420, ayudas, sub-flujos, verificaciones, trampas), basada en MAE330 (primer cliente).
### Changed
- `SKILL.md`, `README.md`: enlaces y regla de no usar `Translator`.
- `knowledge/*`: convenciones, catalogo, patrones, capacidades y bitacora.
- La receta de mantenedor simple queda marcada como probada en el servidor (MAE330).

## [0.2.0] - 2026-11-26
### Added
- Documentos de integracion: compras y ventas con un ERP externo (sin credenciales ni URL).
- Trampas frecuentes de BBj.
- Reglas BBj verificadas en produccion, patrones de pantallas graficas y de archivo local con upsert.
- `tools/check_bbj_numbering.py` y flujo `verify-numbering-and-copies`.
- Convenciones confirmadas: copia de trabajo vs copia en uso, commits solo a pedido, ASCII.
### Changed
- `SKILL.md`: referencias nuevas, herramientas y reglas de commit y copias.
- `SKILL.md`: responder siempre en espanol y citar por numero interno de linea.
- `SKILL.md`: al invocar la skill en una sesion nueva, sincronizar el repositorio con `git fetch` y `git pull --ff-only`.

## [0.1.0] - 2026-11-02
### Added
- Estructura inicial de skill `bbj-developer-expert`.
- Modo REVIEW FIRST.
- Reglas para no inventar arquitectura ni APIs.
- Reglas para numeracion interna BBj (orden y correlacion).
- Checklist de implementacion/revision para lineas numeradas.
- Regla especial para campos con ayuda (GZOOM) y dependencia de maestro/layout.
