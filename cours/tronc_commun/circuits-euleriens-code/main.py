from multi_graph import is_eulerian, eulerian_circuit

multi_graph = { "00": ["00", "01"],
                "01": ["10", "11"],
                "11": ["11", "10"],
                "10": ["00", "01"],
               }

print("Le graphe est eulérien :", is_eulerian(multi_graph))

circuit = eulerian_circuit(multi_graph)
print("Un circuit eulérien associé est :", circuit)

suite = ""

for mot in circuit:
    suite += mot[1]

print("Une suite de brujin : ", suite)