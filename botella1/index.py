from modelo_botella import botella
from modelo_botella_plastica import botella_plastica
from modelo_botella_vidrio import botella_vidrio
from base_datos import BaseDatos

if __name__ == "__main__":
    bd = BaseDatos()

    b1 = botella("Pepsi", "1.5L", "Azul")
    b2 = botella_plastica("CocaCola", "2L", "Plástica", "Redonda", "PET", "Sin tinte")
    b3 = botella_vidrio("Agua", "500ml", "Metálica", "Contour", "Grueso", "Alta")

    print(bd.guardar_botella(b1))
    print(bd.guardar_botella(b2))
    print(bd.guardar_botella(b3))

    print("\n--- BOTELLAS PLÁSTICAS ---")
    for b in bd.listar_plasticas():
        b.imprimir_info()

    print("\n--- BOTELLAS DE VIDRIO ---")
    for b in bd.listar_vidrio():
        b.imprimir_info()
