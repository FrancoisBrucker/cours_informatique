---
layout: layout/post.njk

title: Arbres planaires

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Les arbres planaires sont un cas particulier des arbres plantés où les enfants de chaque sommets sont numérotés de 1 au nombre d'enfants. On appelle ces arbres planaires car cela revient à numéroter les enfant selon leur représentation graphique. De là, les deux graphes suivant ne seront pas égaux :

![pas pareils](./pas-pareil.png)

Car les enfants de la racine ne sont pas placés de la même manière. En numérotant les enfants de gauche à droites, cela donnerait les deux arbres ci-après du coup vraiment différents :

![pas pareils](./pas-pareil-numérotés.png)

Pour éviter d'avoir des nœuds avec une même numérotations et avoir une définition formelle, on encode tout le chemin :

{% note "**Définition**" %}
L'ensemble des suites finies d'entiers strictement positifs ($\mathbb{N}^\star$) est noté $U$. On peut le définir tel que :

<div>
$$
U \coloneqq \{ \epsilon \} \cup \cup_{n\geq 1}(\mathbb{N}^\star)^n
$$
</div>

Avec $\epsilon$ la suite vide et $(\mathbb{N}^\star)^n = \mathbb{N}^\star \times \dots \times \mathbb{N}^\star$ le produit cartésien de taille $n$ de l'ensemble $\mathbb{N}^\star$ des entiers strictement positifs.
{% endnote  %}

> TBD reprendre l'exemple avec les mot


> TBD arbre planaires. Suite de voisins. Montrer approche avec suites de mots.



> un DFS. pour encoder les arbres planaires. c'est un mot de Dyck (E(nfant suivant)/P(arent)) <https://moodle1.u-bordeaux.fr/pluginfile.php/462061/mod_resource/content/0/Slides.pdf>. C'est une bijection. Encode en +1, -1 ou en chemins.
> TBDTrouver exam centrale PC 2011 <https://www.doc-solus.fr/prepa/sci/adc/bin/view.corrige.html?q=PC_MATHS_CENTRALE_1_2021https://www.doc-solus.fr/prepa/sci/adc/bin/view.corrige.html?q=PC_MATHS_CENTRALE_1_2021>
> TBD énumération avec un Dijkstra sur arbre orienté sur demi-grille.
