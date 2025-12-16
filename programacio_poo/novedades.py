from productos import Producto

class Novedades(Producto):
    def __init__(self, titulo, precio, autor, editorial, ano_edicion, clasificacion, tema):
        super().__init__(titulo, precio, autor, editorial, ano_edicion)
        self.clasificacion = clasificacion
        self.tema = tema

    def cambiar_clasificacion(self, nueva):
        anterior = self.clasificacion
        self.clasificacion = nueva
        return anterior, nueva

    def detalles(self):
        return super().detalles() + f"\nClasificación: {self.clasificacion}"