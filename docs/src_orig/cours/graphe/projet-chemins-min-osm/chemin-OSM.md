---
layout: layout/post.njk

title: OpenStreetMap
authors: 
    - François Brucker

eleventyNavigation:
  key: "OpenStreetMap"
  parent: "Projet chemins de longueur minimum"
---

<!-- début résumé -->

Utilisation d'openstreetmap pour trouver des chemin de longueur minimum.

<!-- fin résumé -->

> TBD à finir

> TBD <http://download.geofabrik.de/index.html>

## Code

Il existe de nombreuses bibliothèques de graphes en python, nous allons utiliser ici [`networkx`{.language-}](https://networkx.org), en utilisant la bibliothèque [`osmnx`{.language-}](https://github.com/gboeing/osmnx) qui permet de récupérer des données d'<https://www.openstreetmap.fr/>. Commençons par l'[installer]({{ "/tutoriels/installation-python#packages" | url}})

```
python -m pip install osmnx scikit-learn
```

La commande ci-dessus devrait installer tout ce qui est nécessaire. Testez là en exécutant le code python suivant :

```python
import osmnx as ox

Marseille = ox.graph.graph_from_address('Marseille, France')
ox.plot_graph(Marseille)
```

Vous devriez voir apparaître (après un certain temps) une fenêtre avec un graphe où l'on devine le [vieux-port de Marseille](https://www.google.fr/maps/@43.2944646,5.3601266,16z).

Le type de graphe utilisé (`type(Marseille)`{.language-}) est un [`MultiDiGraph`{.language-}](https://networkx.org/documentation/stable/reference/classes/multidigraph.html), c'est l'équivalent *code* d'un multi-graphe mixte.

### Obtenir des graphes

On peut utiliser aussi d'autres façon de récupérer des données.

#### A partir d'une adresse

{% chemin %}
<https://osmnx.readthedocs.io/en/stable/osmnx.html#osmnx.graph.graph_from_address>
{% endchemin %}

```python
import osmnx as ox

ecm = ox.graph.graph_from_address('Ecole centrale marseille', dist=2000)
ox.plot_graph(ecm)
```

{% info %}
Diminuez la distance pour *reconnaître* l'école.
{% endinfo %}

#### A partir d'une boite `bbox`

{% chemin %}
<https://osmnx.readthedocs.io/en/stable/osmnx.html#osmnx.graph.graph_from_bbox>
{% endchemin %}

```python
import osmnx as ox

marseille_en_grand = ox.graph.graph_from_bbox(43.388, 43.168, 5.498, 5.295, network_type='drive')
ox.plot_graph(marseille_en_grand)
```

{% info %}
Vous pouvez utilisez <http://norbertrenner.de/osm/bbox.html> pour construire vos `bbox`.
{% endinfo %}

#### A partir de coordonnées GPS

{% chemin %}
<https://osmnx.readthedocs.io/en/stable/osmnx.html#osmnx.graph.graph_from_point>
{% endchemin %}

```python
import osmnx as ox

ailefroide = ox.graph.graph_from_point((44.8833273, 6.444307), dist=3000, network_type='all')

ox.plot_graph(ailefroide)
```

{% info %}
On peut facilement voir où c'est grace à google maps : <https://www.google.fr/maps/@44.8833273,6.444307,13z>

Les 3 paramètres sont latitude, longitude, zoom.
{% endinfo %}

### Données

Le graphe crée contient directement les données géographiques associées.

Sur le graphe d'Ailefroide dans un interpréteur python :

```python
>>> import osmnx as ox
>>> ailefroide = ox.graph.graph_from_point((44.8833273, 6.444307), dist=3000, network_type='all')
>>> 
>>> print(len(ailefroide.nodes))
188
>>> print(len(ailefroide.edges))
451
```

Ce graphe a 188 sommets et 452 arêtes. Chaque sommet est un numéro (comme `268931860`) et les arêtes sont des triplets `(sommet origine, sommet arrivé, numéro d'arête)`. Le numéro d'arête est par défaut 0 (c'est le cas général s'il n'y a qu'une arête par couple de sommet).

Pour connaître le sommet associé à une coordonnée, on utilise les fonctions : 

* [`get_nearest_nodes`](https://osmnx.readthedocs.io/en/stable/osmnx.html#osmnx.distance.nearest_nodes)
* [`get_nearest_edges`](https://osmnx.readthedocs.io/en/stable/osmnx.html#osmnx.distance.nearest_edges)

Par exemple sur le graphe d'`ailefroide`{.language-} précédent :

```python
sommet = ox.distance.nearest_nodes(ailefroide, 44.91771033167592, 6.416818457077778)
arete = ox.distance.nearest_edges(ailefroide, 44.91771033167592, 6.416818457077778)
```

La ligne de code `print(ailefroide.nodes[sommet])`{.language-} va nous donner :

```python
{
  'y': 44.8707699, 
  'x': 6.4812867, 
  'street_count': 3
}
```

C'est à dire que le nœud sommet est aux coordonnées GPS (44.8707699, 6.4812867) et est de degré 3.

De même la ligne de code `print(ailefroide.edges[arete])`{.language-} va donner :

```python
{
  'osmid': [871717564, 871717565], 
  'highway': ['path', 'track'], 
  'oneway': False, 
  'reversed': True, 
  'length': 617.9159999999999, 
  'geometry': <shapely.geometry.linestring.LineString object at 0x12ef87fd0>
}
```

De toutes ces propriétés on aura uniquement besoin ici du fait que c'est une route à double sens de 618m de longueur.

### Fond de cartes

Les fond de cartes sont disponibles dans la bibliothèque [contextily](https://contextily.readthedocs.io/en/latest/). Commencez par l'installer :

```
python -m pip install contextily
```

#### Dessiner la carte

On utilise matplotlib :

```python

```

#### Système de coordonnées

Pour trouver un fond de carte adapté, il faut faire attention au système de coordonnées utilisé par la carte, appelé le [CRS](https://medium.com/cr%C3%A9ation-dune-app-cartographique-avec-firebase-vue/.comprendre-les-coordinates-reference-system-crs-b67a88bce63c). POur la carte d'Ailefroide, la commande `print(ailefroide.graph)`{.language-} donne :

```python
{
  'created_date': '2022-11-02 13:46:36', 
  'created_with': 'OSMnx 1.2.2', 
  'crs': 'epsg:4326', 
  'simplified': True
}
```

Ici c'est [epsg:4326](https://epsg.io/4326) qui est utilisé, c'est à dire celui du GPS. Ne confondez pas avec [espg:3857](https://epsg.io/3857) qui est la projection de Mercator (classique des cartes)

## Résolution du problème

si euler ok. 

Si graphe aussi ok avec couplage (on verra l'algo bien plus tard mais ca marche)

Si graphe mixte : np difficile.


## projet


1. OSM et Marseille : chemins
2. OSM et Marseille : circuit de ramassage des ordures [Et si l'on codait tout ça ?]({{ "/cours/graphes/circuits-euleriens" | url }})

> TBD :
>
> * utiliser OSM pour vérifier si marseille est connexe, trouver des chemin entre, etc.
> * utiliser networkx (ou autre pour ça)
