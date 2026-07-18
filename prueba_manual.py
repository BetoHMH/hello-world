# 1. Importamos la palabra que descubrimos en el manual
import platform

# 2. Le pedimos a la Mac que nos entregue sus datos de hardware
sistema_operativo = platform.system()
arquitectura_procesador = platform.machine()

# 3. Desplegamos el reporte en la terminal
print("--- REPORTE DE HARDWARE DE LA MAC ---")
print(f"Sistema Operativo detectado: {sistema_operativo}")
print(f"Arquitectura del Procesador: {arquitectura_procesador}")
