for i in range(1, 4):
    print(f"Grupo {i}:")

    for j in range(1, 6):
        if j == 3:
            print("  Saltando el elemento 3")
            continue  # Solo afecta al bucle interno

        print(f"  Elemento {j}")

    print("Fin del grupo\n")
# Este código muestra cómo usar bucles anidados y la instrucción continue para saltar iteraciones específicas en el bucle interno sin afectar el bucle externo.