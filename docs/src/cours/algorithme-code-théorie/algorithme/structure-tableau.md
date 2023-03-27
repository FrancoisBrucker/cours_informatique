---
layout: layout/post.njk 
title: "Structure : tableau"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title }}"
    parent: "{{ '../' | siteUrl(page.url) }}"

prerequis:
    - "../complexité-moyenne/"
    - "../../code/mémoire-espace-noms/"
---

<!-- début résumé -->

Mise en œuvre de la structure de tableau, qui est la base de tous les conteneurs de donnés.

<!-- end résumé -->

Un [tableau](https://fr.wikipedia.org/wiki/Tableau_(structure_de_donn%C3%A9es)) est un conteneur pouvant contenir $n$ objets(on appelle $n$ la taille d'un tableau). On peut accéder et affecter un objet au tableau grâce à un indice allant de $0$ à $n-1$ : si `t`{.language-} est un tableau `t[i]`{.language-} correspond à l'objet d'indice $i$ du tableau.

Les opérations simples possibles avec un tableau sont :

* **créer un tableau de taille $n$**
* **supprimer un tableau**
* **récupérer et affecter** l'objet d'indice $i$ du tableau (objet `t[i]`{.language-})

## Structure de tableau

En simplifiant un peu, un tableau $t$ est une structure composée deux champs :

* un entier $n$ donnant sa taille
* une adresse en mémoire (notée $\\&t$) permettant de stocker $n$ adresses

Si l'on suppose que l'on possède une mémoire de 1 Go, une adresse entre 0 et $10^9$ nécessite 30 bit et peut donc se coder sur 4 octets ($4 \cdot 8 = 32$ bits). L'adresse du tableau est alors un entier entre 0 et $2^32-1$ et la place allouée en mémoire de $n \cdot 4$ octets.

On ne range pas directement l'objet à stocker dans le tableau, uniquement son adresse dans la mémoire. Cette astuce permet d'allouer la même taille à chaque objet dans le tableau, donc d'obtenir l'adresse de l'objet $t[i]$ en une seule opération : $\\&t + 4 \cdot i$.

## Opérations basiques

Le système (Mac, Windows, Linux ou autre) permet d'allouer ou de dé-allouer de la mémoire en temps constant. On a alors les complexités suivante :

* création d'un tableau de taille $n$ : $\mathcal{O}(1)$ opérations
* suppression d'un tableau : $\mathcal{O}(1)$ opérations

Il est de plus possible d'accéder via le système à un élément quelconque de la mémoire en $\mathcal{O}(1)$ opérations. Ceci  fait qu'on peut accéder à la case mémoire d'indice  $\\&t + 4 \cdot i$ en $\mathcal{O}(1)$ opérations et donc :

* récupérer l'objet $t[i]$ du tableau en $\mathcal{O}(1)$ opérations
* affecter un nouvel objet d'indice $i$ du tableau en $\mathcal{O}(1)$ opérations

{% note %}
La structure de tableau est un moyen optimal (de complexité constante) pour stocker un nombre donné d'objets.
{% endnote %}

## Opérations complexes

Lorsque le nombre d'objets à stocker n'est pas constant, ou qu'il faut redimensionner le tableau, les choses se compliquent. Il est en effet impossible de garantir que l'on redimensionner de la mémoire en temps constant car :

* plusieurs programmes se partagent la mémoire, on ne peut pas garantir que la place à côté de notre tableau est libre
* on ne peut pas allouer ou dé-allouer la mémoire octet par octet (on le fait par *page*> La taille de la page dépend du système, mais c'est souvent 4Ko)

Il est donc impossible de modifier la taille d'un tableau, il faut en recréer un nouveau avec la bonne taille :

* pour augmenter la taille d'un tableau, il faut recréer un tableau vide avec la nouvelle taille puis recopier tous les éléments de l'ancien tableau au nouveau. Cela se fait donc en $\mathcal{O}(n)$ opérations où $n$ est la taille de l'ancien tableau.
* pour réduire la taille d'un tableau, il faut recréer un tableau vide avec la nouvelle taille puis recopier les éléments que l'on veut garder de l'ancien tableau au nouveau. Cela se fait en $\mathcal{O}(n)$ opérations où $n$ est la taille du nouveau tableau.
