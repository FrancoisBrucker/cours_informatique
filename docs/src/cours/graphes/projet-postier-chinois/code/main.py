import osmnx as ox

# Marseille = ox.graph.graph_from_address('Marseille, France')
# ecm = ox.graph.graph_from_address('Ecole centrale marseille', dist=2000)
# marseille_en_grand = ox.graph.graph_from_bbox(43.388, 43.168, 5.498, 5.295, network_type='drive')
ailefroide = ox.graph.graph_from_point((44.8833273, 6.444307), dist=3000, network_type='all')


sommet = ox.distance.nearest_nodes(ailefroide, 44.91771033167592, 6.416818457077778)
arete = ox.distance.nearest_edges(ailefroide, 44.91771033167592, 6.416818457077778)

print(sommet, ailefroide.nodes[sommet])
print(arete, ailefroide.edges[arete])

print(ailefroide.graph)