from modelo_vechiculos import Vehiculos

class ModeloVehiculoMinivan(Vehiculos):
    def __init__(self, modelo, motor, color, tipo_combustible, numero_puertas, capacidad_pasajeros):
        super().__init__(modelo, motor, color, tipo_combustible)
        self.numero_puertas = numero_puertas
        self.capacidad_pasajeros = capacidad_pasajeros

    def imprimir_info(self):
        super().imprimir_info()
        print(f"El numero de puertas es: {self.numero_puertas}")
        print(f"La capacidad de pasajeros es: {self.capacidad_pasajeros}")
        return "Información encontrada de Vehículo Minivan"
