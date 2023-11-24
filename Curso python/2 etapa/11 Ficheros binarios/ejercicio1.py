#ejercicio #1

import pickle

frutas = {"manzana":"aple","naranja":"orange","platano":"banana"}
frutas.values()

fichero = open("fichero1.pckl","wb")

pickle.dump(frutas,fichero)

fichero.close()

fichero2 = open("fichero1.pckl","rb")
diccionario = pickle.load(fichero2)

print(diccionario)

