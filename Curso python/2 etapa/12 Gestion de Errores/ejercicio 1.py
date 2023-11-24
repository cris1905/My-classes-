#ejercicio 1

# try:
# 	num1 = 6
# 	num2 = 3
# 	num3 = 3
# 	operacion = num1 - num2
# 	operacion1 = operacion / num3 
# 	print (operacion1	)

# except ZeroDivisionError:
# 	print("Error, división entre cero")
# except:
# 	print("hay un error")
# else:
# 	print("La operación funcionó correctamente")
# finally:
# 	print("Esta prueba del try ha terminado")


## ejerecicio profesor
def operacion(nume1,nume2,nume3):
	resultado = nume1 / (nume2 - nume3)
	return resultado

nume1 = 6
nume2 = 3
nume3 = 3
try:
	resultado = operacion(nume1,nume2,nume3)
    print(resultado)
except:
	print ("Error. los ultimos numero debenm estar diferentes")
