Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #cadena de texto
>>> cadena1 = "Hola"
>>> cadena2 = "mundo"
>>> print (cadena1 + cadena2)
Holamundo
>>> cadena3 = " "
>>> cadena= cadena1 + cadena3 + cadena2
>>> print cadena
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(cadena)?
>>> print (cadena)
Hola mundo
>>> #funciones de cadenas
>>> len (cadena)
10
>>> # la función len sirve para contar sus valores
>>> cadena.upper()
'HOLA MUNDO'
>>> cadena= cadena.upper()
>>> print (cadena)
HOLA MUNDO
>>> cadena.lower()
'hola mundo'
>>> cadena.split()
['HOLA', 'MUNDO']
>>> cadena5= "uva,manzana,cherrys,mango"
>>> cadena5.split(',')
['uva', 'manzana', 'cherrys', 'mango']
>>> cadena5.split()
['uva,manzana,cherrys,mango']
>>> cadena5.split[]
SyntaxError: invalid syntax
>>> cadena5.split([])
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    cadena5.split([])
TypeError: must be str or None, not list
>>> #imprimir variables en una cadena
>>> nombre= 'cristhian'
>>> apellido = "acosta"
>>> edad= "22"
>>> print("buen día {},feliz {}, cumpleaños".format(nombre,edad))
buen día cristhian,feliz 22, cumpleaños
>>> print ("buen día {}, feliz {} cumpleaños".format(nombre,edad))
buen día cristhian, feliz 22 cumpleaños
>>> total= 10/3
>>> print = total
>>> print (total)
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    print (total)
TypeError: 'float' object is not callable
>>> total = 10/3
>>> print (total)
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    print (total)
TypeError: 'float' object is not callable
>>> total = 10 / 3
>>> print (total)
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    print (total)
TypeError: 'float' object is not callable
>>> t1= float(10 / 3)
>>> print (t1)
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    print (t1)
TypeError: 'float' object is not callable
>>> n1 = 10
>>> n2 = 3
>>> nt= n1 / n2
>>> print (nt)
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    print (nt)
TypeError: 'float' object is not callable
>>> n3 = float(n1)
>>> n4 =float(n2)
>>> print (nt)
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    print (nt)
TypeError: 'float' object is not callable
>>> type n3
SyntaxError: invalid syntax
>>> type (n3)
<class 'float'>
>>> print (float(nt))
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    print (float(nt))
TypeError: 'float' object is not callable
>>> print (n3)
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    print (n3)
TypeError: 'float' object is not callable
>>> 