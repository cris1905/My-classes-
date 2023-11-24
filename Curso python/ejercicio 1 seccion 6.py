##ejercicio 1 sección 6
# lista = [1,2,3,5,25,33,56,75,21,56,89,43,13,62,24]
# if 100 in lista:
#     print("está en la lista")
# else:
#     print("no está")


##como lo hizo el profe
# numero = 21
# if numero in lista:
#     print("está en la lista")
# else:
#     print("no está")   

## de otra forma
# num =int(input("digite un numero: "))
# if num in lista:
#     print("está en la lista")
# else:
#     print("no está")

 ####### ejercicio 2   
# tupla = ("Antonio","pedro","maria")
# print (tupla)
# dato = str (input("digite su nombre por favor: "))
# if dato in tupla:
#      print ("SI")
# else:
#     print ("NO")
### como lo hizo el profe
# tupla = ("Antonio","pedro","maria")
# print (tupla)
# dato = input ()
# if dato in tupla:
#      print ("SI")
# else:
#     print ("NO")
#### ejercicio #3
# conjunto = {1,2,3,4,5}
# print(conjunto)
# conjunto.add (6)
# conjunto.add (7)
# conjunto.add (8)
# conjunto.add (9)
# print(conjunto)
# conjunto.remove(9)
# print(conjunto)
# type(conjunto)
####ejercicio #4
diccionario = {"uno":"one","dos":"two","tres":"three"}
print (diccionario)
diccionario["cuatro"] = "four"
print(diccionario)
dato = str(input("digita un valor: "))
valor = diccionario[dato]
if dato in diccionario:
    print (valor)
else:
    print ("no está en el diccionario")    
    
