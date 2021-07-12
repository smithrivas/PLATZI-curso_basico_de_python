from typing import Mapping


def run():
    mi_diccionario = {
        'llave1': 1,
        'llave2': 2,
        'llave3': 3
    }

    #print(mi_diccionario['llave1'])

    poblacion_paises = {
        'Argentina': 44938712,
        'Brasil': 210147125,
        'Colombia': 50372424
    }

    # Extraer las llaves
    # for pais in poblacion_paises.keys():
    #     print(pais)

    # Extraer los valores
    # for pais in poblacion_paises.values():
    #     print(pais)

    # Extraer las llaves y los valores
    for pais, poblacion in poblacion_paises.items():
        print(pais+' tiene '+str(poblacion)+' habitantes.')


if __name__ == '__main__':
    run()