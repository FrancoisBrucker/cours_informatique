from multi_graph import create_multi_graph, is_eulerian, circuit_from_eulerian, copy_multi_graph, delete_circuit, \
    list_of_circuits, add_circuit, create_from_circuits, raboutage, eulerian_circuit


def test_create_multi_graph_empty():
    assert create_multi_graph([]) == dict()


def test_multi_graph_one_edge():
    assert create_multi_graph([[1, 2]]) == {1: [2], 2: []}


def test_multi_graph_several_edges():
    assert create_multi_graph([[1, 2], [2, 3], [2, 1], [1, 2], [4, 4]]) == {1: [2, 2],
                                                                            2: [3, 1],
                                                                            3: [],
                                                                            4: [4]}


def test_is_eulerian_empty():
    assert is_eulerian(dict())


def test_is_eulerian_one_edge():
    assert is_eulerian(create_multi_graph([[1, 2]])) is False


def test_is_eulerian_loop():
    assert is_eulerian(create_multi_graph([[1, 1]]))


def test_is_eulerian_cycle():
    assert is_eulerian(create_multi_graph([[1, 2], [3, 1], [2, 3]]))


def test_is_eulerian_no_eulerian():
    assert is_eulerian(create_multi_graph([[1, 2], [2, 3], [3, 1], [2, 4]])) is False


def test_circuit_empty():
    assert circuit_from_eulerian(dict()) == []


def test_circuit_no_edge():
    assert circuit_from_eulerian({1: [], 2: []}) == []


def test_circuit_loop():
    assert circuit_from_eulerian(create_multi_graph([[1, 1]])) == [1]


def test_circuit():
    assert circuit_from_eulerian(create_multi_graph([[1, 2], [3, 1], [2, 3]])) in [[1, 2, 3], [2, 3, 1], [3, 1, 2]]


def test_copy_multi_graph():
    graph = create_multi_graph([[1, 1]])
    copy_graph = copy_multi_graph(graph)
    assert copy_graph == graph

    graph[1].append("?")
    assert copy_graph != graph


def test_delete_cycle():
    assert delete_circuit([1, 2, 3], create_multi_graph([[1, 2], [3, 1], [2, 3], [1, 4]])) == {1: [4], 2: [], 3: [], 4: []}


def test_delete_cycle_different_graph():
    initial_graph = create_multi_graph([[1, 2], [3, 1], [2, 3], [1, 4]])
    delete_circuit([1, 2, 3], create_multi_graph([[1, 2], [3, 1], [2, 3], [1, 4]]))

    assert initial_graph == create_multi_graph([[1, 2], [3, 1], [2, 3], [1, 4]])


def test_list_of_circuits_empty():
    assert list_of_circuits(dict()) == []


def test_list_of_circuits_one_circuit():
    circuits = list_of_circuits(create_multi_graph([[1, 2], [2, 3], [3, 1]]))

    assert len(circuits) == 1
    assert set(circuits[0]) == {1, 2, 3}


def test_list_of_circuits_several_circuits():
    circuits = list_of_circuits(create_multi_graph([[1, 2], [2, 3], [3, 1], [1, 1]]))

    assert len(circuits) == 2
    assert {frozenset(circuits[0]), frozenset(circuits[1])} == {frozenset({1, 2, 3}), frozenset({1})}


def test_raboutage_left_empty():
    assert raboutage([], [1, 2]) == [1, 2]


def test_raboutage_right_empty():
    assert raboutage([1, 2], []) == [1, 2]


def test_raboutage():
    assert raboutage([1], [1, 2]) in [[1, 1, 2], [1, 2, 1], [2, 1, 1]]


def test_eulerian_circuit_empty():
    assert eulerian_circuit(dict()) == []


def test_eulerian_circuit_one_loop():
    assert eulerian_circuit(create_multi_graph([[1, 1]])) == [1]


def test_eulerian_circuit():
    assert eulerian_circuit(create_multi_graph([[1, 2], [2, 1], [1, 1]])) in ([1, 2, 1], [1, 1, 2], [2, 1, 1])