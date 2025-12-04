from animales import Animal

class Pez(Animal):
    def __init__(self, nombre, habitat, tipo_agua="Agua salada"):
        super().__init__(nombre, "Pez", habitat)
        self.tipo_agua = tipo_agua

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Tipo de agua: {self.tipo_agua}")
        print("-----")
