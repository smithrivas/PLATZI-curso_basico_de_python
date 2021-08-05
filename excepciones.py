'''Al momento de poner el cero, nos arroja un error ZeroDivisionError
de tal manera que, usamos una excepción.

Así que corre el programa normalmente, excepto cuando el numero sea cero, 
en ese caso solo muestrame la lista'''


def divide_elementos(lista, divisor):
    try:
        return [l / divisor for l in lista]
    except ZeroDivisionError as e:
        print(e)
        return lista

lista = list(range(10))
divisor = int(input('Escribe un numero: '))

print(divide_elementos(lista, divisor))

# -----------------------------------------------------
# AFIRMACIONES

# def primera_letra(lista_de_palabras):
#     primeras_letras = []
    
#     for palabra in lista_de_palabras:
#         assert type(palabra) == str, f'{palabra} no es str'
#         assert len(palabra) > 0, 'no se permiten srt vacios'
        
#         primeras_letras.append(palabra[0].capitalize())
            
#     return primeras_letras