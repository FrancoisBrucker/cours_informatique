---
layout: layout/post.njk 

title: Format Markdown
tags: ['tutoriel', 'markdown']
authors: 
    - François Brucker


eleventyComputed:
    eleventyNavigation:
        key: "{{ page.url }}"
        title: "{{ title | safe }}"
        parent: "{{ '../' | siteUrl(page.url) }}"
---

<!-- début résumé -->

Une introduction au format markdown.

<!-- fin résumé -->

[Markdown](https://fr.wikipedia.org/wiki/Markdown) est un format de fichier texte, donc modifiable par tout éditeur de texte. L'extension de fichier est *".md"*.

L'intérêt de ce format de fichier texte est qu'il est parfaitement lisible dans tout éditeur de texte et qu'on peut de plus le *compiler* dans un autre format comme le pdf ou encore le html si on veut le partager.

{% note %}
Pour écrire confortablement du markdown. Installez un plugin pour votre éditeur préféré. Si vous avez suivi les prés-requis, vous avez déjà du installer l'extension pour vscode.
{% endnote %}

## Syntaxe

Le markdown est un format très simple. Il permet de structurer minimalement un texte, ce qui est suffisant pour la plupart des rapports/documentations de code.

Le texte ci-après est un exemple de ce que l'on peut écrire en markdown.

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

### Balise à connaître

Les principales fonctionnalités sont décrites dans [cette liste](https://www.markdownguide.org/cheat-sheet/#basic-syntax).

#### Sections

```text
# titre du document

## section

### sous-section

#### sous-sous-section
```

#### Paragraphes

Un saut de ligne est nécessaire pour commencer un nouveau paragraphe. Aller à la ligne sera équivalent à un espace.

#### Style inline

Dans le flot du texte, on peut mettre en exergue des parties de texte :

- *en italique* : `*texte*`{.language-}
- **en gras** : `**texte**`{.language-}
- ***en gras et en italique*** : `***texte***`{.language-}
- ~~barré~~ : `~~texte~~`{.language-}
- `code` : `` `texte` ``{.language-}
- équations : `$\LaTeX$`{.language-}

#### Style bloc

En markdown, un bloc commence et finit par une ligne vide.

Plusieurs symboles peuvent être utilisées :

- [code](https://www.markdownguide.org/extended-syntax/#fenced-code-blocks). Mettez le langage utilisé pour activer la coloration syntaxique (par défaut, je mets comme langage `python` lorsque j'écris un algorithme en python) :

    \`\`\`
    print("coucou !")
    \`\`\`

- [remarques](https://www.markdownguide.org/basic-syntax/#blockquotes-1) :

    \> Pierre qui roule n'amasse pas mousse.

- [latex](./#latex){.interne} :

    \\$\\$ \\\frac\{1\}\{2\} \\$\\$

#### Listes

Comme chaque bloc, les listes commencent et finissent toujours par une ligne vide. Il y a deux types de listes :

- [non ordonnées](https://www.markdownguide.org/basic-syntax/#unordered-lists). Chaque item peut commencer par un `*`, un `-` ou encore un `+`. Choisissez en un et tenez vous y dans tout le document :

    \- premier élément
    \- deuxième élément

- [ordonnées](https://www.markdownguide.org/basic-syntax/#ordered-lists)

    1. on met le bon numéro
    2. on met le bon numéro

### Liens

Il y a plusieurs possibilités :

- via un nom : `[nom](lien)`{.language-}. Par exemple `[LMGTFY](https://www.google.fr)`{.language-} qui se compile en : [LMGTFY](https://www.google.fr)
- lien direct : `<https://www.google.fr>`{.language-} qui se compile en : <https://www.google.fr>.

On utilise les liens pour les images, il suffit de rajouter un `!` avant. Par exemple `![ada lovelace](https://upload.wikimedia.org/wikipedia/commons/0/0f/Ada_lovelace.jpg)`{.language-} qui se compile en : ![ada lovelace](https://upload.wikimedia.org/wikipedia/commons/0/0f/Ada_lovelace.jpg)

## Tableaux

```text
| nom colonne 1 | nom colonne 2 | nom colonne 3 |
|---------------|---------------|---------------|
|   m (1, 1)    | m (1, 2)      | m (1, 3)      |
|   m (2, 1)    | m (2, 2)      | m (2, 3)      |
```

Qui se compile en :

| nom colonne 1 | nom colonne 2 | nom colonne 3 |
|---------------|---------------|---------------|
|   m (1, 1)    | m (1, 2)      | m (1, 3)      |
|   m (2, 1)    | m (2, 2)      | m (2, 3)      |

En markdown un tableau a forcément des noms de colonnes. Les deux premières lignes sont donc indispensables.

{% info %}
Il existe des extensions de markdown, comme [commonMark](https://spec.commonmark.org/) utilisé pour ce site. qui permettent de faire beaucoup plus de choses avec des tableaux.
{% endinfo %}

## Code

Il y a deux façon d'écrire du code en markdown :

- en mettant le caractère "\`" avant et après le code :``print("du code")``. Le code écrit de cette façon s'insère dans la phrase
- en mode bloc en commençant et en finissant le bloc par une ligne "\`\`\`".

En mode bloc, le texte suivant :

\`\`\`
for l in "MPCI":
    print("Donnez moi un :", l, "!")
\`\`\`

S'affiche :

```
for l in "MPCI":
    print("Donnez moi un :", l, "!")
```

On a l'habitude de préciser le langage de programmation utilisé. On écrira donc :

\`\`\`python
for l in "MPCI":
    print("Donnez moi un :", l, "!")
\`\`\`

Qui, selon le compilateur markdown utilisé, pourra être affiché/compilé avec la coloration syntaxique :

```python
for l in "MPCI":
    print("Donnez moi un :", l, "!")
```

Préférez toujours cette dernière façon d'écrire du code. C'est plus clair à la lecture et plus joli à la compilation

## Formules mathématiques

Lorsque l'on écrit des textes scientifiques, vient inévitablement la question de l'écriture des équations.

### <span id="latex"></span> Formules en Latex

Le langage [Latex](https://fr.wikipedia.org/wiki/LaTeX) permet d'écrire toutes les équations imaginable (et même plus) avec un petit langage que l'on peut utiliser directement dans un éditeur de texte (ceux qui ont déjà utilisé l'éditeur d'équation de Word savent que c'est l'enfer de devoir tout cliquer).

{% info %}
L'ancêtre de [Latex](https://fr.wikipedia.org/wiki/LaTeX) : [Tex](https://fr.wikipedia.org/wiki/TeX), a été créé par le célèbre informaticien [Donald Knuth](https://fr.wikipedia.org/wiki/Donald_Knuth) par ce qu'il n'existait rien sur ordinateur à l'époque pour écrire [ses livres](https://fr.wikipedia.org/wiki/The_Art_of_Computer_Programming) en respectant une typographie correcte.
{% endinfo %}

Une fois ce langage appris, il est étonnement clair, même non compilé en *jolies formules*. Avec un peut d'habitude, on voit bien que : `$$\cos x=\sum_{k=0}^{\infty}\frac{(-1)^k}{(2k)!}x^{2k}$$`{.language-} est égal à :

<div>
$$
\cos x=\sum_{k=0}^{\infty}\frac{(-1)^k}{(2k)!}x^{2k}
$$
</div>

Quelques aides :

- Un [résumé](http://tug.ctan.org/info/undergradmath/undergradmath.pdf) des possibilités
- un [tuto](https://www.science-emergence.com/Articles/Formules-math%C3%A9matiques-sous-LaTeX/) Latex contenant aussi des instructions pour les équations.

### Formules en markdown

On peut écrire en markdown les équations latex.

- pour une équation dans le texte, on dit *inline* on entoure notre équation  par des `$`{.language-}
- pour équation au milieu de la page, on dit *display*, on entoure notre équation par des `$$`{.language-} et on saute une ligne avant et après les `$$`{.language-}. comme dans l'exemple ci-après.

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

## Plugin Markdown vscode

{% aller %}
[Extensions Markdown pour vscode](/cours/coder-et-développer/éditeur-vscode/extensions/markdown){.interne}
{% endaller %}

## Pour aller plus loin

### Guides

- base markdown et latex : <https://ashki23.github.io/markdown-latex.html>
- base markdown : <https://www.markdownguide.org/> par exemple
- [Mathjax et latex](https://math.meta.stackexchange.com/questions/5020/mathjax-basic-tutorial-and-quick-reference)

### Variantes de markdown

Le format markdown est basique. Il possède plein de variantes qui permettent d'étendre ses possibilités. Deux d'entre elles sont devenus des standard de fait :

- [commonMark](https://spec.commonmark.org/) utilisé pour ce site.
- [github flavored markdown](https://guides.github.com/features/mastering-markdown/).
- [kramdown](https://kramdown.gettalong.org/documentation.html).
