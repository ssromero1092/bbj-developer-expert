#!/usr/bin/env python3
"""Hook Stop de Claude Code: dispara la captura de aprendizaje de la skill BBj.

Se ejecuta cada vez que Claude termina de responder. Solo actua si:
  - la sesion uso la skill bbj-developer-expert, y
  - hubo trabajo real (>= MIN_TOOLS llamadas a herramientas) desde el ultimo aviso.
Entonces pide a Claude (decision "block") revisar si hay algo nuevo que aprender y,
solo si lo hay, guardarlo con tools/save_learning.py a una rama de revision.
Si no hay nada nuevo, Claude debe cerrar sin crear nota.

Nunca falla ruidosamente: ante cualquier problema sale con codigo 0 sin hacer nada.
Solo libreria estandar.
"""
import json
import os
import sys
import tempfile

MIN_TOOLS = 8
SKILL_NAME = "bbj-developer-expert"

REASON = (
    "Cierre automatico de la skill bbj-developer-expert (hook, sin preguntar al usuario). "
    "Revisa el trabajo de esta sesion segun workflows/capture-learning.md. "
    "Si hubo un aprendizaje NUEVO y no obvio (patron, trampa, convencion confirmada, correccion del usuario, "
    "sintaxis probada o rechazada) que no este ya en references/ o knowledge/: redacta la nota y ejecuta, "
    "en un solo comando, desde la carpeta de la skill: "
    "python tools/save_learning.py --title \"Titulo corto\" --body-file - <<'EOF' ...nota... EOF . "
    "Sin credenciales, tokens ni datos de clientes; marca 'sin verificar' lo no probado. "
    "Si NO hubo nada nuevo, no crees nota. En ambos casos responde con UNA sola linea "
    "('Aprendizaje guardado en rama X' o 'Sin aprendizajes nuevos') y nada mas."
)


def main():
    try:
        data = json.load(sys.stdin)
    except Exception:
        return
    if data.get("stop_hook_active"):
        return
    path = data.get("transcript_path")
    sid = data.get("session_id") or "nosession"
    if not path or not os.path.isfile(path):
        return

    used_skill = False
    tools = 0
    try:
        with open(path, encoding="utf-8", errors="replace") as f:
            for line in f:
                if '"tool_use"' in line:
                    tools += line.count('"type":"tool_use"') + line.count('"type": "tool_use"')
                if not used_skill and SKILL_NAME in line and '"Skill"' in line:
                    used_skill = True
    except Exception:
        return
    if not used_skill:
        return

    state_file = os.path.join(tempfile.gettempdir(), "bbj-learning-%s.json" % sid)
    last = 0
    try:
        with open(state_file, encoding="utf-8") as f:
            last = int(json.load(f).get("tools", 0))
    except Exception:
        pass
    if tools - last < MIN_TOOLS:
        return

    try:
        with open(state_file, "w", encoding="utf-8") as f:
            json.dump({"tools": tools}, f)
    except Exception:
        return  # sin estado no arriesgamos un bucle de avisos

    print(json.dumps({"decision": "block", "reason": REASON}))


if __name__ == "__main__":
    try:
        main()
    except Exception:
        pass
