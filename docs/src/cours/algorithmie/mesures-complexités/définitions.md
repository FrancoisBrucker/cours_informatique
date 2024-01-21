---
layout: layout/post.njk

title: Définitions

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

[On l'a vu](../../écrire-algorithmes/pseudo-code/#complexité), on appelle complexité d'un pseudo-code le nombre d'opérations élémentaires utilisées pour son exécution.

Le pseudo-code suivant, qui calcule la dixième valeur de la suite de Fibonacci a une complexité $C = 45$ :

```text#
F = un tableau vide de 10 cases
F[0] = 1
F[1] = 2

pour i allant de 2 à 9:
  F[i] = F[i-1] + F[i-2]

rendre F[9]
```

{% exercice %}
Explicitez les différentes instructions élémentaires pour justifier la valeur de la complexité de l'algorithme précédent.
{% endexercice %}
{% details "corrigé" %}

Il y a quatre types d'instructions élémentaires :

- les affectations :
  - ligne 1 : on affecte une valeur au tableau
  - ligne 2, 3 : on affecte une valeur à une case du tableau
  - ligne 5 : on affecte les valeurs 2 à 9 à la variable i
  - ligne 6 : on affecte une valeur à une case du tableau
- les récupérations de variables :
  - ligne 6 : on récupère les valeurs de 2 cases du tableau
  - ligne 8 : on récupère les valeurs de 1 case du tableau
- opérations sur des entiers :
  - ligne 6 : une somme
- retour de l'algorithme en ligne 8

On en conclut la complexité de chaque ligne :

- ligne 1 : 1 instruction
- ligne 2 : 1 instruction
- ligne 3 : 1 instruction
- ligne 4 : 0 instruction
- ligne 5 : 1 instruction
- ligne 6 : 4 instructions
- ligne 7 : 0 instruction
- ligne 8 : 2 instructions

Comme la ligne 5 et 6 sont exécutées 8 fois, on en conclut que la complexité est :

$$
1+1+1+0+ 8\cdot(1 + 4) + 0 + 2 = 45
$$
{% enddetails %}

Mais souvent la complexité dépend des paramètres du programme, comme par exemple le pseudo-code suivant qui rend la $n$ème valeur de la suite de Fibonacci où $n$ est le paramètre de l'algorithme :

```text#
fonction fibonacci(n):
  F = un tableau vide de n cases
  F[0] = 1
  F[1] = 2

  pour i allant de 2 à n-1:
    F[i] = F[i-1] + F[i-2]

  rendre F[n-1]
```

Le nombre de fois où l'on rentre dans la boucle va dépendre de l'entrée et on a maintenant une complexité de $C(n) = 5\cdot(n-1)$ qui dépend de la valeur du paramètre d'entrée.

{% exercice %}
Montrez que la complexité est bien de $5\cdot(n-1)$
{% endexercice %}
{% details "corrigé" %}

On ne rentre plus 8 fois dans la boucle mais $n-2$ fois. La complexité est alors : $5 + (n-1)\cdot 5 = 5n-5$.

{% enddetails %}

Enfin, en règle générale, la complexité dépend trop profondément de la nature même de ses entrées et empêche d'en tirer une allure général. Par exemple l'algorithme suivant, écrit en python, qui cherche si une `valeur`{.language-} est dans un `tableau`{.language-} :

```text#
fonction est_dans_tableau(valeur, tableau):
    pour chaque élément x du tableau:
        si x == valeur:
            rend OUI
    rend NON
```

La complexité de cet algorithme va dépendre de l'endroit où se trouve la valeur dans le tableau. Si l'on utilise la taille $n$ du tableau comme paramètre de complexité, sa complexité ira de 3 lorsque la valeur est le premier élément du tableau (une affectation de $x$, un test et un retour) à $2n + 1$ si la valeur n'est pas dans le tableau ($n$ affectations de $x$, $n$ tests et un retour). La complexité de l'algorithme est alors $C(i) = 2i + 1$ où $i$ est la position de la valeur dans le tableau.

## Complexité d'un algorithme

> TBD ici

Lorsque l'on utilise un algorithme on a jamais autant de connaissances sur les données, on ne connaîtra par exemple pas toutes les valeurs du tableau, mais juste sa taille. Dans ce cas là on calculera la complexité maximale pour tous les tableaux de même taille.

Il n'y a pas de règle immuable dans le choix des connaissances que l'on s'accorde sur les paramètres. Il faut essayer de prendre les connaissances minimales qui donnent un résultat acceptable tout en prenant en comte toutes les entrées possibles.

Par exemple pour la fonction `fibonacci(n)`{.language-} on a considéré que l'on connaît la valeur de $n$ et pas juste que c'était un entier, sinon la complexité aurait-été le maximum possible pour tous les entiers et on aurait eu une complexité infinie.

Il n'y a pas de règle immuable quand au bon choix de paramètre pour la complexité. Il faut :

1. que ce paramètre permette de traiter tous les cas possibles
2. rester le plus général possible tout en gardant un résultat intéressant.

Les connaissances minimales que l'on possède sur les données sont leurs tailles. Commencez donc par là, puis affinez si nécessaire.

{% note %}

***la taille des entrées d'algorithme*** est le nombre de cases mémoires nécessaires pour les stocker c'est à dire :

- 1 pour un nombre ou un caractère
- la somme des tailles des éléments d'un conteneur
{% endnote %}

Au final :

{% note "**Définition**" %}

***La complexité $C(N)$ d'un algorithme $A(p_1, \dots, p_m)$*** est le nombre maximum d'opérations élémentaires effectuées pour exécuter l'algorithme $A$ avec des entrées dont la some des tailles vaut $N$.
{% endnote %}
{% info %}
Comme dit, si cette complexité est infinie (comme dans le cas de `fibonacci(n)`{.language-}) changez de paramètre $N$.
{% endinfo %}

## Autres types de Complexité

### Complexité min

### Complexité en temps

Si chaque opération élémentaire prend le même temps à être effectuée sur une machine (ou que l'on borne le tout par l'opération élémentaire la plus gourmande), la complexité d'un pseudo-code nous donne un nombre proportionnel au temps qu'il mettra à s'exécuter :

{% note %}
Le temps mis pour un code à être exécuté est proportionnelle à la complexité de son pseudo-code associé.
{% endnote %}

Enfin, L'autre paramètre utile que l'on mesure est le nombre de cases mémoires utilisées par l'algorithme, c'est à dire la taille des variables dont il a besoin pour fonctionner.

Notre fonction `fibonacci(n)`{.language-} par exemple nécessite $n+1$ cases mémoires, en plus de ses paramètres, pour fonctionner :

- $n$ pour le tableau
- 1 pour le stockage de l'entier $i$

Comparez avec l'algorithme suivant qui calcule aussi le $n$ème élément de la suite de Fibonacci :

```text#
fonction fibonacci_sobre(n):
  a = 1
  b = 1

  pour i allant de 2 à n-1:
    c = a + b
    a = b
    b = c

  rendre b
```

Il demande beaucoup moins de mémoire, 4 cases seulement (pour stocker les variables $a$, $b$, $c$ et $i$), ce qui lui permet de calculer de grandes valeurs de la suite de Fibonacci, plus grande que la taille mémoire de l'ordinateur qui exécute l'algorithme.

Sa complexité un peu plus élevée, $8n-12$, mais reste comparable au premier.

{% info %}
Souvent, lors du design de nos algorithmes on aura le choix entre entre consommer beaucoup de mémoire et être sobre en instructions ou le contraire.
{% endinfo %}

### Complexité en Mémoire

{% note "**Définition**" %}

On distinguera trois types de complexités lors de l'exécution d'un pseudo-code/code :

- complexité (en nombre d'instructions) : nombre d'opérations basiques effectuées
- complexité en temps : temps mis pour effectuer le code
- complexité en mémoire : taille mémoire maximale consommée pendant l'exécution

Chacune de ces complexités se calculent en fonctions de paramètres liées à l'entrée de l'algorithme qu'il faut expliciter.
{% endnote %}

Ces trois types de complexités sont liées : 

- la complexité en temps est proportionnelle à la complexité

Notez que comme l'accès à la mémoire compte comme une opération, la complexité en mémoire est
Les complexités vont toutes dépendre des entrées, plus précisément d'un paramètre rendant compte de leur **taille**, c'est à dire du nombre de cases mémoires nécessaires pour les stocker.

> C'est un peut chiant de faire comme ça et c'est pas très utile de faire tous ces détails :
> 
> 1. pas se faire suer avec tous les détails. Par exemple, comment fonctionne la boucle for ? Juste une affectation on bien c'est une somme si on l'écrit avec un tant que ?
> 2. ce qui nous intéresse c'est les grosses valeurs, lorsque c'est petit ça va vite et on s'en fiche.
> 3. la tendance de la complexité est cruciale : faire schéma des complexités.
> solution = $\mathcal{O}$, oméga et théta.
>
> enfin 
De plus 
> allure similaire, même si on va plus vite/plus lentement.

On peut également mesurer le nombre de cases mémoire utilisé par le pseudo-code et on parle alors de *complexité spatiale* pour la distinguer de la complexité en nombre d'opérations.

> TBD : Notez que l'on a pas besoin d'une mesure précise, seule l'allure suffit à déterminer son asymptote.

> TBD : mettre $\mathcal{O}$ (parler de $\Omega$) et ajouter $\Theta$  dans un truc à part pour expliquer pourquoi c'est central en informatique (Turing aussi). Avec hiérarchie des complexité Polynomial vs exponentiel (faire tous les cas).

> notion de complexité : temps nécessaire pour.

## Importance de la complexité

1. nb d'opérations élémentaires = mesure du temps
2. dépend de l'entrée : faire graphique.
