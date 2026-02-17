---
layout: layout/post.njk

title: Algorithmes classiques

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Algorithmes classiques dont l'intérêt est à la fois esthétique (ce sont de jolis algorithmes),pratiques (ils mettent en oeuvre des techniques facilement réutilisables) et didactiques (trouver et prouver leurs fonctionnement vous fera progresser).

## Fibonacci

> - **Utilité** : à connaître car :
>   - exemple de transformation d'un algo de complexité exponentiel à linéaire.
>   - un algorithme dont la complexité vaut sa valeur dans le cas récursif simple
> - **Difficulté** : facile pour la création et la complexité de base


[La suite de Fibonacci](https://fr.wikipedia.org/wiki/Suite_de_Fibonacci) est définie par l'équation de récurrence :

<div>
$$
F(n) =
\begin{cases}
F(n-1) + F(n-2) \text{ si }n> 2\\
F(1) = F(2) = 1
\end{cases}
$$
</div>

Nous allons utiliser cette suite pour donner des techniques utiles pour l'étude d'algorithmes récursifs

### Valeurs

{% exercice %}
En utilisant l'équation de récurrence, montrez que :

<div>
$$
\begin{array}{ccccc}
\Omega((\sqrt{2})^n)&=&F(n)&=& \mathcal{O}(2^n)
\end{array}
$$
</div>

{% endexercice %}
{% details "corrigé" %}
La suite de Fibonacci est clairement croissante (vous pouvez le prouver par récurrence), ce qui permet d'écrire :

<div>
$$
\begin{array}{ccccc}
&&F(n) = F(n-1) + F(n-2)&&\\
2\cdot F(n-2)&\leq&F(n)&\leq& 2\cdot F(n-1)\\
4\cdot F(n-4)&\leq&F(n)&\leq& 4\cdot F(n-2)\\
&&\dots&&\\
2^p\cdot F(n-2p)&\leq&F(n)&\leq& 2^p\cdot F(n-p)\\
2^{n/2}\cdot F(1)&\leq&F(n)&\leq& 2^n\cdot F(1)\\
2^{n/2}&\leq&F(n)&\leq& 2^n\\
(\sqrt{2})^{n}&\leq&F(n)&\leq& 2^n
\end{array}
$$
</div>

{% enddetails %}

En utilisant le fait que la suite de Fibonacci est [une suite récurrente linéaire](https://fr.wikipedia.org/wiki/Suite_r%C3%A9currente_lin%C3%A9aire), on peut même donner une valeur explicite de chaque valeur. Démontrons le :

{% exercice %}
En utilisant le fait que les deux racines du polynôme $P(X) = X^2 -X-1$ sont $\phi_+ = \frac{1 + \sqrt{5}}{2}$ et $\phi_- = \frac{1 - \sqrt{5}}{2}$, montrez que pour $n>0$ :

<div>
$$
\begin{cases}
\phi_+^n = F(n)\phi_+ + F(n-1)\\
\phi_-^n = F(n)\phi_- + F(n-1)\\
\end{cases}
$$
</div>

En déduire la valeur de $F(n)$

{% endexercice %}
{% details "corrigé" %}

Les deux égalités sont clairement vraies (par récurrence) pour tout $n>1$. En les soustrayant et en utilisant le fait que $\phi_+ - \phi_- = \sqrt{5}$ permet de conclure que :

<div>
$$
F(n) = \frac{\phi_+^n - \phi_-^n}{\sqrt{5}}
$$
</div>

{% enddetails %}

### Fibonacci récursif

<span id="algorithme-fibonacci-rec"></span>

```pseudocode/
algorithme fibonacci_rec(n: entier) → entier:
    si n ≤ 2:
        rendre 1
    rendre fibonacci_rec(n-1) + fibonacci_rec(n-2)
```

{% exercice %}
Montrez que le programme précédent est bien un algorithme qui calcule la valeur de Fibonacci.
{% endexercice %}
{% details "corrigé" %}
Il faut démontrer que ce programme est bien un algorithme car il y a plusieurs récursions !

Ceci se fait facilement par une récurrence sur $n$ car chaque appel se rapproche strictement de la condition d'arrêt.

1. initialisation : `fibonacci_rec(n)`{.language-} admet un nombre fini de récursion pour $n\leq 2$.
2. hypothèse de récurrence : `fibonacci_rec(m)`{.language-} admet un nombre fini de récursion pour $m < n$.
3. Pour $n$, `fibonacci_rec(n - 1)`{.language-} et `fibonacci_rec(n-2)`{.language-} se terminent en un nombre fini de récursion donc la ligne 4 de l'algorithme aura aussi un nombre fini de récursion.

Une fois la finitude démontrée la correction est évidente, comme souvent avec les algorithmes récursifs, puisque l'algorithme ne fait que transcrire l'équation de récursion.

{% enddetails %}

{% exercice %}
Montrez que la complexité de l'algorithme `fibonacci_rec(n)`{.language-} est en $\Omega(F(n))$.
{% endexercice %}
{% details "corrigé" %}
En notant $C(n)$ la complexité de `fibonacci_rec(n)`{.language-}, on a clairement l'équation suivante :

<div>
$$
C(n) = \mathcal{O}(1) + C(n-1) + C(n-2)
$$
</div>

On prouve ensuite par récurrence que si $C(m) = \Omega(F(m))$ pour tout $m < n$ alors :

<div>
$$
C(n) = \mathcal{O}(1) + \Omega(F(n-1)) + \Omega(F(n-2)) = \mathcal{O}(1) + \Omega(F(n-1) + F(n-2)) = \mathcal{O}(1) + \Omega(F(n)) = \Omega(F(n))
$$
</div>
{% enddetails %}

Sa complexité est rédhibitoire.

### Récursif terminal

L'algorithme récursif est sous optimal car il recalcule plein de fois la même chose. Pour calculer $F(n)$ il calcule deux fois $F(n-2)$, une fois dans la somme et une fois dans le calcul de $F(n-1)$.

{% exercice %}

Utilisez [la transformation en récursion terminale](../projet-itératif-récursif/#transformer-rec-terminale){.interne} qui consiste à stocker les variables nécessaires au calcul récursif dans des paramètres (il faudra ici stocker 2 résultats indermédiaires, $F(n-1)$ et $F(n-2)$) pour améliorer la complexité de  l'algorithme récursif.
{% endexercice %}
{% details "corrigé" %}

 En utilisant deux accumulateurs, l'un pour $F(n - 1)$, l'autre pour $F(n - 2)$ on obtient :

<span id="algorithme-fibonacci-rec-terminale"></span>

```pseudocode
fonction fibonacci_rec_terminale(n: entier, acc_n_1: entier, acc_n_2: entier) → entier:
     si n == 2:
          rendre acc_n_1
     sinon si n ≤ 1:
          rendre acc_n_2
     
     rendre fibonacci_rec_terminale(n-1, acc_n_1 + acc_n_2, acc_n_1)


algorithme fibonacci_rec(n: entier) → entier:
    rendre fibonacci_rec_terminale(n, 1, 1)

```

L'algorithme se termine  puisque le paramètre d'arrêt de la récursion, `n`{.language-}, décroît strictement à chaque appel.

Par une récurrence triviale sur `n`{.language-}, les paramètres `acc_n_1`{.language-} et `acc_n_2`{.language-} de l'appel de `fibonacci_rec_terminale(n - i, acc_n_1, acc_n_2)`{.language-} valent :

- `acc_n_1`{.language-} vaut $F(i + 2)$
- `acc_n_2`{.language-} vaut $F(i + 1)$

Lors du dernier appel on a `fibonacci_rec_terminale(2, acc_n_1, acc_n_2)`{.language-} et donc `acc_n_1`{.language-} vaut $F(n-2 + 2) = F(n)$

La complexité $C(n)$ de l'algorithme satisfait l'équation de récurrence :

<div>
$$
C(n) = \mathcal{O}(1) + C(n-1)
$$
</div>

On a déjà vu cette récurrence, elle vaut : $C(n) = \mathcal{O}(n)$.

{% enddetails %}

### Fibonacci Itératif

{% exercice %}
Créez un algorithme itératif calculant $F(n)$ avec une complexité de $\mathcal{O}(n)$
{% endexercice %}
{% details "corrigé" %}
On adapte l'algorithme en récursion terminale :

<span id="algorithme-fibonacci-itératif"></span>

```pseudocode
algorithme fibonacci(n: entier) → entier:
    (acc_n_1 := entier) ← 1
    (acc_n_2 := entier) ← 1

    tant que n > 1:
        temp ← acc_n_1 
        acc_n_1 ← acc_n_1 + acc_n_2
        acc_n_2 ← acc_n_1
        n ← n - 1
    
    rendre acc_n_1
```

Sa correction est claire puisque c'est la transcription de l'algorithme récursif terminal et sa complexité est évidemment $\mathcal{O}(n)$.

{% enddetails %}

## $X$ marks the spot

> - **Utilité** : crucial à comprendre
> - **Difficulté** : dur

Un robot se déplace sur une droite à la vitesse de 1 mètre par seconde. Il doit chercher un endroit particulier sur cette droite à $X$ mètres de 0, $X$ pouvant être **positif ou négatif** mais est entier. Cette endroit est inconnu pour le robot, mais s'il passe sur cet endroit il le reconnaîtra.

{% exercice %}
Donnez un algorithme en $\mathcal{O}(X)$ permettant au robot d'atteindre $X$ à partir de sa position initiale qui vaut $0$.
{% endexercice %}
{% details "corrigé" %}

Remarquer que l'on ne peut pas :

1. avancer uniquement dans une direction : il faut osciller
2. osciller en incrémentant d'un pas constant : on est de complexité au carré de $X$ (c'est facile à montrer)

L'idée est d'osciller autour de l'origine en puissances de 2 :

1. avancer de $2^0 = 1$ : position finale $+1$
2. reculer de $2^0 + 2^0$ : position finale $-1$
3. avancer de $2^0 + 2^1$ : position finale $+2$
4. reculer de $2^1 + 2^1$ : position finale $-2$
5. avancer de $2^1 + 2^2$ : position finale $+4$
6. reculer de $2^2 + 2^2$ : position finale $-4$
7. avancer de $2^2 + 2^3$ : position finale $+8$
8. reculer de $2^3 + 2^3$ : position finale $-8$
9. ...

Au pire, le robot arrivera sur la marque $X$ au bout de $2 \cdot \log_2(X)$ itérations.

Il aura effectué un déplacement d'au plus : $2 \cdot (X + X/2 + X/4 + \dots + 1)$ unités. Or $2 \cdot (X + X/2 + X/4 + \dots + 1) = 2\cdot X \cdot \sum_{i=0}^{i=\log_2(X)} 1/2^i = 2\cdot X \cdot(1- 1/2^{\log_2(X)}) = \mathcal{O}(X)$.

L'astuce de se déplacer par puissance de 2 permet de majorer la distance par $X$ car la série des $\sum 1/2^i$ qui est, on l'a vu, convergente. Il est crucial de connaître cette technique qui vous tirera de nombreux mauvais pas en algorithmie.

{% enddetails %}

## Compteur binaire

> - **Utilité** : algorithme à la base de nombreux autres algorithmes d'énumération. A connaître pour son énumération récursive.
> - **Difficulté** : moyen

Un entier écrit sous forme binaire peut s'écrire comme un tableau $x$ composées de bits (entier valant 0 ou 1). Par exemple l'entier 19 s'écrira $N = [1, 1, 0, 0, 1]$ avec $19 = \sum_i N[i] \cdot 2^i$

L'algorithme `algorithme successeur(N: [bit]) → vide:`{.language-} suivant prend en paramètre un entier écrit sous sa forme binaire et qui **le modifie** pour que sa valeur soit l'entier suivant. L'algorithme  n'augmente pas la taille en bits de l'entier passé et donc `succ([1, 1, 1, 1])`{.language-} change le tableau en entrée en `[0, 0, 0, 0]`{.language-}.

Cette fonction permet d'écrire le code suivant :

```pseudocode
(n := entier) ← [1, 1, 0, 0, 1]
successeur(n)
affiche n à l'écran
```

Qui affichera `[0, 0, 1, 0, 1]`{.language-}

{% info %}
Les fonctions qui ne rendent rien modifient souvent leurs paramètres.
{% endinfo %}

### <span id="successeur"></span>L'algorithme

```pseudocode
algorithme successeur(N: [bit]) → vide:
    (i := entier) ← 0

    tant que (i ≤ N.longueur - 1) et (N[i] == 1):
        N[i] ← 0
        i ← i + 1

    si i ≤ N.longueur - 1:
        N[i] ← 1
```

{% details "code python" %}

```python/
def successeur(N):
    i = 0

    while (i < len(N)) and (N[i] == 1):
        N[i] = 0
        i += 1

    if i < len(N):
        N[i] = 1
```

{% enddetails %}

{% exercice %}
Démontrez que l'algorithme précédent répond aux spécifications.
{% endexercice %}
{% details "corrigé" %}
Le successeur d'un élément est l'élément plus 1. La somme du dernier bit de `N`{.language-} avec 1 fait alors soit :

- 1 si le dernier bit vaut 0
- 10 si le dernier bit vaut 1

Si la somme vaut 10, cela revient à réitérer le processus sur le prochain bit.

Donc on commence par regarder le bit `N[i]`{.language-} en commençant par le dernier. S'il vaut :

- 1 on le place à 0 et on incrémente i
- 0 on le place à 1 et on stoppe.

{% enddetails %}

{% exercice %}
Que valent ses complexités min et max ?
{% endexercice %}
{% details "corrigé" %}
La complexité de l'algorithme va dépendre du nombre d'éléments dans la liste en entré. Notons $n = N.\mbox{\small longueur}$.

On remarque (facilement) que cette complexité vaut $C(n) = K \cdot \mathcal{O}(1)$ où $K$ est le nombre de fois où l'on rentre dans la boucle `tant que`{.language-}. D'où :

- complexité (max) : parcourt toute la liste (pour une liste uniquement constituée): $\mathcal{O}(n)$
- complexité min : parcourt 1 seul élément de la liste (pour une liste se terminant par un 0): $\mathcal{O}(1)$
{% enddetails %}

### Complexité en moyenne

Analysez selon le nombre en entrée le nombre d'itérations dans la boucle `tant que`{.language-}.

{% exercice %}
Montrez que que le nombre moyen d'itérations de la boucle `tant que`{.language-} sous un modèle que vous expliciterez, vaut :

<div>
$$
W_\text{moy}(N) = \mathcal{O}(1) \cdot \sum_{i=0}^{N-1} i \cdot \frac{1}{2^{i+1}}
$$
</div>

{% endexercice %}
{% details "corrigé" %}
On suppose que chaque nombre décrit par $N$ peut apparaître de façon équiprobable. En posant $n = N.\mbox{\small longueur}$, séparons les $2^n$ nombres possibles en classes selon le nombre d'itérations dans la boucle :

- dernier élément vaut 0 : 0 itération. Vrai pour $2^n/2$ nombres. Probabilité de 1/2.
- derniers éléments valent `[0, 1]`{.language-} : 1 itération. Vrai pour $(2^N/2)/2 = 2^N/4$ nombres. Probabilité de 1/4.
- derniers éléments valent `[0, 1, 1]`{.language-} : 2 itérations. Vrai pour $(2^N/4)/2 = 2^N/8$ nombres. Probabilité de 1/8.
- ...
- derniers éléments valent `[0] + i *[1]`{.language-} : i itérations. Vrai pour $(2^N/4)/2 = 2^N/2^{i+1}$ nombres. Probabilité de 1/2^{i+1}.
- le premier élément vaut 0 et tous les autres valent 1 : $N-1$ itérations Vrai pour 1 nombre. Probabilité de 1/2^{N}.

Le nombre moyen d'itérations dans la boucle vaut alors :

<div>
$$
W_\text{moy}(N) = \mathcal{O}(1) \cdot \sum_{i=0}^{N-1} i \cdot \frac{1}{2^{i+1}}
$$
</div>

{% enddetails %}

{% exercice %}
Conclure que la moyenne de l'algorithme vaut $\mathcal{O}(1)$
{% endexercice %}
{% details "corrigé" %}
On a vu que $\sum_{i=0}^{+\infty} i \cdot \frac{1}{2^{i}} = 2$, donc $\sum_{i=0}^{N-1} i \cdot \frac{1}{2^{i+1}} \leq \frac{1}{2}\sum_{i=0}^{N-1} i \cdot \frac{1}{2^{i}} \leq \frac{1}{2}\sum_{i=0}^{+\infty} i \cdot \frac{1}{2^{i}} \leq 1$. Ceci montre que $W_\text{moy}(N) \leq \mathcal{O}(1)$.

{% enddetails %}


Que le nombre moyen d'itération valent 1 est assez contre intuitif. Vérifiez expérimentalement qu'en moyenne, si l'on appelle successeur $2^N$ fois à partir de $[0] * N$ :

- on a bien cyclé sur tous les éléments
- en moyenne le nombre d'itération dans la boucle vaut bien 1.

{% exercice %}
Codez l'algorithme `successeur`{.language-} en python puis :

1. modifiez le pour qu'il rende le nombre d'itération dans la boucle effectuée pour calculer le successeur.
2. parcourir tous les nombres possible (en partant de $[0] * N$ affichez itérativement les successeurs)
3. une fois tous les nombres vus, afficher le nombre moyens d'itération de la boucle while de l'algorithme `successeur`{.language-}.

{% endexercice %}
{% details "corrigé" %}
```python
def successeur(N):
    K = 0
    i = 0

    while i < len(N) and (N[i] == 1):
        K += 1

        N[i] = 0
        i += 1

    if i < len(N):
        N[i] = 1

    return K


def tous(n):

    N = [0] * n
    total = 0
    for i in range(2**n):
        K = successeur(N)
        total += K
        print(N, K)

    return total / 2 ** n


x = tous(5)
print(x)

```

{% enddetails %}

### Récursif

<span id="algorithme-compteur-binaire-rec"></span>

```pseudocode
fonction tous_rec(N: [bit], i: entier) → vide:

    si i == -1:
        affiche à l'écran N
    sinon:
        pour chaque (x:= entier) de [0 .. 1]:
        N[i] ← x
        tous_rec(N, i - 1)

algorithme tous(n) → vide:
    N ← nouveau tableau de bit de taille n

    tous_rec(N, N.longueur-1)
```

{% details "code python" %}

```python/
def tous_rec(N, i):
    if i == -1:
        print(N)
    else:
        for x in range(2):
            N[i] = x
            tous_rec(N, i -  1)

def tous(n):
    N = n * [0]
    tous_rec(N, n-1)

tous(5)
```

{% enddetails %}

{% exercice %}
Montrez que l'algorithme ci-dessus est une façon récursive d'afficher tous les nombres binaires à $n$ bits.
{% endexercice %}
{% details "corrigé" %}
Chaque récursion modifie le tableau à une position inférieure, cet élément valant d'abord 0, puis 1 lorsque l'on reviendra à cette fonction après la récursion.

{% enddetails %}
{% exercice %}
Quelle est sa complexité en instruction et en mémoire de cet algorithme ?
{% endexercice %}
{% details "corrigé" %}
La complexité en mémoire est de $n$, car chaque aucune récursion ne crée de nouveau tableau ! C'est le même tableau qui est modifié à chaque récursion.

{% enddetails %}

### Généralisation

{% exercice %}
Modifiez `tous(n: [bit])  → vide`{.language-} pour afficher l'ensemble des jets de $n$ dés à 6 faces ?
{% endexercice %}
{% details "corrigé" %}
Clairement, l'algorithme suivant fonctionne :

```pseudocode
fonction tous_rec(N: [caractère], i: entier) → vide:

    si i == -1:
        affiche à l'écran N
    sinon:
        pour chaque x de ["⚀", "⚁", "⚂", "⚃", "⚄", "⚅"]:
        N[i] ← x
        tous_rec(N, i-1)

algorithme tous(n) → vide:
    N ← nouveau tableau de caractères de taille n

    tous_rec(N, n-1)
```

Ou en python :

```python/
def tous_rec(N, i):
    if i == -1:
        print(N)
    else:
        for x in ["⚀", "⚁", "⚂", "⚃", "⚄", "⚅"]:
            N[i] = x
            tous_rec(N, i -  1)

def tous(n):
    N = n * [0]
    tous_rec(N, n-1)

tous(5)
```

{% enddetails %}


## Tris spéciaux

> - **Utilité** : tris pouvant être utile dans des cas particuliers et surtout à la base de nombreux pièges
> - **Difficulté** : moyen

Des tris utiles dans des cas spécifiques, et dont la complexité semble plus petite que $n\log(n)$. Connaître pourquoi ce n'est (bien sur) pas le cas.

Les tris spéciaux ont des complexités inférieures à $\mathcal{O}(n\log(n))$, ce qui n'est bien sur possible que si l'on se place dans des cas particuliers d'entrées.

### <span id="tri-paquets"></span>Tri par paquets (bucket sort)

{% lien %}
[Tri par paquets](https://fr.wikipedia.org/wiki/Tri_par_paquets)
{% endlien %}


On veut trier les $n$ objets d'un tableau $\mathcal{E}$ par rapport à leur valeur via **une injection** $f: \mathcal{E} \to [0, m[$ allant de $\mathcal{E}$ dans l'ensemble des entiers de 0 à $m-1$.

**_Le tri par paquets_** consiste à créer un tableau de taille $m$ et de ranger chaque élément $o$ de $\mathcal{E}$ dans ce tableau à l'indice $f(o)$. Il suffit ensuite de rendre la restriction de ce tableau aux éléments contenant les éléments de $\mathcal{E}$.

{% exercice %}
Écrire le pseudocode de cet algorithme. On supposera que l'on cherche à trier $n$ entiers.
{% endexercice %}
{% details "corrigé" %}
On peut utiliser l'algorithme suivant, qui modifie le tableau passé en paramètre :

<span id="algorithme-tri-paquet"></span>

```pseudocode
algorithme tri_paquet(E: [entier], f:(entier) → entier) → ∅:
    (m := entier) ← max(f(x) | x de E)
    (T = [entier]) ← [entier]{longueur: m + 1}
    T[:] ← ∅  # ou m + 1 si on a pas accès à ∅ pour un tableau d'entiers

    pour chaque (x:= entier) de E:
        T[f(x)] ← x
    
    (i := entier) ← 0
    pour chaque (x:= entier) de T:
        si x ≠ ∅:
            E[i] ← x
            i ← i + 1
```

Cet algorithme marche car $f$ est une injection, tout éléments de $E$ sera dans T à un indice différent des autres.

{% enddetails %}

{% exercice %}
Quelle est la complexité en temps et en mémoire de cet algorithme ?
{% endexercice %}
{% details "corrigé" %}
La complexité est en $\mathcal{O}(m)$ en temps **et** en mémoire.

{% enddetails %}

{% exercice %}
Utilisez cet algorithme pour trier :

1. $n$ entiers deux à deux différents.
2. comment modifier cet algorithme si les entiers peuvent être égaux ?
3. complexité de cet algorithme ?
{% endexercice %}
{% details "corrigé" %}

Si l'on veut trier $n$ entiers deux à deux différents, on utilise la fonction identité et la complexité est en $\mathcal{O}(\max(E))$.

Cet algorithme est utile si on doit trier des objets via une fonction $f: \mathcal{E} \to [0, m[$ où $m$ borné pas trop grand. C'est souvent le cas lorsque l'on utilise des données complexes, pensez à un tableau excel où nos données sont les lignes et l'index le numéro de la ligne (ou une colonne spécifique dont la valeur va de 1 au nombre de lignes).

Si l'on veut trier des entiers pouvant être égaux, on peut utiliser l'algorithme suivant qui compte dans $T[i]$ le nombre de fois où $i$ est présent dans $E$.

```pseudocode
algorithme tri_paquet(E: [entier]) → ∅:
    m ← max(x | x de E)
    T ← un nouveau tableau d'entier de taille m + 1
    T[:] ← 0  # ou m + 1 si on a pas accès à ∅ pour un tableau d'entiers

    pour chaque x de E:
        T[x] ← T[x] + 1
    
    i ← 0
    pour x allant de 0 à m:
        tant que T[x] > 0:
            E[i] = x
            i ← i + 1
            T[x] ← T[x] - 1

```

{% enddetails %}

{% exercice %}
Quand utiliseriez vous cet algorithme pour trier $n$ objets ?
{% endexercice %}
{% details "corrigé" %}

Il n'y **aucune** relation entre $n$ et $\max(E)$. On peut par exemple tenter de trier le tableau $[1, 2^{10000000}]$, la complexité de notre algorithme sera de $2^{10000000}$ et non pas de 2.

Ce n'est donc **pas** un algorithme linéaire... Mais il est très efficace si les nombres ne sont pas trop grand devant $n$. Ce qui est souvent le cas en pratique.

{% enddetails %}

Rappelez-vous du tri par paquet, on s'en sert parfois dans des problèmes algorithmiques.

### <span id="tri-base"></span>Tri par base

{% lien %}
[Tri par base](https://fr.wikipedia.org/wiki/Tri_par_base)
{% endlien %}


Ce tri s'applique uniquement aux entiers positifs. Notre entrée est une liste $T$ de $n$ de listes de longueur $m$ composées de 0 et de 1 représentant des entiers écrit en base 2 (comme pour le [compteur binaire](../compteur-binaire)). Par exemple : $T = [[1, 0, 0, 1], [0, 1, 1, 1], [1, 0, 0, 0]]$ qui correspond aux nombres $[9, 14, 1]$.

Le principe de ce tri est très simple :

- On considère d'abord le bit de poids le plus faible (_ie._ le plus à gauche). On crée alors deux tableaux L0 et L1 initialement vides et on va itérativement considérer chaque élément de la liste à trier :
  - les entiers dont le bit de poids le plus faible est 0 sont ajoutés à la fin de L0
  - les entiers dont le bit de poids le plus faible est 1 sont ajoutés à la fin de L1
- On concatène les deux sous-listes T = L0 + L1
- On recommence sur le bit à droite de celui qu'on vient de traiter.
- ...

Les parcours des éléments de T se font, toujours, de la gauche vers la droite.

Pour notre exemple :

1. après premiere boucle : $[[0, 1, 1, 1], [1, 0, 0, 1], [1, 0, 0, 0]]$
2. après deuxième boucle : $[[1, 0, 0, 1], [1, 0, 0, 0], [0, 1, 1, 1]]$
3. après troisième boucle :$[[1, 0, 0, 1], [1, 0, 0, 0], [0, 1, 1, 1]]$
4. après quatrième boucle : $[[1, 0, 0, 0], [1, 0, 0, 1], [0, 1, 1, 1]]$

Questions :

{% exercice %}
Donnez le pseudo-code, la preuve et la complexité de cet algorithme.
{% endexercice %}
{% details "corrigé" %}

L'algorithme suivant mime exactement le procédé décrit dans le sujet. Nos données étant des tableaux de bits, l'entrée de l'algorithme est un tableau de tableaux de bit. Cela s'écrit : `[[bit]]`{.language-} :

<span id="algorithme-tri-base"></span>

```pseudocode
algorithme tri_base(T: [[bit]]) → ∅
    (L0 := [[bit]]) ← [[bit]]{longueur: T.longueur}
    (i0 := entier) ← 0

    (L1 := [[bit]]) ← [[bit]]{longueur: T.longueur}
    (i1 := entier) ← 0

    pour (i:= entier) de [0 .. T.longueur[:
        pour chaque x de T:
            si x[i] == 0:
                L0[i0] ← x
                i0 ← i0 + 1
            sinon:
                L1[i1] ← x
                i1 ← i1 + 1
        pour j allant 0 à i0-1:
            T[j] ← L0[j]
        pour j allant 0 à i1-1:
            T[j + i0] ← L1[j]
```

On prouve cet algorithme par invariant de boucle.

> **Invariant de boucle** : À la fin de la ième itération, $T$ est trié si on considère uniquement les i derniers bits de chaque élément.

1. initialisation : à la fin de la première boucle il est clair que les élément finissant par 0 sont placés avant les éléments se finissant par 1.
2. récursion : si l'invariant de boucle est vrai à la fin de la i-1 ème itération, les éléments de L0et de L1 seront trié si on considère uniquement les i derniers bits de chaque élément. Comme le $-i$ bit des éléments de L0 vaut 0 et le $-i$ bit des éléments de L1 valent 1 tous les éléments de L0 sont inférieur aux éléments de L1 et en les concaténant on a bien que les $i$ derniers bit des éléments de T sont triées.
3. à la fin des `T.longueur`{.language-} itérations, l'invariant de boucle montre que les éléments de $T$ sont bien triés.

En notant $m$ la taille des tableaux en entrée et $n$ le nombre de données à trier, on a clairement une complexité de $\mathcal{O}(nm)$.

Si la taille des entiers est fixée, ce qui est le cas au niveau du processeur où tous les entiers sont codés sur 64bits, ce tri est le plus efficace possible : il est linéaire.

{% enddetails %}

Comme pour le tri par paquet, il n'y **aucune** relation entre $n$ et $m$. On peut par exemple tenter de trier les tableaux de taille $m=2^n$, la complexité de notre algorithme sera exponentielle.

Ce n'est donc **pas** un algorithme linéaire en $n$


## Chaînes de caractères

> - **Utilité** : classique mais pas indispensable
> - **Difficulté** : facile avec les indications données

Le but de cet série d'exercices est d'étudier les modifications d'une chaîne de caractères. 

### Sous-séquence

Soient deux chaînes de caractères $S_1$ et $S_2$ de longueurs $n_1$ et $n_2$ respectivement.

{% note "**Définition**" %}
La chaîne $S_2$ est **_une sous-séquence_** de $S_1$ si il existe une fonction strictement croissante $f: [0, n_2[ \to [0, n_1[$ telle que $S_1[f(j)] = S_2[j]$ pour tout $j$ de $[0, n_2[$.
{% endnote %}
{% exercice %}
Proposez, prouvez et donnez la complexité d'un algorithme qui détermine si $S_2$ est une sous-séquence de $S_1$.
{% endexercice %}
{% details "corrigé" %}
```pseudocode
algorithme sous_sequence(S1: chaîne, S2: chaîne) → booléen:
    (i1 := entier) ← 0
    (i2 := entier) ← 0
    tant que i1 < S1.longueur et i2 < S2.longueur:
        si S2[i2] == S1[i1]:
            i2 ← i2 + 1
        i1 ← i1 + 1

    rendre i2 == S2.longueur
```

Comme `i1`{,language-} augmente à chaque itération, la boucle va forcément s'arrêter ce qui finira l'algorithme.

Enfin l'algorithme fonctionne car `i2`{,language-} est incrémenté à la première occurrence possible.

Sa complexité est en $\mathcal{O}(\max(n_1, n_2))$. Cet algorithme est linéaire il est optimal.

{% enddetails %}

### Sous-mot

Soient deux chaînes de caractères $S_1$ et $S_2$ de longueurs $n_1$ et $n_2$ respectivement.

{% note "**Définition**" %}
La chaîne $S_2$ est un **_sous-mot_** de $S_1$ s'il existe un indice $i$ tel que $S_2[j] = S_1[i + j]$ pour tout $j$ de $[0, n_2[$.

{% endnote %}

Être un sous-mot est plus restrictif qu'être une sous-séquence.

{% exercice %}

- Proposez, prouver et donner la complexité d'un algorithme simple qui détermine si $S_2$ est un sous-mot de $S_1$.
- Si toutes les lettres de $S_2$ sont deux à deux différentes, donnez un algorithme en $\mathcal{O}(n_1)$ pour résoudre ce problème.

{% endexercice %}
{% details "corrigé" %}
L'algorithme suivant regrade toutes les possibilités pour $S_2$ d'être un sous-mot de $S_1$. Il s'arrête à la première possibilité. Dans le pire des cas, il va effectuer $\mathcal{O}(n_1 \cdot n_2)$ opérations.

```pseudocode
algorithme sous_mot(S1: chaîne, S2: chaîne) → booléen:
    
    pour chaque i1 de [0 .. S1.longueur[:
        (i2 := entier) ← 0
        (stop := booléen) ← Faux
        tant que (stop == Faux) et (i2 < S2.longueur):
            si S2[i2] == S1[i1 + i2]:
                i2 ← i2 + 1
            sinon:
                stop ← Vrai
        
        si i2 == S2.longueur:
            rendre Vrai

    rendre Faux
```

Si tous les caractères de $S_2$ sont différents, il n'est pas nécessaire de tout recommencer. On peut utiliser l'optimisation suivante, qui donne la complexité voulue :

```pseudocode
algorithme sous_mot(S1: chaîne, S2: chaîne) → booléen:
    (i1, i2 := entier) ← 0, 0
    stop := booléen

    tant que i1 < S1.longueur:
        i2 ← 0        
        stop ← Faux
        tant que (stop == Faux) et (i2 < S2.longueur):
            si S2[i2] == S1[i1 + i2]:
                i2 ← i2 + 1
            sinon:
                stop ← Vrai
        
        si i2 == S2.longueur:
            rendre Vrai
        i1 ← i1 + i2

    rendre Faux
```

{% enddetails %}

### <span id="permutation-circulaire"></span> Permutation circulaire

Étant donné un tableau de caractères $S$ de longueur $n$ et un entier $k$, le problème est de transformer $S$ par **_permutation circulaire_** en décalant (circulairement) tous les éléments de $S$ de $k$ places. Par exemple, avec $S = \text{LongtempsJeMeSuisCouchéDeBonneHeure}$ et $k = 4$, on obtient $S' = \text{eureLongtempsJeMeSuisCouchéDeBonneH}$.

{% exercice %}

Donnez un algorithme optimal simple, `permutation(S: [caractère], k: entier) →[caractère]`{.language-} qui rend à partir de $S$ et de $k$, un nouveau tableau permutation circulaire de $S$ de $k$ caractères.
{% endexercice %}
{% details "corrigé" %}

La solution est optimale puisqu'elle est en $\mathcal{O}(n)$

```pseudocode
algorithme permutation(S: [caractère], k: entier) → [caractère]:
    S2 ← un tableau de n caractères

    pour chaque i de [0 .. k [:
        S2[i] ← S[S.longueur-k + i]
    pour chaque i de [k .. S.longueur[:
        S2[i] ← S[i-k]
    
    rendre S2
```

L'algorithme ci-dessus rend un tableau, il est donc facile de faire le décalage.

{% enddetails %}

On veut maintenant faire une permutation circulaire sur site, _ie._ sans utiliser plus que $\mathcal{O}(1)$ place mémoire supplémentaire (il arrive (par exemple quand on étudie le génome) que $n$ soit très grand). Il faut pour cela
remarquer que permuter circulairement $L$ revient à prendre les $k$ dernières lettres de $L$ et à les mettre en tête. On note $L^R$ la liste $L$ **_renversée_** (par exemple, si $L =\text{Couché}$, $L^R = \text{éhcuoC}$).

{% exercice %}

Donnez un algorithme `retournement(S: [caractère]) → ∅`{.language-} en $\mathcal{O}(n)$ et utilisant $\mathcal{O}(1)$ place mémoire supplémentaire, qui transforme $L$ en $L^R$.

{% endexercice %}
{% details "corrigé" %}
Si on droit qu'à un nombre constant de variables ceci n'est plus possible. Il faut ruser en utilisant des retournements

```pseudocode
algorithme retournement(S: [caractère]) → ∅:
    pour chaque i de [0 .. S.longueur // 2[:
    S[i], S[S.longueur - 1 - i] ← S[S.longueur - 1 - i], S[i]

```

{% enddetails %}

{% exercice %}
Montrez que, si on note $L = AB$, où $B$ est de longueur $k$ (par exemple, avec $L = \text{LongtempsJeMeSuisCouchéDeBonneHeure}$ et $k = 4$, $A =\text{LongtempsJeMeSuisCouchéDeBonneH}$ et $B =\text{eure}$), alors \text{Permut}(L, k) = (A^RB^R)^R$.
{% endexercice %}
{% details "corrigé" %}

Comme $(A^R)^R =  A$ et $(AB)^R = B^RA^R$, on a :

<div>
$$
(A^RB^R)^R = ((B^R)^R)((A^R)^R) = BA
$$
</div>

{% enddetails %}

{% exercice %}
Déduisez-en un algorithme de complexité $\mathcal{O}(n)$ qui permute une liste (de longueur $n$), _ie._ qui transforme $L$ en $\text{Permut}(L,k)$, en utilisant $\mathcal{O}(1)$ espace mémoire supplémentaire.

{% endexercice %}
{% details "corrigé" %}

L'algorithme de permutation est alors tout simple :

<span id="algorithme-permutation"></span>

```pseudocode
algorithme permutation(S: [caractère], k: entier) → ∅:
    retournement(S[:-k])
    retournement(S[k:])
    retournement(S)

```

Et sa complexité est bien $\mathcal{O}(n-k) + \mathcal{O}(k) + \mathcal{O}(n) = \mathcal{O}(n)$.

{% enddetails %}


## pgcd

> - **Utilité** : des résultats sympathiques mais pas indispensable
> - **Difficulté** : moyen à dur


On a déjà vu une version de l'algorithme du pgcd. Rappelons -là :

```pseudocode
algorithme pgcd(a: entier, b: entier) → entier:  # a, b ≥ 0
    a', b' := entier

    tant que min(a, b) > 0:
        a' ← max(a, b) - min(a, b)
        b' ← min(a, b)
        a, b ← a', b'
    
    rendre max(a, b)
```

La version couramment utilisée est celle utilisant un modulo (opérateur `%`{.language-} ou `mod`{.language-} en algorithmie) qui converge plus vite.

Cet algorithme est basé sur le fait que si la division euclidienne de $a$ par $b$ vaut $a = qb + r$ (avec $q$ et $r$ entiers et $r < b$) on a `pgcd(a, b) = pgcd(b, r)`{.language-}.

{% exercice %}
Donnez un algorithme récursif calculant le pgcd en utilisant le modulo.
{% endexercice %}
{% details "corrigé" %}

<span id="algorithme-pgcd-modulo"></span>

```pseudocode
algorithme pgcd_mod(a: entier, b: entier) → entier:  # a, b ≥ 0
    si b == 0:
        rendre a
    si a < b:
        a, b ← b, a
    
    rendre pgcd_mod(b, a mod b)
```

{% enddetails %}


Knuth analyse en détails cet algorithme dans le tome 2 (partie 3.5.2) de [the art of computer programming](https://fr.wikipedia.org/wiki/The_Art_of_Computer_Programming). Comme à chaque fois avec Knuth : les résultats sont précis, intéressants et très bien écrits. Je ne peux que vous conseiller d'allez y jeter un coup d'œil nous ne ferons en effet ici qu'effleurer le sujet.

### Complexité

Avant de prouver sa complexité, commencez par :

{% exercice %}
Démontrez que si $a\geq b$ alors $a \bmod b < \frac{a}{2}$.
{% endexercice %}
{% details "corrigé" %}
Comme $a \bmod b < b$, si $b \leq \frac{a}{2}$ la propriété est démontrée et si $b > \frac{a}{2}$ on a $a // b = 1$ et donc $a \bmod b = a - b < \frac{a}{2}$

{% enddetails %}

Rappelez vous de cette propriété, elle peut se révéler extrêmement utile pour le calcul de complexité :

{% exercice %}
Déduire que le nombre de récursions de l'algorithme récursif utilisant le pgcd est inférieur à $\log_2(\max(a, b))$.
{% endexercice %}
{% details "corrigé" %}

Le nombre de récursions ne peut excéder le nombre de fois où l'on peut diviser $a$ ou $b$ par 2 : il est inférieur à $\log_2(a)$.
{% enddetails %}

{% exercice %}
Si l'opération calculant le modulo est élémentaire, en déduire que la complexité de l'algorithme récursif utilisant le pgcd est en $\mathcal{O}(\ln(\max(a, b)))$.
{% endexercice %}
{% details "corrigé" %}

Si le calcul du modulo s'effectue en $\mathcal{O}(1)$ opérations, la complexité totale de l'algorithme est en $\mathcal{O}(\ln(\max(a, b)))$, ce qui est très bon !

{% enddetails %}


### Pgcd et Fibonacci

On va maintenant montrer que cette complexité est atteinte. Pour cela, exhibons d'étranges propriétés des éléments de [la suite de Fibonacci](../fibonacci/){.interne}.

{% exercice %}
Si $F(n)$ est le $n$ème nombre de la suite de Fibonacci, montrez que $F(n) \bmod F(n-1) = F(n-2)$.
{% endexercice %}
{% details "corrigé" %}

Par définition, on a $F(n+1) = F(n) + F(n-1)$ et comme $F(n) > F(n-1)$, cette équation est aussi la division euclidienne de $F(n)$ par $F(n-1)$ puisqu'elle est unique.

{% enddetails %}

En déduire que :

{% exercice %}
Il y a exactement $n$ récursions de l'algorithme récursif utilisant le pgcd pour calculer le pgcd de  $F(n+1)$ et $F(n)$.
{% endexercice %}
{% details "corrigé" %}

La propriété précédente nous montre que `pgcd_mod(F(n+1), F(n))`{.language-} va appeler `pgcd_mod(F(n), F(n+1) % F(n)) = pgcd_mod(F(n), F(n-1))`{.language-}. Il va donc y avoir $n$ récursion jusqu'à arriver à l'appel de `pgcd_mod(F(1), 0)`{.language-} qui va conclure la récursion.

{% enddetails %}

On a même mieux :

{% exercice %}
Si pour $a> b$ il y a au moins $n$ récursions de l'algorithme récursif, alors $a\geq F(n+1)$ et $b\geq F(n)$.
{% endexercice %}
{% details "corrigé" %}

Montrer que ces nombres sont minimaux se fait simplement par récurrence sur le nombre  de récursions.

- **initialisation**. Pour qu'il y ait qu moins 1 récursion, il faut que $a \geq b \geq 1 = F(2) = F(1) > 0$.
- **récursion**. On suppose que pour faire au moins $k$ itérations il faut que  $a \geq F(k+1)$ et  $b \geq F(k)$. Soit $a \geq b$ deux entiers tels que `pgcd_mod(a, b)`{.language-} effectue $k+1$ itérations. Ceci implique que `pgcd_mod(b, a % b)`{.language-} effectue $k$ itérations, par hypothèse de récursion on a alors que $b \geq F(k+1)$ et $a {\small \\%} b \geq F(k)$ et donc $a \geq F(k+1) + F(k) = F(k+2)$.

Cette propriété permet que l'on peut borner le nombre de récursions par $b$ ! Pour qu'il y ait au moins $n$ récursion, il faut que $a \geq b \geq F(n)$. 

{% enddetails %}

{% exercice %}
Si l'opération calculant le modulo est élémentaire, en conclure que la complexité de l'algorithme récursif utilisant le pgcd est en $\mathcal{O}(\ln(\min(a, b)))$.

{% endexercice %}
{% details "corrigé" %}

Comme $F(n) = \mathcal{O}(2^n)$ on en déduit que le nombre de récursions et donc la complexité de `pgcd_mod(a, b)`{.language-} est en $\mathcal{O}(\ln(\min(a, b)))$. Ce qui est à comparer à l'algorithme avec des soustractions dont la complexité était $\mathcal{O}(\min(a, b))$.

{% enddetails %}

Si cela vous intéresse, vous pouvez jeter un petit coup d'œil au lien suivant qui liste quelques propriétés liées au pgcd des nombres de la suite de Fibonacci :

{% lien %}
<https://proofwiki.org/wiki/GCD_of_Fibonacci_Numbers>
{% endlien %}

### pgcd binaire

{% lien %}
<https://fr.wikipedia.org/wiki/Algorithme_binaire_de_calcul_du_PGCD>
{% endlien %}

Cet algorithme, répertorié dès le 1er siècle (Knuth cite le [九章算术](https://fr.wikipedia.org/wiki/Les_Neuf_Chapitres_sur_l%27art_math%C3%A9matique) chapitre 1 section 6) puis publié dans sa forme actuelle en 1967 par Stein.

<span id="algorithme-pgcd-binaire"></span>

```pseudocode
algorithme pgcd_binaire(a: entier, b: entier) → entier:  # a, b ≥ 0

    si b == 0:
        rendre a
    si a et b sont pairs:
        rendre 2 * pgcd_binaire(a // 2, b // 2)
    si a est impair et b pair:
        rendre pgcd_binaire(a, b // 2)
    si a est pair et b impair:
        rendre pgcd_binaire(a // 2, b)
    si a et b sont impairs:
        si a < b:
            a, b ← b, a
        rendre pgcd_binaire(a - b, b)
```

{% exercice %}
Montrez que l'algorithme `pgcd_binaire(a, b)`{.language-} calcule bien le pgcd des deux entiers positifs a et b.
{% endexercice %}
{% details "corrigé" %}

Les propriétés utilisées conservent clairement le pgcd et, comme pour l'algorithme du pgcd initial, à chaque récursion le max de $a$ et $b$ sera strictement plus petit : on arrivera forcément à la condition d'arrêt ce qui en fait bien un algorithme.

{% enddetails %}

{% exercice %}
Quelle est la complexité de cet algorithme ?
{% endexercice %}
{% details "corrigé" %}

Le calcul de sa complexité se fait comme pour [l'exponentiation indienne](../projet-exponentiation/étude-algorithmique/#complexité-rapide){.interne} et permet de prouver qu'elle est en $\mathcal{O}(\max(a, b))$. L'intérêt de cette version est qu'elle se fait tres simplement en machine où les entiers sont codés par des tableaux de bits et où la multiplication et la division d'un nombre par 2 revient à décaler sa représentation binaire d'un bit vers la droite ou la gauche respectivement.

Il n'y a pas à calculer le modulo, opération plus complexe.

{% enddetails %}







<!-- ds 1 L1 25-26

## {2, 3}-SUM

> - **Utilité** : un classique des concours, sans aucune indications bien sur !
> - **Difficulté** : dur

{% aller %}
[{2, 3}-SUM](./2_3-SUM){.interne}
{% endaller %} -->
