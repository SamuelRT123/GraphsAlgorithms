#Ver rcuacion de recurrencia en internet
def FloydWarschall(graph):
    n = len(graph)
    dp = [[float('inf')] * n for _ in range(n)]

    for i in range(n):
        dp[i][i] = 0

    for u in graph:
        for v, peso in graph[u]:
            dp[u][v] = peso

    for k in range(n):
        for i in range(n):
            for j in range(n):
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])

    return dp

# Grafo representado como lista de adyacencias
graph = {
    0: [(1, 4), (2, 1)],
    1: [(3, 1)],
    2: [(1, 2), (3, 5)],
    3: [(4, 3)],
    4: []
}

spt = FloydWarschall(graph)

print("Matriz de distancias más cortas:")
for row in spt:
    print(row)
