from modelo_vechiculos import Vehiculos

class ModeloVehiculoDeportivo(Vehiculos):
    def __init__(self, modelo, motor, color, tipo_combustible, tipo_deportivo, velocidad_maxima):
        super().__init__(modelo, motor, color, tipo_combustible)
        self.tipo_deportivo = tipo_deportivo
        self.velocidad_maxima = velocidad_maxima

    def imprimir_info(self):
        super().imprimir_info()
        print(f"El tipo de vehiculo deportivo es: {self.tipo_deportivo}")
        print(f"La velocidad maxima es: {self.velocidad_maxima}")
        return "Información encontrada de Vehículo Deportivo"
