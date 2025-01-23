---
layout: layout/post.njk
title: "Projet : Écrire et prouver des algorithmes itératifs et récursifs"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---


Écrire des algorithmes (simples) en pseudo-code pour résoudre des problèmes algorithmiques.

## Maximum d'un tableau

{% exercice %}
Donnez et prouvez **un algorithme récursif** de signature :

```pseudocode
maximum(t: [réel], i: entier) → entier
```

Qui rend un indice $0 \leq j \leq i$ tel que $t[j] = \min(\{t[k] \vert 0\leq k \leq i\})$.
{% endexercice %}
{% details "corrigé" %}

```pseudocode
algorithme maximum(t: [réel], i: entier) → entier
    si i ≥ t.longueur:
        rendre i
    sinon:
        i2 ← maximum(t, i + 1)
        si t[i2] > t[i]:
            rendre i
        sinon
            rendre i2
```

Le paramètre `i`{.language-} est un entier qui augmente strictement. Il sera donc à un moment strictement plus grand que la longueur du tableau qui est constante ce qui stoppera la récursion.

La correction se fait par récurrence sur `i`{.language-} allant de `i = t.tableau`{.language-} à `i = 0`{.language-} en décroissant.

{% enddetails %}

## Concaténation

{% exercice %}
Donnez et prouvez **un algorithme itératif** de signature :

```pseudocode
concaténation(début: [entier], fin: [entier]) → [entier]
```

Qui rend **un nouveau tableau** contenant la concaténation de `début`{.language-} et de `fin`{.language-}.
{% endexercice %}
{% details "corrigé" %}

```pseudocode/
concaténation(début: [entier], fin: [entier]) → [entier]
    t ← tableau de taille début.longueur + fin.longueur
    i = 0

    pour j allant de 0 à début.longueur - 1:
        t[i] ← début[j]
        i ← i + 1

    pour j allant de 0 à fin.longueur - 1:
        t[i] ← fin[j]
        i ← i + 1

    rendre t
```

La finitude est claire puisqu'il n'y a que deux boucles de type `pour chaque`{.language-}.

On a deux boucles, il faut donc à priori 2 invariants, un pour chaque boucle. Ici il est clair que l'on va remplir tous les éléments des tableaux `début`{.language-} et `fin`{.language-} dans `t`{.language-}. L'invariant peut être :

> si $i_0$ est la valeur de $i$ à la ligne 4 (resp. 8) alors à chaque fin d'itération les $i$ éléments de `t`{.language-} à partir de $i_0$ correspondent aux $i$ premiers éléments de `début`{.language-} (resp. `fin`{.language-}).

 Il faut juste faire très attention à l'endroit on commence dans `t`{.language-}. ici c'est Ok car avant la première boucle `i = 0`{.language-} et `i = début.longueur`{.language-} au début de la seconde boucle. Les éléments de `début`{.language-} et `fin`{.language-} ne vont pas se chevaucher dans `t`{.language-} et se suivre sans interruption.

{% enddetails %}

## Suppression de valeurs

Trouver un invariant permet de prouver efficacement un algorithme itératif. Pour des algorithmes simples, les bons invariants sont évidents à prouver une fois trouvé (on ne le donc fera pas explicitement) et permettent une preuve aisée. Entraînez vous avec l'exercice suivant :

{% exercice %}
Donnez et prouvez **un algorithme itératif** de signature :

```pseudocode
supprime(t: [entier], v: entier) → [entier]
```

Qui rend **un nouveau tableau** contenant la restriction de `t`{.language-} aux valeurs différentes de `v`{.language-}.
{% endexercice %}
{% details "corrigé" %}

Pour que l'algorithme fonctionne, il faut commencer par connaître la taille du tableau à créer et donc compter le nombre d’occurrences de `v`{.language-} dans `t`{.language-}. Ensuite, il sera possible de remplir le tableau.

```pseudocode/
algorithme supprime(t: [entier], v: entier) → [entier]
    nombre ← 0
    pour chaque e de t:
        si e == v:
            nombre ← nombre + 1
    t2 ← tableau de taille t.longueur - nombre

    j ← 0
    pour tout i allant de 0 à t.longueur - 1:
        si t[i] ≠ v:
            t2[j] ← t[i]
            j ← j + 1
    
    rendre t2
```

La finitude du programme est clair puisque l'on a que des boucles de type `pour chaque`{.language-}.

On commence à avoir l'habitude des invariants, on peut donc se permettre d'uniquement écrire le résultat d'une boucle **si celle ci est évidente**. C'est le cas de la première boucle : à l'issue de la boucle des lignes 3-5 `nombre`{.language-} vaut le nombre d'occurrences de `v`{.language-} dans `t`{.language-}.

Pour prouver la seconde boucle, l'invariant peut-être :

