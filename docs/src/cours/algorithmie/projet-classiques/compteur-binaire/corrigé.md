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

Le successeur d'un élément est l'élément plus 1. La somme du dernier bit de n avec 1 fait alors soit :

- 1 si le dernier bit vaut 0
- 10 si le dernier bit vaut 1

Si la somme vaut 10, cela revient à réitérer le processus sur l'avant dernier bit.

Donc on commence par regarder le bit n[i] en commençant par le dernier. S'il vaut :

- 1 on le place à 0 et on décrémente i
- 0 on le place à 1 et on stoppe.

## Complexité

La complexité va dépendre du nombre d'éléments dans la liste en entré. Notons $N = len(n)$.

On remarque (facilement) que cette complexité vaut $C(N) = K \cdot \mathcal{O}(1)$ où $K$ est le nombre de fois où l'on rentre dans la boucle.

- complexité max : parcourt toute la liste (pour une liste uniquement constituée): $\mathcal{O}(N)$
- complexité min : parcourt 1 seul élément de la liste (pour une liste se terminant par un 0): $\mathcal{O}(1)$

## Complexité en moyenne

Séparons les $2^N$ nombres possibles en classes selon le nombre d'itérations dans la boucle :

- dernier élément vaut 0 : 0 itération. Vrai pour $2^N/2$ nombres. Probabilité de 1/2.
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

## Vérification expérimentale

```python
def successeur(n):
    K = 0

    while i >= 0 and (n[i] == 1):
        K += 1

        n[i] = 0
        i -= 1

    if i >= 0:
        n[i] = 1

    return K


def tous(N):

    n = [0] * N
    total = 0
    for i in range(2**N):
        total += successeur(n)
        print(n)

    return total / 2 ** N


x = tous(5)
print(x)

```
