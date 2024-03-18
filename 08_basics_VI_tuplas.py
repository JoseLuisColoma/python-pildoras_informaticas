# TUPLAS
# Las tuplas son listas inmutables, es decir, no se pueden modificar después de su creación.
# No se permiten añadir, eliminar o mover elementos (no append, no extend, no remove)
# Si permiten extraer pociones, pero el resultado de la extracción es una tupla nueva.
# Sí permiten búsquedas (método index). Desde la versión 2.7
# Sí permiten comprobar si un elemento se encuentra en una tupla
# ¿Qué utilidad o ventaja tienen sobre las listas?
# Más rápidas
# Menos espacio (mayor optimización)
# Formatean Strings
# Pueden utilizarse como claves en un diccionario (las listas no)
# tupla --> nombreTupla = (elem1, elem2, elem3...)
# pueden también escribirse sin parentesis, con comas, pero no es aconsejable
# método list: para convettir tuplas en listas
# método tuple: para convertir listas en tuplas.
# método count. Cuenta los elemetos que indiquemos
# método len: longitud de una tupla.
# tuplas unitarias. Tuplas con un único elemento: elemento más una coma
# empaquetado (desempaquetado) de tupla

mi_tupla0 = 1, 2, 4
mi_tupla = ('Jose', 13, 1, 1995)
print(type(mi_tupla0))
print(type(mi_tupla))

print(mi_tupla[0])

mi_lista = list(mi_tupla)
print(mi_lista)
print(mi_tupla)

mi_tupla2 = tuple(mi_lista)

print ('Jose' in mi_tupla2)

print(mi_tupla2.count('Jose'))

mi_tupla3 = ('Jose',)
print(len(mi_tupla3))

print(len(mi_lista))
#desempaquetado de tuplas
nombre, dia, mes, anyo = mi_tupla
print(nombre)
print(dia)
print(mes)
print(anyo)
# Empaquetado de tuplas
mi_tupla5 = (nombre, dia, mes, anyo)
print(mi_tupla5)

print(mi_tupla5.index('Jose'))