from multi_graph import create_multi_graph


def test_create_multi_graph_empty():
    assert create_multi_graph([]) == dict()

def test_multi_graph_one_edge():
    assert create_multi_graph([[1, 2]]) == {1: [2], 2: []}