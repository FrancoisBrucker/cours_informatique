
def create_multi_graph(n, edges):
    graph = []
    for i in range(n):
        graph. append([])

    for x, y in edges:
        graph[x].append(y)
    return graph


def is_eulerian(edges):
    number_enter = [0] * len(edges)
    number_exit = [0] * len(edges)

    for vertex in range(len(edges)):
        for neighbor in edges[vertex]:
            number_exit[vertex] += 1
            number_enter[neighbor] += 1

    for vertex in range(len(edges)):
        if number_enter[vertex] != number_exit[vertex]:
            return False
    return True


def circuit_from_eulerian(edges):

    current = None
    for vertex in range(len(edges)):
        if len(edges[vertex]) > 0:
            current = vertex

    if current is None:
        return []

    circuit = [current]

    is_possible = True
    while is_possible:
        is_possible = False
        for next in edges[circuit[-1]]:
            if next not in circuit:
                circuit.append(next)
                is_possible = True
            else:
                pos = circuit.index(next)
                return circuit[pos:] + circuit[:pos]
    return None


def copy_multi_graph(edges):
    return [list(x) for x in edges]


def delete_circuit(circuit, edges):
    new = copy_multi_graph(edges)

    x = circuit[0]

    for y in circuit[1:] + [circuit[0]]:
        new[x].remove(y)
        x = y
    return new


def list_of_circuits(edges):
    circuits = []

    next_circuit = circuit_from_eulerian(edges)
    while next_circuit:
        circuits.append(next_circuit)
        edges = delete_circuit(next_circuit, edges)
        next_circuit = circuit_from_eulerian(edges)

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
