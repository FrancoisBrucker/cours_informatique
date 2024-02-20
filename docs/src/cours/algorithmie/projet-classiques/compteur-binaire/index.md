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

Un entier écrit sous forme binaire peut s'écrire comme une liste $x$ composées de 0 et de 1. Par exemple l'entier 19 s'écrira $[1, 0, 0, 1, 1]$

On vous demande d'écrire la fonction `succ(n)`{.language-} qui prend en paramètre un entier écrit sous sa forme binaire et qui **le modifie** pour que sa valeur soit l'entier suivant. On supposera que l'on n'augmente pas sa taille et donc que `succ([1, 1, 1, 1])`{.language-} change la liste ne entrée en `[0, 0, 0, 0]`{.language-}.

Cette fonction permet d'écrire le code suivant :

```python
n = [1, 0, 0, 1, 1]
succ(n)
print(n)
```

Qui affichera `[1, 0, 1, 0, 0]`{.language-}

{% info %}
Les fonctions qui ne rendent rien modifient souvent leurs paramètres.
{% endinfo %}

### L'algorithme

```python#
def successeur(n):
    i = len(n) - 1

    while (i >= 0) and (n[i] == 1):
        n[i] = 0
        i -= 1

    if i >= 0:
        n[i] = 1
```

Démontrez que l'algorithme précédent répond à la question.

### Complexités min et max

Que valent les complexités min et max de cet algorithme ?

### Complexité en moyenne

Analysez selon le nombre en entrée le nombre d'itérations dans la boucle while. En déduire que le nombre moyen d'itérations de la boucle while vaut :

<div>
$$
W_\text{moy}(N) = \mathcal{O}(1) \cdot \sum_{i=0}^{N-1} i \cdot \frac{1}{2^{i+1}}
$$
</div>

Conclure en utilisant le fait que $\sum_{i=1}^N i \cdot \frac{1}{2^{i+1}}$ tent vers 1 lorsque $N$ tend vers l'infini que l'algorithme va en moyenne ne faire qu'une seule itération et donc que la complexité en moyenne de l'algorithme vaut $\mathcal{O}(1)$.

### Vérification

Que le nombre moyen d'itération vale 1 est assez contre intuitif. Vérifiez expérimentalement qu'en moyenne, si l'on appelle successeur $2^N$ fois à partir de $[0] * N$ :

- on a bien cyclé sur tous les éléments
- en moyenne le nombre d'itération dans la boucle vaut bien 1.
