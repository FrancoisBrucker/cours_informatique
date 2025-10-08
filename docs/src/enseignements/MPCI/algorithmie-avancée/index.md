---
layout: layout/post.njk 
title: "S5 : Algorithmie avancée"

eleventyNavigation:
  order: 3

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title }}"
    parent: "{{ '../' | siteUrl(page.url) }}"

---

<!-- pour l'année prochaine :

- leur donner des trucs à faire.
- faire les parcours et y retourner à chaque cours
- faire plus d'algorithmie -->

## Programme

En trois parties.

### Modèles de calculs et classes de problèmes "utiles"

> Semaine 1

{% aller %}

1. Rappels :
   1. écrire un algorithme avec [un pseudo-code](/cours/algorithmie/pseudo-code/){.interne}
   2. [importance de la complexité polynomiale](/cours/algorithmie/complexité-calculs/importance/){.interne}
2. [Réduction de problèmes](/cours/algorithmie/problème-réduction/){.interne}
3. [Problèmes de NP](/cours/algorithmie/problèmes-NP/){.interne}
4. [Le problème SAT](/cours/algorithmie/problème-SAT/){.interne}

{% endaller %}

### Théorie des graphes

> Semaine 2 à 5

Un outil de modélisation puissant pour résoudre (joliment) nombre de problèmes informatique.

#### Semaine 1

##### Cours 1

> Semaine 1

{% aller %}

1. [Graphes bases](/cours/graphes/structure){.interne} :
   1. rappel des définitions
   2. quelques propriétés sur les degrés, les chemins et les cycles
