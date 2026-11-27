#!/usr/bin/env python3
"""Guarda una nota de aprendizaje de la skill en una rama de revision y la sube.

Uso:
    python tools/save_learning.py --title "Titulo corto" --body-file nota.md
    (o el cuerpo por stdin con --body-file -)

Que hace (sin tocar tu carpeta de trabajo ni la rama actual):
  1. git fetch origin
  2. crea un worktree temporal con la rama nueva aprendizaje/AAAA-MM-DD-slug desde origin/master
  3. escribe knowledge/inbox/AAAA-MM-DD-slug.md
  4. commit SOLO de ese archivo y push -u origin <rama>
  5. borra el worktree temporal

Nunca escribe en master. Rechaza notas con posibles credenciales.
Solo usa la libreria estandar.
"""
import argparse
import datetime
import os
import re
import shutil
import subprocess
import sys
import tempfile

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_PATTERNS = [
    (r"sk-[A-Za-z0-9_\-]{16,}", "clave tipo sk-..."),
    (r"eyJ[A-Za-z0-9_\-]{20,}\.[A-Za-z0-9_\-]{10,}", "token JWT"),
    (r"(?i)(password|passwd|clave|token|secret|api[_-]?key)\s*[:=]\s*\S{6,}", "credencial asignada"),
    (r"https?://[^\s)]*(?:token|key|secret)=[^\s)]+", "URL con credencial"),
]


def git(*args, cwd=REPO, check=True):
    r = subprocess.run(["git", *args], cwd=cwd, capture_output=True, text=True)
    if check and r.returncode != 0:
        sys.exit("git %s fallo:\n%s%s" % (" ".join(args), r.stdout, r.stderr))
    return r.stdout.strip()


def slugify(text):
    text = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
    return (text or "nota")[:50].strip("-")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--title", required=True)
    ap.add_argument("--body-file", required=True, help="archivo con el cuerpo, o - para stdin")
    ap.add_argument("--no-push", action="store_true", help="solo commit local en la rama")
    a = ap.parse_args()

    body = sys.stdin.read() if a.body_file == "-" else open(a.body_file, encoding="utf-8").read()
    for pat, label in SECRET_PATTERNS:
        if re.search(pat, body) or re.search(pat, a.title):
            sys.exit("Nota rechazada: parece contener %s. Quitala y reintenta." % label)

    today = datetime.date.today().isoformat()
    slug = slugify(a.title)
    branch = "aprendizaje/%s-%s" % (today, slug)
    if git("branch", "--list", branch) or git("ls-remote", "--heads", "origin", branch):
        branch += "-" + datetime.datetime.now().strftime("%H%M%S")

    git("fetch", "origin")
    tmp = tempfile.mkdtemp(prefix="bbj-learn-")
    wt = os.path.join(tmp, "wt")
    try:
        git("worktree", "add", "-b", branch, wt, "origin/master")
        rel = "knowledge/inbox/%s-%s.md" % (today, slug)
        path = os.path.join(wt, rel)
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w", encoding="utf-8", newline="\n") as f:
            f.write("---\ntitulo: %s\nfecha: %s\nestado: pendiente de revision\n---\n\n" % (a.title, today))
            f.write(body.strip() + "\n")
        git("add", rel, cwd=wt)
        git("commit", "-m", "Aprendizaje (pendiente de revision): %s" % a.title, cwd=wt)
        if a.no_push:
            print("Commit local en rama %s (sin push)." % branch)
        else:
            git("push", "-u", "origin", branch, cwd=wt)
            print("Rama subida: %s" % branch)
            url = git("remote", "get-url", "origin").removesuffix(".git")
            print("Abrir PR: %s/compare/master...%s?expand=1" % (url, branch))
    finally:
        git("worktree", "remove", "--force", wt, check=False)
        shutil.rmtree(tmp, ignore_errors=True)
        git("worktree", "prune", check=False)


if __name__ == "__main__":
    main()
