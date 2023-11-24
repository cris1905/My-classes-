Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>>  cadena1 = "hola"
 
SyntaxError: unexpected indent
>>> 
>>> 
>>> cadena1 = "hola"
>>> cadena2 = "mundo"
>>> cadenanew = cadena1 + cadena2
>>> print (cadenanew)
holamundo
>>> cadenanew
'holamundo'
>>> num1 = 5
>>> num2 = 2
>>> type(num1)
<class 'int'>
>>> num = 5
>>> cadena = str(hola)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    cadena = str(hola)
NameError: name 'hola' is not defined
>>> num = 5
>>> cadena = str(num)
>>> print (cadena)
5
>>> # conversiones de  tipos de datos
>>> cadena = 23
>>> num = str(cadena)
>>> print (cadena)
23
>>> cadena2 = '24'
>>> type(cadena)
<class 'int'>
>>> type(cadena2)
<class 'str'>
>>> nu3= int(cadena2)
>>> print (cadena2)
24
>>> type(nu3)
<class 'int'>
>>> print (nu3)
24
>>> num4 = float(nu3)
>>> print(num4)
24.0
>>> 