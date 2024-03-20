# EJERCICIO 006
# Mostrar por pantalla los números de Finobacci según sus n términos
# serie de Fibonacci: 1, 1, 2, 3, 5, 8, 13...
print('Programa que calcula los números de Fibonacci')

N = int(input('Introduce el número de términos de la serie: '))
x1 = 1
x2 = 1
for i in range(N):
    print(x1, end=', ')
    # Calculamos el siguiente término en la secuencia de Fibonacci
    sig_termino = x1 + x2

    # Actualizamos los valores de a y b para la siguiente iteración
    x1 = x2
    x2 = sig_termino
