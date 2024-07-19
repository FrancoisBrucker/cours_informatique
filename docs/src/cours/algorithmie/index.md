---
layout: layout/post.njk

title: Algorithmie
tags: ["cours", "algorithmie"]
authors:
  - François Brucker

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

Il est conseillé pour ce cours d'avoir des bases de programmation en python. Pour apprendre vous pouvez vous reporter au cours [coder et développer](/cours/coder-et-développer).

## Algorithmes et programmes

Commençons par définir ce qu'est un algorithme et ce qu'il peut ou ne peut pas faire :

{% aller %}
[Bases théoriques](./bases-théoriques){.interne}
{% endaller %}

On peut maintenant définir une grammaire permettant décrire des algorithmes sous la forme de pseudo-code et s'en servir pour résoudre des problèmes :

{% aller %}
[Écrire des algorithmes](./écrire-algorithmes){.interne}
{% endaller %}

Le pseudo-code ressemble à un langage de programmation comme le python que l'on peut exécuter sur un ordinateur. Voyons comment ceci est possible :

{% aller %}
[Exécuter du code](./exécuter-code){.interne}
{% endaller %}

Maintenant que l'on sait comment écrire des algorithmes en pseudo-code et que l'on peut les compiler (automatiquement) en assembleur pour être (également automatiquement) exécuté sur un ordinateur. Il nous reste une voie à explorer, la voie théorique qui nous permettra d'extraire les lois fondamentale de l'algorithmique pour penser l'informatique :

{% aller %}
[Penser l'algorithmie](./penser-algorithmie){.interne}
{% endaller %}

## On s'entraîne : itératif vs récursif

> TBD premières séries d'exercice permettant comprendre comment créer des algorithmes simple de façon itérative, r´´cursives et comment passer de l'un à l'autre.

Écrire des algorithmes simples en pseudo-code (ou en python) pour résoudre des problèmes algorithmiques.

> TBD : écrire des algos pour résoudre des problèmes.
> TBD essence même d'un algorithme c'est la boucle et les if/them/else
> sinon fait tout le temps la même chose (addition, etc). Le problème est de transformer une idée en code et en succession logique d'arguments (conditions) et d'action (instruction) tant que ce n'est pas résolu (boucles).
>
>
> 1. exos simples avec 1 boucle puis 2 boucles imbriquées (compter le nb d’occurrences,  suppression de doublons, max tableau, etc)
> 2. dichotomie
> 3. récursion et pile d'appel (tours de hanoï ; min et max d'un tableau)
> 4. plusieurs boucles a la suite
> 5. récursion et boucles
>
> voir les parties complexité et remettre si possible les réponse dans cette partie.
>
> exemples :
>
> - <https://www.youtube.com/watch?v=pKO9UjSeLew>

### Algorithmes itératif

### Algorithmes récursif

terminale/ pas terminale. <https://web4.ensiie.fr/~dubois/recursivite.pdf>
TBD :
>
> 1. factorielle.
> 2. Fibonacci
> 3. Triangle de pascal (optimisation pas tout garder)
> 4. hanoi
> 5. lancers de nd6 avec nombre max de récursion à trouver.
> 
### Rendre itératif des algorithmes récursifs

> TBD grace à une todo list (aka une pile)
<https://www.youtube.com/watch?v=HXNhEYqFo0o>

