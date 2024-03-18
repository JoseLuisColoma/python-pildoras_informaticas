# Tipos, operadores, variables
# TIPOS: Númericos (enteros, coma flotante, complejos), Textos (strings), booleanos(True/False)
# OPERADORES: Aritméticos: (+,+-,*,/,%,**,//), Comparacion (==, <, >, <=, >=, !=), Lógicos (AND, OR, NOT),
# Asignacion (=, +=, -=, *=, /=, **=, %=,//=), Especiales (IN, NOT IN, IS, IS NOT)
# Variable: Espacio de meoria del ordenador donde se almacena un valor que podrá cambiar durante la ejecución del programa
# En Python todo son objetos
num = '4'
print(type(num))

mensaje = '''Esto es un mensaje
con tres saltos
de línea'''
print(mensaje)

num1 = 5
num2 = 7

if num1 > num2:
    print('El numero 1 es mayor)')
else:
    print('El numero 2 es mayor')