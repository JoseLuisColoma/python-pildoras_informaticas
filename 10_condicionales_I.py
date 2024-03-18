# Condicional IF
# El flujo de ejecución de un programa es el orden en el que leen y ejecuten las instrucciones.
# Orden natural de arriba a abajo, pero los condicionales y los bucles lo pueden modificar.
# IF condicion a evaluar si se cumple o no se cumple (True o False)

print('Programa de evaluación de notas de alumnos')

nota_alumno = int(input('Introduce la nota del alumno: '))


def evaluacion(nota):
    if nota >= 0 and nota < 5:
        valoracion = 'suspendido'
    elif nota >= 5 and nota <= 10:
        valoracion = 'aprobado'
    else:
        valoracion = 'La nota no existe. DEbe estar comprendida entre 0 y 10.'
    return valoracion


print(evaluacion(nota_alumno))
