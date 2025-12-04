from modelo_vechiculos import Vehiculos

class ModeloVehiculoTipoPesado(Vehiculos):
    def __init__(self, modelo, motor, color, tipo_combustible, capacidad_carga, numero_ejes):
        super().__init__(modelo, motor, color, tipo_combustible)
        self.capacidad_carga = capacidad_carga
        self.numero_ejes = numero_ejes

    def imprimir_info(self):
        super().imprimir_info()
        print(f"La capacidad de carga es: {self.capacidad_carga}")
        print(f"El numero de ejes es de: {self.numero_ejes}")
        return "Información encontrada de Vehículo Tipo Pesado"
