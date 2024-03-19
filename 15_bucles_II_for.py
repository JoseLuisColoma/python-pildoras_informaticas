# Bucles for continuació
# for variable in elemento a recorrer
# Recorrido Strings
# Tipo range
# Notaciones especiales con print

# para confirmar un mail que exista @
email_correcto = False
email = input('Introduce tu direccion de email: ')
for i in email:
    if i == '@':
        email_correcto = True

if email_correcto:
    print('El mail es correcto')
else:
    print('El mail no es correcto')

# para confirmar un mail que exista @ y '.'
contador_arrobas = 0
contador_puntos = 0
email = input('Introduce tu direccion de email: ')
for i in email:
    if i == '@':
        contador_arrobas += 1
    if i == '.':
        contador_puntos += 1

if contador_arrobas == 1 and contador_puntos == 1:
    print('El mail es correcto')
else:
    print('El mail no es correcto')

# Tipo range
for i in range(5):
    print('Hola')

for i in ['Pildoras', ' informaticas']:
    print(i, end=' ')
