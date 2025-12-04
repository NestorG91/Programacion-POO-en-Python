class Animal:
    def __init__(self, nombre, clase_animales, habitat):
        self.nombre = nombre
        self.clase_animales = clase_animales
        self.habitat = habitat

    def mostrar_info(self):
        print(f"Animal: {self.nombre}")
        print(f"Clase: {self.clase_animales}")
        print(f"Hábitat: {self.habitat}")
