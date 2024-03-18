# LISTAS
# Estructura de datos que nos permite almacenar gran cantidad de valores
# (equivalente a los arrays en otros lenguajes de programación)
# En Python las listas pueden ser de diferentes tipos de valores (en otros lenjuajes esto no ocurre con los array)
# Se pueden expandir dinámicamente añadiendo elementos nuevos (otra novedad respecto a los arrays en otros lenguajes)
# nombre_lista = [elem1, elem2, elem3...]
# Los elementos de las listas tienen que ser identificables --> indice

lista = ['Maria','Pepe', 'Marta', 'Antonio']
print(lista)
print(lista[:])
print(lista[2])
print(lista[-2])

# porcion de lista
print(lista[0:3])
print(lista[:3])
print(lista[2:])

# APPEND Para agregar elementos a una lista (lo agrega en el último lugar):
lista.append('Pepe')
print(lista)

# INSERT


# EXTEND Agrega a una lista otra lista u otros elementos


# INDEX (para que nos devuelva el índice del elementos de una lista)
print(lista.index('Maria'))

# IN para ver si un elemento se encuentra en una lista
print ('Pepe' in lista)

lista2 = ['María', 5, True, 80.34]

# REMOVE Eliminar elementos
lista2.remove(5)
print(lista2)

# POP ELimina el último elemento
lista2.pop()
print(lista2)

#Operador suma como contatenador de dos listas
lista3 = lista + lista2
print(lista3)

# Operador multiplicacion
lista4 = lista3*2
print(lista4)


