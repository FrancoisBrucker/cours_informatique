import networkx as nx
import matplotlib.pyplot as plt


Gs = {
    "1": {"2", "3"},
    "2": {"1", "3", "4", "5"},
    "3": {"1", "2", "4", "5"},
    "4": {"2", "3", "5", "6"},
    "5": {"2", "3", "4", "6"},
    "6": {"4", "5"},
}

G = nx.Graph(Gs)

print(G)
nx.draw(G, with_labels=True, font_weight='bold')
plt.show()
