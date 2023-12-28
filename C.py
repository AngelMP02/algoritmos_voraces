def puede_alcanzar_final(nums):
    n = len(nums)
    max_alcanzable = 0  # La máxima posición alcanzable hasta el momento

    for i in range(n):
        # Si en algún momento la posición actual es mayor que la máxima alcanzable, no se puede llegar al final
        if i > max_alcanzable:
            return False

        # Actualiza la máxima posición alcanzable
        max_alcanzable = max(max_alcanzable, i + nums[i])

        # Si la máxima posición alcanzable es igual o mayor al último índice, se puede llegar al final
        if max_alcanzable >= n - 1:
            return True

    return False

# Ejemplos de uso
nums1 = [2, 3, 1, 1, 4]
nums2 = [3, 2, 1, 0, 4]

print(puede_alcanzar_final(nums1))  # Salida: True
print(puede_alcanzar_final(nums2))  # Salida: False
