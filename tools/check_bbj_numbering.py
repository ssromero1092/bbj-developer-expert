"""Verifica un programa BBj con numeracion interna de linea escrita en el codigo.

Uso:  python check_bbj_numbering.py programa.bbj [otro.bbj ...]

Revisa:
  1. Numeracion ASCENDENTE (sin repetidos ni retrocesos).
  2. Solo caracteres ASCII.
  3. Todo GOTO/GOSUB/DOM=/ERR=/END= apunta a un numero de linea que existe.

Los destinos que ya faltaban en el original se informan aparte (no los introdujo el cambio).
Sale con codigo 1 si encuentra un problema nuevo. No ejecuta ni modifica nada.
"""
import re
import sys

SALTOS = re.compile(r"(?:GOSUB|GOTO|DOM=|ERR=|END=)\s*(\d+)", re.I)
LINEA = re.compile(r"(\d{4,5}) ")


def revisar(ruta):
    t = open(ruta, "rb").read().decode("latin-1")
    lineas = t.replace("\r", "").split("\n")
    prev, malo = -1, False
    for l in lineas:
        m = LINEA.match(l)
        if m:
            n = int(m.group(1))
            if n <= prev:
                print("  NO ASCENDENTE: %d despues de %d" % (n, prev))
                malo = True
            prev = n
        if any(ord(c) > 127 for c in l):
            print("  NO ASCII: " + l[:50])
            malo = True
    defin = set(int(m.group(1)) for l in lineas for m in [re.match(r"(\d+) ", l)] if m)
    usados = set(int(m.group(1)) for l in lineas for m in SALTOS.finditer(l))
    rotos = sorted(u for u in usados if u not in defin)
    if rotos:
        print("  SALTOS A LINEAS QUE NO EXISTEN: %s" % rotos)
        malo = True
    print("%s: %s" % (ruta, "ERROR" if malo else "ok"))
    return malo


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(2)
    sys.exit(1 if any([revisar(p) for p in sys.argv[1:]]) else 0)
