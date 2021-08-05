# def main():
#     nombre = input('Por favor ingresa tu nombre: ')
#     respuesta = 'Hola '+nombre+' bienvenido'
#     print(f'{respuesta}, como dato curioso, el saludo incluido tu nombre contiene {len(respuesta)} caracteres.')


# if __name__ == '__main__':
#     main()
# ------------------------------------------------------------

# def main():
#     num1 = int(input('Ingresa un número entero: '))
#     num2 = int(input('Ingresa otro número entero: '))

#     if num1 > num2:
#         print('El primer número es mayor')
#     elif num1 < num2:
#         print('El segundo número es mayor')
#     else:
#         print('Los 2 números son iguales')

# if __name__ == '__main__':
#      main()
# -------------------------------------------------------------

# Nombre y edad de dos personas e indicar quien es mayor.

# def main():
#     nombre_1 = input('Ingresa el nombre de la primera persona: ')
#     edad_1 = int(input('Ingresa la edad de la primera persona: '))
#     nombre_2 = input('Ingresa el nombre de la segunda persona: ')
#     edad_2 = int(input('Ingresa la edad de la segunda persona: '))

#     if edad_1>edad_2:
#         print(f'{nombre_1} es mayor ya que tiene {edad_1} años y {nombre_2} tiene {edad_2} años.')
#     elif edad_1<edad_2:
#         print(f'{nombre_2} es mayor ya que tiene {edad_2} años y {nombre_1} tiene {edad_1} años.')
#     else:
#         print(f'Los dos tienen la misma edad ya que {nombre_1} tiene {edad_1} años y {nombre_2} también tiene {edad_2} años.')


# if __name__ == '__main__':
#     main()
# -------------------------------------------------------------------

# RAIZ CUADRADA

# objetivo = int(input('Ingresa un número entero: '))
# respuesta = 0

# while respuesta**2 < objetivo:
#     respuesta += 1

# if respuesta**2 == objetivo:
#     print(f'La raíz cuadrada de {objetivo} es {respuesta}.')
# else:
#     print(f'El número {objetivo} no tiene raíz cuadrada exacta.')


#----------------------------------------------------------

for i in range(1, 100, 2):
    print(i)