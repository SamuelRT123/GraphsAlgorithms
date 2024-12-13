def bfs(graph, capacity, level, source, sink):
    queue = [source]
    level[source] = 0

    while queue:
        u = queue.pop(0)

        for v in graph[u]:
            if level[v] < 0 and capacity.get(f"{u}-{v}", 0) > 0:
                level[v] = level[u] + 1
                queue.append(v)

    return level[sink] >= 0

def envio(graph, capacity, level, ptr, u, sink, flow):
    if u == sink:
        return flow

    while ptr[u] < len(graph[u]):
        v = graph[u][ptr[u]]

        if level[v] == level[u] + 1 and capacity.get(f"{u}-{v}", 0) > 0:
            curr_flow = min(flow, capacity[f"{u}-{v}"])
            temp_flow = envio(graph, capacity, level, ptr, v, sink, curr_flow)

            if temp_flow > 0:
                capacity[f"{u}-{v}"] -= temp_flow
                capacity[f"{v}-{u}"] = capacity.get(f"{v}-{u}", 0) + temp_flow
                return temp_flow

        ptr[u] += 1

    return 0

def dinic(graph, capacity, source, sink):
    max_flow = 0

    while True:
        level = [-1] * len(graph)
        if not bfs(graph, capacity, level, source, sink):
            break

        ptr = [0] * len(graph)

        while True:
            flow = envio(graph, capacity, level, ptr, source, sink, float('Inf'))
            if flow == 0:
                break
            max_flow += flow

    return max_flow

graph = {
    0: [1, 2],
    1: [0, 2, 3],
    2: [0, 1, 4],
    3: [1, 2, 5],
    4: [2, 3, 5],
    5: [3, 4]
}

capacity = {
    "0-1": 16, "0-2": 13,
    "1-2": 10, "1-3": 12,
    "2-1": 4,  "2-4": 14,
    "3-2": 9,  "3-5": 20,
    "4-3": 7,  "4-5": 4
}

source = 0
sink = 5

print("El flujo máximo es:", dinic(graph, capacity, source, sink))
