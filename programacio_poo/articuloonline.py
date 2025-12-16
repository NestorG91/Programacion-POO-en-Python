from productos import Producto

class ArticuloOnline(Producto):
    def __init__(self, titulo, precio, autor, editorial, ano_edicion, tema):
        super().__init__(titulo, precio, autor, editorial, ano_edicion)
        self.tema = tema

    def publicar(self):
        return "Artículo publicado en línea"

    def detalles(self):
        return super().detalles() + f"\nTema: {self.tema}"