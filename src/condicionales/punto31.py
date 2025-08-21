numeros = [1, 2, 3, 4, 5]
paridad = ["par" if n % 2 == 0 else "impar" for n in numeros]
print(paridad)  # Salida: ['impar', 'par', 'impar', 'par', 'impar']

#Este programa utiliza una lista por comprensión junto con una expresión condicional (operador ternario) para determinar la paridad ("par" o "impar") de cada número en una lista.
