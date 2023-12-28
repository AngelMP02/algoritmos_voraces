def max_area(height):
    max_water = 0
    left_pointer = 0
    right_pointer = len(height) - 1

    while left_pointer < right_pointer:
        # Calcula el ancho y la altura del recipiente actual
        width = right_pointer - left_pointer
        h = min(height[left_pointer], height[right_pointer])

        # Calcula el área y actualiza la cantidad máxima de agua almacenada
        current_area = width * h
        max_water = max(max_water, current_area)

        # Mueve el puntero que apunta a la altura más baja hacia el centro
        if height[left_pointer] < height[right_pointer]:
            left_pointer += 1
        else:
            right_pointer -= 1

    return max_water

# Ejemplo de uso
height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
result = max_area(height)
print(result)  # Salida esperada: 49
