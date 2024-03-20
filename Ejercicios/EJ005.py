# EJERCICIO 005
# Escribir un texto y contar la cantidad de vocales que aparecen en dicho texto

# texto = 'Escribir un texto y contar la cantidad de vocales que aparecen en dich texto'

texto = input('Introduce el texto:')

texto_minusculas = texto.lower()
contador_vocales = 0
contador_a = 0
contador_e = 0
contador_i = 0
contador_o = 0
contador_u = 0

print(len(texto_minusculas))
for i in texto_minusculas:
    if i in ('a', 'e', 'i', 'o', 'u'):
        contador_vocales += 1
    if i == 'a':
        contador_a += 1
    if i == 'e':
        contador_e += 1
    if i == 'i':
        contador_i += 1
    if i == 'o':
        contador_o += 1
    if i == 'u':
        contador_u += 1

print(f'Vocales totales: {contador_vocales}')
print(f'num vocal "a" : {contador_a}')
print(f'num vocal "e" : {contador_e}')
print(f'num vocal "i" : {contador_i}')
print(f'num vocal "o" : {contador_o}')
print(f'num vocal "u" : {contador_u}')
