---
layout: layout/post.njk

title: Algorithmie
tags: ["cours", "algorithmie"]

authors:
  - François Brucker
resume: "Un cours d'algorithmie"

eleventyNavigation:

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Cours d'algorithmie.

{% info %}
_L'informatique n'est pas plus la science des ordinateurs que l'astronomie n'est celle des télescopes_ [E. Dijkstra](https://fr.wikipedia.org/wiki/Edsger_Dijkstra)
{% endinfo %}

Il est conseillé pour ce cours d'avoir des bases de programmation en python. Pour apprendre vous pouvez vous reporter au prérequis.

## <span id="partie-1"></span>Partie I : algorithmes

Tout ce que devrait connaître tout ingénieur de l'informatique.

{% prerequis "**Prérequis**" %}
[Bases de la programmation](/cours/coder-et-développer/bases-programmation/){.interne}
{% endprerequis %}

### Algorithmes et programmes

#### Définitions

Commençons par définir ce qu'est un algorithme et ce qu'il peut ou ne peut pas faire :

{% aller %}
[Bases théoriques](./bases-théoriques){.interne}
{% endaller %}

#### Pseudo code

On peut maintenant définir une grammaire permettant décrire des algorithmes sous la forme de pseudo-code et s'en servir pour résoudre des problèmes :

{% aller %}
[Écrire les algorithmes en pseudo code](./pseudo-code){.interne}
{% endaller %}

#### Thèse de Church-Turing

Le pseudo-code permet d'écrire des programmes sur papier que l'on peut exécuter dans sa tête aidé d'un papier et d'un crayon. Les langages de programmation permettent d'exécuter du code sur un ordinateur un utilisant [un langage de programmation](https://fr.wikipedia.org/wiki/Langage_de_programmation).

Pour la plupart d'entre eux, il est facile de transcrire le pseudo-code en code pouvant être exécuté, on a alors l'implication suivante :

{% note "**Proposition**" %}
Tout ce qui peut s'écrire en pseudo-code peut s'exécuter sur un ordinateur.
{% endnote %}

La réciproque n'est pas prouvée mais de nombreux indices (nous en verrons plusieurs dans la seconde partie de ce cours) tendent à penser que c'est vrai. On supposera donc vrai la proposition suivante, communément admise :

{% note "**Thèse de Church-Turing**" %}
Les notions d'algorithme et de pseudo-code sont équivalentes : tout algorithme peut être écrit en pseudo-code.
{% endnote %}
{% lien %}
[Thèse de Church-Turing](https://fr.wikipedia.org/wiki/Th%C3%A8se_de_Church).
{% endlien %}

La thèse de Church-Turing a été initialement formulée pour les Machines de Turing mais (nous le verrons bien plus tard) pseudo-code et machines de Turing sont deux notions équivalentes. Notez que cette affirmation n'est pas démontrée mais que toutes les tentatives (et il y en a eu) pour infirmer cette affirmation ont été des échecs.

{% lien %}

Voir [cette excellente vidéo d'Arte](https://www.youtube.com/watch?v=Zci9m08HQws) pour une introduction en douceur de la problématique.

{% endlien %}

#### Autres modèles

Le modèle du pseudo-code n'est pas la seule façon d'écrire des algorithmes. La célèbre machine de Turing que l'on verra en partie II en est un exemple. Mais il y en a beaucoup, beaucoup d'autres tous équivalent entre eux :

{% aller %}
[Autres modèles](./autres-modèles){.interne}
{% endaller %}

### Problème algorithmique

Un algorithme est sensé faire quelque chose : à partir de données passées en entrée (ses paramètres) il va produire une sortie. Cette sortie dépend de ses paramètres et répond à une question ou plus généralement résout un problème. Définissons ceci sous la forme de "_problème_" à résoudre _via_ un algorithme :

{% note2 "**Définition**" %}
Un **_problème_** est un texte composé de 3 parties :

- **Nom** : le nom du problème
- **Entrées** : les paramètres dont on a besoin
- **Sortie** : la solution recherchée

{% endnote2 %}

Par exemple :

<span id="problème-max-tableau"></span>

{% note "**Problème**" %}

- **Nom** : MAX
- **Entrée** : un tableau d'entiers
- **Sortie** : l'entier maximum du tableau

{% endnote %}

Comme tout problème n'admet pas forcément un algorithme pour le résoudre (par exemple [la complexité de Kolmogorov](./bases-théoriques/calculabilité/#complexité-Kolmogorov){.interne}, ["quand est-ce qu'on mange ?"](https://www.youtube.com/watch?v=WtetsFQHD9A) ou encore ["le sens de la vie ?"](https://www.youtube.com/watch?v=LAwDWZoETk4)), on se restreindra ici aux problèmes algorithmiques :

<span id="problème-algorithmique"></span>

{% note2 "**Définition**" %}
**_Un problème est algorithmique_** s'il existe un algorithme pour le résoudre, c'est à dire que cet algorithme :

- prend en paramètres les entrées du problème
- donne en sortie la solution recherchée.

{% endnote2 %}

Mais comment prouver qu'un algorithme répond bien au problème posé ? Il faut le prouver. 

### Preuve d'algorithme

Puisqu'il n'existe [aucune méthode générale pour savoir ce que fait un algorithme](./bases-théoriques/arrêt-rice/#théorème-rice){.interne} on ne peut jamais être sur a priori qu'un algorithme donné résous le problème attendu : il faut faire une démonstration spécifique pour chaque algorithme.

Par exemple l'algorithme suivant :

<span id="algorithme-pgcd"></span>

```pseudocode
algorithme pgcd(a: entier, b: entier) → entier:  # a, b ≥ 0
    a', b' := entier
    tant que min(a, b) > 0:
        a' ← max(a, b) - min(a, b)
        b' ← min(a, b)
        a, b ← a', b'
    
    rendre max(a, b)
```

On peut facilement prouver qu'il calcule bien le pgcd de deux nombres positifs car chaque boucle `tant que`{.language-} correspond exactement à une récursion de [la définition récurrente du pgcd que l'on a démontré précédemment](./bases-théoriques/calculabilité/#algorithme-euclide){.interne}. Ce n'est pas la peine d'en faire des tonnes (notre remarque précédente suffit), mais il est nécessaire de justifier tout ce que l'on fait/écrit.

Si la preuve n'est pas évidente, il existe des méthodes qui fonctionnent souvent :

{% aller %}
[Prouver des algorithmes](./prouver-un-algorithme){.interne}
{% endaller %}

### <span id="entraînement-preuve"></span>On s’entraîne : création d'algorithmes itératifs et récursifs

Une série de problème algorithmique à résoudre par des algorithmes simples et clairs. Le but d'un algorithme papier est d'être compris. Faites l'effort de préférer des noms de variables explicites.

{% aller %}
[Projet : Écrire et prouver des algorithmes itératifs et récursifs](./projet-itératif-récursif){.interne}
{% endaller %}

Techniques à connaître pour la mise en oeuvre et l'utilisation d'algorithmes récursifs :

{% aller %}
[Projet : techniques de récursion](./projet-techniques-de-récursion){.interne}
{% endaller %}

On vérifie qu'on sait faire :

{% aller %}
[exercices non corrigés](./exercices-itératif-récursif){.interne}
{% endaller %}

### Complexité d'un algorithme

{% lien %}
[une intro très bien faite sur la complexité des problèmes algorithmiques](https://www.youtube.com/watch?v=n8Z7v09zrl0&list=PLF0b3ThojznQJ6u4FUcpyzi0it5EpR3dh&index=12)
{% endlien %}

Cette partie s'intéresse à la notion de complexités pour un algorithme.

{% aller %}
[Calcul de complexité d'un algorithme](./complexité-calculs){.interne}
{% endaller %}

Maintenant que l'on peut calculer les complexités, on peut reprendre les algorithmes itératifs et récursifs que [nous avons crées précédemment](./projet-itératif-récursif){.interne} :

{% aller %}
[Projet : calculer des complexités d'algorithmes itératifs et récursifs](./projet-calcul-complexite){.interne}
{% endaller %}

On vérifie qu'on sait faire :

{% aller %}
[exercices non corrigés](./exercices-calculs-compexités){.interne}
{% endaller %}

### Complexité d'un problème

Cette notion est centrale en algorithmie, nous en reparlerons encore tout au log de ce cours.

{% aller %}
[Complexité d'un problème algorithmique](./complexité-problème){.interne}
{% endaller %}

Projets :

{% aller %}
1. [Calculer $x^n$](./projet-exponentiation){.interne}
2. [Les suites additives](./projet-suite-additive){.interne}
{% endaller %}

### Complexité en moyenne

{% aller %}
[Complexité en moyenne](./complexité-moyenne){.interne}
{% endaller %}

<!-- TBD

- ajouter un projet de de code. avec tableaux numpy, split de valeurs, enlever le ramasse=miette etc pour bien calculer en moyenne en code

- ajouter des exercices avec l'ordi avec plusieurs algos pour un même problème puis amélioration de la constantes multiplicative.

-->

### Problème du tri

{% aller %}
[Problème du tri](./problème-tris){.interne}
{% endaller %}

### On s'entraîne

#### Complexité

Comme exercice et pour référence, calcul de sommes classiques et utiles en complexité :

<span id="sommes-classiques"></span>

{% aller %}
[Calcul de sommes classiques](./projet-sommes-classiques/){.interne}
{% endaller %}

{% aller %}
[Calcul d'équations classiques](./projet-équations-classiques/){.interne}
{% endaller %}

#### Résolution d'algorithmes classiques

{% aller %}
[Algorithmes classiques](./projet-algorithmes-classiques){.interne}
{% endaller %}

## <span id="partie-2"></span>Partie II : structures de données

{% prerequis "**Prérequis**" %}
[Programmation objet](/cours/coder-et-développer/programmation-objet/){.interne}
{% endprerequis %}

Comment créer de nouveaux types d'objets utilisable pour nos algorithmes :

> TBD ici faire comme go ajouter un mot clé méthode avec un paramètre au début qui est le reciever.

{% aller %}
[Structures de données](structure-données){.interne}
{% endaller %}

Nous allons définir et utiliser ici des structures de données très utiles dans de nombreux problèmes : les **_structures linéaires_**.

{% lien %}
[Structures linéaires](https://www.youtube.com/watch?v=kPqk07Gpj0A)
{% endlien %}

Ces structures sont des conteneurs, comme des tableaux, qu permettent de stocker des éléments. Selon l'usage que l'on voudra en faire on privilégiera telle ou telle structure.


> TBD ajouter un TD/TP sur l'utilité de chaque structure

### Listes chaînées

Enfin, très utilisée dans les langages fonctionnels et le cas où l'on doit supprimer rapidement un élément en milieu de liste, la **_liste chaînée_** :

{% aller %}
[Les listes chaînées](./structure-liste-chaînée){.interne}
{% endaller %}

> TBD maintenir un ordre PAPS. Faire circulaire. Ex graphes cordés ?

### Pile et file

Lorsqu'un algorithme doit gérer un _flux_ de données, il doit être capable de stocker les données arrivante avant de pouvoir les traiter une à une. Les deux structures fondamentales pour cela sont les piles, les files et leurs dérivés :

{% aller %}
[Structure de pile et file](./structure-pile-file){.interne}
{% endaller %}

> TBD pile et tas. Montrer la récursion. Et la decurryfication 

### Listes

La [structure de tableau](pseudo-code/briques-de-base/#tableaux){.interne} est la base de toute structure permettant de stocker des objets. Elle est puissante car elle permet d'accéder en temps constant à tout élément qu'elle stocke (via son index) mais également limitée car le nombre d'objet qu'un tableau peut stocker (sa taille) est déterminé à sa création. Nous verrons dans cette partie que l'on peut faire sauter cette contrainte d'un tableau au prix d'un coût négligeable en complexité :

{% aller %}
[Structure de listes](./structure-liste){.interne}
{% endaller %}

### Dictionnaires

Si les listes permettent de supprimer la première contrainte de l'utilisation des tableaux qui est de déterminer leurs tailles à la création, elle ne permettent pas de pallier la seconde limitation qui est que l'accès aux éléments se fait _via_ des indices entiers. Cette contrainte peut être levée au prix d'une perte de complexité (on ne peut garantir que de bonnes complexités en moyenne et plus maximale) en utilisant des dictionnaires :

{% aller %}
[Structure de dictionnaires](./structure-dictionnaire){.interne}
{% endaller %}

> TBD associer le type {clé: valeur} aux dictionnaire.
> TBD : sortir les ensemble des dictionnaire et leur associer la structure {type}. Comme ça on a les listes avec [type], les dictionnaires avec {type:type} et les ensembles avec {type}.

### Comparaisons des structures de conteneurs

Comparons l'usage les différentes structures de stockage de données en notre possession :

- tableaux :
  - structure simple
  - intérêt : accès au $i$ème élément se fait en $\mathcal{O}(1)$
  - défaut : structure statique, on ne peut ajouter/supprimer des éléments
  - utilisation : si contrôle stricte de la complexité en temps et en espace crucial
- pile :
  - gestion de flux : LIFO
  - utilisation : à la place d'une récursion
- file :
  - gestion de flux : FIFO
  - utilisation : buffer
- listes :
  - structure passe partout
  - intérêt : ajout et suppression en fin de liste en $\mathcal{O}(1)$, accès au $i$ème élément se fait en $\mathcal{O}(1)$
  - défaut : supprimer/ajouter le $i$ème élément se fait en $\mathcal{O}(n-i)$ où $n$ est la taille de la liste.
  - utilisation : à la place d'un tableau si on autorise une taille variable et un pic de complexité de temps en temps
- dictionnaires :
  - clé et valeurs
  - intérêt : ajout et suppression et accès à un élément en $\mathcal{O}(1)$ en moyenne.
  - défaut : pas d'ordre entre en les éléments stockés, complexité max en $\mathcal{O}(n)$ où $n$ est le nombre d'éléments stockés
  - utilisation : lorsque les données ne sont pas des indices et que la complexité en moyenne suffit
- listes chaînées :
  - structure par morceaux où maillon = chaîne
  - intérêt : ajout et suppression en milieu de liste en $\mathcal{O}(1)$
  - défaut : trouver le $i$ème élément se fait en $\mathcal{O}(i)$.
  - utilisation : pour les programmes récursifs et ceux où on modifie souvent le nombre de données stockées tout en conservant l'ordre des données restantes

### Complexité de structures

{% aller %}
[Complexités d'une structure et de ses méthodes](./structures-complexité){.interne}
{% endaller %}

Il est parfois compliqué de calculer la complexité d'une méthode quand celle ci n'effectue pas toujours le même nombre d'opération, par exemple la recherche d'un élément dans un dictionnaire la méthode append des listes.

Si dans le premier cas deux recherches successive peuvent prendre $\mathcal{O}(n)$ opérations (si on a pas de chance) ce n'est pas le cas de la seconde où si un premier append prend $\mathcal{O}(n)$ opérations on sait que l'appel suivant ne prendra que $\mathcal{O}(1)$ opérations.

C'est pourquoi on parle de complexité en moyenne pour les dictionnaires et que l'on fait un calcul en _"complexité amortie"_ pour les listes. Formalisons cette notion :

{% aller %}
[Complexité amortie](./complexité-amortie){.interne}
{% endaller %}

### On s'entraîne : structures

{% aller %}
[Utilisation de structures](./projet-structures){.interne}
{% endaller %}

### Intermède 

Vous en savez maintenant assez pour comprendre et aimer les algorithmes. Nous allons montrer plusieurs exemples de problèmes et d'algorithmes plus intéressant et complexes.

#### Le problème de l'enveloppe convexe

Aussi aimé des algorithmiciens que le problème du tri, mais plus complexe à appréhender c'est pourquoi on le montre souvent plus tard, le problème de l'enveloppe convexe de points de $\mathbb{R}^2$ peut se résoudre d'un nombre incroyable de manières toutes plus élégantes les unes que les autres :

> TBD le faire avec des structures. et décomposer le gros pavé qui suit en petits bouts.

{% aller %}
[Problème de l'enveloppe convexe](./enveloppes-convexes){.interne}
{% endaller %}

<!-- 

#### Algorithmes classiques, mais dur.

> TBD ajouter une partie algorithmes classiques, v2 (les durs : col matrice, médiane en temps linéaire, Karatsuba pour la multiplication d'entiers)
 -->

## <span id="partie-3"></span>Partie III : problèmes

On se focalise sur les problèmes algorithmes et les moyens, classiques, de les résoudre.

On a vu au début de ce cours que certains problèmes [ne pouvaient pas être résolu par un algorithme](./bases-théoriques/calculabilité){.interne} (certains réels ne sont pas calculables, le problème de l'arrêt, etc) : certaines questions resteront sans réponse. De plus, on a vu également que même s'il existe un algorithme pour résoudre un problème mais que si [sa complexité est exponentielle](./complexité-calculs/importance){.interne} le temps de calcul sera rédhibitoire : certaines questions resteront sans réponse en pratique.

### Réductions : passer d'un problème à un autre

Pour voir u peu plus clair dans tous ces problèmes algorithmiques aux complexités pouvant être très différente, on se dote d'un ordre appelé _réduction_ permettant de hiérarchiser les problèmes :

{% aller %}
[Réduction de problèmes](./problème-réduction){.interne}
{% endaller %}

### Classes de problèmes

{% lien %}
<https://hardness.mit.edu/>
{% endlien %}

Pouvoir séparer les problèmes selon la facilité de leurs résolutions semble une bonne approche. On sait par exemple que le [problème du tri](./problème-tris){.interne} est de complexité $\mathcal{O}(n\ln(n))$ où $n$ est la taille du tableau d'entiers à trier ou encore que la complexité du [problème de l'exponentiation](./projet-exponentiation){.interne} est en $\mathcal{O}(\ln(n))$ où $n$ est l'exposant. Mais qu'en est-il d'un problème quelconque ? Cela nécessite quelques investigations avant de pouvoir ne serait-ce que poser le problème.

{% aller %}
[Problèmes NP](./problèmes-NP){.interne}
{% endaller %}

Le problème SAT est notre exemple de problème NP-complet. On va le voir sous différentes coutures :

{% aller %}
[Problème SAT](./problème-SAT){.interne}
{% endaller %}

### Intermède : l'algorithme qui résout tout

Avant de finir cette première partie du cours, accordons nous un intermède. Regardons une bizarrerie algorithmique, mais fondamentale dans la compréhension de ce qu'est la complexité.

{% aller %}
[L'algorithme de la recherche universelle](./recherche-universelle){.interne}
{% endaller %}

> TBD dire que complexité ce n'est pas tout. La constante devant est aussi importante !

### Design d'algorithmes

> TBD intro pour dire si on a un nouveau problème, comment chercher à le résoudre.

{% aller %}
[Design d'algorithmes](./design-algorithmes){.interne}
{% endaller %}

### Problèmes classiques

Ci-après quelques exemples classique de problèmes algorithmes (NP-complet ou non) pouvant se résoudre de multiples manières. Les connaître permet de rapidement forger une solution pour un problème nouveau.

#### Problème du sac à dos

Le problème du sac à dos est notre exemple de problème NP-complet. On va le voir sous différentes coutures :

{% aller %}
[Problème du sac à dos](./problème-sac-à-dos){.interne}
{% endaller %}

<!-- ### Jolis problèmes

On place ici quelques problèmes requérant une bonne compréhension algorithmique pour être résolu. Ce sont souvent des problèmes ardus mais la beauté de leur résolution vaut le détour.

#### Subsetsum

> TBD 3-sum complet
> TBD subsetsum en programmation dynamique

#### Chiffrement super-croissant

> -TBD chiffrage et décryptage avec un sac à dos super croissant !

#### Calcul de la médiane

> TBD enlever médiane du diviser pour régner et le mettre ici -->

<!-- #### Résolution de problèmes algorithmiques classiques

{% aller %}
[Problèmes classiques](./projet-problemes-classiques){.interne}
{% endaller %} -->

<!--

## Exercices

> ici : selection linéaire.

On rappelle ici tous les exercices que l'on va voir dans les différentes parties,

### Partie I

### Partie II

 ### Problèmes et exercices

### super croissant
> SAc a dos
>
> et piece dans le cas pas super croissant.
> 
> TBD rendu avec programmation dynamique dans le cas quelconque 9.4 de <https://info-llg.fr/option-mpsi/pdf/09.dynamique.pdf>

### autre bidules

> TBD mettre médiane en temps linéaire ici (supprimer la fin de k-select de la partie diviser pour régner).
> TBD arithmétique binaire et Karatsuba,
> TBD SUBSET-SUM par programmation dynamique <https://en.wikipedia.org/wiki/Subset_sum_problem#Pseudo-polynomial_time_dynamic_programming_solutions>

> TBD on reprend tous les exos jusque là
> TBD on ajoute les énoncés des exos durs.
> TBD faire de l'ordre dans les autres exos.

#### SUBSET SUM

> TBD def : <https://fr.wikipedia.org/wiki/Probl%C3%A8me_de_la_somme_de_sous-ensembles>

Prenons par exemple une instance $E$ du problème de somme de sous-ensemble et quelqu'un affirme que $E'$
 en est une solution. Il est aisé de vérifier la véracité de cette affirmation avec l'algorithme ci-dessous, qui prend deux paramètres, $E$
 et $E'$ :

1. On vérifie que $\vert E \vert \leq \vert E' \vert$ ce qui peut se faire en $\mathcal{O}(\vert E \vert)$ opérations en comptant chaque élément de $E'$
 et en s'arrêtant soit après en avoir compté tous les éléments soit lorsque le compte dépasse strictement $\vert E \vert$.
2. On vérifie que $E'$ est bien un sous-ensemble de $E$, ce qui peut se faire en $\mathcal{O}(\vert E \vert \cdot \vert E' \vert) = \mathcal{O}(\vert E \vert^2)$ opérations (on vérifie que chaque élément de $E'$ est dans $E$).
3. On somme les éléments de $E'$ et on vérifie que la somme finale vaut $t$
, ce qui se fait en $\mathcal{O}(\vert E' \vert) = \mathcal{O}(\vert E \vert)$ opérations.

La complexité totale du vérifieur est donc de $\mathcal{O}(\vert E \vert^2)$ opérations et ne dépend pas du paramètre $E'$.

> TBD à refaire
>
> TBD 2-SUM ≤ 2-SUM'
> TBD 2-SUM' ≤ 3-SUM
> TBD 3-SUM ≤ 3-SUM'
> TBD 3-SUM' ≤ SUBSET-SUM
> TBD SUBSET-SUM ≤ PARTITION
>

### SUBSET-SUM

Le cas général de 3-SUM est le problème SUBSET-SUM où on cherche juste un ensemble d'indice $I$ tel que $\sum_{i \in I}T[i] = s$.

> TBD montrer que 3-SUM' ≤ SUBSET-SUM (on s'arrange pour ajouter K, K' et K'' tel que pK + p'K'+p''K'' ≠ K + K'+ K'' pour tous p, p' et p'' et très grans devant les valeurs de T. T' et T''. On cherche ensuite  s=K+K'+K'')
> TBd en déduire 3-SUM ≤ SUBSET-SUM
> TBD montrer que SUBSET-SUM ≤ [PARTITION](https://fr.wikipedia.org/wiki/Probl%C3%A8me_de_partition)

> TBD à montrer.
>
> TBD <https://gnarlyware.com/blog/proving-set-partition-problem-is-np-complete-using-reduction-from-subset-sum/> -->

## <span id="partie-4"></span>Partie IV : structures de données avancées

> TBD ici parler de pointeurs et l'ajouter comme type de base. Distinguer l'objet de son adresse (ie. variable). Tout se passe comme si avant on avait que des pointeurs : un pointeur est comme un objet "variable" Fait pour gagner du temps : on met tout dans la pile par défaut. Cela accélère mais ajoute une complexité. Par défaut un tableau est constitué d'objets mis bout à bout. Permet d'avoir des tableaux de variables comme avant en utilisant des pointeurs.
>
> cette architecture est préférée pour des raisons de rapidité : car :
>
> - pas d'indirection
> - les objets dans les tableaux sont côte à côte ce qui permet des gains avec la mémoire cache.
> - objet mutable = pas d'allocation d'objet superflue
>
> Mais est est plus complexe à mettre en œuvre côté algorithme et code car un objet devient mutable par défaut. Et on ne gagne rien avec les notation O.
> TBD conséquence : supprimer les additions de la chaîne de caractère.
> TBD vérifier que tout se passe bien pour le type matrice : ie. de taille fixe.
> TBD ou alors en parler avec les structures ?
> TBD ici faire comme en go lorsque tu passes un tableau en paramètre c'est tout le tableau que tu passes
> TBD pile et mémoire expliciter la pile d'appel. avec passages de paramètres dans les fonctions. On suppose en algo que l'on a pas de soucis mais en C il faut y faire gaffe et en rust c'est interdit. En go le compilateur fait attention (escape pass du compilateur)

> TBD <https://research.swtch.com/godata>

{% aller %}
[Structures de données avancées](./structure-données-avancée){.interne}
{% endaller %}

## <span id="partie-5"></span>Partie V : modèles

Tout ce que devrait connaître tout ingénieur aimant l'informatique.

> TBD jeu d'instructions minimal.
> TBD pseudo-code = fonction booléenne finie + instruction de contrôle et boucles.
> > TBD attention à l'affectation de tableaux et aux fonctions : on autorise pas l'affectation de tableau. Tout est copié et idem pour les fonctions on la reécrit. Change la complexité temporelle * spatiale, mais ok.

### Pseudo-code

> TBD comment arriver au jeu d'instruction "minimal" permettant d'aller de pseudo-code à code exécutable

#### Pseudo-code et données binaires

{% aller %}
[Fonctions booléennes et pseudo-code](./fonctions-booléennes){.interne}
{% endaller %}

#### Pseudo-code et SAT

{% aller %}
[SAT et pseudo-code](pseudocode-SAT){.interne}
{% endaller %}

{% aller %}
[SAT et les problèmes de NP](SAT-problème-NP){.interne}
{% endaller %}

#### Exécuter du pseudo-code

> TBD von Neumann
> TBD problème de l'infini.
> TBD découpage des objets en mots pour les fonctions (16, 32, 64)
> TBD mais en interne tout est fait avec NAND

##### Pseudo-assembleur

> TBD pseudo-code minimale avec juste NAND et affectation binaire
> Dire que l'on peut donner des variables spécifique pour NAND et résultat d'affectation ce qui sépare les variables que l'on manipule de celle que l'on stocke
> On peut même encore simplifier avec juste une seule grosse variable que l'on appelle la mémoire. c'est ce que l'on va faire maintenant.

> TBD pseudo-code et FB
> est à l'assembleur ce que le pseudo-code est au code. Un principe.

> TBD fini mais permet de gérer l'infini si on le relance.

> TBD compilation il faut des langages

> abstraction pour calculer. Fonction = calculer et pseudo-code = implémenter.
> doit permettre de gérer l'infini et doit être facile à appréhender. Pour l'instant les fonction c'est abstrait (le pseudo-code n'est pas donné) et le pseudo-assembleur est fini. La pirouette qui le rend infini est un peu artificielle.
> Automates et Turing = réfléchir.
> TBD ajouter lambda calcul

##### Modèle de Von Neumann

> TBD Modèle de Von Neumann
> modèle de Von Neumann qui est implémenté dans tous les ordinateurs
> TBD attention bit dans registre et adresses ! <https://azeria-labs.com/arm-data-types-and-registers-part-2/>
> TBD monter big endian et différence entre mémoire et fonction sur 64 bits.
> on accede jamais a un bit spécifique
>
> TBD monter que les opérations arithmétique peuvent être faite par morceau (de 64bit)

{% aller %}
[Exécuter du code](./exécuter-code){.interne}
{% endaller %}

Le pseudo-code permet de concevoir des algorithmes pouvant être exécutés au tableau par des humains. L'assembleur quant à lui, language de la machine, permet d'exécuter des algorithmes sur des processeurs.
Pseudo-code et assembleurs sont équivalents : les problèmes que l'on peut résoudre avec l'un sont également résoluble avec l'autre (et réciproquement). On peut même transcrire en assembleur un programme écrit en pseudo-code de façon automatique (on a évoqué sans rentrer dans les détails les moyens d'y parvenir) il est donc courant d'écrire son code en pseudo-code, facile à lire et à maintenir, puis de laisser un compilateur le transcrire en assembleur pour être exécuté.

> Exécution automatique. Pas par un humain.

#### Pseudo-code non déterministe et NP

> TBD le thm de Levin cook démontré

> TBD. Ceci va nous permettre de démontrer le théorème de Levin-Cook.
> TBD : tout NP c'est SAT


{% aller %}
[problème SAT](./problème-SAT){.interne}
{% endaller %}

### Modèle fonctionnel

On a vue qu'un algorithme était un moyen de calculer une fonction. Précisons un peut cela en voyant quelles fonctions on peut effectivement calculer à l'aide d'un pseudo-code.

{% aller %}
[Algorithmes et fonctions](./fonctions-récursives){.interne}
{% endaller %}

> TBD lambda calcul. Ironie, c'est le premier langage Le lisp.
> TBD algorithme = fonction

### <span id="langages"></span>Langages

> DBD déf

#### Problèmes de décisions

Nous allons dans cette partie approfondir et démontrer proprement des choses que nous avons laissées en suspend à la fin de la partie I, à savoir les classes de problèmes NP et les problèmes NP-complets.

{% aller %}
[Problèmes de décision](./décision-problèmes){.interne}
{% endaller %}

> TBD dire que les deux vision des problèmes NP sont équivalentes. La solution des problèmes est le certificat des problèmes de décision. Le non déterminisme c'est trouver la solution, puis la vérification est est déterministe.

{% aller %}
[Exemples de problèmes NP complets](./exemples-problèmes-NPC){.interne}
{% endaller %}

> TBD faire bin packing NP-complet et rappeler qu'on a une heuristique gloutonne (cf. cours glouton) : <https://eecs.wsu.edu/~cook/aa/hw/s7/s7.html#:~:text=We%20can%20prove%20the%20bin,the%20bin%2Dpacking%20decision%20problem.>


#### Chaînes de caractères

> TBD premier exemple de lien encore code et structure de calcul équivalente.

> TBD on a déjà utilisé les chaines de caractères à de nombreuses reprise. Nous allons maintenant pouvoir étudier plus attentivement. Comme les algo sont de $\\{0, 1\\}^\star$ à $\\{0, 1\\}^\star$, c'est une structure fondamentale pour penser l'algorithmie et comme tout est écrit, en particulier le code, elles sont au centre de nombreux problèmes courant.

{% aller %}
[Chaines de caractères](./structure-chaine-de-caractères){.interne}
{% endaller %}

#### Machine de Turing

> Refaire.
> pseudo-assembleur.
> Permet deux choses :
>
> 1. exécuter du code. modèle de von Neumann pour . Ici taille fixe
> 2. prouver des algorithme : SAT / retour sur NP / non déterminisme co-NP
> 3. fonction sens inverse. Hash.
> Turing. Equivalent. hiérarchie des complexité

> TBD parler de NP et  co-NP factorisation et discrete log.
> TBD pas uniquement décision. Mais peut donner une version décision du pb : <https://cstheory.stackexchange.com/a/25468>

> TBD dire que circuit = taille fixée (voir conversion vers sat d'un problème. Dépend de la taille.)
> TBD ici uniquement partie code avec assembleur.
> TBD levin avec mémoire finie ou on veut : nb exponentiel. Mais si on peut aller que à gauche et à droite prop aux nb d'instructions.
> 
> TBD ici faire la machine avec mémoire finie et montrer que c'est de la logique = sat ; utiliser le pseudo-code de Knuth pour cela en montrant que pseudo-code = assembleur dans le modèle de Von Neumann
> TBD remanier le début de l'algorithmie pour décaler la file récursive ?
>
> TBD puis montrer que Turing = logique = sat.


> TBD NP/coNP par factorisation et discrete log. Dire que prime is polynomial (<https://en.wikipedia.org/wiki/AKS_primality_test>).
> TBD pas uniquement décision. Mais peut donner une version décision du pb : <https://cstheory.stackexchange.com/a/25468>
> TBD SAT dire que raisonnable puisque fct booléenne finie = SAT. Le côté dur est de montrer que ça reste vrai si l'entrée bouge.
> TBD fonction calculable = binaire + boucles = pseudo-code.
> TBD reléguer Turing à un modèle et tout faire avec le pseudo-code.
> TBD pseudo-assembleur infini en doublant la taille de l'adressage si besoin et on recommence tout l'algo.

Nous avons jusqu'à présent utilisé le modèle du pseudo-code pour créer des algorithmes.

Le pseudo-code est la partie émergée de l'algorithmie. Il permet de créer efficacement des programmes et des algorithmes. Ils sont cependant peu pratiques pour deux cas d'intérêt :

- exécuter des programmes avec un ordinateur
- penser l'algorithmie

Commençons par comprendre comment exécuter du code :

Cependant pour penser l'algorithmie, c'est à dire étudier ce qui peut ou ne peut pas être résoluble par le calcul, pseudo-code et assembleur sont encore trop _riches_ (on peut aller n'importe où dans la mémoire par exemple, on suppose l'existence de la fonction `NAND`{.language-}, etc). Il ne faut conserver que les éléments indispensables pour pouvoir écrire tout ce que l'on peut faire en pseudo-code.

> TBD pour Turing dire ok avec doublement de la mémoire si nécessaire et pseudo-assembleur.

C'est ce que propose Turing avec sa célèbre Machine : une base théorique minimale de ce qu'est l'informatique :

{% aller %}
[Machine de Turing](./machine-turing){.interne}
{% endaller %}

Nous allons agrandir dans cette partie les différents modèles de création de programmes qui produisent des résultats équivalents. On sait déjà que les programmes crées en pseudo-codes sont équivalents à ceux crées en pseudo-assembleur, eux même équivalents à ceux que l'on peut exécuter sur un processeur suivant l'architecture de Von Neumann (tous les processeurs la suive). C'est aussi le cas pour les machines de Turing :

{% note "**Théorème**" %}

Pseudo-code et machine de Turing sont deux notions équivalentes.

{% endnote %}
{% details "preuve", "open" %}

- **On peut simuler une Machines de Turing avec du pseudo-assembleur** :
  Clair puisque l'on peut simuler l'exécution d'une machine de Turing universelle en pseudo-code. Le site <https://turingmachine.io/> en est un exemple.
- **On peut simuler du pseudo-assembleur avec une Machines de Turing** :
  1. les [compositions de machines](./machine-turing/composition){.interne} montrent que l'on peut avoir les mêmes structures de contrôle qu'en pseudo-assembleur (exécution séquentielle et saut conditionnels)
  2. il est facile de faire une fonction de transition qui simule l'opération `NAND`{.language-}
  3. on peut avoir autant de ruban qu'on le veut et écrire où on veut en mémoire : on peut utiliser le modèle de von Neumann avec une machine de Turing

{% enddetails %}

#### Compilation

> bases de la compilation

### Algorithme

> TBD plein de modèles équivalent : pseudo-code, turing, fonctions, etc.

Toutes les tentatives de généraliser le modèle de la machine de Turing ont été vains. Il semble que ce modèle capte exactement ce qu'est un algorithme. C'est pourquoi les informaticiens sont intimement convaincu que la thèse de Turing-Church est vraie :

{% note "**Thèse de Church-Turing**" %}
Les notions d'algorithme et de machine de Turing sont équivalentes.

Tout algorithme peut être écrit avec une machine de Turing.
{% endnote %}

En bon informaticien, on considérera la thèse de Church-Turing vérifiée et, comme pseudo-code et machines de Turing sont équivalents :

- on écrira tous nos algorithmes en pseudo-code
- pseudo-code et algorithme seront considérés comme synonyme.

Le calcul est donc quelque chose d’éminemment local : une tête de lecture et un état, c'est la succession de ces modifications locales qui produit un résultat global. De plus, on a pas besoin de types ou de structures de données compliquées dans le modèle : seul le bit et la fonction `NAND` sont indispensable. Toutes les autres structures de données comme les listes, les piles, et autres dictionnaires sont géré par du code.

{% lien %}

- <https://plato.stanford.edu/entries/turing-machine/#ThesDefiAxioTheo>
- <https://www.youtube.com/watch?v=jUnbX27jbvY>

{% endlien %}

De part les nombreuses équivalences, lorsque l'on cherchera à démontrer des résultats sur les algorithmes en général on se ramènera aux machines de Turing, au pseudo-code ou aux fonctions récursives.

Enfin, pour savoir si un modèle donné est général, il suffit de montrer qu'il peut simuler une machine de Turing. C'est ce qu'on appelle être Turing complet.

#### Turing complet

Grâce à la machine de Turing universelle, démontrer qu'un langage est [Turing complet](https://fr.wikipedia.org/wiki/Turing-complet) c'est à dire qu'il permet de calculer tout ce qu'une machine de Turing peut calculer revient à montrer qu'on peut simuler une machine de Turing.

{% note "**définition**" %}
Un système est dit [Turing complet](./https://fr.wikipedia.org/wiki/Turing-complet) s'il permet de faire tout ce qu'une machine de Turing peut faire.
{% endnote %}

Avoir un modèle Turing Complet nous assure, en suivant la thèse de Church-Turing que ce modèle peut calculer tous les algorithmes. Pour montrer qu'un modèle est Turing-complet, on peut soit écrire un simulateur de machine de Turing (pour un langage comme python par exemple) ou, comme on l'a vu avec le pseudo-assembleur, montrer que l'on possède :

- de la mémoire
- un saut conditionnel à un endroit donnée du code
- la fonction `NAND` (ou la fonction `XOR`)

Cette preuve permet de montrer que les systèmes suivant sont Turing complet :

- un processeur
- la quasi-totalité des langages de programmation
- excel
- Factorio
- Minecraft
- ...

Ce qu'il faut retenir de tout ça, c'est qu'il est très facile d'être Turing Complet mais impossible d'être plus !


## <span id="partie-6"></span>Partie VI : aléatoire

> TBD hasard et algorithmes randomisés.

> TBD méthode probabiliste. premier exemple : <https://www.youtube.com/watch?v=4weMmFZSBtI>
{% aller %}
[Mélanger un tableau](./projet-mélange){.interne}
{% endaller %}

> TBD pi et nb aléatoire (nombre univers ?) : <https://www2.lbl.gov/Science-Articles/Archive/pi-random.html>
> TBD nombre aléatoires : <https://xkcd.com/221/> et <https://imgur.com/random-number-generator-bwFWMqQ>

> TBD : projet Multiplication de matrices randomisé calcul et vérification.: <https://www.stat.berkeley.edu/~mmahoney/f13-stat260-cs294/Lectures/lecture02.pdf> <https://eranraviv.com/randomized-matrix-multiplication/> <https://en.wikipedia.org/wiki/Freivalds%27_algorithm> <https://www.youtube.com/watch?v=z0ykhV15wLw>

> TBD <https://www.youtube.com/watch?v=LUCvSsx6-EU> ?
> TBD SAC à dos deuxième problème dur : montrer que plus dur que SAT, donc équivalent.
> TBD réduction sac a dos à bi-partition : <https://datamove.imag.fr/denis.trystram/SupportsDeCours/2017KnapSack.pdf>
> TBD subsetsum ≤ bi-partition : <https://gnarlyware.com/blog/proving-set-partition-problem-is-np-complete-using-reduction-from-subset-sum/>
> TBD premier et random : <https://www.youtube.com/watch?v=tBzaMfV94uA>
