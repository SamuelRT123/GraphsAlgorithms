
def FloydWarschall(vertices, MapConexiones):
    n = len(vertices)
    dp = [[float('inf')] * n for _ in range(n)]

    for i in range(n):
        dp[i][i] = 0

    for i in range(n):
        for j in range(n):
            key = vertices[i] + vertices[j]
            if key in MapConexiones:
                dp[i][j] = MapConexiones[key]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])

    return dp