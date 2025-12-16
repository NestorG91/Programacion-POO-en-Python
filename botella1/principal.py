from base_datos import Base_datos
from modelo_botella import  botella 

obj_base_datos = Base_datos()
material = input("Ingrese el material de la botella (plástico/vidrio): ").strip().lower()
diseño = input("Ingrese el diseño de la botella: ").strip()
tinte = input("Ingrese el tinte de la botella: ").strip()

obje_botella = (material, diseño, tinte)
obj_base_datos.guardar_objeto(obje_botella)