def count_in_range(arr, num, low, high):
    
    count = 0
    for i in range(low, high + 1):
        if arr[i] == num:
            count += 1
    return count

def majority_element_dc(arr, low, high):
  
    # Caso base: un solo elemento
    if low == high:
        return arr[low]

    # 1. Dividir
    mid = (low + high) // 2

    # 2. Recursión
    maj_izq = majority_element_dc(arr, low, mid)
    maj_der = majority_element_dc(arr, mid + 1, high)

    # 3. Combinar
    # Si los mayoritarios de ambas mitades son iguales, ese es el candidato
    if maj_izq == maj_der:
        return maj_izq

    # Si son diferentes, contamos ambos en el rango actual
    count_izq = count_in_range(arr, maj_izq, low, high)
    count_der = count_in_range(arr, maj_der, low, high)
    
    # Comparamos con el tamaño del rango actual
    current_size_half = (high - low + 1) / 2

    if count_izq > current_size_half:
        return maj_izq
    elif count_der > current_size_half:
        return maj_der
    else:
        # No hay mayoritario en este rango
        return -1

def find_majority_element(arr):
    n = len(arr)
    if n == 0:
        return -1
        
    candidate = majority_element_dc(arr, 0, n - 1)
    
    if candidate == -1:
        return -1
        
    # Verificación final (necesaria porque la recursión 
    # solo comprueba > (rango/2), no > (N/2) global)
    count = count_in_range(arr, candidate, 0, n - 1)
    
    if count > n / 2:
        return candidate
    else:
        return -1


arr1 = [2, 2, 1, 1, 1, 2, 2]
print(f"Arreglo: {arr1}")
print(f"Elemento Mayoritario: {find_majority_element(arr1)}") 

arr2 = [3, 3, 3, 4, 0, 3]
print(f"\nArreglo: {arr2}")
print(f"Elemento Mayoritario: {find_majority_element(arr2)}") 