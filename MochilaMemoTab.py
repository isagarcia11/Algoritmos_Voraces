def knapsack_memo(v, w, capacidad):
    """
    Resuelve el problema de la mochila 0/1 usando programación dinámica con memoización (enfoque Top-Down).

    El objetivo es maximizar el valor total de los objetos seleccionados sin exceder la capacidad de la mochila.
    Cada objeto solo puede tomarse una vez (0/1).

    Args:
        v (list[int]): Lista de valores de los objetos (índice 0 a n-1).
        w (list[int]): Lista de pesos de los objetos (mismo orden que v).
        capacidad (int): Capacidad máxima de la mochila (peso máximo permitido).

    Returns:
        int: Valor máximo posible sin exceder la capacidad.

    Complejidad:
        - Temporal: O(n × capacidad) → cada estado (i, cap) se calcula una sola vez.
        - Espacial: O(n × capacidad) → en el peor caso, se almacenan todos los estados en el diccionario memo.

    Ejemplo:
        v = [2, 5, 10, 14, 15], w = [1, 3, 4, 5, 7], capacidad = 8
        → retorna 19 (selecciona B y D)
    """
    n = len(v)  # Número total de objetos
    memo = {}   # Diccionario para almacenar resultados de subproblemas: clave = (i, cap), valor = resultado óptimo

    def dp(i, cap):
        """
        Función recursiva auxiliar que calcula el valor máximo para los objetos desde i hasta n-1,
        con una capacidad restante de 'cap'.

        Args:
            i (int): Índice del objeto actual (i va de 0 a n-1).
            cap (int): Capacidad restante de la mochila.

        Returns:
            int: Valor máximo posible con los objetos restantes y la capacidad dada.
        """
        # Caso base 1: No hay más objetos por considerar
        if i == n:
            return 0
        
        # Caso base 2: No queda capacidad en la mochila
        if cap == 0:
            return 0

        # Verificar si el subproblema ya fue resuelto (memoización)
        if (i, cap) in memo:
            return memo[(i, cap)]

        # Opción 1: NO tomar el objeto actual (i)
        # → seguimos con el siguiente objeto (i+1) y misma capacidad
        sin_tomar = dp(i + 1, cap)

        # Opción 2: TOMAR el objeto actual (solo si cabe)
        tomar = 0  # Valor por defecto si no cabe
        if w[i] <= cap:
            # Tomamos el valor del objeto + el resultado óptimo con:
            # - siguiente objeto (i+1)
            # - capacidad reducida (cap - w[i])
            tomar = v[i] + dp(i + 1, cap - w[i])

        # Guardamos el mejor resultado entre tomar o no tomar
        memo[(i, cap)] = max(sin_tomar, tomar)

        # Retornamos el resultado óptimo para este subproblema
        return memo[(i, cap)]

    # Iniciar la recursión desde el primer objeto (índice 0) y capacidad total
    return dp(0, capacidad)


from typing import List

def knapsack_tab(v: List[int], w: List[int], capacidad: int) -> int:
    """
    Resuelve el problema de la mochila 0/1 usando programación dinámica con tabulación (Bottom-Up).

    Se construye una tabla dp[i][cap] que representa el valor máximo posible
    al considerar los primeros i objetos (índices 0 a i-1) con una capacidad máxima de 'cap'.

    Args:
        v (List[int]): Lista de valores de los objetos (índice 0 = primer objeto).
        w (List[int]): Lista de pesos de los objetos (mismo orden que v).
        capacidad (int): Capacidad máxima de la mochila.

    Returns:
        int: Valor máximo posible sin exceder la capacidad.

    Complejidad:
        - Temporal: O(n × capacidad) → se recorre toda la tabla una vez.
        - Espacial: O(n × capacidad) → se almacena la tabla completa dp.

    Ejemplo:
        v = [2, 5, 10, 14, 15], w = [1, 3, 4, 5, 7], capacidad = 8
        → retorna 19 (selecciona objetos B y D)
    """
    n = len(v)  # Número total de objetos

    # Crear tabla dp: dp[i][cap] = valor máximo con objetos 0..i-1 y capacidad 'cap'
    # dp[0][...] = 0 → sin objetos
    # dp[...][0] = 0 → sin capacidad
    dp = [[0] * (capacidad + 1) for _ in range(n + 1)]

    # Llenar la tabla fila por fila (objeto por objeto)
    for i in range(1, n + 1):           # i = 1 → considerando el objeto i-1
        for cap in range(1, capacidad + 1):  # cap = capacidad actual
            # Caso 1: NO tomar el objeto i-1
            no_tomar = dp[i-1][cap]

            # Caso 2: TOMAR el objeto i-1 (solo si cabe)
            if w[i-1] <= cap:
                tomar = v[i-1] + dp[i-1][cap - w[i-1]]
                dp[i][cap] = max(no_tomar, tomar)
            else:
                # No cabe → solo podemos no tomarlo
                dp[i][cap] = no_tomar

    # Resultado: valor máximo con todos los objetos y capacidad total
    return dp[n][capacidad]
