# expreciones regulares (search, findall, split, sub)
import re
# texto = "Hola, mi nombre es antronio"
# resultado = re.search("nombre",texto)

# if (resultado):
#  	print("cadena encontrada")
# else:
# 	print("cadena no encontrada")

# re.search("^antronio$",texto) para buscar una frase que acabe con antronio
# re.search("hola",texto) para buscar una linea dentro de la cadena de texto que empiece por hola
# re.search("mi.*es",texto) para buscar un patron en una cadena

#findall busca todas las ocurrncias en una cadena de texto

texto = """
El coche de luis es rojo,
el coche de juan es blanco,
y el conche de marta es rojo
"""
re.findall("conche.*rojo", texto)
