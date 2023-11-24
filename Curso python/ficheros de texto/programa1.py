import moduloficheros

nombre_fichero = 'fichero1.txt'
fichero = moduloficheros.Fichero(nombre_fichero)

texto = 'Esta es la primavera fila del fichero.\nEsta será la segunda fila.'
fichero.grabar_fichero(texto)

texto = '\nEste es un texto incluido en la tercera fila'
fichero.incluir_fichero(texto)

texto_leido = fichero.leer_fichero()
print(texto_leido)