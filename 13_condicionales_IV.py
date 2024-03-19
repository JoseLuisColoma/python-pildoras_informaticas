# Condicionales
# operadores lógicos AND y OR ( AND -> y si además, OR -> o si no)
# Operador in

# Programa que evalúe si un alumno que va a entrar en un colegio tiene derecho a beca o no
# Evalúa 3 cosas para la ayuda:
# distancia > 40km
# número hermanos > 2 (familia numerosa)
# salario familiar < 20.00€

print('PROGRAMA DE BECAS AÑO 2024')

DISTANCIA_BECA = 40.0
NUM_HERMANOS_BECA = 2
SALARIO_BECA = 20000  # pesa más que las otras 2 condiciones

nombre_alumno = input('Introduce el nombre del alumno: ')
distancia = float(input('Introduce la distancia a la que vives: '))
hermanos = int(input('Introduce el número de hermanos en el Centro: '))
salario = float(input('Introduce el salario familiar anual: '))

if distancia > DISTANCIA_BECA and hermanos >= NUM_HERMANOS_BECA or salario <= SALARIO_BECA:
    print(f'El alumno {nombre_alumno} tiene derecho a beca')
else:
    print(f'El alumno {nombre_alumno} no tiene derecho a beca')

# Operador in
# Un alumno de ingeniería informática tiene que elegir entre una serie de asignaturas optativasde un listado
print('\n')
print('ASIGNATURAS OPTATIVAS INGENIERIA INFORMÁTICA')
print('Asignaturas optativas: Informática gráfica - Pruebas de software - Usabilidad y accesibilidad')
opcion = input('Elige la asignatura escogida: ')
asignatura = opcion.lower();
if asignatura in ('informática gráfica', 'pruebas de software', 'usabilidad y accesibilidad'):
    print('Has elegido correctamente la asignatura optativa')
    print(f'Asignatura optativa elegida: {asignatura.upper()}')
else:
    print('No has elegido correctamente la asignatura optativa')
