def calcular_precio_con_iva(precio_base, tasa_iva=0.21):
    return precio_base * (1 + tasa_iva)

precio_final = calcular_precio_con_iva(100)
print(f"Precio con IVA: {precio_final} €")  # Imprime: Precio con IVA: 121.0 €
# Este código define una función que calcula el precio final de un producto después de aplicar el IVA, utilizando un valor por defecto para la tasa de IVA.