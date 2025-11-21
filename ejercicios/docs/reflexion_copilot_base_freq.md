# Reflexión sobre la ayuda de Copilot / asistente

Resumen en pocas líneas:

- Sugerencias aceptadas: dividir el flujo en funciones claras (`parse_args`,
  `read_file`, `extract_first_fasta_sequence`, `clean_sequence`,
  `compute_counts`, `print_results`) y mejorar el manejo de I/O con
  `with open(...)` y `splitlines()`.
- Sugerencias rechazadas: cambiar el comportamiento de salida (por ejemplo,
  convertir todos los mensajes de aviso a `stdout`) — decidí mantener avisos
  y errores en `stderr` para facilitar integraciones/pipe.
- Parte más difícil: preservar exactamente el formato de salida y el orden
  de las operaciones mientras se reestructura el código. Fue importante
  mantener los mensajes y redondeos (2 decimales) iguales al original.

Notas:

- El refactor respeta el comportamiento original y facilita futuras mejoras
  (procesar todas las secuencias, salida en CSV, soporte para bases ambigüas).
