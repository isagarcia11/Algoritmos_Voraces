def merge_sort_and_count(arr_indices, counts):
    n = len(arr_indices)
    if n <= 1:
        return arr_indices

    # 1. Dividir
    mid = n // 2
    
    # 2. Vencer (Recursión)
    left = merge_sort_and_count(arr_indices[:mid], counts)
    right = merge_sort_and_count(arr_indices[mid:], counts)

    # 3. Combinar
    merged = []
    i, j = 0, 0 # Punteros para left y right

    while i < len(left) and j < len(right):
        # Si el de la izquierda es más pequeño o igual
        if left[i][0] <= right[j][0]:
            # Este es el paso clave:
            # 'left[i]' es mayor que 'j' elementos de la mitad derecha
            # que ya hemos procesado (y que estaban a su derecha original).
            original_index = left[i][1]
            counts[original_index] += j
            
            merged.append(left[i])
            i += 1
        else:
            # El de la derecha es más pequeño
            merged.append(right[j])
            j += 1

    # Copiar elementos restantes
    while i < len(left):
        original_index = left[i][1]
        counts[original_index] += j # Sumar los 'j' restantes
        merged.append(left[i])
        i += 1
        
    while j < len(right):
        merged.append(right[j])
        j += 1
        
    return merged

def count_smaller_elements(arr):
    n = len(arr)
    counts = [0] * n
    
    # Creamos la lista de (valor, indice_original)
    arr_indices = list(enumerate(arr))
    # Intercambiamos para que sea (valor, indice)
    arr_indices = [(val, idx) for idx, val in arr_indices]

    merge_sort_and_count(arr_indices, counts)
    return counts

arr1 = [5, 2, 6, 1, 3]
print(f"Arreglo: {arr1}")
print(f"Conteos: {count_smaller_elements(arr1)}") 