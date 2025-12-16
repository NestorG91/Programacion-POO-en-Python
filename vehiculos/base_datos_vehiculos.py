from modelo_vehiculo_Minivan import ModeloVehiculoMinivan
from modelo_vehiculo_Deportivo import ModeloVehiculoDeportivo
from modelo_vehiculo_TipoPesado import ModeloVehiculoTipoPesado

class BaseDatosVehiculos:
    def __init__(self):
        self.vehiculos = []
        
    def guardar_vehiculo(self, vehiculo):
        self.vehiculos.append(vehiculo)
        return "Vehículo guardado correctamente"
    
    def listar_todos(self):
        return self.vehiculos
    
    def listar_deportivos(self):
        return [v for v in self.vehiculos if isinstance(v, ModeloVehiculoDeportivo)]
    
    def listar_minivan(self):
        return [v for v in self.vehiculos if isinstance(v, ModeloVehiculoMinivan)]
    
    def listar_tipo_pesado(self):
        return [v for v in self.vehiculos if isinstance(v, ModeloVehiculoTipoPesado)]