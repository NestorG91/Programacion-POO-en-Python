class Producto:
    def __init__(self, titulo, precio, autor, editorial, ano_edicion):
        self.titulo = titulo
        self.precio = precio
        self.autor = autor
        self.editorial = editorial
        self.ano_edicion = ano_edicion

    def vender(self):
        return f"Producto '{self.titulo}' vendido"

    def comprar(self):
        return f"Producto '{self.titulo}' comprado"

    def detalles(self):
        return (
            f"Título: {self.titulo}\n"
            f"Precio: {self.precio}\n"
            f"Autor: {self.autor}\n"
            f"Editorial: {self.editorial}\n"
            f"Año: {self.ano_edicion}"
        )
