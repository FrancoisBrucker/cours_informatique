---
layout: page
title:  "Format markdown"
categories: langage markdown
tags: informatique cours 
---

Une introduction au format markdown. C'est le langage que nous utiliserons majoritairement pour écrire les cours.

<!--more-->

## Qu'est-ce ?

[Markdown](https://fr.wikipedia.org/wiki/Markdown) est un format de fichier texte, donc modifiable par tout éditeur de texte. L'extension de fichier est *".md"*.

Il est facilement lisible dans un éditeur de texte, et il existe de nombreuses façon de l'exporter que ce soit en html (pour l'ouvrir avec un navigateur comme chrome ou firefox) ou en pdf.

> Tout ce site a par exemple été écrit en markdown (plus précisément une extension de celui-ci nommé [kramdown](https://kramdown.gettalong.org/documentation.html)) puis transformé en html grâce à [jekyll](https://jekyllrb.com/). Le code source du site est [visible](https://github.com/FrancoisBrucker/cours_informatique), en particulier le code source de [ce fichier](https://github.com/FrancoisBrucker/cours_informatique/blob/master/docs/tutos/_posts/2021-08-30-format-markdown.md) (cliquez sur le bouton `raw` à droite, juste avant que le fichier ne soit représenté).

## syntaxe

Markdown permet facilement d'écrire des titres, des liste, mettre des choses en exergue, etc.

> Pour une introduction et une liste des possibilités offertes, n'hésitez pas à consulter le site : <https://www.markdownguide.org/>

Le format markdown est basique. Il possède plein de variantes qui permettent d'étendre ses fonctionnalités. Les principales variantes utilisées sont :

* celle de [github](https://guides.github.com/features/mastering-markdown/).
* le [kramdown](https://kramdown.gettalong.org/documentation.html).

## markdown avec vscode

Suivez [ce tutoriel]({% post_url tutos/editeur/vsc/2021-09-14-vsc-markdown %}) pour installer les packages indispensables pour faire du markdown avec [vscode]({% post_url tutos/editeur/vsc/2021-09-03-vsc-installation-et-prise-en-main %}).

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

>Il ne faut pas mettre d'espace après le premier `$` et avant le dernier `$` sinon, pandoc ne reconnaîtra pas que ce sont des équations que vous voulez écrire. Ansi `$ \frac{1}{2}$` affichera `$ \frac{1}{2}$`, alors que `$\frac{1}{2}$` affichera $\frac{1}{2}$.
{: .attention}

## export

Si le markdown est pratique pour être écrit et lu rapidement, pour de long documents ou le partage de ceux-ci, il est important de les exporter dans un format plus :

* imprimable comme le pdf ou l'html
* modifiable comme un docx ou un fichier latex
* un autre format que l'on aime.

### export simple

Avec les extension que l'on a installé, il est déjà possible d'exporter le markdown en html, puis — via un navigateur — de l'exporter en pdf. Voir partie [preview du tutoriel]({% post_url tutos/editeur/vsc/2021-09-14-vsc-markdown %}#export-et-preview) pour l'éditeur vscode.

Cela suffit pour la majorité des cas.

### utilitaire pandoc

Si l'on veut exporter dans des formats plus exotiques ou encore finement contrôler le résultat de l'export, on peut utiliser le logiciel  [pandoc](https://pandoc.org/).

[pandoc](https://pandoc.org/) est un monstre. Il permet (parfois avec un peu d'huile de coude il est vrai) de convertir à peut prêt tout document en un autre format (voir les [démos](https://pandoc.org/demos.html) pour différentes conversions).

#### Installation de pandoc

D'après la [doc](https://pandoc.org/installing.html), selon le système d'exploitation :

{% details sous linux %}
`sudo apt install pandoc` dans un [terminal]({% post_url /tutos/systeme/2021-08-24-terminal %})
{% enddetails %}

{% details sous mac %}
installez [brew](https://brew.sh/) puis `brew install pandoc` dans un [terminal]({% post_url /tutos/systeme/2021-08-24-terminal %})
{% enddetails %}

{% details sous windows %}
installez [Chocolatly](https://chocolatey.org/) puis `choco install pandoc` dans un [terminal]({% post_url /tutos/systeme/2021-08-24-terminal %})
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

## misc

Quelques liens potentiellement intéressant :

* pimp my markdown dans vsc : <https://medium.com/@pierrepaci/enhance-your-markdown-experience-using-vscode-3caf489888b8>
* pimp my pandoc : <https://learnbyexample.github.io/customizing-pandoc/>
