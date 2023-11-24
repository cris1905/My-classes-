Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> num1 = 5
>>> num2 = 3
>>> suma = num1+num2
>>> strsuma = str(suma)
>>> print "El resustado es",strsuma"
SyntaxError: Missing parentheses in call to 'print'. Did you mean print("El resustado es",strsuma")?
>>> print "el resultado" + strsuma
SyntaxError: Missing parentheses in call to 'print'. Did you mean print("el resultado" + strsuma)?
>>> print ("el resultado es",strsuma)
el resultado es 8
>>> 