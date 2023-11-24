# # clases y objetos poo
# class ClaseSilla:
#     color = "blanco"
#     precio = 100

# objetoSilla1 = ClaseSilla()
# objetoSilla1.color
    

#  class persona:
#      def __init__(self,nombre,edad):
#          self.nombre = nombre
#          self.edad = edad

#     def saludar (self):
#         print("hola, me llamo {} y tengo {} años".format(self.nombre,self.edad))



# persona1= persona ("juan",35)
# persona1.saludar()    
colores = ["rojo","verde","azul"]

def incluir_color(colores,color):
    colores.append(color)

color = "negro"
incluir_color(colores,color)
print (colores)            