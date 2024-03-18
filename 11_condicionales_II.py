# Programa edad
print("Verificación de acceso")
edad = int(input('Introduce tu edad: '))
if edad < 18:
    print('No puedes pasar')
else:
    print('Puedes pasar')


#Programa nota (más elaborado)
nota_alumno = int(input('Introduce la nota: '))

if nota_alumno <= 10 and nota_alumno >= 9:
    print('Sobresaliente')
elif nota_alumno < 9 and nota_alumno >= 7:
    print('Notable')
elif nota_alumno < 7 and nota_alumno >= 6:
    print('Bien')
elif nota_alumno < 6 and nota_alumno >= 5:
    print('Suficiente')
else:
    print('Insuficiente')
