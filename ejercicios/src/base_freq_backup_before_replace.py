#!/usr/bin/env python3
# Backup copy of the previous `base_freq.py` before replacing with cleaned version.

import argparse
import os
import sys

# ---------------------------
# ARGPARSE (mezclado en el código)
# ---------------------------
parser = argparse.ArgumentParser(
    description="Calcula la frecuencia de A, T, G y C de un archivo FASTA con UNA sola secuencia."
)
parser.add_argument("fasta", help="Archivo FASTA que contiene una sola secuencia.")
args = parser.parse_args()

ruta = args.fasta

# ---------------------------
# VALIDACIONES (mezcladas, no modularizadas)
# ---------------------------
if not os.path.exists(ruta):
    print("Error: el archivo no existe:", ruta)
    sys.exit(1)

# Intento leer el archivo completo (usar context manager)
try:
    with open(ruta, "r", encoding="utf-8") as fh:
        contenido = fh.read()
except Exception as e:
    print("Error al leer el archivo:", e, file=sys.stderr)
    sys.exit(1)

# Verificar que parece FASTA
if ">" not in contenido:
    print("Error: El archivo no parece estar en formato FASTA.")
    sys.exit(1)

# ---------------------------
# PROCESAMIENTO DE FASTA 
# ---------------------------
partes = contenido.split(">")

if len(partes) < 2:
    print("Error: FASTA vacío o sin secuencia válida.")
    sys.exit(1)

# Tomamos el primer bloque después del encabezado
bloque = partes[1].strip().splitlines()

header = bloque[0] if len(bloque) > 0 else ""
sec = "".join(bloque[1:]).strip().upper()

if len(sec) == 0:
    print("Error: la secuencia está vacía.")
    sys.exit(1)

# Validar solo caracteres ATGC (ignorar guiones u otros)
bases_validas = {"A", "T", "G", "C"}
seq_limpia_parts = []
invalid_counts = {}

for base in sec:
    if base in bases_validas:
        seq_limpia_parts.append(base)
    else:
        invalid_counts[base] = invalid_counts.get(base, 0) + 1

seq_limpia = "".join(seq_limpia_parts)

if len(seq_limpia) == 0:
    print("Error: la secuencia no contiene bases válidas (A,T,G,C).", file=sys.stderr)
    sys.exit(1)

# Si hubo caracteres inválidos, imprimimos un resumen conciso
if invalid_counts:
    total_invalid = sum(invalid_counts.values())
    inv_summary = ", ".join([f"{v} x '{k}'" for k, v in sorted(invalid_counts.items(), key=lambda x: -x[1])])
    print(f"Aviso: se ignoraron {total_invalid} caracteres inválidos: {inv_summary}", file=sys.stderr)

# ---------------------------
# CÁLCULO DE FRECUENCIAS (mezclado)
# ---------------------------
total = len(seq_limpia)
a = seq_limpia.count("A")
t = seq_limpia.count("T")
g = seq_limpia.count("G")
c = seq_limpia.count("C")

# ---------------------------
# IMPRESIÓN DE RESULTADOS
# ---------------------------
print("Encabezado:", header)
print("Longitud secuencia válida:", total)
print("Frecuencias:")
print("A:", a, f"({round((a/total)*100,2)}%)")
print("T:", t, f"({round((t/total)*100,2)}%)")
print("G:", g, f"({round((g/total)*100,2)}%)")
print("C:", c, f"({round((c/total)*100,2)}%)")
