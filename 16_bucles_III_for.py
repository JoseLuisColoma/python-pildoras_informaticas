num = 1
for i in range(1, 21, 5):
    print(f'valor de la variable {num}')
    num += 1

valido = False
email = input('Introduce tu email: ')

for i in range(len(email)):
    if email[i] == '@':
        valido = True

if valido:
    print('email correcto')
else:
    print('email incorrecto')

