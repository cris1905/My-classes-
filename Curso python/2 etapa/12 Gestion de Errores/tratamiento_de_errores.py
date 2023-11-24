# try .... except... else....finally

try:
	num1 = 5
	num2 = 0
	division = num1 / num2
	print (division)

except ZeroDivisionError:
	print("Error, división entre cero")
except:
	print("hay un error")
else:
	print("La operación funcionó correctamente")
finally:
	print("Esta prueba del try ha terminado")


