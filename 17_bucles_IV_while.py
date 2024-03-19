# Bucle While . Indeterminado
# While condicion: \cuerpo del bucle
# ojo con los bucles infinitos (un bucle en el que la condicion siempre es verdadera)
import math

i = 1
while i <= 3:
    print('ejecución ' + str(i))
    i += 1
print('Terminó la ejecución')

# Programa que pregunte la edad. Si la edad es negativa lo vuelve a preguntar hasta que nos dé una edad positiva

edad = int(input('Intruduce tu edad: '))
while edad < 5 or edad > 100:
    print('La edad es incorrecta. Vuelve a intentaarlo')
    edad = int(input('Intruduce tu edad: '))
print(f'Tienes {edad} años')

# Calcular la raiz cuadrada de un número
print('Programa de cálculo de raíz cuadrada')
num = float(input('Introduce un número, por favor: '))
intentos =0
while num < 0:
    print('No se puede hallar la raíz cuadrada de un número negativo')
    if intentos == 3:
        print('Has consumido demasiados intentos. el programa ha finalizado')
        break
    num = float(input('Introduce un número positivo: '))
    if num < 0:
        intentos += 1

if intentos < 3:
    resultado = math.sqrt(num)
    print(f'La raiz cuadrada de {num} es {round(resultado, 2)}')

