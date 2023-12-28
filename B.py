def min_caramelos(hunger):
    n = len(hunger)
    
    # Inicializamos el array de caramelos con 1 para cada niño
    candies = [1] * n
    
    # Paso de izquierda a derecha
    for i in range(1, n):
        if hunger[i] > hunger[i - 1]:
            candies[i] = candies[i - 1] + 1
    
    # Paso de derecha a izquierda
    for i in range(n - 2, -1, -1):
        if hunger[i] > hunger[i + 1]:
            candies[i] = max(candies[i], candies[i + 1] + 1)
    
    # La suma de caramelos es la respuesta
    return sum(candies)

# Ejemplos
hunger1 = [1, 0, 2]
print(min_caramelos(hunger1))  # Salida esperada: 5

hunger2 = [1, 2, 2]
print(min_caramelos(hunger2))  # Salida esperada: 4
