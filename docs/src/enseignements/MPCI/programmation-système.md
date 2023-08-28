---
layout: layout/post.njk 
title: "S5 : Programmation Système"

eleventyNavigation:
  order: 3

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title }}"
    parent: "{{ '../' | siteUrl(page.url) }}"

---

Objectif : Le but de cette UE est d’acquérir les connaissances nécessaires en programmation bas-niveau et système. Quatre volets seront abordés :

* Système Linux/Ubuntu
* Programmation bas niveau avec le langage C
* décompilation de fichier et utilisation du le assembleur x86
* Communication inter-processus et programmation concurrente

## Note

La note de cette UE résulte de cette formule :

$$
\max (\frac{DM+ DS + ET}{3}, ET)
$$

Avec :

* $DM$ devoir(s) maison ou exposé(s)
* $DS$ la note du devoir surveillé
* $ET$ est l'examen terminal
