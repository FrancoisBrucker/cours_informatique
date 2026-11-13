---
layout: layout/post.njk

title: "Algorithmie et aléatoire"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

> Tableau aléatoire parler de fisher-yates et du moyen de trouver des choses aléatoires en informatique. Notion de pseudo-aléatoire et de process physique pour l'aléatoire trouver des ref.

> 
> TBD un ordi est déterministe. PAS d'aléatoire. Deux solutions :
> - on simule l'aléatoire
> - on en cherche de l'extérieur (entropie)

## Nombres aléatoire et pseudo-aléatoires

> TBD pseudo-aléatoire (modulo et le démontrer) et aléatoire. On suppose qu'on a un truc aléatoire, genre /dev/random sous unix qui prend des paramètre extérieur pour générer de l'entropie.

## Permutation et Tableaux aléatoires

> TBD Fisher-Yates

La complexité en moyenne est également un moyen rapide et simple d'estimer la complexité d'un code. Pour estimer la complexité en moyenne d'un algorithme codé, on mesure le temps pris par l'algorithme pour s'exécuter avec des données aléatoires et on en fait la moyenne (c'est [un estimateur sans biais de la moyenne théorique](<https://fr.wikipedia.org/wiki/Estimateur_(statistique)#Estimateur_de_la_moyenne_de_Y>)).
