# Correcto
def crear_perfil(nombre, edad, ciudad="Madrid"):
    return f"Perfil: {nombre}, {edad} años, {ciudad}"# Incorrecto - causaría un error de sintaxis
# def crear_perfil(nombre, ciudad="Madrid", edad):
#     return f"Perfil: {nombre}, {edad} años, {ciudad}"
#Esta función toma un nombre, una edad y una ciudad (con un valor predeterminado) y devuelve una cadena que describe el perfil de la persona.