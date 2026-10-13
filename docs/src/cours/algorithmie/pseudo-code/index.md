---
layout: layout/post.njk
title: Pseudo-code

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

<!-- TBD

Mettre en info une structure plus avancé que l'on verra plus tard avec les pointeurs. Pa utile pour les complexité en O et les langages de script (python, js ne font pas la diff) amis si on veut faire des programmes plus optimisé voir systeme c'est important.


Parler de pseudo-code objet dans la 1ère partie : variable lien vers objet en mémoire. Dire que le modèle est ainsi taille de variable fixe vers objet. mutable et non mutable selon ce qu'on peut faire dessus.

Une variable vaut None lorsqu'elle est crée.
Puis affectée à l'adresse d'un objet en mémoire explicitement. 

- Il ne faut pas utiliser des variables non initialisées
- None est réservé aux variables non initialisées (?)
- un tableau est un objet composé de variables de même type.

- if then = forme pure. Puis else et elif du sucre syntaxique que l'on définira. Va être utile pour la fin ou l'on fera l'equivalence pseudo-code et fonction logique. 



- int et str pas de taille finies
- dire mémoire = tableau avec indice
- int composé de bits et str de char (parmi un alphabet fini). Chacun de taille fixe.
- str n'est pas un tableau : chaque case correspond à un caractère. Montrer la diff entre []char et str dans le cadre du pseudo-code objet.
- float est aussi fini : approximation d'un réel.
- une var déclarée vaut None. C'est un emplacement en mémoire réservé aux variables. Chaqeu variable à la même taille = une adresse On lui affecte un objet
- un tableau est un objet qui contient des variables :
  - déclaré vaut None
  - crée chaque case vaut None
- toute variable déclarée doit être affectée.

-->




{% lien %}
[On the foolishness of "_natural language programming_"](https://www.cs.utexas.edu/~EWD/transcriptions/EWD06xx/EWD667.html)
{% endlien %}

[La définition générale d'un algorithme](../bases-théoriques/définition/#définition-règles-générales){.interne} ne spécifie rien sur les instructions à utiliser, juste qu'elles doivent être décrites en un nombre fini de mots. Un **_pseudo-code_** est une proposition d'instructions possibles pour décrire un algorithme, compréhensibles par un humain.

Ce n'est cependant pas une langue car il n'y a pas de place pour l'ambiguïté ni l'invention : tout doit y être rigoureusement défini, et chaque étape élémentaire doit être réalisable en un temps fini par un humain.

Ce n'est pas non plus un langage informatique dont le but est d'être compris par un ordinateur. Il est communément admis que tout algorithme peut être écrit en **_pseudo-code_** :

<span id="règles"></span>
{% note2 "**Définition**" %}
Un pseudo-code est une succession de lignes qui seront exécutées **_en séquence_** les unes à la suite des autres. Chaque ligne est composée d'une instruction qu'il faut réaliser avant de passer à la ligne suivante.
{% endnote2 %}

Les langages de programmation classiques comme [python](https://www.python.org/), [go](https://go.dev/) ou encore [rust](https://www.rust-lang.org/fr) se transcrivent aisément en pseudo-code et réciproquement. Ce sont deux notions équivalentes :

- on utilisera le pseudo-code pour l'étude théorique des algorithmes
- on codera ces algorithme dans un langage dédié à être exécuté lorsque l'on voudra les tester. Dans le cadre de ce cours on utilisera le python.

## Éléments de pseudo-code

### Briques de base

Commençons par décrire la _grammaire de base_ du pseudo-code :

{% aller %}
[Briques de base](briques-de-base){.interne}
{% endaller %}

### Algorithmes en pseudo-code

On peut maintenant utiliser les différentes instructions du pseudo-code pour écrire nos algorithmes :

{% aller %}
[Algorithmes et Fonctions en pseudo-code](algorithmes-fonctions){.interne}
{% endaller %}

## Écrire du bon pseudo-code

Un bon pseudo-code doit être compréhensible en tant que tel, sans commentaires.

Pour cela il faut :

- expliciter la signature de vos algorithmes
- utiliser des noms de variables ou de fonctions explicites et utile à la compréhension
- séparer les différentes parties d'un algorithmes en fonctions au nom explicite.

Leurs noms importent peu, seuls leurs fonctions sont importantes. Vous pouvez donc utiliser les mots qui vous plaisent, du moment qu'ils sont compréhensible pour vous et — surtout — pour votre lecteur. Le plus souvent, on utilisera un mix de python et de français, ou d'anglais.

## Opérateurs utilisés en pseudo-code

Plusieurs opérateurs ressemblant à l'égalité sont utilisés en pseudo-code, attention à bien comprendre leurs différences.

- `x := y`{.language-} : on définie `x`{.language-} comme étant `y`{.language-}
- `x ← y`{.language-} : on affecte `x`{.language-} à la valeur de `y`{.language-}
- `x = y`{.language-} : avec les définitions et les propriétés de `x`{.language-} et `y`{.language-} les valeurs des eux variables sont toujours égales. C'est une conséquence.
- `x == y`{.language-} : on teste l'égalité entre les valeurs de `x`{.language-} et de `y`{.language-}. vrai si la valeur de x vaut la valeur de y et faux sinon

## _"Abus"_ de notation

On se permettra, lorsque l'instruction est assez claire de procéder à des raccourci pour rendre le pseudocode plus digeste. Attention, la plupart de ces opérations ne seront pas des opérations élémentaires !

{% aller %}
[Abus de notation](abus){.interne}
{% endaller %}
