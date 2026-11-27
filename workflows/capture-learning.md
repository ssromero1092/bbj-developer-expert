# Capturar aprendizaje (automatico, a rama de revision)

Al cerrar cada tarea, la skill registra lo aprendido sin esperar a que el usuario lo pida. Nada llega a `master` sin revision humana.

## Disparo automatico
El hook `Stop` (`tools/learning_hook.py`, registrado en `~/.claude/settings.json`) corre al terminar cada respuesta. Solo actua si la sesion uso esta skill y hubo 8 o mas llamadas a herramientas desde el ultimo aviso; entonces pide a Claude cerrar con este flujo, sin preguntar al usuario. Si no hay nada nuevo, no se crea nota.

## Cuando
Al final de cada tarea (analisis, correccion, conversion, explicacion), si hubo algo de estos tipos:
- Patron o regla BBj que funciono (o fallo) y no esta en `references/` ni `knowledge/`.
- Trampa o error nuevo y su causa.
- Decision o convencion que el usuario confirmo.
- Correccion del usuario a algo que la skill propuso.
- Sintaxis probada (o rechazada) en su servidor.

Si no hubo nada nuevo, no crear nota.

## Como
1. Redactar la nota en espanol, ASCII, corta, con estas secciones: `Contexto`, `Aprendizaje`, `Evidencia` (programa y numero interno de linea), `Estado` (`probado en servidor` o `sin verificar`), `Donde deberia ir` (archivo destino sugerido).
2. Guardarla en un archivo temporal y ejecutar:
   `python tools/save_learning.py --title "Titulo corto" --body-file <archivo>`
3. El script crea la rama `aprendizaje/AAAA-MM-DD-slug` desde `origin/master`, hace commit solo de `knowledge/inbox/...md` y la sube. No toca la rama actual ni los cambios sin confirmar.
4. Informar al usuario en una linea: nombre de la rama y enlace para abrir el PR.

## Prohibido en la nota
- Credenciales, tokens, claves, URLs con secretos, datos de clientes. El script rechaza patrones comunes, pero la revision previa es responsabilidad de quien redacta.
- Presentar como verificado algo que no se probo. Marcar `sin verificar`.
- Inventar APIs o sintaxis BBj.

## Revision (humana)
El responsable revisa el PR: si la nota es correcta, la incorpora a su archivo destino (`references/`, `knowledge/`), la anota en `knowledge/knowledge-change-log.md` y borra el archivo de `inbox/`. Si no, cierra el PR.

## Si falla
Sin red, sin permisos de escritura o sin remoto: usar `--no-push` (queda el commit local en la rama) e informar al usuario. No intentar otras vias.
