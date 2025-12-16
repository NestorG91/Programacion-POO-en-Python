from modelo_botella_plastica import botella_plastica
from modelo_botella_vidrio import botella_vidrio

class BaseDatos:
    def __init__(self):
        self.botellas = []
        
    def guardar_botella(self, botella):
        self.botellas.append(botella)
        return "Botella guardada correctamente"
    
    def listar_botellas(self):
        return self.botellas
    
    def listar_plasticas(self):
        return [b for b in self.botellas if isinstance(b, botella_plastica)]
    
    def listar_vidrio(self):
        return [b for b in self.botellas if isinstance(b, botella_vidrio)]