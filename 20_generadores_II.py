# instrucción yield from
# Utilidad: Simplificar el código de los generadores en el caso de utilizar bucles anidades.
# un * delante de un argumento de una función indica al programa que va a recibir un número indeterminado de elementos
# y que esos argumentos que no sabemos cuántos son los va a recibir en forma de TUPLA

# Función tradicional
def devuelve_ciudades(*ciudades):
    for elemento in ciudades:
        for subelemento in elemento:
            yield subelemento


ciudades_devueltas = devuelve_ciudades('Madrid', 'Barcelona', 'Valencia', 'Bilbao')

print(next(ciudades_devueltas))
print(next(ciudades_devueltas))

# Con generadores yield from
def devuelve_ciudades(*ciudades):
    for elemento in ciudades:
        #for subelemento in elemento:
            yield from elemento

ciudades_devueltas = devuelve_ciudades('Madrid', 'Barcelona', 'Valencia', 'Bilbao')

print(next(ciudades_devueltas))
print(next(ciudades_devueltas))
