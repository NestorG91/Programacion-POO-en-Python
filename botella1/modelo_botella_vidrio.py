from modelo_botella import botella

class botella_vidrio(botella):
    def __init__(self, marca, capacidad, tapa, forma, grosor, transparencia):
        super().__init__(marca, capacidad, tapa)
        self.forma = forma
        self.grosor = grosor
        self.transparencia = transparencia

    def reutilizar_botella(self):
        print(f"La botella se va a reutilizar, forma: {self.forma}")

    def imprimir_info(self):
        print(f"La forma es: {self.forma}")
        print(f"El grosor es: {self.grosor}")
        print(f"La transparencia es: {self.transparencia}")
        super().imprimir_info()
        return "Información encontrada de Botella Vidrio"
        