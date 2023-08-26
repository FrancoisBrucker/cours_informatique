---
layout: layout/post.njk

title: Projet chemins avec hub
authors: 
    - François Brucker

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

<!-- début résumé -->

> TBD à faire
> * idem que chemin mais avec villes > 10000 en ne supprimant pas l'île de France
> * utiliser networkx pour les algorithmes
> * mettre des hubs en place avec le 1/3

## Chemin de poids min dans des grands graphes

C'est la technique utilisée par google maps. Pour le graphe de google maps, il est impossible de faire un algorithme de Dijkstra à chaque requête, cela prendrait bien trop de temps !

On ne peut pas non plus mettre les chemins en dur, car il faudrait une base de donnée gigantesque. Comment résoudre ce problème épineux ?

En utilisant des hubs ! On remarque en effet que lorsque l'on fait un plus court chemin entre 2 sommets quelconques sur un graphe de google maps les débuts de chemins sont souvent identiques (on prend les grandes routes) et divergent fortement à la fin (petites routes jusqu'à la destination).

On procède alors à un pré-traitement en calculant pour chaque sommet $x$ tous les chemins les plus courts (on crée l'[arborescence](../chemin-poids-min#arborescence){.interne} de ce sommet). Et pour chaque chemin ainsi crée, on choisit la ville avec le plus d'habitants qui se trouve sur le second tiers du chemin. Toutes ces villes constituent les *hubs* de ce sommet $x$.

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

