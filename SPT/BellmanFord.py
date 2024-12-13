def BellmanFord(graph, origen):
    distanceTo = {v: float("inf") for v in graph}
    distanceTo[origen] = 0

    TotalConexiones = []
    pesos = {}
    for u in graph:
        for v, weight in graph[u]:
            TotalConexiones.append((u, v))
            pesos[f"{u}{v}"] = weight

    for _ in range(len(graph) - 1):
        for origen, destino in TotalConexiones:
            if distanceTo[origen] + pesos[f"{origen}{destino}"] < distanceTo[destino]:
                distanceTo[destino] = distanceTo[origen] + pesos[f"{origen}{destino}"]

    return distanceTo

graph = {
    0: [(1, 4), (2, 1)],
    1: [(3, 1)],
    2: [(1, 2), (3, 5)],
    3: [(4, 3)],
    4: []
}

print("Matriz de distancias más cortas:")
for v in graph:
    row = BellmanFord(graph, v)
    print(list(row.values()))
