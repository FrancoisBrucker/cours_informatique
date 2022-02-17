---
layout: page
title:  "Format markdown"
tags: langage markdown
---

Une introduction au format markdown.

<!--more-->

## Qu'est-ce ?

[Markdown](https://fr.wikipedia.org/wiki/Markdown) est un format de fichier texte, donc modifiable par tout éditeur de texte. L'extension de fichier est *".md"*.

L'intérêt de ce format de fichier texte est qu'il est parfaitement lisible dans tout éditeur de texte et qu'on peut de plus le *compiler* dans un autre format comme le pdf ou encore le html si on veut le partager.

> Par exemple, tout ce site a par exemple été écrit en markdown (plus précisément une extension de celui-ci nommé [kramdown](https://kramdown.gettalong.org/documentation.html)) puis transformé en html grâce à [jekyll](https://jekyllrb.com/). Le code source du site est [visible](https://github.com/FrancoisBrucker/cours_informatique), en particulier le code source de [ce fichier](https://github.com/FrancoisBrucker/cours_informatique/blob/master/docs/tutos/_posts/2021-08-30-format-markdown.md) (cliquez sur le bouton `raw` à droite, juste avant que le fichier ne soit représenté).

## syntaxe

Markdown permet facilement de représenter des titres, des listes, mettre des choses en exergue, ..., uniquement avec du texte. Ce format est à la base un guide de lecture de fichiers textes.

Par exemple, `*coucou*` signifie que `coucou` est en exergue (ce qui sera traduit par une police en italique à l'exportation en html ou pdf par exemple), ou encore `**salut !**` signifie que `salut !` est important (et sera traduit par une police en gras à l'exportation en html ou pdf).

> Pour une introduction et une liste des possibilités offertes, vous pouvez consulter le site : <https://www.markdownguide.org/> par exemple
{: .note}

Le format markdown est basique. Il possède plein de variantes qui permettent d'étendre ses possibilités. Deux d'entre elles sont devenus des standard de fait :

* [github flavored markdown](https://guides.github.com/features/mastering-markdown/).
* [kramdown](https://kramdown.gettalong.org/documentation.html).

> Vous pouvez écrire du markdown dans le format github ou kramdown. Les principales fonctionnalités sont décrites dans [ce site](https://www.markdownguide.org/cheat-sheet/)
{: .note}

## markdown avec vscode

L'éditeur de texte [vscode]({% link _tutoriels/editeur/vsc/2021-09-03-vsc-installation-et-prise-en-main.md %}) permet d'écrire et d'exporter facilement du markdown. Sa documentation comporte une [partie consacrée au markdown](https://code.visualstudio.com/docs/languages/markdown). Nous allons utiliser deux extensions :

* [Markdown All in One](https://marketplace.visualstudio.com/items?itemName=yzhang.markdown-all-in-one) qui permet de fluidifier l'écriture de markdown et permet un export de celui-ci en html.
* [markdownlint](https://marketplace.visualstudio.com/items?itemName=DavidAnson.vscode-markdownlint) qui souligne en orange les fautes de style (un espace après un `.` par exemple) et les erreurs de markdown (sauf dans la hiérarchie des paragraphes par exemple).

> Le seconde extension est un [linter](https://mindsers.blog/fr/post/linting-good-practices/), qui incite à utiliser les bonnes pratiques d'écriture. Il en existe pour quasi tous les langages.

## Formules mathématiques

Lorsque l'on écrit des textes scientifique, vient inévitablement la question de l'écriture des équations.

### latex

Le langage [Latex](https://fr.wikipedia.org/wiki/LaTeX) permet d'écrire toutes les équations imaginable (et même plus) avec un petit langage que l'on peut utiliser directement dans un éditeur de texte (ceux qui ont déjà utilisé l'éditeur d'équation de Word savent que c'est l'enfer de devoir tout cliquer).

>L'ancêtre de [Latex](https://fr.wikipedia.org/wiki/LaTeX) : [Tex](https://fr.wikipedia.org/wiki/TeX), a été créé par le célèbre informaticien [Donald Knuth](https://fr.wikipedia.org/wiki/Donald_Knuth) par ce qu'il n'existait rien sur ordinateur à l'époque pour écrire [ses livres](https://fr.wikipedia.org/wiki/The_Art_of_Computer_Programming) en respectant une typographie correcte.

Une fois ce langage appris, il est étonnement clair, même non compilé en *jolies formules*. Avec un peut d'habitude, on voit bien que : `$$\cos x=\sum_{k=0}^{\infty}\frac{(-1)^k}{(2k)!}x^{2k}$$` est égal à :

$$\cos x=\sum_{k=0}^{\infty}\frac{(-1)^k}{(2k)!}x^{2k}$$

Quelques aides :

* Un [résumé](http://tug.ctan.org/info/undergradmath/undergradmath.pdf) des possibibités
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

$$3+2$$

```

Lorsque vous faites de l'exportation en html, les mathématiques sont représentées en utilisant [Mathjax](https://www.mathjax.org/). Ce [post](https://math.meta.stackexchange.com/questions/5020/mathjax-basic-tutorial-and-quick-reference) résume les possibilités basique de mathjax pour écrire des équations.

>Il ne faut pas mettre d'espace après le premier `$` et avant le dernier `$` lorsque l'on écrit des équations, sinon les convertisseur ne reconnaitront pas que ce sont des équations que vous voulez écrire. Ansi `$ \frac{1}{2}$` affichera `$ \frac{1}{2}$`, alors que `$\frac{1}{2}$` affichera $\frac{1}{2}$.
{: .attention}

## export

Si le markdown est pratique pour être écrit et lu rapidement, pour de long documents ou le partage de ceux-ci, il est important de les exporter dans un format plus :

* imprimable comme le pdf ou l'html
* modifiable comme un docx ou un fichier latex
* un autre format que l'on aime.

### avec vscode

Pour exporter le markdown dans quelque chose de plus joli avec vscode, on peut utiliser la [palette de commande]({% link _tutoriels/editeur/vsc/2021-09-03-vsc-installation-et-prise-en-main.md %}#palette-de-commande) pour exécuter la commande : *markdown All in One: Print current document to HTML* : qui va rendre un fichier html.

Cela suffit pour la majorité des cas.

### utilitaire pandoc

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
