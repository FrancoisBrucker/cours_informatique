---
layout: layout/post.njk 
title: Format Markdown

tags: ['tutoriel', 'markdown']
---

{% pres-requis %}
* vsc plugin markdwon
{% endpres-requis %}

<!-- début résumé -->

Une introduction au format markdown.

<!-- fin résumé -->



> [Markdown](https://fr.wikipedia.org/wiki/Markdown) est un format de fichier texte, donc modifiable par tout éditeur de texte. L'extension de fichier est *".md"*.
{.note}

L'intérêt de ce format de fichier texte est qu'il est parfaitement lisible dans tout éditeur de texte et qu'on peut de plus le *compiler* dans un autre format comme le pdf ou encore le html si on veut le partager.

> Tout ce site par exemple été écrit en markdown avant d'être compilé en html. Le code source est [visible](https://github.com/FrancoisBrucker/cours_informatique), en particulier celui de [ce fichier](https://github.com/FrancoisBrucker/cours_informatique/blob/master/docs/_tutoriels/format-markdown.md) (cliquez sur le bouton `raw` à droite, juste avant que le fichier ne soit représenté).

{% note %}
Pour écrire confortablement du markdown. Installez un plugin pour votre éditeur préféré, pour vscode, [suivez ce tutoriel](../vsc-plugin-markdown).
{% endnote %}

## syntaxe

Le markdown est un format très simple. Il permet de structurer minimalement un texte, ce qui est suffisant pour la plupart des rapports/documentations de code.

### un exemple {#exemple}

{% exercice %}
Dans vscode, créez un nouveau fichier que vous appellerez *"exemple.md"* (*".md"* est l'extension par défaut des fichiers markdown).

Copiez/collez-y- le texte ci-dessous et sauvez le fichier.
{% endexercice %}


```text

# Un petit peu de Markdown

## quoi ?

Le [Markdown](https://fr.wikipedia.org/wiki/Markdown) est un format texte éditable et visualisable dans tout éditeur.

## comment ?

### style 

- peut écrire en *italique*
- ou en **gras**
- du `code` 
- des équations latex comme $2 \pi + \frac{1}{2}$

### bloc

On peut aussi écrire des blocs de code, comme :

1. des équations en latex
2. du code python
3. du texte brut

```

Le texte ci-dessus est un petit panel de ce qu'on peut faire en markdown. Il montre en particulier comment on peut représenter :

* des sections
* des liste ordonnées ou non
* du style (italique, gras, code, équations)

Vous voyez que ce format est *lisible* directement dans vscode (on comprend qu'un titre est un titre par exemple). Mais on  peut aussi *compiler* ce fichier texte en html.

> Dans vscode, en ayant comme onglet actif celui contenant le fichier *"exemple.md"*, ouvrez la [palette de commande](../vsc-installation-et-prise-en-main#palette-de-commande) et taper la commande `markdown All in One: Print current document to HTML`.
>
> **Attention** : une commande dans la palette commence toujours par `>` qui doit être le 1er caractère.
>
{.a-faire}

Après l'exécution de cette commande, vous aurez un fichier *"exemple.html"* dans le même dossier que votre fichier *"exemple.md"*.

> Ouvrez le fichier *"exemple.html"* dans votre navigateur favori pour voir le résultat.
{.a-fair}

### balise à connaître

Les principales fonctionnalités sont décrites dans [cette liste](https://www.markdownguide.org/cheat-sheet/#basic-syntax).

#### sections

```text
# titre du document

## section

### sous-section

#### sous-sous-section

```

#### paragraphes

Un saut de ligne est nécessaire pour commencer un nouveau paragraphe. Aller à la ligne sera équivalent à un espace.

#### style inline

Dans le flot du texte, on peut mettre en exergue des parties de texte :

* *en italique* : `*texte*`
* **en gras** : `**texte**`
* ***en gras et en italique*** : `***texte***`
* ~~barré~~ : `~~texte~~`
* `code` : `` `texte` ``
* équations : `$\LaTeX$`

#### style bloc

En markdown, un bloc commence et finit par une ligne vide.

Plusieurs symboles peuvent être utilisées :

* [code](https://www.markdownguide.org/extended-syntax/#fenced-code-blocks). Mettez le langage utilisé pour activer la coloration syntaxique (par défaut, je mets comme langage `text` lorsque j'écris un algorithme en pseudo-code)
* [remarques](https://www.markdownguide.org/basic-syntax/#blockquotes-1)
* [latex](#latex)

#### listes

Comme chaque bloc, les listes commencent et finissent toujours par une ligne vide. Il y a deux types de listes :

* [non ordonnées](https://www.markdownguide.org/basic-syntax/#unordered-lists). Chaque item peut commencer par un `-`, un `*` ou encore un `+`. Choisissez en un et tenez vous y dans tout le document.
* [ordonnées](https://www.markdownguide.org/basic-syntax/#ordered-lists)

## Formules mathématiques

Lorsque l'on écrit des textes scientifiques, vient inévitablement la question de l'écriture des équations.

### latex {#latex}

Le langage [Latex](https://fr.wikipedia.org/wiki/LaTeX) permet d'écrire toutes les équations imaginable (et même plus) avec un petit langage que l'on peut utiliser directement dans un éditeur de texte (ceux qui ont déjà utilisé l'éditeur d'équation de Word savent que c'est l'enfer de devoir tout cliquer).

>L'ancêtre de [Latex](https://fr.wikipedia.org/wiki/LaTeX) : [Tex](https://fr.wikipedia.org/wiki/TeX), a été créé par le célèbre informaticien [Donald Knuth](https://fr.wikipedia.org/wiki/Donald_Knuth) par ce qu'il n'existait rien sur ordinateur à l'époque pour écrire [ses livres](https://fr.wikipedia.org/wiki/The_Art_of_Computer_Programming) en respectant une typographie correcte.

Une fois ce langage appris, il est étonnement clair, même non compilé en *jolies formules*. Avec un peut d'habitude, on voit bien que : `$$\cos x=\sum_{k=0}^{\infty}\frac{(-1)^k}{(2k)!}x^{2k}$$` est égal à :

$$\cos x=\sum_{k=0}^{\infty}\frac{(-1)^k}{(2k)!}x^{2k}$$

Quelques aides :

* Un [résumé](http://tug.ctan.org/info/undergradmath/undergradmath.pdf) des possibilités
* un [tuto](https://www.science-emergence.com/Articles/Formules-math%C3%A9matiques-sous-LaTeX/) Latex contenant aussi des instructions pour les équations.

### en markdown

On peut écrire en markdown les équations latex.

* pour une équation dans le texte, on dit *inline* on entoure notre équation  par des `$`
* pour équation au milieu de la page, on dit *display*, on entoure notre équation par des `$$` et on saute une ligne avant et après les `$$`. comme dans l'exemple ci-après.

Equation en mode inline :

```text
je pense que $3 + 2$ vaut 5.
```

Equation en mode *display* :

```tex

$$
3+2
$$

```

Lorsque vous faites de l'exportation en html, les mathématiques sont représentées en utilisant la bibliothèque [Mathjax](https://www.mathjax.org/).

>Il ne faut pas mettre d'espace après le premier `$` et avant le dernier `$` lorsque l'on écrit des équations, sinon les convertisseur ne reconnaitront pas que ce sont des équations que vous voulez écrire. Ansi `$ \frac{1}{2}$` affichera `$ \frac{1}{2}$`, alors que `$\frac{1}{2}$` affichera $\frac{1}{2}$.
{.attention}

## pour aller plus loin

### guides

* base markdown et latex : <https://ashki23.github.io/markdown-latex.html>
* base markdwon : <https://www.markdownguide.org/> par exemple
* [Mathjax et latex](https://math.meta.stackexchange.com/questions/5020/mathjax-basic-tutorial-and-quick-reference)

### variantes de markdown

Le format markdown est basique. Il possède plein de variantes qui permettent d'étendre ses possibilités. Deux d'entre elles sont devenus des standard de fait :

* [commonMark](https://spec.commonmark.org/) utilisé pour ce site.
* [github flavored markdown](https://guides.github.com/features/mastering-markdown/).
* [kramdown](https://kramdown.gettalong.org/documentation.html).