2. Rappel : [encodage d'un graphe](/cours/graphes/encodage/){.interne}
3. [cliques et stables](/cours/graphes/cliques-stables/){.interne}

{% endaller %}

##### Cours 2

{% aller %}

1. [chemins cycles et connexité](/cours/graphes/chemins-cycles-connexite/){.interne}
   1. chemin
   2. composante connexe
2. [Parcours eulériens](/cours/graphes/parcours-eulériens/){.interne}
3. [Parcours hamiltoniens](/cours/graphes/parcours-hamiltoniens/){.interne}
4. applications :
   - problème du [postier chinois](/cours/graphes/projet-postier-chinois/){.interne}
   - problème du digicode aussi appelé [mots de Bruijin](/cours/graphes/projet-mots-bruijn/){.interne}

{% endaller %}

#### Semaine 2

{% aller %}

1. [version théorie des graphes des arbres](/cours/graphes/arbres/){.interne}
   - [définitions](/cours/graphes/arbres/définitions/){.interne}
   - [tracés d'arbres](/cours/graphes/arbres/tracés/){.interne}
2. [Arbres couvrants](/cours/graphes/arbres/arbres-couvrants/){.interne}
3. [Cayley et Prüfer](/cours/graphes/arbres/cayley/){.interne}
4. [Arbres planaires et chemins de Dyck](/cours/graphes/arbres/arbres-planaires/){.interne}
5. [Arbres de Catalan](/cours/graphes/arbres/arbres-catalan/){.interne}

{% endaller %}

{% faire "**DM**" %}

L'ET de l'année dernière :

[ET 2024-2025](./ET/et.pdf){.interne}

{% endfaire %}
{% attention %}
À rendre sur papier pour le **10 octobre 2025**.
{% endattention %}

#### Semaine 3

{% aller %}

[graphes bi-parti](/cours/graphes/graphe-biparti/){.interne}

{% endaller %}

#### Semaine 4

{% aller %}

1. rappel sur [les flots](/cours/graphes/flots/){.interne}
2. couplage :
    - [problème](/cours/graphes/couplages/problème/){.interne} et [chemins augmentant](/cours/graphes/couplages/chemins-augmentant/){.interne}
    - [graphes bi-parti](/cours/graphes/couplages/couplage-bi-parti/){.interne} et idée de la [généralisation aux graphes quelconques](/cours/graphes/couplages/couplage-cas-général/){.interne}.
    - [couplage max dans les graphes bi-partis](/cours/graphes/couplages/couplage-max-bi-parti/){.interne} (si on a le temps)
3. [colorabilité des sommets d'un graphe](/cours/graphes/colorabilité/coloration-sommets/){.interne}
4. [graphes planaires](/cours/graphes/graphes-planaires/){.interne}

{% endaller %}

### DS

[sujet du DS](./DS-25-26/ds.pdf){.interne}

### Cryptographie

{% aller %}

[Sécurité](/cours/sécurité/){.interne}

{% endaller %}

> TBD en 2 semaines
> algo
> protocoles
> pgp et envois de message chiffrés

### Bonus

> TBD au choix :
>
> - recherche universelle
> - théorème de Cook-Levin
> - graphes infinis
> - méthode probabiliste ?
> - ...

## Annales

- [DS 24/25](./DS-24-25/ds.pdf)
- [ET 24/25](./DS-24-25/et.pdf)

<!-- ### Peut-être 

- Langage C
- Réseaux
- Graphes et réseaux (sociaux) 
 -->

<!--

### Problèmes de flots

#### Cours 1 : problèmes

[Problème et résolutions flots](/cours/graphes/flots/){.interne}

#### Cours 2 : applications

Exercices sur les flots :

1. [applications directs](/cours/graphes/flots-exercices/){.interne}
2. [Problèmes de transport](/cours/graphes/projet-flots-modélisation/){.interne}
3. [Bataille de la Marne](/cours/graphes/projet-bataille-de-la-marne/){.interne}

### Graphes biparti

1. [graphes bi-parti](/cours/graphes/graphe-biparti/){.interne} bases
2. [parcours de graphes classiques](/cours/graphes/parcours-largeur-profondeur/){.interne}

### DS

Temporellement placé juste après le cours 6.

[sujet](./DS/ds.pdf)

### Couplages dans les graphes

Cours 1 et 2

1. [graphes bi-parti](/cours/graphes/graphe-biparti/){.interne} (fin) :
   1. théorème de Graham-Pollack
   2. NP-complétude de la reconnaissance triparti
2. [couplage](/cours/graphes/couplage/){.interne}
3. Application : algorithme de Christofides
4. [$k$-connectivité d'un graphe](/cours/graphes/connectivité/){.interne}

### Cryptographie

Cours 1, 2 et 3

{% aller %}
[Cryptographie](/cours/sécurité/){.interne}
{% endaller %}

### Colorabilité

> TBD

### Planarité

> TBD

### Graphes aléatoires et infini

> TBD 
> 
## Autre


- [Algorithme de la recherche universelle](/cours/algorithmie/recherche-universelle/){.interne}
- révisoins

 ### C

{% lien %}
Le but de cette partie est d'avoir assez de bases en C pour s'amuser.

N'hésitez pas à suivre et à faire également les exercices du cours suivant :

<https://www.0de5.net/stimuli/a-reintroduction-to-programming/essentials/just-enough-c-to-have-fun>
{% endlien %}

1. Cours 1 : Système et consequences pour le code
   1. [architecture générale](/cours/système-et-réseau/architecture-ordinateur/#général){.interne}
   2. Mémoire :
      1. [organisation système de la mémoire](/cours/système-et-réseau/système-exploitation/process/#forme-finale){.interne}
      2. différence entre pile et tas
   3. [cours de C](/cours/système-et-réseau/langage-c/){.interne} : survole tout jusqu'aux exercices. A préparer chez vous
2. Cours 2 : [exercices en C](/cours/système-et-réseau/langage-c/exercices){.interne}

{% faire "**DM**" %}
Faire en C le [projet sac à dos](/cours/algorithmie/problème-sac-à-dos/projet){.interne}

A rendre pour le 18 octobre.
{% endfaire %}

> TBD année prochaine :
>
> 1. les faire préparer le cours :
>    1. lire le cours : (pseudo-assembleur si pas préparé avant), von Neumann et C avant
>    2. faire le premier exercice
> 2. pendant le cours faire le système avec [radare2](https://book.rada.re/intro/overview.html) qui décompile à la volée comme dans <https://www.youtube.com/watch?v=76acHVJfziw.

-->

## Modalités de contrôle

### Note

La note de cette UE résulte de cette formule :

$$
\max (\frac{DM+ DS + ET}{3}, ET)
$$

Avec :

- $DM$ devoir(s) maison ou exposé(s)
- $DS$ la note du devoir surveillé
- $ET$ est l'examen terminal

### Rendus

- un dm
- une présentation d'une jolie démonstration du proof from the book.
- un ds de théorie des graphes
