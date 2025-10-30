def camino_minimo(matriz):
    m, n = len(matriz), len(matriz[0])
    dp = [float('inf')] * n
    dp[0] = matriz[0][0]
    
    for j in range(1, n):
        dp[j] = dp[j-1] + matriz[0][j]
    
    for i in range(1, m):
        dp[0] += matriz[i][0]
        for j in range(1, n):
            dp[j] = matriz[i][j] + min(dp[j], dp[j-1])  # arriba, izquierda
    
    return dp[-1]
