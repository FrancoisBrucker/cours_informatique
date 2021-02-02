---
layout: page
title:  "Format markdown"
category: cours
tags: informatique cours 
---


## Qu'est-ce ?

[Markdown](https://fr.wikipedia.org/wiki/Markdown) est un format de fichier texte, donc éditable par tout éditeur de texte. L'extension de fichier est *".md"*.

Il est facilement lisible das un éditeur de texte, et il existe de nombreuses façon de l'exporter que ce soit en html (pour l'ouvrir avec un navigateur comme chrome ou firefox) ou en pdf.

> Tout ce site a par exemple été écrit en markdown puis transformé en html grace à [jekyll](https://jekyllrb.com/). Le code source du site est [visible](https://github.com/FrancoisBrucker/cours_informatique), en particulier le code source de [ce fichier](https://github.com/FrancoisBrucker/[cours_informatique.md](https://github.com/FrancoisBrucker/cours_informatique/blob/master/docs/cours/tuto/format_markdown.md)) (cliquez sur le bouton `raw` à droite, juste avant que le fichier ne soit représenté).

## syntaxe

Markdown permet facilement d'écrire des titres, des liste, mettre des choses en exergue, etc.

* [Une liste de ces possibilités](https://guides.github.com/features/mastering-markdown/).
* une [cheat sheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)
* [Une introduction en français](https://docs.zettlr.com/fr/reference/markdown-basics/)

> **Attention** : le format markdown possède plein de variantes. Une variante populaire est celle de github, mais sachez qu'il en existe de nombreuses, chacune apportant ses spécificités.

## markdown avec vscode

<https://code.visualstudio.com/docs/languages/markdown>

### extensions

On peut ajouter des extensions pour faciliter l'écriture en markdown :

* [Markdown All in One](https://github.com/yzhang-gh/vscode-markdown). Dans les préférences du module, on décoche *Markdown > Extenstion > Math:Enabled*. Les maths seront en effet utilisées avec le module suivant
* [markdownlint](https://learnbyexample.github.io/customizing-pandoc/) un linter pour écrire du joli markdown.
* [Markdown+Math](https://github.com/goessner/mdmath) pour gérer les formules mathématiques comme :
  * $\frac{1}{2}$
  * $$ \sum_{i=1}^n i^2$$
* [Markdown Preview Enhanced](https://shd101wyy.github.io/markdown-preview-enhanced/#/). Permet d'avoir des feuilles de styles jolies lorsque l'on converti du markdown.

### export et preview

Pour exporter le markdwon dans quelque chose de plus joli :

* pour compiler : *ctrl/cmd + shift + p : markdown All in One: Print current document to HTML*
* pour faire une preview : *ctrl/cmd + shift + p : markdown: Open preview* Mais cela n'utilise pas l'extension Markdown Preview Enhanced, c'est donc plus limité comme rendu.

## Formules mathématiques

Lorsque l'on écrit des textes scientifique, vient inévitablement la question de l'écriture des équations. Le langage [Latex](https://fr.wikipedia.org/wiki/LaTeX) permet d'écrire toutes les équations imaginable (et même plus) avec un petit langage que l'on peut utiliser directement dans un éditeur de texte (ceux qui ont déjà utilisé l'éditeur d'équation de Word savent que c'est l'enfer de devoir tout cliquer). Une fois ce langage appris, il est étonnement clair, même non compilé en *jolies formules*. Avec un peut d'habitude, on voit bien que : `$$\cos x=\sum_{k=0}^{\infty}\frac{(-1)^k}{(2k)!}x^{2k}$$` est égal à :

$$\cos x=\sum_{k=0}^{\infty}\frac{(-1)^k}{(2k)!}x^{2k}$$

En markdown, on ne peut pas écrire tout en Latex (autant utiliser latex dans ce cas...) seulement ses équations, c'est à dire des mathématiques écrites entre `$` (pour une équation dans le flux du texte) ou `$$` (pour une équation avec un saut de ligne avant et après celle-ci).

Quelques aides :

* Un [résumé](http://tug.ctan.org/info/undergradmath/undergradmath.pdf) des possibibités
* un [tuto](https://www.science-emergence.com/Articles/Formules-math%C3%A9matiques-sous-LaTeX/) Latex contenant aussi des instructions pour les équations.

**Remarques** :

* Pour le markdown, il faudra  utiliser  `$$`et `$` (les notation Tex) plutôt que `\[` et  `\(` (notations latex).
* Lorsque vous faites de l'exportation en html, les mathématiques sont représentées en utilisant [Mathjax](https://www.mathjax.org/) (voir [une aide](ttps://math.meta.stackexchange.com/questions/5020/mathjax-basic-tutorial-and-quick-reference) de mathjax)
* L'ancêtre de [Latex](https://fr.wikipedia.org/wiki/LaTeX) : [Tex](https://fr.wikipedia.org/wiki/TeX), a été créé par le célébrissime informaticien [Donald Knuth](https://fr.wikipedia.org/wiki/Donald_Knuth) par ce qu'il n'existait rien sur ordinateur à l'époque pour écrire [ses livres](https://fr.wikipedia.org/wiki/The_Art_of_Computer_Programming) en respectant une typographie correcte.

>**Attention**, il ne faut pas mettre d'espace après le premier `$` et avant le dernier `$` sinon, pandoc ne reconnaîtra pas que ce sont des équations que vous voulez écrire. Ansi `$ \frac{1}{2}$` affichera `$ \frac{1}{2}$`, alors que `$\frac{1}{2}$` affichera $\frac{1}{2}$.

## export

Si le markdown est pratique pour être écrit et lu rapidement, pour de long documents ou le partage de ceux-ci, il est important de les exporter dans un format plus :

* imprimable comme le pdf ou l'html
* modifiable comme un docx ou un fichier latex
* un autre format que l'on aime.

### export simple

Avec les extension que l'on a installé, il est déjà possible d'exporter le markdown en html, puis — via un navigateur — de l'exporter en pdf. Voir partie [export et preview](#export-et-preview).

Cela suffit pour la majorité des cas. Si l'on veut exporter dans des formats plus exotique ou encore finement contrôler le résultat de l'export, il faut utiliser des logiciel plus complexe, comme [pandoc](https://pandoc.org/) dont le boulot est de convertir à peut prêt n'importe quel format en un (quelconque) autre  format.

### utilitaire pandoc

[pandoc](https://pandoc.org/) est un monstre. Il permet (parfois avec un peu d'huile de coude il est vrai) de convertir à peut prêt tout document en un autre format (voir les [démos](https://pandoc.org/demos.html) pour différentes conversions).

#### Installation de pandoc

D'après la [doc](https://pandoc.org/installing.html), selon le système d'exploitation :

* Linux : `sudo apt install pandoc` dans un terminal
* Mac : installez [brew](https://brew.sh/) puis `brew install pandoc`
* Windows : installez [Chocolatly](https://chocolatey.org/) puis `choco install pandoc`

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

>**Remarque** : Si vous avez à compiler plein de fois votre page, n'oubliez pas qu'utiliser la *flèche du haut* dans un terminal rappelle la dernière commande utilisée. Donc même une commande avec plein de paramètres est facile à réutiliser. Il suffit d'appuyer sur la flèche du haut.

Lorsque je fais mes tests en html, après chaque re-compilation je recharge la page avec *"F5"* ou *"ctrl+R"* dans le navigateur. Le process est **très rapide**.

### pimp my markdown

TBD : mais ça à l'air fascinant

<https://medium.com/@pierrepaci/enhance-your-markdown-experience-using-vscode-3caf489888b8>

<https://learnbyexample.github.io/customizing-pandoc/>
