# Enfoque mejorado: siempre devuelve una lista (vacía en caso de error)
def filtrar_positivos(numeros):
    if not isinstance(numeros, list):
        return []  # Lista vacía en caso de error

    return [num for num in numeros if num > 0]
#esta función filtra los números positivos de una lista dada, devolviendo una lista vacía si la entrada no es una lista válida.