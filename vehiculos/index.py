from modelo_vehiculo_Minivan import ModeloVehiculoMinivan
from modelo_vehiculo_Deportivo import ModeloVehiculoDeportivo
from modelo_vehiculo_TipoPesado import ModeloVehiculoTipoPesado
from base_datos_vehiculos import BaseDatosVehiculos
from modelo_vechiculos import Vehiculos

if __name__ == "__main__":
    bd = BaseDatosVehiculos()

    v1 = Vehiculos("Toyota", "V8", "Gris", "Gasolina")
    v2 = ModeloVehiculoDeportivo("Ferrari", "V8 Turbo", "Rojo", "Gasolina", "Superdeportivo", 340)
    v3 = ModeloVehiculoMinivan("Honda Odyssey", "V6", "Blanco", "Gasolina", 7, 4)
    v4 = ModeloVehiculoTipoPesado("Volvo FH16", "D16", "Amarillo", "Diesel", 25, "Carga pesada")

    print(bd.guardar_vehiculo(v1))
    print(bd.guardar_vehiculo(v2))
    print(bd.guardar_vehiculo(v3))
    print(bd.guardar_vehiculo(v4))

    print("\n--- VEHÍCULOS DEPORTIVOS ---")
    for v in bd.listar_deportivos():
        v.imprimir_info()

    print("\n--- VEHÍCULOS MINIVAN ---")
    for v in bd.listar_minivan():
        v.imprimir_info()

    print("\n--- VEHÍCULOS PESADOS ---")
    for v in bd.listar_tipo_pesado():
        v.imprimir_info()