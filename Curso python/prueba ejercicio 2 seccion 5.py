minimo = 20
maximo = 500
dato = str(input("digita un valor: "))
numero = int(dato)
if numero < minimo:
	print("Valor bajo")
if numero > maximo:
	print("Valor alto")
if (numero > minimo) and (numero < maximo):
	print("valor medio")