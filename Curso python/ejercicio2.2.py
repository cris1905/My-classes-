Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> fruta = "banana"
>>> fruta[:3]
'ban'
>>> fruta[1:4]
'ana'
>>> cadena = "Esto es un texto de ejemplo"
>>> len(cadena)
27
>>> cadena[15:20]
'o de '
>>> cadena [11:15]
'text'
>>> cadena [11:16]
'texto'
>>> # tarea 1 hecha
>>> cadena [0:3]
'Est'
>>> #tarea 2
>>> Longitud = cadena
>>> strolongitud = str(longitud)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    strolongitud = str(longitud)
NameError: name 'longitud' is not defined
>>> strolongitud = str(Longitud)
>>> mayuscula = cadena.upper()
>>> resultado = mayuscula + strlomgitud
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    resultado = mayuscula + strlomgitud
NameError: name 'strlomgitud' is not defined
>>> resultado = mayuscula + strolongitud
>>> print resultado
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(resultado)?
>>> resultado= (mayuscula,"con el texto",strolongitud)
>>> print (resultado)
('ESTO ES UN TEXTO DE EJEMPLO', 'con el texto', 'Esto es un texto de ejemplo')
>>> longitud = len(cadena)
print (longitud)



