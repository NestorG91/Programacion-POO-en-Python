from mamifero import Mamifero
from reptil import Reptil
from pez import Pez
from escarabajo import Escarabajo
from ave import Ave

def main():
    # Mamífero: Caballo
    caballo = Mamifero("Caballo", "Pradera", tiene_pelo=True, tiene_patas=4)
    caballo.mostrar_info()

    # Reptil: Cocodrilo
    cocodrilo = Reptil("Cocodrilo", "Río / Pantano", tipo_escamas=True, venenoso=False)
    cocodrilo.mostrar_info()

    # Pez: Cirujano Vela
    pez_cirujano = Pez("Cirujano Vela", "Océano", tipo_agua="Agua salada")
    pez_cirujano.mostrar_info()

    # Escarabajo: Rinoceronte
    rinoceronte = Escarabajo("Rinoceronte", "Sabana", tipo_exoesqueleto=True)
    rinoceronte.mostrar_info()

    # Ave: Pato
    pato = Ave("Pato", "Laguna / Lago", puede_volar=True)
    pato.mostrar_info()

if __name__ == "__main__":
    main()
