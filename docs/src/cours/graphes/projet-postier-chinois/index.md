---
layout: layout/post.njk

title: "Problème du postier chinois"
authors: 
    - François Brucker

eleventyNavigation:
  key: "Problème du postier chinois"
  parent: "Graphes"
---

<!-- début résumé -->

Un problème d'optimisation où la théorie des graphes peut aider.

<!-- fin résumé -->

Nous allons étudier le problème du [postier chinois](https://fr.wikipedia.org/wiki/Probl%C3%A8me_du_postier_chinois), proposé par le mathématicien chinois [管梅谷](https://fr.wikipedia.org/wiki/Meigu_Guan) en 1962 :

{% note "**Définition :**" %}
Soit $G = (V, E, A)$ un [graphe mixte](../structure#definition-graphe-mixte) connexe, et $f: E \cup A \rightarrow \mathbb{R}^+$ une fonction de valuation des arcs et arêtes.

Le **problème du postier chinois** consiste à trouver un pseudo-circuit (des arêtes/arcs peuvent apparaître plusieurs fois) passant par toutes les arêtes et les arcs du graphe mixte de coût (la somme des valuations des arcs/arêtes le constituant) minimum.
{% endnote %}

Nous nous intéresserons ici à un cas particulier du problème où $G$ est juste un graphe :

{% note "**Définition :**" %}
Soit $G = (V, E)$ un graphe connexe, et $f: E \rightarrow \mathbb{R}^+$ une fonction de valuation des arêtes.

Le **problème du postier chinois** consiste à trouver un pseudo-cycle (des arêtes peuvent apparaître plusieurs fois) passant par toutes les arêtes du graphe de coût (la somme des valuations des arcs/arêtes le constituant) minimum.
{% endnote %}

Le problème du postier chinois permet de modéliser les problèmes de tournées (poste, ramassage des ordures, ...) dans des villes.

{% info %}
On est obligé de  considérer des pseudo-cycles car le graphe considéré n'est pas forcément [eulérien](../parcours-eulériens) : il faut passer plusieurs fois par certaines arêtes pour en atteindre d'autres.
{% endinfo %}

## Modélisation d'une ville par un graphe

Prenons l'exemple de la poste. Un facteur doit passer par chaque rue d'un quartier pour délivrer le courier, le départ et l'arrivée de sa tournée se faisant au bureau de poste du quartier. Pour que sa tournée soit la plus courte possible il faut qu'il repasse le moins possible par les même rues.

Pour modéliser cela informatiquement, il faut commencer par modéliser une ville ou un quartier par un graphe mixte. La façon classique de procéder est de considérer :

* que les croisements forment l'ensemble des sommets
* les routes à double sens forment les arêtes
* les routes à sens unique forment les arcs

Dans ce qui suivra :

* on considérera ue toutes les routes sont à double-sens (non orienté)
* qu'il ne peux exister qu'une route entre deux croisement (pas de multi-graphe)

Un quartier, une ville ou la partie du monde considéré est un graphe $G=(V, E)$ connexe où :

* les rues sont les arêtes
* les croisements sont les sommets

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

Ce graphe a 188 sommetd et 452 arêtes. Chaque sommet est un numéro (comme `268931860`) et les arêtes sont des triplets `(sommet origine, sommet arrivé, numéro d'arête)`. Le numéro d'arête est par défaut 0 (c'est le cas général s'il n'y a qu'une arête par couple de sommet).

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

Les fond de cartes sont disponibles dans la bibliothèque [contextily](https://contextily.readthedocs.io/en/latest/). Commençez par l'installer :

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
