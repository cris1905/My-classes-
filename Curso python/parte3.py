Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> resultado = 10 / 3
>>> print (resultado)
3.3333333333333335
>>> print ("el resultado es {r:1.2}" .format(r=resultado))
el resultado es 3.3
>>> print ("el resultado es {r:1.3}" .format(r=resultado))
el resultado es 3.33
>>> #f-strings
>>>  nombre = "antonio"
 
SyntaxError: unexpected indent
>>> nombre = "antonio"
>>> edad = "22"
>>> print ("Buenos dias {nombre}, feliz {edad} cumpleaños")
Buenos dias {nombre}, feliz {edad} cumpleaños
>>> print(f"Buenos dias {nombre}, feliz {edad})
      
SyntaxError: EOL while scanning string literal
>>> print(f"Buenos dias {nombre}, feliz {edad}")
Buenos dias antonio, feliz 22
>>> print(f"Buenos dias {nombre}, feliz {edad} cumpleaños")
Buenos dias antonio, feliz 22 cumpleaños
>>> print (f"Buenos dias {nombre}, feliz {edad} cumpleaños")
Buenos dias antonio, feliz 22 cumpleaños
>>> print("introduce un nombre")