---
layout: layout/post.njk

title: Définitions et premiers calculs

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

[On l'a vu](../../écrire-algorithmes/pseudo-code/#complexité), on appelle complexité d'un pseudo-code le nombre d'opérations élémentaires utilisées pour son exécution. Si chaque opération élémentaire prend le même temps à être effectuée sur une machine (humaine ou mécanique), la complexité d'un pseudo-code nous donne un nombre proportionnel au temps qu'il mettra à s'exécuter.


> TBD : Notez que l'on a pas besoin d'une mesure précise, seule l'allure suffit à déterminer son asymptote.

> TBD : mettre $\mathcal{O}$ (parler de $\Omega$) et ajouter $\Theta$  dans un truc à part pour expliquer pourquoi c'est central en informatique (Turing aussi). Avec hiérarchie des complexité Polynomial vs exponentiel (faire tous les cas).

> notion de complexité : temps nécessaire pour.

## Définition

1. nb d'opérations élémentaires = mesure du temps
2. dépend de l'entrée : faire graphique.
3. outil pour la mesurer : $\mathcal{O}$ (parler de $\Omega$) et ajouter $\Theta$. Limite lorsque entree grossi. Si petit on s'en fiche ca va vite.