---
layout: layout/post.njk 
title: Les possibilités d'édition en markdown

tags: ['tutoriel', 'markdown', 'eleventy']
---

Comparer le résultat au [code source](https://raw.githubusercontent.com/FrancoisBrucker/do-it/main/src/blog/possibilite-markdown.md).

## titre `##`

### titre `###`

#### titre `####`

##### titre `#####`

## liens

* [post 2 chemin relatif](../post-2)
* [post 2 chemin absolu]({{ "/blog/post-2" | url }})
* [post 2 chemin relatif avec une ancre](../post-2#images)
* [post 2 chemin absolu avec une ancre]({{ "/blog/post-2" | url }}#images)

## listes

### non ordonnées 

* un
* deux
* trois

### ordonnées

1. un
2. deux
3. trois

## quotes

### une quote normale
> Une quote normale
> sur deux lignes.

### une mise en garde

#### sans titre

{% attention %}
Une mise en garde.
{% endattention %}

#### avec titre

{% attention "**faisez** attention" %}
Une *grosse* mise en garde.
{% endattention %}


### une note

#### sans titre

{% note %}
Une note à retenir.
{% endnote %}

#### avec titre

{% note "**Proposition**" %}
Un énoncé de proposition.
{% endnote %}

### une information

#### sans titre

{% info %}
Un truc marrant ou une information utile, mais pas indispensable.
{% endinfo %}

#### avec titre

{% info "***lol* !**" %}
Un truc marrant ou une information utile, mais pas indispensable.
{% endinfo %}

### un chemin

{% chemin %}
[Tutoriels]({{ ".." | url }}) / [{{title}}]({{ "." | url }})
{% endchemin %}

### un chemin  plus un prés-requis

#### sans titre

{% chemin %}
[Tutoriels]({{ ".." | url }}) / [{{title}}]({{ "." | url }})
{% endchemin %}
{% pres-requis %}
* un cerveau en état de marche
* notion de web
{% endpres-requis %}


#### avec titre

{% chemin %}
[Tutoriels]({{ ".." | url }}) / [{{title}}]({{ "." | url }})
{% endchemin %}
{% pres-requis "À lire avant de commencer :" %}
* *graphes* de Claude Berge
* *hypergraphes* de Claude Berge
{% endpres-requis %}

## algorithmes

### programme

```python
permutations(T):
l = [1, 3, 2, 6, 4, 5]
print(l.max())
```

### avec lignes numérotées

```python#
permutations(T):
l = [1, 3, 2, 6, 4, 5]
print(l.max())
```

### dans le texte 

* par défaut : `l = [1, 3, 2, 6, 4, 5]`
* on dit que c'est un langage : `l = [1, 3, 2, 6, 4, 5]`{.language-python}.

## images {#images}

![WTFs/minute](../possibilite-markdown-wtfm.jpg)

> Notez le `..` qui est important dans tous les liens.

## équations

$$2+2 = \frac{1}{2}$$

Et un $\log(3)^2$ dans une phrase.

## exercice

Un texte avant.
{% exercice %}
Une **question** ou un **exercice** à faire. Avec du $\LaTeX$ dedans : $\sum_x\delta(x)$
{% endexercice %}
Un texte après.

## details

### dans le texte

Un texte avant.
{% details "spoiler" %}
Quelque chose de caché. Que l'on peut *écrire* en `Markdown` 
{% enddetails %}
Un texte après.

### dans un exercice

Un texte avant.
{% exercice %}
Un exercice à faire.
{% endexercice %}
{% details "corrigé" %}
Le corrigé de l'exercice.
{% enddetails %}
Un texte après.

## tables

On utilise les possibilités de [multimarkdown](https://fletcher.github.io/MultiMarkdown-6/syntax/tables.html)

### de base 

| titre colonne 1  | titre colonne 2 |
| ---------------- | --------------- |
| Content Cell     | Content Cell  |
| Content Cell     | Content Cell  |


### sans titre



| ------------- | ------------- |
| Content Cell  | Content Cell  |
| Content Cell  | Content Cell  |


### multi-colonne


| ------------- | ------------- |
|     Content Cell             ||
| Content Cell  | Content Cell  |


### multi-ligne

| ------------- | ------------- |
| Content Cell  | Content Cell  |
| ^^            | Content Cell  |

### plusieurs ligne dans une cellule

| ------------- | ------------- |
| Content Cell  | * Content Cell  | \
| Content Cell  | * Content Cell  |
| Content Cell  | Content Cell  |


### alignement horizontal

| :- | :-: | -: |
| Content Cell  | Content Cell  | Content Cell |
| Content Cell  | Content Cell  |Content Cell  |
| Content Cell  | Content Cell  |Content Cell  |


### alignement vertical

On ajoute un style, mais il ne faut pas que ce soit la dernière colonne. 

| ------------- | ------------- |
| Content Cell  {style="vertical-align:middle"}| Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus eleifend, orci nec pharetra lacinia, lacus dolor euismod ipsum, quis pulvinar ipsum urna non purus. Cras accumsan ex ligula, eu pellentesque mauris congue ac. Integer venenatis elementum est ac imperdiet. Etiam lectus purus, imperdiet gravida commodo non, faucibus at metus. Maecenas elit nibh, venenatis a efficitur vitae, placerat vitae nulla. Fusce volutpat nisl sem, vel iaculis risus sagittis vel. Nunc felis tellus, sollicitudin eu felis vel, cursus egestas arcu. Sed laoreet ex a nisl vestibulum, id placerat leo pellentesque. Praesent nec ultrices purus, ut congue elit. Pellentesque in diam ultrices purus volutpat lacinia. | 
| Content Cell  | Content Cell  |

Pour la dernière colonne, il faut ajouter une colonne vide : 

| ------------- | ------------- | - |
| Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus eleifend, orci nec pharetra lacinia, lacus dolor euismod ipsum, quis pulvinar ipsum urna non purus. Cras accumsan ex ligula, eu pellentesque mauris congue ac. Integer venenatis elementum est ac imperdiet. Etiam lectus purus, imperdiet gravida commodo non, faucibus at metus. Maecenas elit nibh, venenatis a efficitur vitae, placerat vitae nulla. Fusce volutpat nisl sem, vel iaculis risus sagittis vel. Nunc felis tellus, sollicitudin eu felis vel, cursus egestas arcu. Sed laoreet ex a nisl vestibulum, id placerat leo pellentesque. Praesent nec ultrices purus, ut congue elit. Pellentesque in diam ultrices purus volutpat lacinia. | Content Cell  {style="vertical-align:middle"}| | 
| Content Cell  | Content Cell  | |

## résumé

Deux balises à placer entre le résumé de votre post : 

```text
<!-- début résumé -->

Ici le résumé. 

<!-- fin résumé -->
```
