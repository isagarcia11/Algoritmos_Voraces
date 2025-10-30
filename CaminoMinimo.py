def camino_minimo(matriz):
    """
    Calcula el costo mínimo para ir desde la esquina superior izquierda (0,0)
    hasta la esquina inferior derecha (m-1, n-1) en una matriz de costos,
    moviéndose solo hacia la derecha o hacia abajo.
    
    Parámetros:
    -----------
    matriz : list[list[int]]
        Matriz de tamaño m x n donde cada celda matriz[i][j] representa un costo.

    Retorna:
    --------
    int
        El costo total mínimo del recorrido.
    
    Complejidades:
    --------------
    - Tiempo: O(m × n) → se recorren todas las celdas de la matriz una sola vez.
    - Espacio: O(n) → solo se almacena una fila a la vez (optimización espacial).
    """

    # Dimensiones de la matriz
    m, n = len(matriz), len(matriz[0])
    
    # dp[j] almacenará el costo mínimo para llegar a la celda (i, j)
    # Inicialmente se llena con infinito, excepto la primera celda
    dp = [float('inf')] * n
    dp[0] = matriz[0][0]

    # Inicializar la primera fila (solo se puede venir desde la izquierda)
    for j in range(1, n):
        dp[j] = dp[j-1] + matriz[0][j]

    # Procesar las siguientes filas
    for i in range(1, m):
        # La primera columna solo puede venir desde arriba
        dp[0] += matriz[i][0]

        # Actualizar el resto de las celdas (de izquierda a derecha)
        for j in range(1, n):
            # Para llegar a (i, j), se puede venir:
            # - desde arriba → dp[j]
            # - desde la izquierda → dp[j-1]
            # Se elige el mínimo de los dos
            dp[j] = matriz[i][j] + min(dp[j], dp[j-1])

    # El último valor contiene el costo mínimo total al llegar a (m-1, n-1)
    return dp[-1]
