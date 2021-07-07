nombre = input('Ingresa un nombre: ')

# MAYUSCULA
print('Mayuscula: '+nombre.upper())
# MINUSCULA
print('Minuscula: '+nombre.lower())
# PRIMERA MAYUSCULA
print('Primera en mayuscula: '+nombre.capitalize())
# QUITAR ESPACIOS
print('Quitar espacios: '+nombre.strip())
# REEMPLAZAR
print('Reemplazar letras: '+nombre.replace('a', 'o'))
# POSICION DE LA LETRA
print('Posicion de un caracter: '+nombre[0])
# CANTIDAD DE CARACTERES
print('Cantidad de caracteres: ' + str(len(nombre)))


# DIVIDIR UNA CADENA DE TEXTO
print('Dividir texto: '+nombre[0:3])
print('Dividir texto de dos en dos: '+nombre[0:4:2])
print('Orden inverso del orden de las letras: '+nombre[::-1])