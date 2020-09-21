
def create_multi_graph(edges):
    graph = dict()
    for x, y in edges:
        graph[x] = []
        graph[y] = []
    for x, y in edges:
        graph[x].append(y)
    return graph
