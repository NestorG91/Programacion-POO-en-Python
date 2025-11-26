from modelo_botella import botella
from modelo_botella_plastico import botella_plastica
#+++++++++codigo principal++++++++++
#aqui va la logica del negocio

#instancia del padre
objbotella = botella("Pepsi", "1.5L", "Azul")
objbotella.imprimir_info()
#instancia hija
objbotella_plastica = botella_plastica("CocaCola", "2L", "Roja", "Redondo", "Plastico PET", "Sin tinte")
dato_out = objbotella_plastica.imprimir_info() 
print(dato_out)