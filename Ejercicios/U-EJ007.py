# UDEMY EJERCICIO 7
# Programa que solicite al usuario los datos para calcular el área de un Círculo (●),
# finalmente mostrar el resultado en pantalla.
# Area = PI*(Radio**2)
import math

PI = math.pi
print("CALCULAR EL AREA DEL CÍRCULO")

print('Dame el radio de círculo: ')
radio = float(input('> '))

area = round(PI * math.pow(radio, 2), 3)

print(f'El área de un círculo de radio {radio} es {area}')