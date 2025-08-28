encontrado = False

for i in range(5):
    for j in range(5):
        if i * j > 10:
            print(f"Valor encontrado: {i} * {j} = {i*j}")
            encontrado = True
            break  # Sale del bucle interno

    if encontrado:
        break  # Sale del bucle externo
# Este código busca el primer par (i, j) en dos bucles anidados cuya multiplicación sea mayor que 10, y utiliza break para salir de ambos bucles una vez encontrado el primer caso.