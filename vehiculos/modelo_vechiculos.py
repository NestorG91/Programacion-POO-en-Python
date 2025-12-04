class Vehiculos:
    def __init__(self, modelo, motor, color, tipo_combustible):
        self.modelo = modelo
        self.motor = motor
        self.color = color
        self.tipo_combustible = tipo_combustible

    def imprimir_info(self):
        print(f"El modelo del vehiculo es: {self.modelo}")
        print(f"El motor de vehiculo es: {self.motor}")
        print(f"El color del vehiculo es: {self.color}")
        print(f"El tipo de combustible es: {self.tipo_combustible}")
