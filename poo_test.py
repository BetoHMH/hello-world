# 1. El Plano de Ingeniería (La Clase)
class ComputadoraMainframe:
    def __init__(self, modelo, ram_kb, anio): # <--- Añadimos anio aquí
        self.modelo = modelo      
        self.ram_kb = ram_kb      
        self.anio = anio                       # <--- Registramos el año en el objeto

    def ejecutar_proceso(self):   
        # Modificamos el reporte final para que también imprima el año de fabricación:
        print(f"[{self.modelo} - Año: {self.anio}] Procesando código con {self.ram_kb} KB de RAM...")

# 2. Fabricación en memoria (Pasamos el año como tercer dato)
computadora_1980 = ComputadoraMainframe("IBM System/370", 4096, 1980)
computadora_moderna = ComputadoraMainframe("MacBook Pro M-Series", 16777216, 2026)

# 3. Orden de encendido
computadora_1980.ejecutar_proceso()
computadora_moderna.ejecutar_proceso()
computadora_1980.e 