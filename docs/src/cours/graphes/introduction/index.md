---
layout: layout/post.njk

title: Introduction à la théorie des graphes

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

À partir des définitions générales sur de leur utilité algorithmique et pratique, nous allons raconter une histoire à priori simple dont les ramifications vont nous montrer de nombreuses facettes de la théorie des graphes.

## <span id="structure"></span> Structure d'un graphe

{% aller %}

1. [Structure d'un graphe](structure){.interne}
2. [Encodage de graphes](encodage){.interne}

{% endaller %}

Connexités :

{% aller %}

[Chemins, cycle et connexité](chemins-cycles-connexite){.interne}

{% endaller %}

Les plus simples des graphes connexes :

{% aller %}

[Les Arbres](arbres){.interne}

{% endaller %}

## Aller d'un sommet à un autre

{% aller %}

[Chemin de valuation minimale dans un graphe](chemins-valuation-min){.interne}

{% endaller %}

## Parcourir tout le graphe

### Graphes Eulérien


L'origine de la théorie des graphe :

{% aller %}

[Chemins et cycles Eulérien](parcours-eulériens){.interne}

{% endaller %}

Et une conséquence inattendue (exercice de modélisation) :

{% aller %}

[Mots de Bruijn](mots-bruijn){.interne}

{% endaller %}

Codons tout ça :

{% aller %}

[Projet : Graphes eulérien](projet-graphes-eulerien){.interne}

{% endaller %}

> ICI graphes eulériens.
> 1. combien il y en a 
>   1. graphes : nombre diff. à sommets fixés
>   2. idée pour les trouver puis formules
>   3. générer des graphes eulérien :
>     1. tous : tous les graphes à n-1 sommets 
>     2. en piocher 1 : générer un graphe aléatoire : Erdos reny. Outils de preuve car  tout existe presque surement dans un graphe aléatoire.

### Graphes Hamiltoniens

> TBD parler de 2-opt (dirigé ou pas) et de la 2-approximation si distance sur graphe complet.
> TBD ce qu'on a fait avec ds arêtes pourquoi pas le faire avec des sommets ?

> TBD garder juste dirac et tournois existencxe puis méthode probabiliste
> TBD ajouter algo en $2^n$ qui est mieux que n!



> TBD Garder couplage pour pas dans l'intro.
> TBD : 
> 1. définition du problème.
> 2. cas où on sait le faire :
>   1. tournoi + méthode probabiliste (cf ds 2026)
>   1. degrés dirac (déplacer ore dans les parties détaillées)
>   2. arbres 
>   3. acyclique pour chemin le plus long : et conséquence inattendue sr le BTP (pb d'ordonnancements. Aussi DFS !)
> 3. cas général métrique et complet
>   1. pas simple : exhaustif avec backtrack + branch and bound
>   2. approximation : 
>     1. 2-opt 
>     2. performance garantie :  algo + ALM
{% aller %}

> TBD est-ce normal que l'on ne puisse pas trouver d'algo simple pour résoudre le pb ?

1. [Chemins et cycles Hamiltonien](parcours-hamiltoniens){.interne}
2. [cycle-chemin](./projet-chemins-cycles){.interne}

{% endaller %}

> TBD voir comment faire pour aller mieux -> pb du couplage.
> TBD à la fin du couplage. Se poser la question de résolution exacte ? NP-complet. et on y va.
> TBD ci NP algo
