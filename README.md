# Les cours d'informatique de l'ecm


On devrait voir ici  différents cours de 1A, 2Ai MIE et 3A en informatique.

https://francoisbrucker.github.io/cours_informatique/index.html

# Contribuer

Le site est généré en utilisant [jekyll]( https://jekyllrb.com) qui est un générateur de site statique.

## jekyll

[Jekyll]( https://jekyllrb.com) agglomère des pages pouvant être écrite en différents langages (html, markdown, etc) en un site web cohérent.

### fonctionnement général


Nous utiliserons le langage [markdown](https://fr.wikipedia.org/wiki/Markdown) comme langage d'écriture de nos page (ou plutôt une variante de celui-ci appelé [kramdown](https://kramdown.gettalong.org/index.html) mais les différences sont minimes) qui a l'intérêt d'être compréhensible dans son format texte et facilement *compilable* en html, pdf, ou autre. Le markdown (ou ses multiples variante) est un format d'écriture très utilisé en développement.

Ces pages sont ensuite *compilée* en html par jekyll en utilisant des templates, ce qui permet de garder une unité au site.

Ces fichiers compilées forment un site qui peut ensuite être placé sur n'importe quel serveur admettant des site statique (par défaut, le site compilé est placé dans le dossier build).

### installation

>On suit les [instrutions](https://jekyllrb.com/docs/).

Comme on le voit, il y a des [prés-requis](https://jekyllrb.com/docs/installation/#requirements), en particulier [ruby](https://www.ruby-lang.org/en/) qui est le langage dans le lequel jekyll est écrit (jekyll a été écrit par un des développeur de github célèbre site lui aussi écrit en [ruby on  rails](https://rubyonrails.org/) et [erlang](https://en.wikipedia.org/wiki/Erlang_(programming_language))).

Commencez donc par installer ruby.

> **Nota Bene :** Sous mac avec Brew, il faudra rajouter le chemin de ruby de brew dans le
> PATH pour ne plus utiliser le ruby de mac.

#### ruby et ses gems

En ruby, une bibliothèque est appelée [gem](https://guides.rubygems.org/what-is-a-gem/) et s'installe via la commande `gem`.


Pour savoir est la gemme liée à Jekyll, on peut taper la commande : `gem info jekyll`. 
Qui donne chez moi :

~~~ shell
jekyll (4.1.1)
    Authors: Tom Preston-Werner, Parker Moore, Matt Rogers
    Homepage: https://jekyllrb.com
    License: MIT
    Installed at: /usr/local/lib/ruby/gems/2.7.0

    A simple, blog aware, static site generator.
~~~


> **Nota Bene : ** Sous mac avec [[https://brew.sh/][brew]], les *gems* ne sont pas
> automatiquement mis dans un endroit exécutable. Il faut rajouter le chemin dans le path. 
> Chez moi, ça donne (en utilisant le chemin de la gem liée à Jekyll) à la fin de mon `.zshrc` (ou `.bashrc` si vous êtes avec bash ) : `export PATH="/usr/local/opt/ruby/bin:/usr/local/lib/ruby/gems/2.7.0/bin:$PATH"`

#### bundler

On va gérer toutes ces gems avec [[bundler](https://bundler.io/) qui est l'équivalent de `npm`/`yarn` pour ruby. On va l'installer avec la commande `gem` : `gem install bundler`

### Initialiser un nouveau site avec Jekyll


On se place à la racine du site et on initialise bundle :

~~~ shell 
bundle init
~~~

Cette commande va créer un fichier `Gemfile` qui va contenir les différents package que l'on veut installer. Nous on aura besoin de jekyll :

~~~ shell 
bundle add jekyll
~~~

Cela va ajouter la dépendance de jekyll au fichier `Gemfile` et créer un fichier [[`Gemfile.lock`](https://bundler.io/rationale.html#checking-your-code-into-version-control).

On peut maintenant créer un site jekyll vide qui va contenir tous les fichiers sources nécessaires à la création du site. On utilisera la commande bundle et son action exec pour exécuter une gem, ici jekyll :

~~~ shell
bundle exec jekyll new docs
~~~

La commande précédante a créé un template de site dans le dossier `docs`. Ce dossier va contenir plein de fichiers. Chez moi la commande `tree docs` donne : 

~~~ shell
docs
├── 404.html
├── Gemfile
├── Gemfile.lock
├── _config.yml
├── _posts
│   └── 2020-08-28-welcome-to-jekyll.markdown
├── _site
│   ├── 404.html
│   ├── about
│   │   └── index.html
│   ├── assets
│   │   ├── main.css
│   │   ├── main.css.map
│   │   └── minima-social-icons.svg
│   ├── feed.xml
│   ├── index.html
│   └── jekyll
│       └── update
│           └── 2020
│               └── 08
│                   └── 28
│                       └── welcome-to-jekyll.html
├── about.markdown
└── index.markdown

9 directories, 15 files
~~~

### voir et/ou compiler son site

Si l'on veut juste voir son et qu'il se mette à jour à chaque modification, on utilise le mode *preview* de jekyll qui crée un serveur web temporaire qui compile à la volée vos fichiers et les montre en local sur le port 4000 par défaut (http://127.0.0.1:4000) :

~~~ shell
cd docs
bundle exec jekyll serve
~~~

Si l'on veut compiler son site et obtenir le site statique complet dans le dossier `_site` vous pouvez taper la commande : 


~~~ shell
cd docs
bundle exec jekyll build
~~~

### Combiner la création d'un site avec github

Ce n'est pas une manipulation basique, et qui n'est utile que si l'on veut déployer son site jekyll sur github en n'utilisant pas les moyens mis directement à disposition par github. Les instruction sont disponible [là]( https://docs.github.com/en/github/working-with-github-pages/setting-up-a-github-pages-site-with-jekyll)


## Organisation des pages

### projet

Le projet contient deux dossiers :

  - dossier : `docs` : contient les fichiers sources du site
  - dossier `resources` : les ressources brutes comme les images non redimensionnées, les fichiers de tests, etc.


### site
 
Le site (dans le dossier `docs`) contient 3 collections : *_1A*, *_2A* et *_3A* dont les fichiers sont automatiquement ajoutés au site. Ces collections correspondent aux déroulé du cours et des UEes, et inclut les *vrais* cours qui sont eux dans le dossier *cours*. 

Le dossier *assets* contient les images, et autres pdf nécessaire aux pages générales. Chaque cours contient ses propres assets.
