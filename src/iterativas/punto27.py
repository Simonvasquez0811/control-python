def es_primo(n):
    if n < 2:
        return False

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False  # No es primo, salimos inmediatamente

    return True  # Si llegamos aquí, es primo

#Este código verifica si un número es primo o no.