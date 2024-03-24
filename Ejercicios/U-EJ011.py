# UDEMY EJERCICIO 11
# Escribir un programa que solicite al usuario un número entero y muestre en pantalla
# si el número es Positivo (+) o Negativo (-). En caso de que el número sea igual a cero (0)
# se debe mostrar en pantalla: El número no es Positivo ni Negativo.

num = int(input('Introduce un número entero: '))
if num > 0:
    print('El número es Positivo')
elif num < 0:
    print('El número es Negativo')
else:
    print('El número no es Positivo ni Negativo.')
