---
layout: layout/post.njk

title: Corrigé

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

## 2-SUM

### Algorithme en $\mathcal{O}(T.\mbox{\small longueur}^2)$

> TBD : brute force avec 2 boucles imbriquées

### Algorithme en $\mathcal{O}(T.\mbox{\small longueur}\ln(T.\mbox{\small longueur}))$

> TBD : avec un tri

### Algorithme en $\mathcal{O}(\max(T))$

> TBD : bucket sort de la valeur absolue. Dès que l'on rencontre la case la deuxième fois on sort.
> TBD attention : même si on ne visite pas toutes les cases du tableau il faut les initialiser à 0 (le contenu de la mémoire est inconnu à l'affectation).

> TBD complexité spatiale $\mathcal{O}(\max(T))$ ce qui est déraisonnable car cela peut être aussi grand que l'on veut.
> TBD c'est même exponentiel en la taille du tableau ($\log_2(n)$ bits pour stocker l'entier $n$).
> TBD : même si la complexité de créer un tableau de taille arbitraire est en  $\mathcal{O}(2)$, et que l'on ne fait de boucle que sur la taille du tableau, l'algorithme est tout de même en $\mathcal{O}(\max(T))$ car il faut initialiser les cases : à la création d'un tableau ses valeurs sont indéterminées.

## 3-SUM

### Algorithme en $\mathcal{O}(T.\mbox{\small longueur}^3)$

> TBD : brute force avec 3 boucle imbriquées

### Algorithme en $\mathcal{O}(T.\mbox{\small longueur}^2)$

> TBD : un tri puis on cherche en $\mathcal{O}(T.\mbox{\small longueur})$ s'il existe i et j pour lesquels $T[i] + T[j] = -T[k]$ pour k allant de 0 à la taille du tableau ($\mathcal{O}(T.\mbox{\small longueur})$ boucles)
