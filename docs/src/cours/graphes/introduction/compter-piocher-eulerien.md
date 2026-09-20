---
layout: layout/post.njk

title: Compter et piocher des circuits Eulériens

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

## Nombre de graphes eulériens

> 1. graphes : nombre diff. à sommets fixés
> 2. idée pour les trouver puis formules
> 3. générer des graphes eulérien :
>   1. tous : tous les graphes à n-1 sommets 
>   2. en piocher 1 : générer un graphe aléatoire : Erdos reny. Outils de preuve car  tout existe presque sûrement dans un graphe aléatoire.

## Nombre de circuits eulériens

> nombre de circuit eulériens d'un graphe : <https://fr.wikipedia.org/wiki/Th%C3%A9or%C3%A8me_de_BEST>
> permet d'en piocher un au hasard en ordonnant les permutations.

> algo en trouver 1 : algo <https://fr.wikipedia.org/wiki/Algorithme_de_Havel-Hakimi>. Algo pour savoir si ça existe à degré fixé et en construire 1.
> Markov pour les trouver tous.

## Nombre de cycles eulériens

> orientation
>
## Piocher un cycle eulérien

> on commence par piocher une arborescence au hasard puis permutation au hasard.