# EJERCICIO 007
# Juego CHO HAN
# El juego tradicional japonés Cho Han consiste en titar 2 dados en vaso.
# Los jugadores deben adivinar si la suma de los dados en Cho (par) o Han (impar)
# Simular este juego en Python, donde un jugador ingresará cuanto dinero desea apostar en cada turno
# Cada jugador empieza en su billetera con 10€
# Si por ejemplo se apuesta 2€, si gana, tendrá 12. Si pierde, tendrá 8€.
# El juego termina cuando el jugador se queda a 0€ o cuando ingrese "no deseo continuar"
# Se deberá mostrar el juego de cada rondam el dinero que tiene en la billetera y al finalizar todas las rondas
# se deberá mostrar la cantidad de partidas que ganó el jugador
import random
import time
import sys


print('BIENVENIDO AL JUEGO "CHO HAN"')

contador_partidas = 0
cont_ganadas = 0

jugar = 'si'
terminar = 'no'

billetera = int(input('Introduce el dinero que quieres apostar: '))
print(f'Empiezas con {billetera}€')

while billetera > 0:

    def imprimir_animacion():
        for _ in range(3):  # Repetir 3 veces para imprimir tres puntos
            sys.stdout.write(".")  # Imprimir un punto
            sys.stdout.flush()  # Asegurarse de que el punto se muestra en la consola inmediatamente
            time.sleep(1)  # Esperar 1 segundo antes de imprimir el siguiente punto

    jugar = input('¿Deseas jugar una partida al "CHO HAN"?: ').lower()

    if jugar != terminar:
        apuesta_jugador = int(input('¿Cuánto dinero quieres apostar?: '))

        if apuesta_jugador <= billetera:
            print('La apuesta es correcta. Empezamos')
            time.sleep(1)

        else:
            print('No tienes suficiente dinero en la billetera para hacer la apuesta')
            continue

        resultado_jugador = input('¿Cómo crees que será el resultado, "PAR" o "IMPAR"?: ')
        resultado_jugador_form = resultado_jugador.upper()

        print('Tira los dados!')
        time.sleep(1)

        # Simular el lanzamiento del dado
        print("Lanzando los dados", end='', flush=True)
        imprimir_animacion()  # Llamar a la función para imprimir la animación de puntos
        print()  # Salto de línea después de la animación

        # Generar un valor aleatorio entre 1 y 6
        dado1 = int(random.randint(1, 6))
        dado2 = int(random.randint(1, 6))

        suma_dados = dado1 + dado2

        # Ver si el resultado es PAR o IMPAR
        if (dado1 + dado2) % 2 == 0:
            resultado = 'PAR'
        else:
            resultado = 'IMPAR'
        # Imprimir el resultado del lanzamiento del dado
        print(f'El resultado del lanzamiento del dado1 es: {dado1}')
        print(f'El resultado del lanzamiento del dado2 es: {dado2}')
        print(f'La suma es {suma_dados} y es {resultado}')

        time.sleep(2)

        if resultado_jugador_form == resultado:
            print('¡Has ganado!')
            billetera = billetera + apuesta_jugador * 2
            cont_ganadas += 1
        else:
            print('¡Has perdido!')
            billetera = billetera - apuesta_jugador

        print(f'Tienes en la billetera actualmente: {billetera}€')
        contador_partidas += 1

    else:
        print('FIN DEL JUEGO')
        print(f'Has jugado {contador_partidas} partidas')
        print(f'Has ganado {cont_ganadas} partidas')
        print(f'Actualmente en la billetera tienes {billetera}€')
        break




