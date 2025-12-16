from productos import Producto

class Libro(Producto):
    def __init__(self, titulo, precio, autor, editorial, ano_edicion, genero):
        super().__init__(titulo, precio, autor, editorial, ano_edicion)
        self.genero = genero

    def detalles(self):
        return super().detalles() + f"\nGénero: {self.genero}"