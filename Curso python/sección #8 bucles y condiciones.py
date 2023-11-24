###### condiciones if ...else
# a= 8
# b= 4
# c=2
# d=6
# if (a>b):
#     print("a es mayor que b")
# if (a>b) and (d>c):
#     print("la primera expresión es correcta")
# if (a>c) and (b>d):
#     print("la primera expresión es correcta")
# else:
#     print("la primera expresión no es correcta")
# if (a>b):
#     print("a es mayor que b")
# elif (a == b):
#     print ("a es igual que b")
# else:
#     print("ninguna expresión es correcta")   
# bucle for 
# colores = ["rojo","verde","äzul"]
# for color in colores:
#     print(color)
# cadena = "hola mundo"
# for caracter in cadena:
#     print(caracter) 
# range(0,8)
# for numero in range (8):
#     print(numero)
# for numero in range (3,8,2):
#     print(numero)

########
#########break para el bucle
# for numero in range (10):
#     if numero ==5:
#         break
#     print(numero)

##### continue - para parar solo la interación actual 
# for numero in range(10):
#     if (numero ==6): ## si el numero es 6 no continues
#         continue
#     print(numero)

###### for doble
# for num1 in range(4):
#     for num2 in range (3):
#         print(num1,num2)

#### while 
# valor = 1 
# fin = 10
# while (valor < fin):
#     print (valor)
#     valor=valor + 1

# valor = 1 
# fin = 10
# while (valor < fin):
#     print (valor)
#     valor=valor + 1
#     if (valor == 5):
#         break

######## continue 
# while (valor < fin):
#     valor = valor + 1
#     if (valor == 6):
#         continue
#     print(valor)

### ejejrcio 1 
# diccionario = {"manzana":"aple","naranja":"orange","platano":"babana","limon":"lemon"}
# print (diccionario["naranja"])
# diccionario["piña"] = "pineapple"
# for clave in diccionario:
#     print(clave)

############### como lo hizo el profe
# print (diccionario["naranja"])
# diccionario["piña"] = "pineapple"
# for clave,valor in diccionario.items():
#     print("{} en ingles es {}".format(clave,valor))


##############
######ejercicio 2 

# nota = 4.5
# trabajo_realizado = 'si'
# if (nota >= 4) and (trabajo_realizado == 'si'):
#     nota_final= 'aprovado'
# else:
#     nota_final = 'suspenso'   
# print (nota_final)   

##############3
#ejercicio 3

inicio = 1
fin =6 
while (inicio < fin):
    print ("Esto es la fila  {}".format(inicio))
    inicio = inicio + 1
    if (inicio == 6):
        break


######## como lo hizo el profe
# inicio = 1
# fin =6   
# while (inicio < fin):
#     texto = "Esta es la fila " + str(inicio)
#     print(texto)
#     inicio = inicio + 1 