
def create_multi_graph(edges):
    graph = dict()
    for x, y in edges:
        graph[x] = []
        graph[y] = []
    for x, y in edges:
        graph[x].append(y)
    return graph


def is_eulerian(multi_graph):
    number_enter = dict()
    number_exit = dict()

    for vertex in multi_graph:
        number_enter[vertex] = 0
        number_exit[vertex] = 0

    for vertex in multi_graph:
        for neighbor in multi_graph[vertex]:
            number_exit[vertex] += 1
            number_enter[neighbor] += 1

    for vertex in multi_graph:
        if number_enter[vertex] != number_exit[vertex]:
            return False
    return True


def circuit_from_eulerian(multi_graph):

    current = None
    for vertex in multi_graph:
        if len(multi_graph[vertex]) > 0:
            current = vertex

    if current is None:
        return []

    circuit = [current]

    is_possible = True
    while is_possible:
        is_possible = False
        for next in multi_graph[circuit[-1]]:
            if next not in circuit:
                circuit.append(next)
                is_possible = True
            else:
                pos = circuit.index(next)
                return circuit[pos:] + circuit[:pos]
    return None


def copy_multi_graph(multi_graph):
    return {x: list(y) for x, y in multi_graph.items()}


def delete_circuit(circuit, multi_graph):
    new = copy_multi_graph(multi_graph)

    x = circuit[0]

    for y in circuit[1:] + [circuit[0]]:
        new[x].remove(y)
        x = y
    return new


def list_of_circuits(multi_graph):
    circuits = []

    next_circuit = circuit_from_eulerian(multi_graph)

    while next_circuit:
        circuits.append(next_circuit)
        multi_graph = delete_circuit(next_circuit, multi_graph)
        next_circuit = circuit_from_eulerian(multi_graph)

    return circuits


def raboutage(circuit1, circuit2):

    if circuit1 == []:
        return list(circuit2)
    elif circuit2 == []:
        return list(circuit1)
    intersection = set(circuit1).intersection(circuit2)

    if not intersection:
        return None

    x = intersection.pop()
    pos_x_1 = circuit1.index(x)
    pos_x_2 = circuit2.index(x)

    return circuit1[:pos_x_1] + circuit2[pos_x_2:] + circuit2[:pos_x_2] + circuit1[pos_x_1:]


def eulerian_circuit(multi_graph):

    circuits = list_of_circuits(multi_graph)

    if not circuits:
        return []

    current = []

    for circuit in circuits:
        current = raboutage(current, circuit)

    return current