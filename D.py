def min_swaps_to_adjacent(row):
    n = len(row) // 2  # Número de parejas
    pair_positions = {}  # Almacena las posiciones de cada pareja

    # Guarda las posiciones de cada pareja
    for i in range(2 * n):
        pair_positions[row[i]] = i

    swaps = 0

    # Itera sobre las parejas
    for i in range(0, 2 * n, 2):
        # Verifica si la pareja está separada
        if row[i] // 2 != row[i + 1] // 2:
            # Encuentra la posición de la pareja que debería estar junto
            target_position = pair_positions[row[i] // 2 * 2 + 1]

            # Intercambia las personas de la pareja
            row[i + 1], row[target_position] = row[target_position], row[i + 1]

            # Actualiza las posiciones después del intercambio
            pair_positions[row[i + 1]] = i + 1
            pair_positions[row[target_position]] = target_position

            swaps += 1

    return swaps

# Ejemplos de uso
row1 = [0, 2, 1, 3]
row2 = [3, 2, 0, 1]

print(min_swaps_to_adjacent(row1))  # Salida: 1
print(min_swaps_to_adjacent(row2))  # Salida: 0
