# UDEMY EJERCICIO 15
# Escribir un programa que solicite al usuario una letra y diga si esta es MAYÚSCULA o minúscula.
# (con código ASCII)

letra = input('Introduce una letra: ')
if letra >= 'A' and letra <= 'Z':
    print(f'La letra {letra} es MAYÚSCULA')
elif letra >='a' and letra<= 'z':
    print(f'La letra {letra} es MINÚSCULA')
else:
    print('El valor introducido no es un letra')