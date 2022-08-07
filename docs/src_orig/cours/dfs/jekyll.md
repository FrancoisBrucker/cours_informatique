---
layout: page
title:  ""
category: cours
tags: combat web
author: Baptiste Mahé
---
![Jekyll logo](../../assets/jekyll_logo.png)




## Qu'est-ce que c'est ?

[Jekyll](https://jekyllrb.com/) est un `générateur` de sites statiques à partir de languages qui ne sont pas lus par le navigateur (type Markdown et Yaln). Jekyll un package [Ruby](https://www.ruby-lang.org/en/) et requiert le programme `gem` pour l'installation et `bundle` le gestionnaire de packages de Ruby.

## Ruby, Gem et Bundle (+ installation)

> TBD : à mettre dans le tuto.
> * ajouter `gem "webrick"` dans *"Gemfile"* ce n'est plus dans bundle. 
> * ruby avec brew (sous mac) attention au path (quelque part dans *"/usr/local/opt/ruby/bin/rub"*)
{.attention}

Ruby est un **langage de programmation** open-source dynamique qui met l'accent sur la simplicité et la productivité. Sa syntaxe élégante en facilite la lecture et l'écriture. [Example](https://www.includehelp.com/ruby/programs.aspx), Hello World en ruby :

~~~ ruby
=begin
Ruby program to print Hello World.
=end

puts "Hello World!"
~~~

Output : `Hello World!`

Avant d'installer `ruby` il est nécessaire d'avoir les programmes de compilation en C et C++, si vous ne les avez pas encore :

~~~ sh
sudo apt install make gcc g++ # pour Linux/WLS
xcode-select --install # pour MacOS
~~~

On peut maintenant installer ruby :

~~~ sh
sudo apt install ruby-full # pour Linux/WLS
brew install ruby  # pour MacOS
~~~

Les fichiers ruby sont en `.rb` et la commande pour les executer est : `ruby filename.rb`. Pour un tuto c'est [ici](https://www.youtube.com/watch?v=vgSQ97FDSvM&list=PLjwdMgw5TTLVVJHvstDYgqTCao-e-BgA8&ab_channel=Grafikart.fr)

En installant Ruby on installe aussi son **package manager** `gem` (comme `pip` pour Python). Gem sert à gérer (installer, supprimer, chercher, etc...) les packages Ruby.

Pour installer des packages à l'aide de `gem` :

~~~ sh
sudo gem install package-name
~~~

Pour plus de documentation sur `gem` voir [ici.](https://guides.rubygems.org/rubygems-basics/)

Nous pouvons donc maintenant utiliser `gem` pour installer Jekyll et Bundler :

~~~ sh
sudo gem install bundler jekyll
~~~

Pour tester l'installation :

~~~ sh
jekyll -v
~~~

Vous devriez obtenir quelque chose comme : `jekyll 4.X.X`

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

(executer cette commande dans le dossier `cours_informatique/docs/` pour servir le site de M. Brucker)

Ensuite naviguer à l'adresse `http://127.0.0.1:4000` avec votre navigateur et votre site Jekyll devrait y être affiché. (rajouter `/cours_informatiques/` pour le site de M. Brucker)

Une fois l'application finie il faut la **compiler** en html pour qu'elle soit comprise par le navigateur en production :

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

La configuration du projet est contenue dans le fichier YAML `_config.yml` généré automatiquement par la création du projet jekyll. YAML ou Yet Another Markup Language, est un format de représentation des données comme XML.

A l'initialisation, le fichier `_config.yml` contient les informations suivnates :

~~~yml
title: Your awesome title
email: your-email@example.com
description: >- # this means to ignore newlines until "baseurl:"
  Write an awesome description for your new site here. You can edit this
  line in _config.yml. It will appear in your document head meta (for
  Google search results) and in your feed.xml site description.
baseurl: "" # the subpath of your site, e.g. /blog
url: "" # the base hostname & protocol for your site, e.g. http://example.com
twitter_username: jekyllrb
github_username:  jekyll

# Build settings
theme: minima
plugins:
  - jekyll-feed
~~~

`title` permet de modifier le titre affiché dans l'onglet du site.

`email` `description` `twitter_username` et `github_username` sont des donées que l'ont peut accéder dans toute l'application à travers les templates.

`theme` définit le thème Jekyll de l'application. [Tuto sur les thèmes Jekyll.](https://jekyllrb.com/docs/themes/)

`plugins` défnit les plugins Jekyll utilisés dans l'applications. [Tuto sur les plugins Jekyll.](https://jekyllrb.com/docs/plugins/)

`baseurl` et `url` permettent de gérer le rooting de l'application.
