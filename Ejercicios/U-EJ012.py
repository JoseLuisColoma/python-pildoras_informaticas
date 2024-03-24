# UDEMY EJERCICIO 12
# Escribir un Programa que solicite al usuario la edad de 2 personas, y diga cuál es mayor.
# Ejemplo: - La Primera persona es mayor!
# Si la edad de ambos es igual se muestra el siguiente mensaje: - Ambos tienen la misma edad!

edad1 = int(input('Introduce la edad de la persona 1: '))
edad2 = int(input('Introduce la edad de la persona 2: '))
if edad1 > edad2:
    print('- La Primera persona es mayor!')
elif edad1 < edad2:
    print('- La Segunda persona es mayor!')
else:
    print('- Ambos tienen la misma edad!')