> TBD :
>
> cours ici  <https://www.cs.odu.edu/~zeil/cs361/latest/Public/recursionConversion/index.html#converting-recursive-algorithms-to-iteration>
> 1. factorielle (reprendre ce qu'on a vue et le formaliser)
> 2. recursive simple : montrer que l'on peut sauver les paramètre et les remettre avec une todo list
> 3. on peut faire mieux avec récursivité terminale et sa chaîne d'égalité.
> 4. fonction 91 de Mc Carty. Récursif mais pas terminal. Montrer qu'on peut le rendre terminal.
> 5. Fibonacci. par terminal. On utilise la pile. Puis on simplifie. A la fin fibo plus besoin de pile.
> 6. Pas toujours le cas. Exemple : Ackermann.
>
> - recursivité terminale = qu'une suite d'égalité. C'est donc super.
> - <https://www.lirmm.fr/~dony/notesCours/c4.s.pdf>
> - <https://www.enseignement.polytechnique.fr/informatique/INF321/Amphis12/amphi5.pdf>
> - <https://web4.ensiie.fr/~dubois/recursivite.pdf> fact est récursive primitive.L'écrire de façon itérative.

### Fonction 91 de McCarty

Dans le même ordre d'idée que la fonction de Takeuchi.

> TBD : <https://fr.wikipedia.org/wiki/Fonction_91_de_McCarthy>
>
> TBD a écrire algo avec récursion puis : essayer de se passer de f(f(x))
>
> 1. écrire comme récursion terminale (cf. wikipédia pour la fonction et <https://fr.wikipedia.org/wiki/R%C3%A9cursion_terminale> pour la définition)
> 2. avec un tant que utiliser <https://www.cs.odu.edu/~zeil/cs361/latest/Public/recursionConversion/index.html#converting-recursive-algorithms-to-iteration> pour faire <https://www.corsi.univr.it/documenti/OccorrenzaIns/matdid/matdid779820.pdf>
>  
> récursivité terminale = qu'une suite d'égalité. C'est donc super.
>

> TBD et quelle est sa valeur ?

#### Ackermann, le retour

Essayons de voir comment écrire l'algorithme d'Ackermann sans toutes ces récurrences, comme on l'a fait avec la fonction 91.

Pour calculer $\text{Ack}(m, n)$ :

1. soit $m=0$ alors $A = n+1$
2. soit $m>0$ et $n=0$ et alors $A = \text{Ack}(m-1, 1)$
3. soit $m>0$ et $n>0$ et alors :
     1. $A = \text{Ack}(m, n-1)$
     2. $A = \text{Ack}(m-1, A)$

On voit que ce n'est pas une formulation récursive terminale à cause du troisième cas. En 3.2 :

- on utilise la valeur de $A$ calculée en 3.1
- on utilise la valeur que valait $m$ avant 3.1

Il faut donc se rappeler de $m$ pour le calcul de 3.2 tout en utilisant la valeur de $A$ calculée précédemment. Pour ce genre de récursion, on peut utiliser une [TODO list](https://fr.wikipedia.org/wiki/To-do_list) qui nous permet de nous rappeler toutes les tâches à effectuer et des variables à sauvegarder :

1. on commence avec une TODO liste vide
2. positionner les variables $m$ et $n$ à leurs valeurs et $A$ à 0
3. on ajoute à la liste le triplet (1, m, n)
4. tant que la TODO liste n'est pas vide :
   1. prendre le dernier item de la list (en le supprimant de la liste)
      1. si le premier élément de l'item vaut 1 alors on affecte :
         1. $m$ au second élément du triplet
         2. $n$ au troisième élément du triplet
      2. si le premier élément vaut 2 alors on affecte :
         1. $m$ au second élément du triplet
         2. $A$ à $n$
   2. On fait le calcul :
      1. si $m=0$ alors $A=n+1$
      2. si $m>0$ et $n=0$ alors on ajoute $(1, m-1, 1)$ à la TODO list
      3. si $m>0$ et $n>0$ alors :
          - on ajoute $(2, m-1)$ à la TODO list
          - on ajoute $(1, m, n-1)$ à la TODO list
5. rendre $A$

> TBD faire $A(2, 3)$

On peut même se passer de $A$ complètement :

1. on commence avec une TODO liste vide
2. positionner les variables $m$ et $n$ à leurs valeurs
3. on ajoute à la liste l'entier $m$
4. tant que la TODO liste n'est pas vide :
   1. prendre le dernier item de la list (en le supprimant de la liste) et en l'affectant à $m$
   2. On a un choix selon les valeurs de $m$ et $n$ :
      - si $m=0$ alors $n=n+1$
      - si $m>0$ et $n=0$ alors (récursion terminale):
          - $n = 1$
          - ajoute l'entier $m-1$ à la TODO  List
      - $m>0$ et $n>0$ alors :
          - ajoute l'entier $m-1$ à la TODO  List
          - ajoute l'entier $m$ à la TODO  List
          - $n=n-1$
5. rendre $A$

{% info %}
Implémentation en python en utilisant une liste comme TODO-list :

```python
def Ack(m, n):
    s = [m]
    while (s):
        m = s.pop()
        if m == 0:
            n += 1
        elif n == 0:
            s.append(m - 1)
            n = 1
        else:
            s.append(m - 1)
            s.append(m)
            n -= 1
        return n
```

{% endinfo %}

> pas récursivité terminale = il faut faire des trucs en plus de la récursion. Il faut se rappeler de que l'on veut faire. Avec une TODO list (faire exemple avec ack petit) = pile en informatique
> faire un item de la todo list = dépile.
>

> 
> truc à faire = empile
> <https://www.cs.odu.edu/~zeil/cs361/latest/Public/recursionConversion/index.html#conversion-using-stacks>
> 1. curryfication puis decurryfication
> A(m, n) = A(0, n')
> A'(s, n) = A'(s[:-1], A(s[-1], n))
> A'([m], n) = A(m, n) par récurrence sur m+n = k
>
> TBD faire la preuve que c'est ok (voir <https://stackoverflow.com/a/54356919>)

{% info %}
Notez que tout algorithme récursif peut s'écrire de façon itérative avec une TODO-list (une pile).
{% endinfo %}

## Complexités

Cette partie s'intéresse à la notion de complexités pour un algorithme et un problème.

{% aller %}
[Calcul de complexité d'un algorithme](./complexité-calculs){.interne}
{% endaller %}
{% aller %}
[Complexité d'un problème algorithmique](./complexité-problème){.interne}
{% endaller %}

La notion de complexité est centrale en algorithmie, nous en reparlerons encore plus tard dans le cours.

## On s'entraîne : problèmes liés à l'exponentiation

{% aller %}
[Calculer $x^y$](./projet-exponentiation){.interne}
{% endaller %}
{% aller %}
[Les suites additives](./projet-suite-additive){.interne}
{% endaller %}

> TBD reprendre les exos d'avant avec calcul de complexité.

## Complexité en moyenne

{% aller %}
[Complexité en moyenne](./complexité-moyenne){.interne}
{% endaller %}

## Problème du tri

{% aller %}
[Problème du tri](./problème-tris){.interne}
{% endaller %}

## On s'entraîne : exercices de complexité et de preuve

{% aller %}
[Algorithmes classiques](./projet-classiques){.interne}
{% endaller %}

> TBD faire un lien avec les exos vu en écriture d'algo + complexité pour que tout soit aussi là.

## Structures linéaires

{% aller %}
[Chaines de caractères](./structure-chaine-de-caractères){.interne}
{% endaller %}
{% aller %}
[Conteneurs](./structure-conteneurs){.interne}
{% endaller %}

> TBD ajouter exos pour dictionnaires.

## Complexité amortie

> TBD A déplacer plus tard. Attention à l'amortie des dict/liste.

{% aller %}
[Complexité amortie](./complexité-amortie){.interne}
{% endaller %}

## Design d'algorithmes

{% aller %}
[Design d'algorithmes](./design-algorithmes){.interne}
{% endaller %}

## Problème du "sac à dos"

> TBD Intro NP et NPC. Doit tenir 2h pour montrer pourquoi NP = problème algo et réduction simple (max ≤ tri ; en trouver un autre.
> on a égalité si ≤ et ≥. Faire exemple simple puis faire SAT = 3-sat (le faire)).
>
> question P ≤ NP ouverte.
> 
> TBD : Dire, mais laisser la démo pour plus tard, que SAT est supérieur à tout.
> tbf montrer dans la partie sac à dos qu'il est inf à sat.
> ici exemple de problème pas dans P (on ne sais pas)

{% aller %}
[Problème du sac à dos](./problème-sac-à-dos){.interne}
{% endaller %}

> TBD : ici stop partie I. Ensuite Partie II.

## Classes de Problèmes Algorithmiques

> TBD Nouvelle partie en algo.

{% aller %}
[Classes de problèmes algorithmiques](./classes-problèmes){.interne}
{% endaller %}

> Ici Turing et NPC avec SAT.

## Désordre et hasard

{% aller %}
[Mélanger un tableau](./projet-mélange){.interne}
{% endaller %}

> TBD nombre aléatoires

## Enveloppes convexes

{% aller %}
[Problème de l'enveloppe convexe](./enveloppes-convexes){.interne}
{% endaller %}

> TBD nombre aléatoires
