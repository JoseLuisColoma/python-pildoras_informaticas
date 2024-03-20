# Pila de llamadas / descripción o nombre del error (ZeroDivisionError)

# Ejemplo excepciones (división por cero)
def suma(num1, num2):
    return num1 + num2


def resta(num1, num2):
    return num1 - num2


def multiplica(num1, num2):
    return num1 * num2


def divide(num1, num2):
    try:
        return num1 / num2
    except ZeroDivisionError:
        print('No se puede dividir entre 0')
        print('Operación errónea')


while True:
    try:
        op1 = (int(input("Introduce el primer número: ")))
        op2 = (int(input("Introduce el segundo número: ")))
        break
    except ValueError:
        print('Los valores introducidos no son correctos. Inténtalo de nuevo')

operacion = input("Introduce la operación a realizar (suma,resta,multiplica,divide): ")

if operacion == "suma":
    print(suma(op1, op2))

elif operacion == "resta":
    print(resta(op1, op2))

elif operacion == "multiplica":
    print(multiplica(op1, op2))

elif operacion == "divide":
    print(divide(op1, op2))

else:
    print("Operación no contemplada")

print("Operación ejecutada. Continuación de ejecución del programa ")

# Otro ejemplo


def dividir():

    try:
        num1 = float(input('Introduce el primer número: '))
        num2 = float(input('Introduce el segundo número: '))

        print('La division es: ' + str(num1 / num2))

    except ValueError:
        print('El valor introducido es erróneo)')

    except ZeroDivisionError:
        print('No se puede dividir entre cero)')

    finally:
        print('Cálculo finalizado')


dividir()
