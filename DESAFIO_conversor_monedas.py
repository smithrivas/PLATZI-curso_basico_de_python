# PRIMERA VERSION
# dolares = input("驴Cuantos dolares tienes? ")
# dolares = float(dolares)
# valor_dolar = 3875
# pesos = dolares*valor_dolar
# pesos = int(pesos)
# pesos = str(pesos)
# print("Tienes $"+pesos+" pesos")

# SEGUNDA VERSION
# menu = """
# Bienvenido al conversor de monedas 馃挵

# 1 - Pesos Colombianos
# 2 - Pesos Argentinos
# 3 - Pesos Mexicanos

# Elige una opci贸n: """

# opcion = input(menu)

# if opcion == '1':
#     pesos = input("驴Cu谩ntos pesos Colombianos tienes? ")
#     pesos = float(pesos)
#     valor_dolar = 3875
#     dolares = pesos / valor_dolar
#     dolares = round(dolares, 2)
#     dolares = str(dolares)
#     print("Tienes $"+dolares+" d贸lares")
# elif opcion == '2':
#     pesos = input("驴Cu谩ntos pesos Argentinos tienes? ")
#     pesos = float(pesos)
#     valor_dolar = 65
#     dolares = pesos / valor_dolar
#     dolares = round(dolares, 2)
#     dolares = str(dolares)
#     print("Tienes $"+dolares+" d贸lares")
# elif opcion == '3':
#     pesos = input("驴Cu谩ntos pesos Mexicanos tienes? ")
#     pesos = float(pesos)
#     valor_dolar = 24
#     dolares = pesos / valor_dolar
#     dolares = round(dolares, 2)
#     dolares = str(dolares)
#     print("Tienes $"+dolares+" d贸lares")
# else:
#     print('Por favor ingresa una opci贸n correcta.')

# TERCERA VERSION
def conversor(tipo_moneda, valor_dolar):
    pesos = input("驴Cu谩ntos pesos " + tipo_moneda + " tienes? ")
    pesos = float(pesos)    
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $"+dolares+" d贸lares")

menu = """
Bienvenido al conversor de monedas 馃挵

1 - Pesos Colombianos
2 - Pesos Argentinos
3 - Pesos Mexicanos

Elige una opci贸n: """

opcion = input(menu)

if opcion == '1':
    conversor('pesos Colombianos', 3875)
elif opcion == '2':
    conversor('pesos Argentinos', 65)
elif opcion == '3':
    conversor('pesos Mexicanos', 24)
else:
    print('Por favor ingresa una opci贸n correcta.')