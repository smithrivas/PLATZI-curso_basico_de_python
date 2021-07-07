def conversacion(mensaje):
    print('Hola')
    print('Como estás')
    print(mensaje)
    print('Adios')

opcion = int(input('Elige una opcion: (1, 2, 3): '))
if opcion == 1:
    conversacion('Elegiste la opcion 1')
elif opcion == 2:
    conversacion('Elegiste la opcion 2')
elif opcion == 3:
    conversacion('Elegiste la opcion 3')
else:
    print('Elige una opcion correcta')

# def sumar(a, b):
#     print('Se sumarán 2 números: ')
#     suma = a + b
#     return suma

# resultado = sumar(4, 5)
# print(resultado)