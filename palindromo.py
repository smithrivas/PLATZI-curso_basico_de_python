def palindromo(palabra):    
    palabra = palabra.lower().replace(' ','')    
    return palabra == palabra[::-1]


def run():
    palabra = input("Escribe una palabra para validar si es un palindromo: ")    
    if palindromo(palabra):
        print('Es un palindromo')
    else:
        print('No es un palindromo')


if __name__ == '__main__':
    run()