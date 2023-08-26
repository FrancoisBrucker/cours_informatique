---
layout: layout/post.njk

title: Contribuer au site
tags: ['tutoriel', 'markdown', 'eleventy']
authors:
    - François Brucker

eleventyNavigation:
  prerequis:
    - ../format-markdown/

eleventyComputed:
    eleventyNavigation:
        key: "{{ page.url }}"
        title: "{{ title | safe }}"
        parent: "{{ '../' | siteUrl(page.url) }}"
---

<!-- début résumé -->

Les différentes possibilités d'écriture de post pour ce site. On rappellera des possibilités de [commonMark](https://spec.commonmark.org/) (extension de Markdown utilisé ici) ainsi que des shortcodes spécialement écrites.

<!-- fin résumé -->

Comparer le résultat au [code source](https://raw.githubusercontent.com/FrancoisBrucker/do-it/main/src/blog/possibilite-markdown.md).

## titre `##`

### titre `###`

#### titre `####`

##### titre `#####`

## liens

* [post 2 chemin relatif](../post-2){.interne}
* [post 2 chemin absolu]({{ "/blog/post-2" | url }}){.interne}
* [post 2 chemin relatif avec une ancre](../post-2#images){.interne}
* [post 2 chemin absolu avec une ancre]({{ "/blog/post-2" | url }}#images){.interne}

{% attention %}
Notez le `..` pour accéder au dossier courant des sources.
{% endattention %}

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

{% attention "**Faites** attention" %}
Une *grosse* mise en garde.
{% endattention %}

### Une note

#### Note sans titre

{% note %}
Une note à retenir.
{% endnote %}

#### Note avec titre

{% note "**Proposition**" %}
Un énoncé de proposition.
{% endnote %}

### Une information

#### Information sans titre

{% info %}
Un truc marrant ou une information utile, mais pas indispensable.
{% endinfo %}

#### Information avec titre

{% info "***lol* !**" %}
Un truc marrant ou une information utile, mais pas indispensable.
{% endinfo %}

### Un chemin

{% chemin %}
[Tutoriels]({{ ".."  }}) / [{{title}}]({{ "."  }})
{% endchemin %}

### Lien externe

{% lien %}
<www.google.fr>
{% endlien %}

### Lien interne

{% aller %}
[Tutoriels]({{ ".." }})
{% endaller %}

### Un chemin  plus un prérequis

#### Prérequis sans titre

{% chemin %}
[Tutoriels]({{ ".."  }}) / [{{title}}]({{ "."  }})
{% endchemin %}
{% prerequis %}

* un cerveau en état de marche
* notion de web

{% endprerequis %}

#### Prérequis avec titre

{% chemin %}
[Tutoriels]({{ ".."  }}) / [{{title}}]({{ "."  }})
{% endchemin %}
{% prerequis "À lire avant de commencer :" %}

* *graphes* de Claude Berge
* *hypergraphes* de Claude Berge

{% endprerequis %}

## Algorithmes

### Programme

```python
permutations(T):
l = [1, 3, 2, 6, 4, 5]
print(l.max())
```

### Avec lignes numérotées

```python#
permutations(T):
l = [1, 3, 2, 6, 4, 5]
print(l.max())
```

### Dans le texte

* par défaut : `l = [1, 3, 2, 6, 4, 5]`
* on dit que c'est un langage : `l = [1, 3, 2, 6, 4, 5]`{.language-}.

## Images { #images }

![WTFs/minute](wtfm.jpg)

{% attention %}
On a pas mis de `..` ici car le fichier est un index.
{% endattention %}

## Equations

$$2+2 = \frac{1}{2}$$

Et un $\log(3)^2$ dans une phrase.

{% attention "Il faut escaper les caractères de contrôle" %}

$$
\sigma(s,i) = \left\\\{
    \begin{array}{ll}
        \tau_{si} & \mbox{si } \{s,i\} \in E \\\\
        \infty & \mbox{sinon.}
    \end{array}
\right.
$$

Ou inclure dans du html (ce qui est plus simple) :

<div>
$$
\sigma(s,i) = \left\{
    \begin{array}{ll}
        \tau_{si} & \mbox{si } \{s,i\} \in E \\
        \infty & \mbox{sinon.}
    \end{array}
\right.
$$
</div>

{% endattention %}

## Interactions avec le lecteur

### Exercice

Un texte avant.
{% exercice %}
Une **question** ou un **exercice** à faire. Avec du $\LaTeX$ dedans : $\sum_x\delta(x)$
{% endexercice %}
Un texte après.

### A faire

Un texte avant.
{% faire %}
Quelque-chose à faire.
{% endfaire %}
Un texte après.

## Details

### Details dans le texte

```text
<div>
&#123;% details "spoiler" %}
Quelque chose de caché. Que l'on peut *écrire* en `Markdown`
&#123;% enddetails %}
</div>
```

Un texte avant.
{% details "spoiler" %}
Quelque chose de caché. Que l'on peut *écrire* en `Markdown`
{% enddetails %}
Un texte après.

### Details dans le texte ouvert

```text
<div>
&#123;% details "spoiler", "open" %}
Quelque chose de caché. Que l'on peut *écrire* en `Markdown`
&#123;% enddetails %}
</div>
```

Un texte avant.
{% details "spoiler", "open" %}
Quelque chose de caché. Que l'on peut *écrire* en `Markdown`
{% enddetails %}
Un texte après.

### Solution d'un exercice

Un texte avant.
{% exercice %}
Un exercice à faire.
{% endexercice %}
{% details "corrigé" %}
Le corrigé de l'exercice.
{% enddetails %}
Un texte après.

## Tables

On utilise les possibilités de [multimarkdown](https://fletcher.github.io/MultiMarkdown-6/syntax/tables.html)

### Tables de base

| titre colonne 1  | titre colonne 2 |
| ---------------- | --------------- |
| Content Cell     | Content Cell  |
| Content Cell     | Content Cell  |

### Tables sans titre

| ------------- | ------------- |
| Content Cell  | Content Cell  |
| Content Cell  | Content Cell  |

### Tables multi-colonne

| ------------- | ------------- |
|     Content Cell             ||
| Content Cell  | Content Cell  |

### Tables multi-ligne

| ------------- | ------------- |
| Content Cell  | Content Cell  |
| ^^            | Content Cell  |

### plusieurs ligne dans une cellule

| ------------- | ------------- |
| Content Cell  | * Content Cell  | \
| Content Cell  | * Content Cell  |
| Content Cell  | Content Cell  |

### Alignement horizontal

| :- | :-: | -: |
| Content Cell  | Content Cell  | Content Cell |
| Content Cell  | Content Cell  |Content Cell  |
| Content Cell  | Content Cell  |Content Cell  |

### Alignement vertical

On ajoute un style, mais il ne faut pas que ce soit la dernière colonne.

| ------------- | ------------- |
| Content Cell  {style="vertical-align:middle"}| Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus eleifend, orci nec pharetra lacinia, lacus dolor euismod ipsum, quis pulvinar ipsum urna non purus. Cras accumsan ex ligula, eu pellentesque mauris congue ac. Integer venenatis elementum est ac imperdiet. Etiam lectus purus, imperdiet gravida commodo non, faucibus at metus. Maecenas elit nibh, venenatis a efficitur vitae, placerat vitae nulla. Fusce volutpat nisl sem, vel iaculis risus sagittis vel. Nunc felis tellus, sollicitudin eu felis vel, cursus egestas arcu. Sed laoreet ex a nisl vestibulum, id placerat leo pellentesque. Praesent nec ultrices purus, ut congue elit. Pellentesque in diam ultrices purus volutpat lacinia. |
| Content Cell  | Content Cell  |

Pour la dernière colonne, il faut ajouter une colonne vide :

| ------------- | ------------- | - |
| Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus eleifend, orci nec pharetra lacinia, lacus dolor euismod ipsum, quis pulvinar ipsum urna non purus. Cras accumsan ex ligula, eu pellentesque mauris congue ac. Integer venenatis elementum est ac imperdiet. Etiam lectus purus, imperdiet gravida commodo non, faucibus at metus. Maecenas elit nibh, venenatis a efficitur vitae, placerat vitae nulla. Fusce volutpat nisl sem, vel iaculis risus sagittis vel. Nunc felis tellus, sollicitudin eu felis vel, cursus egestas arcu. Sed laoreet ex a nisl vestibulum, id placerat leo pellentesque. Praesent nec ultrices purus, ut congue elit. Pellentesque in diam ultrices purus volutpat lacinia. | Content Cell  {style="vertical-align:middle"}| |
| Content Cell  | Content Cell  | |

## Ecrire un post

### Structure

* si un unique ficher : `nom.md`{.fichier}
* si plusieurs fichiers de ressources ou des des sous parties :
  * un dossier `nom`{.fichier} et tous les fichiers à l'intérieur
  * fichier principal : `nom/index.md`{.fichier}

### Résumé

Deux balises à placer entre le résumé de votre post. Il est à placer entre les balises :

* `<!-- début résumé -->`
* `<!-- fin résumé -->`

### Entête

```text
---
layout: layout/post.njk 
title: Vsc extension Markdown
tags: ['vsc', 'tutoriel', 'markdown']

authors: 
    - François Brucker
    - Esprit Lesaint
---

```

Changez le :

* titre
* le ou les auteurs (vous pouvez ne mettre qu'un seul auteur)

Puis ajoutez :

* un chemin
* des prerequis
* un résumé
