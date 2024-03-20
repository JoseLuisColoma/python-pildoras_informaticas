# EJERCICIO 002
# Calcular la suma de TODOS LOS n números enteros ingresados, la suma de los pares
# y la suma de los impares

suma_total = 0
suma_pares = 0
suma_impares = 0

n = int(input('Introduce la cantidad de números a ingresar: '))
while n <= 0:
    print('El número es incorrecto. Debe ser un número natural. Vuelve a intentarlo')
    n = int(input('Introduce un número positivo: '))

while n > 0:
    num = int(input('Introduce un número: '))
    if num % 2 == 0:
        suma_pares += num
    else:
        suma_impares += num

    suma_total += num
    n = n - 1

print(f'suma total = {suma_total}')
print(f'suma pares = {suma_pares}')
print(f'suma impares = {suma_impares}')

