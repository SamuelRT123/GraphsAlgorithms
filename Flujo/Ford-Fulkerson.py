def bfs(graph, capacity, s, t, parent):
    visited = [False] * len(graph)
    queue = [s]
    visited[s] = True

    while queue:
        u = queue.pop(0)

        for v in graph[u]:
            if not visited[v] and capacity.get(f"{u}-{v}", 0) > 0:
                queue.append(v)
                visited[v] = True
                parent[v] = u

                if v == t:
                    return True

    return False

def ford_fulkerson(graph, capacity, source, sink):
    parent = [-1] * len(graph)
    max_flow = 0

    while bfs(graph, capacity, source, sink, parent):
        path_flow = float('Inf')
        s = sink
        while s != source:
            path_flow = min(path_flow, capacity.get(f"{parent[s]}-{s}", 0))
            s = parent[s]

        v = sink
        while v != source:
            u = parent[v]
            capacity[f"{u}-{v}"] -= path_flow
            capacity[f"{v}-{u}"] = capacity.get(f"{v}-{u}", 0) + path_flow
            v = parent[v]

        max_flow += path_flow

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

print("El flujo máximo es:", ford_fulkerson(graph, capacity, source, sink))
