# Funciones
# Qué: Cjto de líneas de código agrupadas (bloque de código) que funcion como una unidad realizando una tarea específica
# Las funciones pueden devolver valores (no necesariamente)
# Las funciones en Python pueden tener párametros/argumentos)
# Las funciones también se les denomina "métodos" cuando están definidas dentro de una clase
# Utilidad: Reutilizar el códifo (cuando sea necesario o si es necesario)
# Sintaxis: def nombre_funcion(): / instrucciones de la función / return (opcional). Parentesis: zona de parámetros)
# Ejecución. Hay llamar a la función,
# Funciones predefinidas (bouilt in) y funciones propias (las que creamos conforme las utilizamos)

def suma_numeros(num1, num2):
    return print(f'las suma de {num1}+{num2} es {num1+num2}')


def mensajes():
    print('Estamos aprendiendo Python')
    print('Estamos aprendiendo funciones básicas')
    print('Poco a poco iremos avanzando')
    print('\n')

suma_numeros(5, 7)

mensajes()
mensajes()
mensajes()
