from mamifero import Mamifero
from reptil import Reptil
from pez import Pez
from escarabajo import Escarabajo
from ave import Ave
from animales import Animal
from base_datos_animales import BaseDatosAnimales

if __name__ == "__main__":
    bd = BaseDatosAnimales()
    
    a1 = Animal("Leon", "Mamífero", "Sabana")
    a2 = Mamifero("Caballo", "Pradera", tiene_pelo=True, tiene_patas=4)
    a3 = Reptil("Cocodrilo", "Río / Pantano", tipo_escamas=True, venenoso=False)
    a4 = Pez("Cirujano Vela", "Océano", tipo_agua="Agua salada")
    a5 = Escarabajo("Rinoceronte", "Sabana", tipo_exoesqueleto=True)
    a6 = Ave("Pato", "Laguna / Lago", puede_volar=True)

    print(bd.guardar_animal(a1))
    print(bd.guardar_animal(a2))
    print(bd.guardar_animal(a3))
    print(bd.guardar_animal(a4))
    print(bd.guardar_animal(a5))
    print(bd.guardar_animal(a6))
   
    print("\n--- MAMÍFEROS ---")
    for a in bd.listar_mamiferos():
        a.mostrar_info()

    print("\n--- REPTILES ---")
    for a in bd.listar_reptiles():
        a.mostrar_info()

    print("\n--- PECES ---")
    for a in bd.listar_peces():
        a.mostrar_info()

    print("\n--- ESCARABAJOS ---")
    for a in bd.listar_escarabajos():
        a.mostrar_info()
                                 
    print("\n--- AVES ---")
    for a in bd.listar_aves():
        a.mostrar_info()


    
