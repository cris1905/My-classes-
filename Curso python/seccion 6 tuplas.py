Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> ###listas
>>> colors = ["rojo","amarillo","verde"]
>>> colors.("azul")
SyntaxError: invalid syntax
>>> colors.append("azul")
>>> colors.remove("amarillo")
>>> print ("verde")
verde
>>> print (colors)
['rojo', 'verde', 'azul']
>>> colors[1] = "naranja"
>>> print (colors)
['rojo', 'naranja', 'azul']
>>> colors[1].remove
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    colors[1].remove
AttributeError: 'str' object has no attribute 'remove'
>>> colors.remove[1]
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    colors.remove[1]
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> colors.remove(1)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    colors.remove(1)
ValueError: list.remove(x): x not in list
>>> colors.append("amrillo")
>>> colors.append("morado")
>>> print (colors)
['rojo', 'naranja', 'azul', 'amrillo', 'morado']
>>> for color in colors:
	print(color)

	
rojo
naranja
azul
amrillo
morado
>>> 
>>> colors.clear
<built-in method clear of list object at 0x00000184389A2640>
>>> print (colors)
['rojo', 'naranja', 'azul', 'amrillo', 'morado']
>>> colors.remove([1])
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    colors.remove([1])
ValueError: list.remove(x): x not in list
>>> colors.clear()
>>> print(colors)
[]
>>> 