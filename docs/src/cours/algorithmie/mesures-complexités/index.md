---
layout: layout/post.njk

title: Mesures de complexités

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

> TBD : mettre $\mathcal{O}$ (parler de $\Omega$) et ajouter $\Theta$  dans un truc à part pour expliquer pourquoi c'est central en informatique (Turing aussi). Avec hiérarchie des complexité Polynomial vs exponentiel (faire tous les cas).

> notion de complexité : temps nécessaire pour.

## Définition

1. nb d'opérations élémentaires = mesure du temps
2. dépend de l'entrée : faire graphique.
3. outil pour la mesurer : $\mathcal{O}$ (parler de $\Omega$) et ajouter $\Theta$. Limite lorsque entree grossi. Si petit on s'en fiche ca va vite.