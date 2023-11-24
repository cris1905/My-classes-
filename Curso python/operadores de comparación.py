Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> ### opeadores de asignació
>>> #operadores de asignación
>>> ##(==,!=,>,<,>=,<=)
>>> num1 = 6
>>> num2 = 4
>>> num1 == num2
False
>>> num1 = 4.0
>>> num2 = 6.0
>>> type (num1)
<class 'float'>
>>> num2 = 5
>>> num2=4
>>> print (num2)
4
>>> num2 == num1
True
>>> cadena1 = "hola"
>>> cadena2 = "hola"
>>> cadena1 == cadena2
True
>>> cadena2 = "hello"
>>> cadena1 == cadena2
False
>>> if (cadena == "hola"):
	print ("dijo hola")

	
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    if (cadena == "hola"):
NameError: name 'cadena' is not defined
>>> if (cadena1 == "hola"):
	print ("dijo hola")

	
dijo hola
>>> # != distinto de
>>> num1 = 3
>>> num2 = 5
>>> num1 != num2
True
>>> num1 > num2
False
>>> num1 < num2
True
>>> num2 >= num1
True
>>> num2 <= num1
False
>>> 