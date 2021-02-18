from multi_graph import create_multi_graph, is_eulerian, circuit_from_eulerian
from multi_graph import copy_multi_graph, delete_circuit, list_of_circuits
from multi_graph import raboutage, eulerian_circuit


def test_create_multi_graph_empty():
    assert create_multi_graph(0, []) == []


def test_create_multi_graph_empty_three_vertices():
    assert create_multi_graph(3, []) == [[], [], []]


def test_multi_graph_one_edge():
    assert create_multi_graph(2, [[0, 1]]) == [[1], []]


def test_multi_graph_several_edges():
    edges = [[0, 1], [1, 2], [1, 0], [0, 1], [3, 3]]
    assert create_multi_graph(4, edges) == [[1, 1], [2, 0], [], [3]]


def test_is_eulerian_empty():
    assert is_eulerian([])


def test_is_eulerian_one_edge():
    assert is_eulerian(create_multi_graph(2, [[0, 1]])) is False


def test_is_eulerian_loop():
    assert is_eulerian(create_multi_graph(1, [[0, 0]]))


def test_is_eulerian_cycle():
    assert is_eulerian(create_multi_graph(3, [[0, 1], [2, 0], [1, 2]]))


def test_is_eulerian_no_eulerian():
    edges = create_multi_graph(4, [[0, 1], [1, 2], [2, 0], [1, 3]])
    assert is_eulerian(edges) is False


def test_circuit_empty():
    assert circuit_from_eulerian([]) == []


def test_circuit_no_edge():
    assert circuit_from_eulerian([[], []]) == []


def test_circuit_loop():
    assert circuit_from_eulerian(create_multi_graph(1, [[0, 0]])) == [0]


def test_circuit():
    assert circuit_from_eulerian(create_multi_graph(3, [[0, 1], [2, 0], [1, 2]])) in [[0, 1, 2], [1, 2, 0], [2, 0, 1]]


def test_copy_multi_graph():
    edges = create_multi_graph(1, [[0, 0]])
    copy_edges = copy_multi_graph(edges)
    assert copy_edges == edges

    edges[0].append("X")
    assert copy_edges != edges


def test_delete_cycle():
    new_edges = delete_circuit([0, 1, 2], create_multi_graph(4, [[0, 1], [2, 0], [1, 2], [0, 3]]))
    assert new_edges == [[3], [], [], []]


def test_delete_cycle_different_graph():
    initial_graph = create_multi_graph(4, [[0, 1], [2, 0], [1, 2], [0, 3]])
    delete_circuit([0, 1, 2], initial_graph)
    
    assert initial_graph == create_multi_graph(4, [[0, 1], [2, 0], [1, 2], [0, 3]])


def test_list_of_circuits_empty():
    assert list_of_circuits([]) == []



def test_list_of_circuits_one_circuit():
    circuits = list_of_circuits(create_multi_graph(3, [[0, 1], [1, 2], [2, 0]]))

    assert len(circuits) == 1
    assert set(circuits[0]) == {0, 1, 2}


def test_list_of_circuits_several_circuits():
    circuits = list_of_circuits(create_multi_graph(3, [[0, 1], [1, 2], [2, 0], [0, 0]]))

    assert len(circuits) == 2
    assert {frozenset(circuits[0]), frozenset(circuits[1])} == {frozenset({0, 1, 2}), frozenset({0})}


def test_raboutage_left_empty():
    assert raboutage([], [0, 1]) == [0, 1]


def test_raboutage_right_empty():
    assert raboutage([0, 1], []) == [0, 1]


def test_raboutage():
    assert raboutage([0], [0, 1]) in [[0, 0, 1], [0, 1, 0], [1, 0, 0]]


def test_eulerian_circuit_empty():
    assert eulerian_circuit([]) == []


def test_eulerian_circuit_one_loop():
    assert eulerian_circuit(create_multi_graph(1, [[0, 0]])) == [0]


def test_eulerian_circuit():
    assert eulerian_circuit(create_multi_graph(2, [[0, 1], [1, 0], [0, 0]])) in ([0, 1, 0], [0, 0, 1], [1, 0, 0])