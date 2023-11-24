Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> ##operadores lógicos (and, or , not)
>>>  num1 = 4
 
SyntaxError: unexpected indent
>>> num1 = 4
>>> num2 = 6
>>> num3 = 7
>>> num4 = 8
>>>  num1 > num2
 
SyntaxError: unexpected indent
>>> num1 > num2
False
>>> num3 > num4
False
>>> (num1 > num2) and (num1 < num2)
False
>>> (num1 < num2) and (num3 < num2)
False
>>> ## operador or
>>> #sirve para saber si si uno de los dos es verdadero
>>> (num1 < num2) or (num3 < num2)
True
>>> (num1 > num2) and (num3 < num2)
False
>>> (num1 < num2) and (num3 > num2)
True
>>> ##operador not
>>> ###No al valor
\
>>> not (num1 < num2)
False
>>> not (num1 > num2)
True
>>> 