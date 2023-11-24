Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> ##tuplas
>>> tupla_colors = ("verde","amarillo","azul")
>>> for color in tupla_colors:
	print(color)

	
verde
amarillo
azul
>>> ##en las tuplas no se pueden modifiicar elementos.
>>> tupla_colors[2]
'azul'
>>> tupla_colors[2]
'azul'
>>> len(tupla_colors)
3
>>> ########conjuntos
>>> colores = {"marron","verde","celeste","azul"}
>>> print (colores)
{'marron', 'verde', 'azul', 'celeste'}
>>> colores.add("negro")
>>> print (colores)
{'verde', 'celeste', 'marron', 'azul', 'negro'}
>>> for color in colores:
	print (color)

	
verde
celeste
marron
azul
negro
>>> colores.remove("marron")
>>> print (colores)
{'verde', 'celeste', 'azul', 'negro'}
>>> colores.add("amarillo")
>>> print ("colores")
colores
>>> print (colores)
{'verde', 'celeste', 'amarillo', 'azul', 'negro'}
>>> print.__format__(colores)
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    print.__format__(colores)
TypeError: __format__() argument must be str, not set
>>> 