> à la fin de chaque itération, `t2`{.language-} contient la restriction des `i + 1`{.language-} premiers éléments de `t` différents de `v`{.language-}.

La preuve de l'invariant est évidente et permet de prouver l'algorithme en se plaçant à la fin de la dernière itération.

{% enddetails %}

Utilisez l'algorithme `concaténation`{.language-} de la question précédente pour résoudre l'exercice suivant :

{% exercice %}
Donnez et prouvez **un algorithme récursif** de signature :

```pseudocode
supprime(t: [entier], v: entier) → [entier]
```

Qui rend **un nouveau tableau** contenant la restriction de `t`{.language-} aux valeurs différentes de `v`{.language-}. Le nouveau tableau aura la même taille que le tableau `t`{.language-} passé en premier paramètre.
{% endexercice %}
{% details "corrigé" %}

```pseudocode/
algorithme supprime(t: [entier], v: entier) → [entier]
    si t.longueur == 0:
        rendre t

    t2 ← tableau de longueur t.longueur - 1
    pour i allant de 0 à t2.longueur - 1:
        t2[i] ← t[i + 1]
    
    si t[0] == v:
        rendre concaténation([], supprime(t2, v))
    sinon:
        rendre concaténation([t[0]], supprime(t2, v))
```

Il n'y a qu'une seule récursion par algorithme et la taille du tableau passé en paramètre est strictement plus petite : il y a un nombre finie de récursion puisque la condition terminale est basée sur une taille nulle de tableau.

Pour la correction une récurrence immédiate sur la taille du tableau nous permet de conclure.

{% enddetails %}

## Retournement d'un tableau

{% exercice %}
Donnez et prouvez **un algorithme récursif** de signature :

```pseudocode
reverse_indice(t: [entier], i: entier) → ∅
```

Qui **modifie le tableau** passé en entrée (il ne rend rien !) de telle sorte que les éléments $t[j]$ et $t[t.longueur - 1 - j]$ soit échangés pour tous $i \leq j < t.longueur - i$
{% endexercice %}
{% details "corrigé" %}

```pseudocode
algorithme reverse_indice(t: [entier], i: entier) → ∅
    si 
```

> TBD algorithme récursion terminale
> TBD finitude
> TBD correction

{% enddetails %}

Lorsque l'on crée des algorithmes récursif, on a souvent besoin d'initialiser les paramètres. Par exemple si l'on veut retourner complètement un tableau il faudrait écrire `reverse_indice(t: [entier], 0)`{.language-}. Le paramètre $i$ est un paramètre important pour la récursion mais inutile pour l'appel global. Pour éviter d'avoir des paramètres inutile on _encapsulera_ la fonction récursive dans un algorithme dont le seul but est d'initialiser la récursion. Pour le retournement d'un tableau, l'algorithme sera :

```pseudocode
fonction reverse_indice(t: [entier], i: entier) → ∅
    ...  # code de la fonction récursive

algorithme reverse(t: [entier]) → ∅
    reverse_indice(t, 0)
```

> TBD ici reprendre maximum récursif, avec encapsulation.

## Récursion terminale

> TBD on voit que la récursion est le dernier calcul dans l'exemple précédent. On appelle ça récursion terminale. Ceci permet de créer des algorithmes itératif. Le faire là avant de généraliser.

> TBD factorielle pas terminale. Le rendre terminale
> 
> terminale/ pas terminale. <https://web4.ensiie.fr/~dubois/recursivite.pdf>
> 
> récursivité terminale = qu'une suite d'égalité. C'est donc super.

## Dichotomie

> TBD est présent tableau trié.
> TBD récursif -> récursif terminal -> itératif
> <https://www.cs.odu.edu/~zeil/cs361/latest/Public/recursionConversion/index.html#converting-recursive-algorithms-to-iteration>

## Fonction 91 de McCarty

Mais parfois on crois que c´st pas possible alors que ça l'est.

Dans le même ordre d'idée que la fonction de Takeuchi.

> inventeur du lisp.

> TBD : <https://fr.wikipedia.org/wiki/Fonction_91_de_McCarthy>
>
> TBD a écrire algo avec récursion puis : essayer de se passer de f(f(x))
>
> 1. écrire comme récursion terminale (cf. wikipédia pour la fonction et <https://fr.wikipedia.org/wiki/R%C3%A9cursion_terminale> pour la définition)

<https://www.corsi.univr.it/documenti/OccorrenzaIns/matdid/matdid779820.pdf>
> 

> TBD et quelle est sa valeur ?

## Fibonacci

> Marche pas toujours ex : Fibonacci. On ruse.
> On peut montrer que toutes les fonctions récursives ne peuvent pas être terminale.

## Pair et impair

> TBD Récursion croisée
