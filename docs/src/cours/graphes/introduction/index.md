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

## Graphes Eulérien

L'origine de la théorie des graphe :

{% aller %}

[Chemins et cycles Eulérien](parcours-eulériens){.interne}

{% endaller %}

Et une conséquence inattendue (exercice de modélisation) :

{% aller %}

[Mots de Bruijn](projet-mots-bruijn){.interne}

{% endaller %}

> ICI graphes eulériens.
> 1. combien il y en a 
>   1. idée pour les trouver puis formules
>   2. générer un graphe aléatoire : Erdos reny. Intro + graphe Rado + isomorphisme
> 2. distribution des degrés pairs ? Y'en a qui existent pas.
>   1. formule générale + algo pour en trouver 1
>   2. suite décroissantes -> graphes EUlérien et généraux
>   3. les trouver tous ? Au moins aléatoirement.



> TBD générer des graphes avec degrés fixe pour essayer nos algorithmes
> TBD on random des nombres dans une borne et on continue
> TBD connexité <https://www.cambridge.org/core/services/aop-cambridge-core/content/view/4BE766CCFDF1704C196AA182C0C5EC88/S0008414X00044734a.pdf/combinatorial_properties_of_matrices_of_zeros_and_ones.pdf> le montre avec des matrices, nous juste avec un graphe.

## Graphes Hamiltoniens

> TBD ce qu'on a fait avec ds arêtes pourquoi pas le faire avec des sommets ?

> TBD : 
> 1. définition du problème.
> 2. cas où on sait le faire :
>   1. degrés
>   2. arbres + partie arbres (déf + ALM)
>   3. acyclique : et conséquence inattendue sr le BTP
> 3. cas général métrique et complet
>   1. pas simple : exhaustif avec backtrack + branch and bound
>   2. approximation : 
>     1. 2-opt 
>     2. performance garantie : 
>       1. algo + ALM
>       2. idée du couplage (avec performance garantie mais si on pouvait faire ça mieux ce serait bien !)
> 4. couplage : ici juste complet avec méthode hongroise.
{% aller %}

> TBD est-ce normal que l'on ne puisse pas trouver d'algo simple pour résoudre le pb ?

1. [Chemins et cycles Hamiltonien](parcours-hamiltoniens){.interne}
2. [cycle-chemin](./projet-chemins-cycles){.interne}

{% endaller %}

> TBD voir comment faire pour aller mieux -> pb du couplage.
> TBD à la fin du couplage. Se poser la question de résolution exacte ? NP-complet. et on y va.
> TBD ci NP algo
