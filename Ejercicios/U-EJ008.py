# UDEMY EJERCICIO 8
# Programa que solicite al usuario los datos para llevar Grados Farenheit a Grados Celcius.
# celcius = (fahrenheit - 32.0) * 5.0 / 9.0

print("CONVERSOR DE GADOS FAHRENHEIT A CELSIUS")

print('Dame los grados en Farenheit: ')
fahrenheit = float(input('> '))

celsius = round((fahrenheit - 32.0) * 5.0 / 9.0, 1)

print(f'{fahrenheit} grados fahrenheit son {celsius} grados celsius')