---
layout: layout/post.njk

title: Corrigé

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

## Algorithme

Le successeur d'un élément est l'élément plus 1. La somme du dernier bit de `N`{.language-} avec 1 fait alors soit :

- 1 si le dernier bit vaut 0
- 10 si le dernier bit vaut 1

Si la somme vaut 10, cela revient à réitérer le processus sur l'avant dernier bit.

Donc on commence par regarder le bit `N[i]`{.language-} en commençant par le dernier. S'il vaut :

- 1 on le place à 0 et on décrémente i
- 0 on le place à 1 et on stoppe.

La complexité de l'algorithme va dépendre du nombre d'éléments dans la liste en entré. Notons $n = N.\mbox{\small longueur}$.

On remarque (facilement) que cette complexité vaut $C(n) = K \cdot \mathcal{O}(1)$ où $K$ est le nombre de fois où l'on rentre dans la boucle `tant que`{.language-}. D'où :

- complexité (max) : parcourt toute la liste (pour une liste uniquement constituée): $\mathcal{O}(n)$
- complexité min : parcourt 1 seul élément de la liste (pour une liste se terminant par un 0): $\mathcal{O}(1)$

## Complexité en moyenne

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

On a vu que $\sum_{i=0}^{+\infty} i \cdot \frac{1}{2^{i}} = 2$, donc $\sum_{i=0}^{N-1} i \cdot \frac{1}{2^{i+1}} \leq \frac{1}{2}\sum_{i=0}^{N-1} i \cdot \frac{1}{2^{i}} \leq \frac{1}{2}\sum_{i=0}^{+\infty} i \cdot \frac{1}{2^{i}} \leq 1$. Ceci montre que $W_\text{moy}(N) \leq \mathcal{O}(1)$.

## Vérification expérimentale

```python
def successeur(N):
    K = 0

    while i >= 0 and (N[i] == 1):
        K += 1

        N[i] = 0
        i -= 1

    if i >= 0:
        N[i] = 1

    return K


def tous(n):

    N = [0] * n
    total = 0
    for i in range(2**n):
        total += successeur(N)
        print(n)

    return total / 2 ** n


x = tous(5)
print(x)

```

## Récursif

### Preuve

Chaque récursion modifie le tableau à une position inférieure, cet élément valant d'abord 0, puis 1 lorsque l'on reviendra à cette fonction après la récursion.

### Complexité en mémoire

La complexité en mémoire est de $n$, car chaque aucune récursion ne crée de nouveau tableau ! C'est le même tableau qui est modifié à chaque récursion.

## Généralisation

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
