---
layout: layout/post.njk
title: Projet chemin de longueur min et openstreetmap
authors: 
    - François Brucker

eleventyNavigation:
  key: "Projet chemin de longueur min et openstreetmap"
  parent: "Graphes"
---

<!-- début résumé -->

Application du problème de la recherche de chemins de longueur minimum à la création de trajets routiers.

<!-- fin résumé -->

> TBD à finir

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


### grand graphes

C'est la technique utilisée par google maps. Pour le graphe de google maps, il est impossible de faire un algorithme de Dijkstra à chaque requête, cela prendrait bien trop de temps !

On ne peut pas non plus mettre les chemins en dur, car il faudrait une base de donnée gigantesque. Comment résoudre ce problème épineux ?

En utilisant des hubs ! On remarque en effet que lorsque l'on fait un plus court chemin entre 2 sommets quelconques sur un graphe de google maps les débuts de chemins sont souvent identiques (on prend les grandes routes) et divergent fortement à la fin (petites routes jusqu'à la destination).

On procède alors à un pré-traitement en calculant pour chaque sommet $x$ tous les chemins les plus courts (on crée l'arborescence de ce sommet). Et pour chaque chemin ainsi crée, on choisit la ville avec le plus d'habitants qui se trouve sur le second tiers du chemin. Toutes ces villes constituent les *hubs* de ce sommet $x$.

{% note %}
Notez que si l'on va de A à B sur des routes à double sens, le hub pour le chemin allant de A à B est le même que le hub pour le chemin allant de B à A.
{% endnote %}

Sur une carte de géographie, on remarque qu'il y a très peu de hubs !

Une fois ce pré-traitement effectué, lorsqu'un utilisateur veut aller de A à B :

1. google choisi un hub commun H1 à A et B et crée 2 routes, une allant de A à H1 et l'autre allant de H1 à B
2. on récurse pour les chemins créés en cherchant un hub commun H2 à A et H1 et un hub commun H2' à H1 et B et ainsi de suite jusqu'à arriver à des chemins *"courts"*.
3. jusqu'à arriver à des chemins courts où l'on peut faire un dijkstra entre les deux sommets rapidement.

Le temps de calcul en est très réduit puisque les hubs sont calculés en amont de la requête.

{% exercice %}
Montrez avec les 3 (plus belles) villes (de France) que sont Marseille, Strasbourg et Brest comment les choix de hubs peuvent drastiquement influencer le chemin proposé.
{% endexercice %}
{% details "solution" %}
* Marseille a Dijon et Paris dans ses hub. Le premier pour aller de Marseille à Strabourg et le second pour aller de Marseille à Brest
* Strasbourg à également Dijon et Paris dans ses hubs le premier pour aller à Marseille (c'est symétrique) et le second pour aller à Brest.

![chemin hubs](chemin_hubs.png)

Google maps peut alors vous proposer deux grands chemins pour aller de Marseille à Strasbourg, soit en passant par Dijon soit par Paris (bon il ne le fait pas car un chemin est bien plus long que l'autre, mais c'est l'idée).

Les hubs, en plus d'être efficaces en temps de calculs sont aussi une chouette solution pour proposer des itinéraires différents pour aller entre 2 villes.
{% enddetails %}
