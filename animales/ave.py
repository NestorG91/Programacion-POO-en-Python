from animales import Animal

class Ave(Animal):
    def __init__(self, nombre, habitat, puede_volar=True):
        super().__init__(nombre, "Ave", habitat)
        self.puede_volar = puede_volar

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Puede volar: {self.puede_volar}")
        print("-----")
