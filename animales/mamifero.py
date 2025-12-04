from animales import Animal

class Mamifero(Animal):
    def __init__(self, nombre, habitat, tiene_pelo=True, tiene_patas=4):
        super().__init__(nombre, "Mamífero", habitat)
        self.tiene_pelo = tiene_pelo
        self.tiene_patas = tiene_patas

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Tiene pelo: {self.tiene_pelo}")
        print(f"Número de patas: {self.tiene_patas}")
        print("-----")
