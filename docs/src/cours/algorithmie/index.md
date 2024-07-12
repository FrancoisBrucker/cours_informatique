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

> TBD : déplacer complexité à après. Insister sur algorithme = programme + fin et preuve de ce que ça fait.

{% aller %}
[Exécuter du code](./exécuter-code){.interne}
{% endaller %}

> Dire que algo = au tableau/papier et pour les humains. Deux branches ensuite : exécution sur un ordinateur/réfléchir à la nature même de l'algorithmie (Turing). Selon ce qu'on voudra faire on utilisera l'un ou l'autre des formalismes. Nous Algo et on laisse la machine (le python) transcrire en langage machine pour être exécuté. Penser les algo se fera plus tard, mais on vous montre juste le modèle, archi connu : la machine de Turing.

### Penser l'informatique

> TBD : Turing.
> faire Fibonacci avec une machine de Turing.
> dire que structure de donnée = code et que l'on a besoin de rien comme outil pour exécuter du code : juste une façon de stocker et une façon d'écrire conditionnellement. Le code est LOCAL.

> TBD le plus minimal c'est la machine de Turing, mais d'un point de vue opérationnel il est minimal car c'est ce qui est appelé assembleur.
> faire les call avec des jump
> à la fin dire qu'il y a souvent plusieurs autres méthodes dans les langages machines pour aider (donner exemple, sub, mul, gestion approximation de réel, call/ret et surtout la pile qu'on verra bien plus tard.), mais on peut tout faire avec ce qu'on a la.
> 
> Passer d'un pseudo code à un langage machine simple et montrer sn équivalence. Ceci permettra de montrer plus facilement que des langages sont équivalents.
> Langage simplifié où les variables n'existent pas et le boucles sont remplacés par des saut. Tout langage informatique peut être transcrit en langage machine
> instructions finie et 1 ou deux paramètres et une sortie dans des variables fixées et de taille fixé disons 64bits appelées registres.
> variables = un grand tableaux de cases de taille fixée. Disons 64bits

{% aller %}
[Penser l'informatique](){.interne}
{% endaller %}

## On s'entraîne

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

TBD :
>
> 1. factorielle.
> 2. Fibonacci
> 3. Triangle de pascal (optimisation pas tout garder)
> 4. hanoi
> 
### Rendre itératif des algorithmes récursifs

> TBD :
>
> 1. factorielle.
> 2. recursive simple : montrer que l'on peut sauver les paramètre et les remettre avec une todo list
> 3. on peut faire mieux avec récursivité terminale et sa chaîne d'égalité.
> 4. fonction 91 de Mc Carty. Récursif mais pas terminal. Montrer qu'on peut le rendre terminal.
> 5. Fibonacci
> 6. un truc avec todo-list.
> 2. montrer que l'on peut l
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

> Ici fion théorique = Turing et NPC avec SAT.

#### Machines de Turing

> TBD :
> passer de pseudo-assembleur à turing :
>
> - opérations (ok, juste bits)
> - code vers transitions
> - ruban unique (registre)
> - pointeur unique
> - RAM vers décalage de 1
>
> Code de Von Neuman = MTU
> 1. pseudo-code = algorithme : thèse de Church/Turing
> 2. uniquement binaire
> 3. pas besoin de :
>   - séparer variables et mémoire
>   - de RAM juste se déplacer de 1
>   - code, juste des états
> 4. on est arrivé à la Machine de Turing. Donc code ≤ Turing
> 5. comme on peut simuler ue machine de Turing avec un algo : Turing ≤ code

> TBD : ne garder que la machine à 1 ruban ici.

Cette partie est là pour vous montrer que pseudo-code et machines de Turing sont deux notions équivalentes. On aura également besoin des machines de Turing bien plus tard, lorsque nous rencontrerons les classes de problèmes.

{% aller %}
[Machines de Turing](./machine-turing){.interne}
{% endaller %}

## Autres modèles

L'écriture d'algorithmes sous la forme de pseudo-code n'est qu'une des nombreuses façon d'en écrire. Nous allons en voir 4 toutes équivalentes les unes avec les autres !

>
> TBD : Turing vers formule SAT.
> donc algorithme = formule logique.

>
> TBD : séparer modèle et MTU qui permet de simuler dans le modèle. C'est le principe d'un ordinateur.
> TBD encore d'autres ! jeu de la vie, ...


#### Lambda calcul

> TBD : pour les matheux qui veulent s'encanailler à faire de l'informatique
> Catégories et types : <https://bartoszmilewski.com/2014/10/28/category-theory-for-programmers-the-preface/>, <https://ncatlab.org/nlab/show/computational+trilogy>
> <https://www.youtube.com/watch?v=_n4LIt2WPzE>
> Maths : <https://www.paultaylor.eu/~pt/prafm/index.html>
> <https://www.haskell.org/> :
>
> - intro : <https://www.youtube.com/watch?v=UhM_H3lFk_Q>
> - playlist <https://www.youtube.com/watch?v=Vgu82wiiZ90&list=PLe7Ei6viL6jGp1Rfu0dil1JH1SHk9bgDV>
> - livre : <https://learnyouahaskell.com/>

#### Automates cellulaires

> TBD : Jeu de la vie
> TBD : <https://fr.wikipedia.org/wiki/Automate_cellulaire#R%C3%A8gle_110>

#### Équivalence des différentes approches

> TBD : à supprimer de la partie sur les machines de Turing et à mettre ici.
> TBD MTU = langage universel

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
