# continue --> saltar a la siguiente interacción de bucle.
# EjBucle con 10 vueltas, y en la vuelta 5 encuentra
# pass --> devolver un null, como si no ejecutara un bucle. Casos muy específicos (para definir clases nulas)
# o si desarrollando quieres dejar un trozo de código pendiente y le pones un pass
# else --> similar dentro de un condicional (o si no)

# continue
for letra in 'python':
    if letra == 'h':
        continue
    print(letra, end=' ')
# p y t o n

# contar el número de caracteres que tiene un string
nombre = 'pildoras informaticas'
contador = 0
for i in nombre:
    if i == ' ':
        continue
    contador += 1

print(contador)

# pass
class MiClase:
    pass
    # TODO

def mi_funcion():
    # TODO
    pass

# else
email = input('Introduce tu email, por favor: ')
for i in email:
    if i=='@':
        arroba = True
        break
else:
    arroba = False

print(arroba)