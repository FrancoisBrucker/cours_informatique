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
maximum_rec(t: [réel], i: entier) → entier
```

Qui rend un indice $0 \leq j \leq i$ tel que $t[j] = \min(\{t[k] \vert 0\leq k \leq i\})$.
{% endexercice %}
{% details "corrigé" %}

```pseudocode
algorithme maximum_rec(t: [réel], i: entier) → entier
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

```pseudocode/
algorithme reverse_indice(t: [entier], i: entier) → ∅
    si t.longueur - 1 - i > i:
        temp ← t[i]
        t[i] ← t[t.longueur - 1 - i]
        t[t.longueur - 1 - i] ← temp

        reverse_indice(t, i + 1)
```

Les lignes 3-5 permettent d'échanger les valeurs `t[i]`{.language-} et `t[t.longueur - 1 - i]`{.language-} du tableau. On peut aussi écrire `t[i], t[t.longueur - 1 - i] ← t[t.longueur - 1 - i], t[i]`{.language-}, comme on le ferait en python, si l'on autorise le fait d'affecter 2 valeurs **en même temps**.

Le finitude est claire puisque :

1. il n'y a qu'un appel récursif
2. chaque appel se rapproche strictement de la condition d'arrêt

La correction vient du fait que l'on échange bien des valeurs symétriques du tableau par rapport à l'indice du milieu du tableau qui est ici la partie entière de $t.longueur - 1/ 2$.

{% enddetails %}
{% attention %}
Lorsque l'on manipule des indices de tableau il faut **toujours** :

1. attentivement vérifier que tout se passe bien.
2. faire attention aux divisions entières.

{% endattention %}

Lorsque l'on crée des algorithmes récursif, on a souvent besoin d'initialiser les paramètres. Par exemple si l'on veut retourner complètement un tableau il faudrait écrire `reverse_indice(t: [entier], 0)`{.language-}. Le paramètre $i$ est un paramètre important pour la récursion mais inutile pour l'appel global. Pour éviter d'avoir des paramètres inutile on _encapsulera_ la fonction récursive dans un algorithme dont le seul but est d'initialiser la récursion. Pour le retournement d'un tableau, l'algorithme sera :

```pseudocode
fonction reverse_indice(t: [entier], i: entier) → ∅
    ...  # code de la fonction récursive

algorithme reverse(t: [entier]) → ∅
    reverse_indice(t, 0)
```

La méthode ci-dessus est indispensable à connaître car lorsque l'on manipule des algorithmes récursifs les paramètres font office de variables que l'opn pourrait avoir pour des algorithmes itératifs.

Entraînons nous :

{% exercice %}
Encapsulez la fonction récursive `maximum_rec(t: [réel], i: entier) → entier`{.language-pseudocode} du premier exercice dans une fonction permettant de rendre le maximum d'un tableau passé en paramètre.

{% endexercice %}
{% details "corrigé" %}

```pseudocode
algorithme maximum(t: [entier]) → entier
    rendre maximum_rec(t, 0)
```

{% enddetails %}

## Récursion terminale

{% lien %}
[Récursion terminale](https://fr.wikipedia.org/wiki/R%C3%A9cursion_terminale)
{% endlien %}

```pseudocode

algorithme f(n: A) → B:
    si c(n) == Vrai:
        rendre g(n)
    sinon:
        rendre f(h(n))
```

Où `c: A → Booléen`{.language-}, `g: A → B`{.language-} et `h: A → A`{.language-} sont trois fonctions parfaitement définies.

Pour que la définition de `f`{.language-} ait du sens il faut bien sur que chaque récursion sr _rapproche_ de la condition d'arrêt. C'est ce qu'il faut démontrer pour chaque algorithme sous la forme d'une récursion terminale.

La récursion terminale est sympathique car équivalente à la forme itérative suivante :

```
algorithme f(n: A) → B:
    tant que c(n) est Faux:
        n ← h(n)
    rendre g(n)
```

Ce qui permet une implémentation en machine efficace (c'est ce que font les compilateur lorsque'ils repèrent une telle forme).

> A peut être de toute forme, c'est souvent un type composé comme on le verra.

### un

> plus petite puissance de 2 strictement plus grande que n
> signature à deux paramètres.
> 
### Transformer en une forme terminale
Entraînons nous à écrire de tels algorithmes :

```pseudocode
algorithme factorielle(n: entier  # n > 1
                      ) → entier:
    si n == 1:
        rendre 1
    rendre n * factorielle(n-1)
```

> TBD pas terminale
> pour le rendre terminale on ajoute un paramètre qui va véhiculer les calculs intermédiaire
> TBD donner la signature et à eux de faire.

> TBD autre exo.

> TBD la def. et pourquoi c'est bien.
> TBD formalise le fait d'avoir plus que paramètre que nécessaire : on donne les résultats intermédiaires en paramètre. Cela permet de réduire le nombre d'appels et transforme la récursion en itération (en machine c'est comme ça qu'on fait)

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

{% lien %}
[John McCarty](https://fr.wikipedia.org/wiki/John_McCarthy) fût un informaticien de renom et le créateur [du langage Lisp](https://fr.wikipedia.org/wiki/Lisp) en 1958. Lisp est le premier langage fonctionnel et a été [le deuxième langage de programmation](https://fr.wikipedia.org/wiki/Histoire_des_langages_de_programmation) au monde, deux ans après le Fortran.

{% endlien %}

Mais parfois on crois que c´est pas possible alors que ça l'est.

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

## Récursion croisée

Une dernière technique qui peut être utile est la récursion croisée qui définie une fonction par rapport à une autre et réciproquement :

{% exercice %}
Écrire les deux fonctions récursives suivantes sans utiliser de division entière :

```pseudocode
algorithme pair(n: entier) → booléen
algorithme impair(n: entier) → booléen
```

Vous pourrez utiliser le fait que `pair(0)`{.language-} est vrai alors que'`impair(0)`{.language-} est faux.

{% endexercice %}
{% details "corrigé" %}

```pseudocode
algorithme pair(n: entier) → booléen
    si n == 0:
        rendre Vrai
    rendre non impair(n - 1)

algorithme impair(n: entier) → booléen
    si n == 0:
        rendre Faux
    rendre non pair(n - 1)

```

La finitude est claire puisque :

1. il n'y a qu'un appel récursif
2. chaque appel se rapproche strictement de la condition d'arrêt

La correction est évidente par définition de la parité.

{% enddetails %}
