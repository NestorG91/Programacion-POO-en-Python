from animales import Animal

class Escarabajo(Animal):
    def __init__(self, nombre, habitat, tipo_exoesqueleto=True):
        super().__init__(nombre, "Escarabajo", habitat)
        self.tipo_exoesqueleto = tipo_exoesqueleto

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Tiene exoesqueleto: {self.tipo_exoesqueleto}")
        print("-----")
