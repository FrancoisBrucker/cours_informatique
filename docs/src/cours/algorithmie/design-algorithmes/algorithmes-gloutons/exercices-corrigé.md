---
layout: layout/post.njk
title: "Exercices gloutons : corrigé"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

## Glouton optimal

### Recouvrement

<https://algo.gricad-pages.univ-grenoble-alpes.fr/L3I-S5-algo/TD1-10-corrige.pdf>
> recouvrement de points par des intervalles exo 3
### réservation SNCF

#### solution possible ?

Une solution en $\mathcal{O}(n+K)$ : 

```python
d = [0] * K

for i in range(n):
    d[t[i]] += 1

for t in range(K):
    if d[t] > P:
        print("le train", t, "contient", d[t] - P, "passagers de trop.")
```

#### solution approchée

### Ordonnancement, la variante

C'est pareil. Il suffit de dire que la perte est un gain et de maximiser le gain.

### Ordonnancement, le retour

> introduction à l'algorithmique p393

#### Formalisation du problème

#### Algorithme

#### Dates de disponibilité

#### Interruption de tâches

