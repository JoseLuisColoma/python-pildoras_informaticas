# Diccionarios
# Estructuras de datos que nos permiten almacenar valores de diferente tipo (numeros, cadenas de texto, booleanos)
# e incluso listas u otros diccionarios
# La principal caracteristica de los diccionarios es que los datos se almacena a una clave de tal forma que se crea una
# asociacion de CLAVE:VALOR para cada elemento almacenado
# Los elementos almacenados no están ordenados.
# El orden es indiferente a la hora de almacenar información en un diccionario

dic = {'España': 'Madrid', 'Alemania': 'Berlin', 'Francia': 'Paris', 'Inglaterra': 'Londres'}
# Agregar
print(dic['España'])
dic['Italia'] = 'Lisboa'
print(dic)
# Modificar
dic['Italia'] = 'Roma'
print(dic)
# ELiminar
del dic['Inglaterra']
print(dic)

dic2 = {'Alemania': 'Berlin', 23: 'Jordan', 'Mosqueteros': 3}
print(dic2)

mi_tupla = ('España', 'Francia', 'Inglaterra')
mi_diccionario = {mi_tupla[0]: 'Madrid', mi_tupla[1]: 'Paris', mi_tupla[2]: 'Berlin'}
print(mi_diccionario)

mi_lista = ['España', 'Francia', 'Inglaterra']
mi_dic2 = {mi_lista[0]: 'Madrid', mi_lista[1]: 'Paris', mi_lista[2]: 'Berlin'}
print(mi_dic2)

chicagoBulls = {23:'Jordan', 'Nombre': 'Michael', 'Equipo':'Chicago Bulls', 'anillos': {'temporadas': [1991,1992,1993,1996,1997,1998]}}
print( chicagoBulls)

print(chicagoBulls.keys())
print(chicagoBulls.values())
print(len(chicagoBulls))