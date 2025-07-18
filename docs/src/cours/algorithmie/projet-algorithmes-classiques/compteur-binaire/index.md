---
layout: layout/post.njk

title: Compteur binaire

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

{% lien %}
[Corrigé](./corrigé){.interne}
{% endlien %}

Un entier écrit sous forme binaire peut s'écrire comme un tableau $x$ composées de bits (entier valant 0 ou 1). Par exemple l'entier 19 s'écrira $[1, 0, 0, 1, 1]$

L'algorithme `algorithme successeur(N: [bit]) → vide:`{.language-} suivant prend en paramètre un entier écrit sous sa forme binaire et qui **le modifie** pour que sa valeur soit l'entier suivant. L'algorithme  n'augmente pas la taille en bits de l'entier passé et donc `succ([1, 1, 1, 1])`{.language-} change le tableau en entrée en `[0, 0, 0, 0]`{.language-}.

Cette fonction permet d'écrire le code suivant :

```pseudocode
n ← [1, 0, 0, 1, 1]
successeur(n)
affiche n à l'écran
```

Qui affichera `[1, 0, 1, 0, 0]`{.language-}

{% info %}
Les fonctions qui ne rendent rien modifient souvent leurs paramètres.
{% endinfo %}

## <span id="successeur"></span>L'algorithme

```pseudocode
algorithme successeur(N: [bit]) → vide:
    i ← N.longueur - 1

    tant que (i ≥ 0) et (N[i] == 1):
        N[i] ← 0
        i ← i - 1

    si i ≥ 0:
        N[i] ← 1
```

{% details "code python" %}

```python/
def successeur(N):
    i = len(N) - 1

    while (i >= 0) and (N[i] == 1):
        N[i] = 0
        i -= 1

    if i >= 0:
        N[i] = 1
```

{% enddetails %}

{% faire %}
Démontrez que l'algorithme précédent répond aux spécifications.
{% endfaire %}
{% faire %}
Que valent ses complexités min et max ?
{% endfaire %}

## Complexité en moyenne

Analysez selon le nombre en entrée le nombre d'itérations dans la boucle `tant que`{.language-}.

{% faire %}
Montrez que que le nombre moyen d'itérations de la boucle `tant que`{.language-} sous un modèle que vous expliciterez, vaut :

<div>
$$
W_\text{moy}(N) = \mathcal{O}(1) \cdot \sum_{i=0}^{N-1} i \cdot \frac{1}{2^{i+1}}
$$
</div>

{% endfaire %}
{% faire %}
Conclure que la moyenne de l'algorithme vaut $\mathcal{O}(1)$
{% endfaire %}

### Vérification

Que le nombre moyen d'itération valent 1 est assez contre intuitif. Vérifiez expérimentalement qu'en moyenne, si l'on appelle successeur $2^N$ fois à partir de $[0] * N$ :

- on a bien cyclé sur tous les éléments
- en moyenne le nombre d'itération dans la boucle vaut bien 1.

{% faire %}
Codez l'algorithme `successeur`{.language-} en python puis :

1. modifiez le pour qu'il rende le nombre d'itération dans la boucle effectuée pour calculer le successeur.
2. parcourir tous les nombres possible (en partant de $[0] * N$ affichez itérativement les successeurs)
3. une fois tous les nombres vus, afficher le nombre moyens d'itération de la boucle while de l'algorithme `successeur`{.language-}.

{% endfaire %}

### Récursif

<span id="algorithme-compteur-binaire-rec"></span>

```pseudocode
fonction tous_rec(N: [bit], i: entier) → vide:

    si i == -1:
        affiche à l'écran N
    sinon:
        pour chaque x de [0 .. 1]:
        N[i] ← x
        tous_rec(N, i-1)

algorithme tous(n) → vide:
    N ← nouveau tableau de bit de taille n

    tous_rec(N, n-1)
```

{% details "code python" %}

```python/
def tous_rec(N, i):
    if i == 0:
        print(n)
    else:
        for x in range(2):
            N[i] = x
            compteur(N, i -  1)

def tous(n):
    N = n * [0]
    tous_rec(N, n-1)
```

{% enddetails %}

{% faire %}
Montrez que l'algorithme ci-dessus est une façon récursive d'afficher tous les nombres binaires à $n$ bits.
{% endfaire %}

{% faire %}
Quelle est sa complexité en instruction et en mémoire de cet algorithme ?
{% endfaire %}

### Généralisation

{% faire %}
Modifiez `tous(n: [bit])  → vide`  pour afficher l'ensemble des jets de $n$ dés à 6 faces ?
{% endfaire %}
