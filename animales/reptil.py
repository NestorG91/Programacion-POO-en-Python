from animales import Animal

class Reptil(Animal):
    def __init__(self, nombre, habitat, tipo_escamas=True, venenoso=False):
        super().__init__(nombre, "Reptil", habitat)
        self.tipo_escamas = tipo_escamas
        self.venenoso = venenoso

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Tiene escamas: {self.tipo_escamas}")
        print(f"¿Venemoso?: {self.venenoso}")
        print("-----")
