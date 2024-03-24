# UDEMY EJERCICIO 14
# Introducir un número por teclado y que se muestre un mensaje indicando si es múltiplo de 3.

num = int(input('>>> Introduce un número por teclado: '))
if num % 3 == 0 and num != 0:
    print('El número es múltiplo de 3')
elif num % 3 != 0:
    print('El número no es múltiplo de 3')
else:
    print('El número es el 0 y no es múltiplo de 3')