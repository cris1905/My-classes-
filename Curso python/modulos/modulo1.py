class coche:
    def __init__(self,marca,color,combustible,cilindrada):
        self.marca = marca
        self.color = color
        self.combustible = combustible
        self.cilindrada = cilindrada

    def mos_caracteristicas(self):
        print ("Este coche es de la marca {} de color {} de {} y una cilindrada de {}"
              .format(self.marca,self.color,self.combustible,self.cilindrada))
# carro1 = coche ("honda","rojo","gasolina","1.6")
# carro1.mos_caracteristicas()  

#lambda 
resultado = lambda num1, num2, num3 : (num1+num2+num3)/3
resultado (4,5,6)
print(resultado)
