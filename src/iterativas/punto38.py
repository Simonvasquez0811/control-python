modo_debug = False

for i in range(100):
    # En modo normal, no mostramos nada durante el procesamiento
    if not modo_debug:
        pass
    else:
        print(f"Procesando iteración {i}")

    # Código de procesamiento real aquí
# Este código muestra cómo usar la instrucción pass en un bucle