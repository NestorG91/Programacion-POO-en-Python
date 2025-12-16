from ave import Ave
from escarabajo import Escarabajo
from mamifero import Mamifero
from pez import Pez
from reptil import Reptil

class BaseDatosAnimales:
    def __init__(self):
        self.animales = []
        
    def guardar_animal(self, animal):
        self.animales.append(animal)
        return "Animal guardado exitosamente"
    
    def listar_todos(self):
        return self.animales
    
    def listar_aves(self):
        return [a for a in self.animales if isinstance(a, Ave)]
    
    def listar_escarabajos(self):
        return [a for a in self.animales if isinstance(a, Escarabajo)]
    
    def listar_mamiferos(self):
        return [a for a in self.animales if isinstance(a, Mamifero)]
    
    def listar_peces(self):
        return [a for a in self.animales if isinstance(a, Pez)]
    
    def listar_reptiles(self):
        return [a for a in self.animales if isinstance(a, Reptil)]