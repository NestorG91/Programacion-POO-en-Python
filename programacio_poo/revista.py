from productos import Producto

class Revista(Producto):
    def __init__(self, titulo, precio, autor, editorial, ano_edicion, categoria):
        super().__init__(titulo, precio, autor, editorial, ano_edicion)
        self.categoria = categoria

    def detalles(self):
        return super().detalles() + f"\nCategoría: {self.categoria}"
