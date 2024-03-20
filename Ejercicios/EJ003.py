# EJERCICIO 003
# Calcular el PRODUCTO de todos los n números enteros ingresados, el producto de los pares
# y el producto de los impares

producto_total = 1
producto_pares = 1
producto_impares = 1

n = int(input('Introduce la cantidad de números a ingresar: '))

while n <= 0:
    print('El número es incorrecto. Debe ser un número natural. Vuelve a intentarlo')
    n = int(input('Introduce un número positivo: '))

for i in range(1, n+1):
    num = int(input('Introduce un número:  '))
    if num % 2 == 0:
        producto_pares *= num
    else:
        producto_impares *= num

    producto_total *= num

print(f'Producto total = {producto_total}')
print(f'Producto pares = {producto_pares}')
print(f'Producto impares = {producto_impares}')
