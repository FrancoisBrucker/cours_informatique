---
layout: page
title:  ""
category: cours
tags: combat web
author: Baptiste Mahé
---
![Jekyll logo](../../assets/jekyll_logo.png)

## Qu'est-ce que c'est ?

[Jekyll](https://jekyllrb.com/) est un `générateur` de site statique à partir de languages qui ne sont pas lu par le navigateur (type Marckdown et Yaln). Jekyll un package [Ruby](https://www.ruby-lang.org/en/) et requiert le programme `gem` pour l'installation et `bundle` le gestionnaire de packages de Ruby.

## Ruby, Gem et Bundle (+ installation)

Ruby est un **langage de programmation** open-source dynamique qui met l'accent sur la simplicité et la productivité. Sa syntaxe élégante en facilite la lecture et l'écriture. [Example](https://www.includehelp.com/ruby/programs.aspx), Hello World en ruby :

~~~ ruby
=begin 
Ruby program to print Hello World.
=end

puts "Hello World!"
~~~

Output : `Hello World!`

Pour installer Ruby sur votre machine :

~~~ sh
sudo apt install ruby-full # pour Linux/WLS
sudo brew install ruby-full # pour MacOS
~~~

Les fichiers ruby sont en `.rb` et la commande pour les executer est : `ruby filename.rb`. Pour un tuto c'est [ici](https://www.youtube.com/watch?v=vgSQ97FDSvM&list=PLjwdMgw5TTLVVJHvstDYgqTCao-e-BgA8&ab_channel=Grafikart.fr)

En installant Ruby on installe aussi son **package manager** `gem` (comme `pip` pour Python). Gem sert à gérer (installer, supprimer, chercher, etc...) les packages Ruby.

Pour l'utiliser il est nécessaire d'avoir les programmes de compilation en C et C++, si vous ne les avez pas encore :

~~~ sh
sudo apt install make gcc g++ # pour Linux/WLS
sudo brew install make gcc g++ # pour MacOs
~~~

Pour installer des packages à l'aide de `gem` :

~~~ sh
sudo gem install package-name
~~~

Pour plus de documentation sur `gem` voir [ici.](https://guides.rubygems.org/rubygems-basics/)

Nous pouvons donc maintenant utiliser `gem` pour installer Jekyll et Blunder :

~~~ sh
sudo gem install bundler jekyll
~~~

Pour tester l'installation :

~~~ sh
jekyll -v
~~~

vous devriez obtenir quelque chose comme : `jekyll 4.X.X`

## Quelques fonctionalités

**Créer** un projet Jekyll :

~~~ sh
sudo jekyll new my-jekyll-site
~~~

Avec la commande `tree my-jekyll-site` on peut voir la **structure** d'un projet jekyll vierge

~~~ sh
my-jekyll-site
├── 404.html
├── about.markdown
├── _config.yml
├── Gemfile
├── Gemfile.lock
├── index.markdown
└── _posts
    └── 2020-09-24-welcome-to-jekyll.markdown
~~~

Démarrer un **server local** pour développer le projet Jeckyll

~~~ sh
cd my-jekyll-site
bundle exec jekyll serve
~~~

(executer cette commande dans le dossier cours_informatique/docs/ pour servir le site de M. Brucker)

Ensuite naviguer à l'adresse `http://127.0.0.1:4000` avec votre navigateur et votre site Jekyll devrait y être affiché. (rajouter `/cours_informatiques/` pour le site de M. Brucker)

Une fois l'application fini il faut la **compiler** en html pour qu'elle soit comprise par le navigateur en production :

~~~ sh
bundle exec jekyll build
~~~

Cette commande créer un dossier `_site` où le site compilé sera stocké.

## Le langage Markdown

Dans notre site Jekyll il va falloir "coder" en Markdown. Comme le HTML le Markdown et un langage de **balisage** qui se veut être facile à lire par les humains (mais du coup moins facile pour les navigateurs...).

C'est le langages de base des fichiers README sur GitHub. Les fichiers `.md` et `.markdown` sont les fichiers interprétés en Markdown.

Jekyll utilise un sous-type de Markdown, le **kramdown** de Github.

Une bonne overview de Markdown [ici.](https://guides.github.com/features/mastering-markdown/)

## La configuration

La configuration du projet est contenu dans le fichier YAML `_config.yml` généré automatiquement par la création du projet jekyll. YAML ou Yet Another Markup Language, est un format de représentation des données comme XML.

*TODO: finir explications configs*
