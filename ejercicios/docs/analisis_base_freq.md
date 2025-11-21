# Análisis breve de `src/base_freq.py`

Resumen rápido:

- El programa original mezcla responsabilidades: parseo de argumentos,
  validaciones de fichero, lectura, parseo del formato FASTA, limpieza de la
  secuencia y salida todo en el mismo flujo secuencial.
- No hay funciones: todo está en el nivel global, lo que dificulta pruebas y
  reutilización.
- Nombres y estructuras poco modulares: variables como `contenido`, `sec`,
  `seq_limpia` están sueltas y la lógica de avisos imprime un mensaje por
  cada carácter inválido (ruido en la salida).

Problemas detectados:

- Mezcla de I/O con lógica: leer archivos y procesar secuencia no está
  separada, lo que impide test unitarios.
- Manejo de líneas: uso de `split("\n")` en lugar de `splitlines()` puede
  comportarse distinto con distintos finales de línea.
- Mensajes de error/aviso impresos en `stdout` y no siempre en `stderr`.

Propuesta de rediseño (resumen):

- Separar en funciones pequeñas y con responsabilidades claras:
  1. `parse_args()` — parsea argumentos.
  2. `read_file(path)` — validaciones de existencia y lectura.
  3. `extract_first_fasta_sequence(content)` — parsea y devuelve header+seq.
  4. `clean_sequence(seq)` — filtra bases válidas y cuenta inválidos.
  5. `compute_counts(seq)` + `print_results(...)` — cálculo e impresión.

Con esta separación se preserva el comportamiento original, facilita la
lectura del código y permite añadir opciones (p.ej. `--all`) en el futuro sin
reorganizar todo el fichero.
