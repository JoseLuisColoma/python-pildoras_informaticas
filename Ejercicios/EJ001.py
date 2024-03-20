# EJERCICIO 001
# Calcular la suma de los cuadrados de los n primeros numeros naturales,
# teniendo en cuenta que los n números deben ser positivos

suma_total = 0
num = int(input('Introduce un número positivo: '))
while num <= 0:
    print('El número es incorrecto. Debe ser un número natural. Vuelve a intentarlo')
    num = int(input('Introduce un número positivo: '))

for n in range(1, num+1):
    elevar_cuadrado = n ** 2
    suma_total += elevar_cuadrado

print(f'La suma de los cuadrados de los n primeros números naturales es: {suma_total}')