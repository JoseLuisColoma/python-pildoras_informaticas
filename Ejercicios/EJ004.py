# EJERCICIO 004
# determinar el menor número de N valores ingresados utilizan bucle FOR

n = int(input('Introduce la cantidad de números a ingresar: '))

# inicializando con el infinito
menor = float('inf')
while n <= 0:
    print('El número es incorrecto. Debe ser un número natural. Vuelve a intentarlo')
    n = int(input('Introduce la cantidad de números a ingresar: '))

for i in range(n):
    num = int(input('Introduce un número:  '))
    if num < menor:
        menor = num

print(f'Menor número de todos los ingresados = {menor}')
