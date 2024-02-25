# Matriz inicial
primer_array1 = [[19, 18, 17],
                 [16, 15, 14],
                 [13, 12, 11]]

# Mostrar matriz desordenada
print("La matriz primera array 1 desordenada:")
for row in primer_array1:
    print(row)

# Ordenar la matriz
for row in primer_array1:
    row.sort()

# Mostrar matriz ordenada
print("\n La matriz primera array 1 esta  ordenada:")
for row in primer_array1:
    print(row)