---
layout: page
title:  "Format markdown"
tags: langage markdown
---

Une introduction au format markdown.

<!--more-->

> [Format Markdown]({% link _tutoriels/format-markdown.md %})
>
> Prérequis :
>
> * [vscode]({% link _tutoriels/editeur/vsc/vsc-installation-et-prise-en-main.md %})
>
{: .chemin}

## Qu'est-ce ?

> [Markdown](https://fr.wikipedia.org/wiki/Markdown) est un format de fichier texte, donc modifiable par tout éditeur de texte. L'extension de fichier est *".md"*.
{: .note}

L'intérêt de ce format de fichier texte est qu'il est parfaitement lisible dans tout éditeur de texte et qu'on peut de plus le *compiler* dans un autre format comme le pdf ou encore le html si on veut le partager.

> Tout ce site par exemple été écrit en markdown avant d'être compilé en html. Le code source est [visible](https://github.com/FrancoisBrucker/cours_informatique), en particulier celui de [ce fichier](https://github.com/FrancoisBrucker/cours_informatique/blob/master/docs/_tutoriels/format-markdown.md) (cliquez sur le bouton `raw` à droite, juste avant que le fichier ne soit représenté).

### plugins vscode

L'éditeur de texte [vscode](https://code.visualstudio.com/) permet d'écrire et d'exporter facilement du markdown. Sa documentation comporte une [partie consacrée au markdown](https://code.visualstudio.com/docs/languages/markdown). Nous allons utiliser deux extensions :

* [Markdown All in One](https://marketplace.visualstudio.com/items?itemName=yzhang.markdown-all-in-one) qui permet de fluidifier l'écriture de markdown et permet un export de celui-ci en html.
* [markdownlint](https://marketplace.visualstudio.com/items?itemName=DavidAnson.vscode-markdownlint), un [linter](https://mindsers.blog/fr/post/linting-good-practices/) qui souligne en jaune les fautes de style de markdown (saus dans la hiérarchie des sections par exemple) pour que vous puissiez les corriger et écrire parfaitement du markdown

> Installez les deux plugins ci-dessus dans votre vscode.
{: .a-faire}

### export en html

Si le markdown est pratique pour être écrit et lu rapidement, pour de long documents ou le partage de ceux-ci, il est important de les exporter dans un format comme le html.

Avec le plugin *Markdown All in One* de vscode, il suffit de taper la commande :

```text
markdown All in One: Print current document to HTML
```

dans la [palette de commande]({% link _tutoriels/editeur/vsc/vsc-installation-et-prise-en-main.md %}#palette-de-commande) (que l'on peut copier/coller). Ceci va créer un fichier html contenant votre code markdown *compilé*.

## syntaxe

Le markdown est un format très simple. Il permet de structurer minimalement un texte, ce qui est suffisant pour la plupart des rapports/documentations de code.

### un exemple

> Dans vscode, créez un nouveau fichier que vous appellerez *"exemple.md"* (*".md"* est l'extension par défaut des fichiers markdown).
>
> Copiez/collez-y- le texte ci-dessous et sauvez le fichier.
{: .a-faire}

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

Vous voyez que ce format est *lisible* directement dans vscode (on comprend qu'un titre est un titre par exemple). Mais o  peut aussi *compiler* ce fichier texte en html.

> Dans vscode, en ayant comme onglet actif celui contenant le fichier *"exemple.md"*, ouvrez la [palette de commande]({% link _tutoriels/editeur/vsc/vsc-installation-et-prise-en-main.md %}#palette-de-commande) et taper la commande `markdown All in One: Print current document to HTML`.
>
> **Attention** : une commande dans la palette commence toujours par `>` qui doit être le 1er caractère.
>
{: .a-faire}

Vous devez avoir crée un fichier *"exemple.html"* dans le même dossier que votre fichier *"exemple.md"*.

> Ouvrez le fichier *"exemple.html"* dans votre navigateur favori pour voir le résultat.
{: .a-fair}

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
* ~~barré~~ : `~~texte~~`
* `code` : `` `texte` ``
* équations : \$latex\$

#### style bloc

En markdown, un bloc commence et fini par une ligne vide.

Plusieurs symboles peuvent être utilisées :

* [code](https://www.markdownguide.org/extended-syntax/#fenced-code-blocks). Mettez le langage utilisé pour pour activer la coloration syntaxique (par défaut, je mets comme langage `text` lorsque j'écris un algorithme en pseudo-code)
* [remarques](https://www.markdownguide.org/basic-syntax/#blockquotes-1)
* [latex](#latex)

#### listes

Comme chaque bloc, les listes commencent et frinissent toujours par une ligne vide. Il y a deux types de listes :

* [non ordonnées](https://www.markdownguide.org/basic-syntax/#unordered-lists). Chaque item peut comencer par un `-`, un `*` ou encore un `+`. Choisissez en un et tenez vous y dans tout le document.
* [ordonnées](https://www.markdownguide.org/basic-syntax/#ordered-lists)

## Formules mathématiques

Lorsque l'on écrit des textes scientifique, vient inévitablement la question de l'écriture des équations.

### latex {#latex}

Le langage [Latex](https://fr.wikipedia.org/wiki/LaTeX) permet d'écrire toutes les équations imaginable (et même plus) avec un petit langage que l'on peut utiliser directement dans un éditeur de texte (ceux qui ont déjà utilisé l'éditeur d'équation de Word savent que c'est l'enfer de devoir tout cliquer).

>L'ancêtre de [Latex](https://fr.wikipedia.org/wiki/LaTeX) : [Tex](https://fr.wikipedia.org/wiki/TeX), a été créé par le célèbre informaticien [Donald Knuth](https://fr.wikipedia.org/wiki/Donald_Knuth) par ce qu'il n'existait rien sur ordinateur à l'époque pour écrire [ses livres](https://fr.wikipedia.org/wiki/The_Art_of_Computer_Programming) en respectant une typographie correcte.

Une fois ce langage appris, il est étonnement clair, même non compilé en *jolies formules*. Avec un peut d'habitude, on voit bien que : `$$\cos x=\sum_{k=0}^{\infty}\frac{(-1)^k}{(2k)!}x^{2k}$$` est égal à :

$$\cos x=\sum_{k=0}^{\infty}\frac{(-1)^k}{(2k)!}x^{2k}$$

Quelques aides :

* Un [résumé](http://tug.ctan.org/info/undergradmath/undergradmath.pdf) des possibilités
* un [tuto](https://www.science-emergence.com/Articles/Formules-math%C3%A9matiques-sous-LaTeX/) Latex contenant aussi des instructions pour les équations.

### en markdown

On peut écrire en markdown les équation latex.

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
{: .attention}

## pour aller plus loin

### guides

* base markdown et latex : <https://ashki23.github.io/markdown-latex.html>
* base markdwon : <https://www.markdownguide.org/> par exemple
* [Mathjax et latex](https://math.meta.stackexchange.com/questions/5020/mathjax-basic-tutorial-and-quick-reference)

### variantes de markdown

Le format markdown est basique. Il possède plein de variantes qui permettent d'étendre ses possibilités. Deux d'entre elles sont devenus des standard de fait :

* [github flavored markdown](https://guides.github.com/features/mastering-markdown/).
* [kramdown](https://kramdown.gettalong.org/documentation.html).

### export avec l'utilitaire pandoc

Si l'on veut exporter dans des formats plus exotiques ou encore finement contrôler le résultat de l'export, on peut utiliser le logiciel  [pandoc](https://pandoc.org/).

[pandoc](https://pandoc.org/) est un monstre. Il permet (parfois avec un peu d'huile de coude il est vrai) de convertir à peut prêt tout document en un autre format (voir les [démos](https://pandoc.org/demos.html) pour différentes conversions).

#### Installation de pandoc

D'après la [doc](https://pandoc.org/installing.html), selon le système d'exploitation :

{% details sous linux %}
`sudo apt install pandoc` dans un [terminal]({% link _tutoriels/systeme/2021-08-24-terminal.md %})
{% enddetails %}

{% details sous mac %}
installez [brew](https://brew.sh/) puis `brew install pandoc` dans un [terminal]({% link _tutoriels/systeme/2021-08-24-terminal.md %})
{% enddetails %}

{% details sous windows %}
installez [Chocolatly](https://chocolatey.org/) puis `choco install pandoc` dans un [terminal]({% link _tutoriels/systeme/2021-08-24-terminal.md %})
{% enddetails %}

Selon le format d'export, il vous faudra d'autres logiciels. Je vous conseille d'ores et déjà d'[installer latex](https://www.latex-project.org/get/) pour pouvoir facilement exporter en pdf sans passer par html et un navigateur.

#### exemple d'utilisation : en html

Pour l'export en html, j'utilise la commande suivante qui m'écrit de jolies équations avec <https://www.mathjax.org/> : `pandoc --mathjax --standalone --metadata pagetitle="titre page" --metadata charset="UTF-8"  page.md -o page.html`

* premier élément : le nom de la commande, ici `pandoc`.
* cette commande prend en entrée le fichier `page.md` qui est le dernier élément de la ligne
* les autres éléments de la lignes sont des [arguments](https://fr.wikipedia.org/wiki/Commandes_Unix#Le_passage_d'arguments_aux_commandes). Dans le monde des commandes, il y a deux types de paramètres "un `-` suivit d'une lettre" et "deux `--` suivi d'un mot" Ces paramètre peuvent être suivi d'arguments, c'est à dire des mots ne commençant pas par un `-` (`-o page.html`), ou pas (`--mathjax`) Notre commande a 4 paramètres :
  * `-o page.html`. *Un paramètre avec un argument*. Le fichier se sorti s'appellera `page.html`. Il determine le type de sortie (ici de l'html) et sera dans le même dossier que le fichier `page.md`
  * `--mathjax`. *Un paramètre sans argument*. On utilise la bibliothèque mathjax pour *compiler* les équations latex
  * `--standalone`. *Un paramètre sans argument*. On crée un fichier html complet (par défaut, `pandoc` ne crée qu'un bout de html qui peut être combiner avec d'autres bout)
  * `--metadata pagetitle="titre page"`. *Un paramètre avec un argument*. En combinaison avec le paramètre `standalone`. Permet de donner un titre à la page html, ici "titre page".
  * `--metadata charset="UTF-8"`. *Un paramètre avec un argument*. Permet de spécifier l'encodage des caractères (voir cours sur les fichiers). Devrait permettre de voir les accents.

>Si vous avez à compiler plein de fois votre page, n'oubliez pas qu'utiliser la *flèche du haut* dans un terminal rappelle la dernière commande utilisée. Donc même une commande avec plein de paramètres est facile à réutiliser. Il suffit d'appuyer sur la flèche du haut.

Lorsque je fais mes tests en html, après chaque re-compilation je recharge la page avec *"F5"* ou *"ctrl+R"* dans le navigateur. Le process est **très rapide**.
