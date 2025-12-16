from modelo_botella import botella

class botella_plastica(botella):
    def __init__(self, marca, capacidad, tapa, diseño, material, tinte):
        super().__init__(marca, capacidad, tapa)
        self.diseño = diseño
        self.material = material
        self.tinte = tinte

    def reciclar_botella(self):
        print(f"La botella se va a reciclar, material: {self.material}")

    def imprimir_info(self):
        super().imprimir_info()
        print(f"El diseño es: {self.diseño}")
        print(f"El material es: {self.material}")
        print(f"El color es: {self.tinte}")
        return "Información encontrada de Botella Plástica"