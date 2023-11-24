# pickile - modulo para grabar ficheros binarios

import pickle

lista_de_colores = ["verde","azul","rojo","amarillo"]
fichero = open("fichero_colores.pckl","wb")

pickle.dump(lista_de_colores,fichero) #para grabar la lista de colores

fichero.close()                                                                                                                                                                 