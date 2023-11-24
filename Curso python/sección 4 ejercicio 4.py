Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> ##seción 5 ejercicio 4
>>> print ("introduce el pri")
introduce el pri
>>> dato1=str(input("Introduce el primer número"))
Introduce el primer número
>>> 
>>> 4
4
>>> dato1=str(input("Introduce el primer número: "))
Introduce el primer número: 4
>>> print dato1
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(dato1)?
>>> print (dato1)
4
>>> dato2=str(input("Introduce el primer número: "))
Introduce el primer número: 5
>>> type (dato2)
<class 'str'>
>>> num1= int(dato1)
>>> type (num1)
<class 'int'>
>>> num2 = int(dato2)
>>> suma= num1 + num2
>>> print (suma)
9
>>> strsuma= str (suma)
>>> type (strsuma)
<class 'str'>
>>> resultado = ("La suma es" + strsuma)
>>> print (resultado)
La suma es9
>>> resultado = (" La suma es " + strsuma)
>>> print (resultado)
 La suma es 9
>>> 