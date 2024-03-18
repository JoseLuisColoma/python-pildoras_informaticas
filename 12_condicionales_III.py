# Condicionales. No existe la estructura Switch
# Concatenacion de operadores de comparacion al utilizar un condicional
# operadores lógicos and y or
# operador in
# Ejemplo Salarios de la empresa

salario_presidente = int(input("Introduce salario Presidente: "))
print("Salario presidente: " + str(salario_presidente))

salario_director = int(input("Introduce salario del Director: "))
print(f'Salario directo: {salario_director}')

salario_jefe_area = int(input("Introduce salario del Jefe de Área: "))
print(f'Salario jefe de área: {salario_jefe_area}')

salario_administrativo = int(input("Introduce salario del Administrativo: "))
print(f'Administrativo: {salario_administrativo}')

if salario_administrativo < salario_jefe_area < salario_director < salario_presidente:
    print('Todo funciona correctamente')
else:
    print('Algo falla en esta empresa')
