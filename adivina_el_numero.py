import random


def run():
    numero_aleatorio = random.randint(1,100)
    numero_elegido = int(input('Elige un número entre 1 y 100: '))
    while numero_elegido != numero_aleatorio:
        if numero_elegido < numero_aleatorio:
            print('Incorrecto, elige un número más grande')
        else:
            print('Incorrecto, elige un número más pequeño')
        numero_elegido = int(input('Ingresa otro número: '))
    print('¡Ganaste!')


if __name__ == '__main__':
    run()