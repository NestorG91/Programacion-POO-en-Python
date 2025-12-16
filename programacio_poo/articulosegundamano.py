from productos import Producto

class ArticuloSegundaMano(Producto):
    def __init__(self, titulo, precio, autor, editorial, ano_edicion, clasificacion, tema, vendedor):
        super().__init__(titulo, precio, autor, editorial, ano_edicion)
        self.clasificacion = clasificacion
        self.tema = tema
        self.vendedor = vendedor

    def detalles(self):
        return (
            super().detalles() +
            f"\nClasificación: {self.clasificacion}\n"
            f"Tema: {self.tema}\n"
            f"Vendedor: {self.vendedor}"
        )
