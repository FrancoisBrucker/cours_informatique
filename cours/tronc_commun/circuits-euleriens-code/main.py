from multi_graph import is_eulerian, eulerian_circuit

vertices = ["00", "01", "11", "10"]
edges = [[0, 1], [3, 2], [2, 3], [0, 1]]


print("Le graphe est eulérien :", is_eulerian(edges))

circuit = eulerian_circuit(edges)
print("Un circuit eulérien associé est :", circuit)

suite = ""

for mot in circuit:
    suite += vertices[mot][1]

print("Une suite de brujin : ", suite)