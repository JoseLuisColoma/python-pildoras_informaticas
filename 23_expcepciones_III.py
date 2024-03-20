# Lanzamiento de Expcepciones
# Instrucción RAISE
# Creación de excepciones propias (más adelante en el curso cuando veamos POO)

# Ejemplo 1

import math

def evalua_edad(edad):
    if edad < 0:
        raise TypeError('No se permiten edades negativas')
    if edad < 20:
        return 'eres muy joven'
    elif edad < 40:
        return 'eres joven'
    elif edad < 65:
        return 'eres maduro'
    elif edad < 100:
        return 'Cuídate...'


print(evalua_edad(20))

# Ejemplo 2


def calcula_raiz(num):
    if num < 0:
        raise ValueError('El número no puede ser negativo')
    else:
        return math.sqrt(num)


op1 = int(input('Introduce un número: '))

try:
    print(calcula_raiz(op1))
except ValueError as ErrorDeNumeroNegativo:
    print(ErrorDeNumeroNegativo)

print('Programa terminado')
