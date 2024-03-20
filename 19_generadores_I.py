# Qué son: Estructuras que extren valores de una función y se almacenarán en objeton iterables
# (que se pueden recorrer con un bucle). Esto valores se almacenan de uno en uno.
# Cada vez que un generador almacena un valor, esta permanece en estado pausado hasta que se solicita el siguiente.
# Esta característica es conocida como "suspensión de estado". Los valores los devuelven de 1 en 1
# Funcionamiento: Funcion tradicional (return) vs Generador (yield)
# Qué utilidad tienen?:
# Son más eficientes que las funciones tradicionales.
# Muy útiles con listas de valores infinitos
# Bajo determinados escenarios, será muy útil que un generador devuelva los valores de uno en uno.
# Método NEXT()
# Sintaxis: deg generaNumeros(); / yield numeros (también puede llevar un return)

# Ejemplo que genere números pares.
# FUNCIÓN TRADICIONAL
def generaPares(limite):
    num = 1
    lista = []
    while num < limite:
        lista.append(num*2)
        num += 1
    return lista


print(generaPares(10))

# GENERADOR
def generaPares(limite):
    num = 1
    while num < limite:
        yield num * 2
        num += 1


devuelvePares = generaPares(10)


print(next(devuelvePares))
print('Aquí podría haber más código')

print(next(devuelvePares))
print('Aquí podría haber más código')

print(next(devuelvePares))
print('Aquí podría haber más código')
