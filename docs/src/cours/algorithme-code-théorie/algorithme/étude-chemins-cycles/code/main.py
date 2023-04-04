import random

import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

from algorithme import kruskal, routes_rec, glouton, décroisement, parcours_rec, d
from dessins import draw, draw_segments
from données import VILLES_100

segments = kruskal(VILLES_100)
print(len(segments))

# routes = routes_rec(None, str(0), str(1), segments)
routes = glouton(VILLES_100, str(0))

# routes = []
# parcours_rec(None, str(0), segments, routes)

# routes = décroisement(routes, 94, 99, VILLES_100)

# for k in range(100):
#     for i in range(len(VILLES_100) - 2):
#         for j in range(i + 2, len(VILLES_100)):
#             # print(i, j)
#             routes = décroisement(routes, i, j, VILLES_100)

segments_route = [(routes[i], routes[i + 1]) for i in range(len(routes) - 1)]
segments_route.append((routes[-1], routes[0]))
print(sum([d(x[0], x[1], VILLES_100) for x in segments_route]))

ax = draw(VILLES_100)
# draw_segments(ax, VILLES_100, segments)
draw_segments(
    ax,
    VILLES_100,
    segments_route,
    mcolors.CSS4_COLORS["dodgerblue"],
)
plt.show()
