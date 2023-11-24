class Fichero:
	def __init__(self,nombre):
		self.nombre = nombre
		self.nombre = nombre

	def grabar_fichero(self,texto):
			Fichero = open(self.nombre,"wt")
			Fichero.write(texto)
			Fichero.close()


	def incluir_fichero(self,texto):
			Fichero = open(self.nombre,"at")
			Fichero.write(texto)
			Fichero.close()

	def leer_fichero(self):
			Fichero = open(self.nombre,"rt")
			texto = Fichero.read()
			return texto					