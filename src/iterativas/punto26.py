while True:
    entrada = input("Escribe algo (o 'salir' para terminar): ")

    if entrada.lower() == 'salir':
        print("Programa terminado.")
        break

    print(f"Has escrito: {entrada}")
# Este código solicita al usuario que escriba algo y repite hasta que escriba 'salir'.