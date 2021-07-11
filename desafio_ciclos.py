def run():
    import random
    print('Minijuego: Tienes 5 oportunidades para adivinar un número al azar entre 1 y 10.')        
    oportunidades = 5
    respuesta = random.randint(1, 10)
    numero = int(input('Por favor ingresa un número: '))
    
    while oportunidades > 0:                                                
        oportunidades -= 1        
        if numero == respuesta:            
            print('Felicitaciones, adivinaste el número oculto, la respuesta correcta es: '+str(respuesta))                
            break
        elif oportunidades == 0:            
            print('Game over!! el número correcto era: '+str(respuesta))        
            break
        numero = int(input('Número errado, por favor ingresa otro número: '))


if __name__ == '__main__':
    run()