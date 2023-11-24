Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> fruit1 = ["manzana","pera"]
>>> friut2 = ["manzana","pera"]
>>> fruit = fruit1
>>> fruit is fruit1
True
>>> fruit.append("naranja")
>>> fruit
['manzana', 'pera', 'naranja']
>>> fruit1
['manzana', 'pera', 'naranja']
>>> ['manzana', 'pera', 'naranja']
['manzana', 'pera', 'naranja']
>>> 
>>> fruit is not fruit1
False
>>> fruit is not fruit2
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    fruit is not fruit2
NameError: name 'fruit2' is not defined
>>> fruit is not friut2
True
>>> `## operadores de pertenencia
SyntaxError: invalid syntax
>>> ## operadores de pertenencia
>>> ### (in, not in)
>>> frutas = ["manzana","pera","naranja"]
>>> frutas = "pera"
>>> frutas = ["manzana","pera","naranja"]
>>> frutas1 = "pera"
>>> frutas1 in frutas
True
>>> frutas1 not in frutas
False
>>> frutas2 = "melocoton"
>>> frutas2 not in frutas
True
>>> 