---
layout: layout/post.njk
title: Pseudo-code

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

[La définition générale d'un programme](../bases-théoriques/définition/#définition-règles-générales) ne spécifie rien sur les instructions à utiliser, juste qu'elles doivent être décrites en un nombre fini de mots. Un **_pseudo-code_** est une proposition d'instructions possibles pour décrire un programme, compréhensibles par un humain.

Ce n'est cependant pas une langue car il n'y a pas de place pour l'ambiguïté ni pour l'interprétation : tout doit y être rigoureusement défini et chaque étape élémentaire doit être réalisable en un temps fini par un humain.

{% lien %}
[On the foolishness of "_natural language programming_"](https://www.cs.utexas.edu/~EWD/transcriptions/EWD06xx/EWD667.html){.externe}
{% endlien %}

Ce n'est pas non plus un langage informatique dont le but est d'être exécuté par un ordinateur.  Le but d'un pseudo-code est d'être compris par d'autres humains et doit être vu comme une démonstration mathématique : un algorithme prouve à d'autres humains qu'un problème est solvable par un ordinateur.

<div id="définition-pseudo-code"></div>

{% definition %}
Un **_pseudo-code_** est une succession de lignes qui seront exécutées **_en séquence_**.

- chaque ligne est composée d'une instruction qu'il faut réaliser avant de passer à la ligne suivante,
- chaque instruction est clairement définie et est réalisable par un humain muni d'un papier et d'un crayon
{% enddefinition %}

Si le but premier d'un pseudo-code est d'être compris par un humain, Les langages de programmation classiques comme [python](https://www.python.org/){.externe}, [go](https://go.dev/){.externe} ou encore [rust](https://www.rust-lang.org/fr){.externe} se transcrivent aisément en pseudo-code et réciproquement (ce sont deux notions équivalentes).

{% retenir %}

- on utilisera le pseudo-code pour l'étude théorique des algorithmes
- on codera ces algorithme dans un langage dédié à être exécuté lorsque l'on voudra les tester. Dans le cadre de ce cours on utilisera le python, puis le go et enfin le rust.

{% endretenir %}

## Écrire du pseudo-code

Commençons par décrire la _grammaire de base_ du pseudo-code :

{% aller %}
1. [Briques de base](briques-de-base)
2. [Abus de notation](abus)
{% endaller %}

On peut maintenant utiliser les différentes instructions du pseudo-code pour écrire nos algorithmes :

{% aller %}
1. [Algorithmes et Fonctions en pseudo-code](algorithmes-fonctions)
2. [Algorithmes itératifs et récursifs](récursifs-itératifs)
{% endaller %}

Un bon pseudo-code doit être compréhensible en tant que tel, sans commentaires.

Pour cela il faut :

- expliciter la signature de vos algorithmes,
- utiliser des noms de variables ou de fonctions explicites et utile à la compréhension,
- séparer les différentes parties d'un algorithmes en fonctions au nom explicite.

Leurs noms importent peu, seuls leurs fonctions sont importantes. Vous pouvez donc utiliser les mots qui vous plaisent, du moment qu'ils sont compréhensible pour vous et — surtout — pour votre lecteur. Le plus souvent, on utilisera un mix de python et de français, ou d'anglais.

## Opérateurs utilisés en pseudo-code

Plusieurs opérateurs ressemblant à l'égalité sont utilisés en pseudo-code, attention à bien comprendre leurs différences.

- `ref x T`{.language-} : on définit la variable `x`{.language-} pouvant référencer des objets de type `T`{.language-}
- `x ← y`{.language-} : on affecte `x`{.language-} à la valeur de `y`{.language-}
- `x == y`{.language-} : on teste l'égalité entre les valeurs de `x`{.language-} et de `y`{.language-}. L'expression est vraie si la valeur de x vaut la valeur de y et faux sinon. Par exemple ` 2 * x + 2 == 10`{.language-}

Les autres opérateurs possible en algorithmie sont :

- `x := y`{.language-} : on définit `x`{.language-} comme étant `y`{.language-}. Par exemple $f(x) \coloneqq max(x, 10)$
- `x = y`{.language-} : avec les définitions et les propriétés de `x`{.language-} et `y`{.language-} les valeurs des eux variables sont toujours égales. C'est une conséquence comme $\cos(\pi) = -1$.
