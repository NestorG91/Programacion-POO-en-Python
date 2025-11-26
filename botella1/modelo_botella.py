class botella:
    def _init_(self, marca, capacidad, tapa):
        self.marca = marca
        self.capacidad = capacidad
        self.tapa = tapa

    
    def llenar_botella(self, capacidad):
        print(f"La botella se esta llenando: {capacidad}")
        print(f"se va a suar la tapa: {self.tapa}")

    def cerrar_botella(self, dato_cantidad):
        print(f"se uso la tapa: {self.tapa}")
        print(f"cantidad de tapas usadas: {dato_cantidad}")
        return dato_cantidad
    
    def imprimir_info(self):
        #metodo imprime la informacion de los atributos
        print(f"la marca es: {self.marca} ")
        print(f"tipo de tapa es: {self.tapa} ")
        print(f"la tapa de la botellla es: {self.capacidad} ")