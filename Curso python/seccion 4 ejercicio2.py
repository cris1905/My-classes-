Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> cadena = "Esto es un texto de ejemplo"
>>> longitud = len(cadena)
>>> print (longitud)
27
>>> strlongitud = str(longitud)
>>> print (strlongitud)
27
>>> type(strlongitud)
<class 'str'>
>>> mayusculas = cadena.upper()
>>> print (mayusculas)
ESTO ES UN TEXTO DE EJEMPLO
>>> resultado = (mayusculas + "tiene longitud de" + srtlongitud)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    resultado = (mayusculas + "tiene longitud de" + srtlongitud)
NameError: name 'srtlongitud' is not defined
>>> resultado = (mayusculas, "tiene longitud de" ,strlongitud)
>>> print (resultado)
('ESTO ES UN TEXTO DE EJEMPLO', 'tiene longitud de', '27')
>>> resultado = (mayusculas, 'tiene longitud de' ,strlongitud)
>>> print (resultado)
('ESTO ES UN TEXTO DE EJEMPLO', 'tiene longitud de', '27')
>>> resultado = (mayusculas + 'tiene longitud de' + strlongitud)
>>> print (resultado)
ESTO ES UN TEXTO DE EJEMPLOtiene longitud de27
>>> resultado = (mayusculas + ' tiene longitud de ' + strlongitud)
>>> print (resulltado)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    print (resulltado)
NameError: name 'resulltado' is not defined
>>> 
>>> print (resultado)
ESTO ES UN TEXTO DE EJEMPLO tiene longitud de 27
>>> 