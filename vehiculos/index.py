from modelo_vehiculo_Minivan import ModeloVehiculoMinivan
from modelo_vehiculo_Deportivo import ModeloVehiculoDeportivo
from modelo_vehiculo_TipoPesado import ModeloVehiculoTipoPesado

# Instancia Minivan
obj_minivan = ModeloVehiculoMinivan("Honda Odyssey", "V6", "Plateado", "Gasolina", 4, 7)
print(obj_minivan.imprimir_info())
print("-----")

# Instancia Deportivo
obj_deportivo = ModeloVehiculoDeportivo("Ferrari", "V8Turbo", "Amarillo", "GasolinaPremium", "Superdeportivo", 340)
print(obj_deportivo.imprimir_info())
print("-----")

# Instancia Tipo Pesado
obj_tipo_pesado = ModeloVehiculoTipoPesado("Volvo FH16", "D16", "Blanco", "Diesel", 25, "Carga pesada")
print(obj_tipo_pesado.imprimir_info())
print("-----")
