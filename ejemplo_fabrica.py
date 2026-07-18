# 1. Traemos el reloj de fábrica del sistema de Python
from datetime import datetime

# 2. Fabricamos un objeto que captura el segundo exacto de "AHORA"
momento_actual = datetime.now()

# 3. Le pedimos al objeto que use sus métodos para extraer los datos
print("--- REPORTE DE TIEMPO DEL MAIN FRAME ---")
print(f"Año en curso: {momento_actual.year}")
print(f"Hora exacta del sistema: {momento_actual.hour}:{momento_actual.minute}")
