# UDEMY EJERCICIO 6
# Programa que solicite al usuario los datos para calcular el área de un Triángulo (▲),
# finalmente mostrar el resultado en pantalla.
# Area = (Base*Altura)/2

print("CALCULAR EL AREA DEL TRIANGULO")

print('Dame la base del triángulo: ')
base = float(input('> '))
print('Dame la altura del triángulo: ')
altura = float(input('> '))

area = (base * altura)/2

print(f'El área de un triángulo de base {base} y altura {altura} es {area}')
