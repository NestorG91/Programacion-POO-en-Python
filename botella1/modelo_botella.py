class botella:
    def __init__(self, marca, capacidad, tapa):
        self.marca = marca
        self.capacidad = capacidad
        self.tapa = tapa

    def imprimir_info(self):
        # Método imprime la información de los atributos
        print(f"La marca es: {self.marca}")
        print(f"Tipo de tapa: {self.tapa}")
        print(f"La capacidad de la botella es: {self.capacidad}")