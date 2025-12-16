from libro import Libro
from revista import Revista
from articulosegundamano import ArticuloSegundaMano
from novedades import Novedades
from articuloonline import ArticuloOnline

def main():
    libro = Libro("Cien Años de Soledad", 45000, "García Márquez", "Editorial X", 1967, "Novela")
    print(libro.detalles())
    print(libro.vender())
    print("-----")

    revista = Revista("National Geographic", 15000, "Varios", "NatGeo", 2023, "Ciencia")
    print(revista.detalles())
    print(revista.comprar())
    print("-----")

    usado = ArticuloSegundaMano("Manual Mecánica", 20000, "Autor Y", "Editorial Y", 2005, "Usado", "Mecánica", "Carlos")
    print(usado.detalles())
    print(usado.vender())
    print("-----")

    nov = Novedades("Tech 2025", 60000, "Autor Z", "Editorial Z", 2025, "Nuevo", "Tecnología")
    old, new = nov.cambiar_clasificacion("Destacado")
    print(f"Cambio: {old} → {new}")

if __name__ == "__main__":
    main()
