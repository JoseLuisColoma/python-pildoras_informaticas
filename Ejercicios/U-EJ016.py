# UDEMY EJERCICIO 16
# Escribir un programa que solicite al usuario 3 números, compararlos y decir cual es mayor.

num1 = int(input('Introduce el número 1: '))
num2 = int(input('Introduce el número 2: '))
num3 = int(input('Introduce el número 3: '))

if num1 > num2:
    if num1 > num3:
        mayor = num1
    else:
        mayor = num3
else:
    mayor = num2

print(f'El mayor número de {num1}, {num2}, {num3} es: {mayor}')