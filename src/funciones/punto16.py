def saludar(nombre):
    print(f"Hola, {nombre}")
    # No hay return explícito

resultado = saludar("Laura")
print(f"La función devolvió: {resultado}")  # Imprime: La función devolvió: None
# Este código define una función que saluda a una persona y muestra que, al no tener un return explícito, devuelve None por defecto.