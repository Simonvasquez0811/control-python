def saludar(nombre, mensaje="¡Bienvenido!"):
    print(f"Hola {nombre}. {mensaje}")

saludar("Carlos")  # Usa el mensaje predeterminado
# Imprime: Hola Carlos. ¡Bienvenido!

saludar("María", "¿Cómo estás hoy?")  # Usa el mensaje personalizado
# Imprime: Hola María. ¿Cómo estás hoy?
#Esta función toma un nombre y un mensaje opcional (con un valor predeterminado) y saluda a la persona con el mensaje proporcionado o el predeterminado.