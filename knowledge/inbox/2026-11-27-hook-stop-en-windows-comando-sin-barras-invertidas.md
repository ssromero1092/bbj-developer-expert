---
titulo: Hook Stop en Windows: comando sin barras invertidas
fecha: 2026-11-27
estado: pendiente de revision
---

## Contexto
Se registro el hook Stop de la skill en ~/.claude/settings.json (Windows) para disparar la captura de aprendizaje.

## Aprendizaje
- Un comando con rutas de Windows escritas con barras invertidas se daÃ±a al generarse el JSON desde un script (\b y \t pasan a ser caracteres de control). Solucion: usar `python -c` con `os.path.expanduser('~/.claude/skills/...')` y barras normales.
- Comprobar `os.path.isfile(p)` antes de ejecutar evita un error en cada respuesta cuando la skill aun no esta instalada.
- Si la rama ya fue unida por PR en GitHub, `git push origin master` es rechazado; basta `git fetch` y `git merge --ff-only origin/master`.

## Evidencia
El hook se disparo en una sesion real despues de usar la skill con 8 o mas llamadas a herramientas.

## Estado
probado en servidor (probado en la maquina del usuario con Windows 11 y Python 3.14)

## Donde deberia ir
knowledge/verified-capabilities.md (seccion de herramientas de la skill)
