---
layout: page
title:  "git et github"
category: tutorial
tags: dev git 
---

# But

Base de l'utilisation de git et de github comme *origin*.

Git est le logiciel de [gestion de versions](https://fr.wikipedia.org/wiki/Gestion_de_versions) actuel et [github)[https://github.com/] un moyen pratique de stocker et diffuser ses projets en utilisant git.

On va vous montrer ici comment utiliser les deux de concert. 

Ce n'est pas un cours avancé de git/github, mais il devrait vous permettre de vous en sortir et d'utiliser correctement ces deux outils complémentaires.

  - gestion de l'origin comme source. Dire que c'est une convention
  - origin -> changement dans la config.
  - rebase on pull
  - revenir à une version précédente
  - dire que l'on commite souvent et une fois par jour à l'origin
  -github organisation ?
  - TBD élèves : 
    - un récap des commandes et ajout de trucs qu'ils connaissent.
    - un lien vers le projet fini ?
  
  

# initialisation 

Commencer par installer `git` si ce n'est pas encore fait et créez vous un compte sur [github](https://github.com/). Ce compte github sera utilisé pour tout le cours et vous pourrez  placer vos projet personnels montrable à vos futurs employeurs. Donc utilisez une adresse mail de contact ainsi qu'une photo de profil et un nom présentable. 

## Configuration minimale git

Vous allez travailler sur vos projets git à plusieurs. Il faut pouvoir à tout moment savoir qui a fait quoi sur le projet. Il est donc impératif que vos données personnelles soient à jour.

Renseigner ces infos de façon globale pour tout projet (vous pourrez changer ces infos pour chaque projet, mais mettez des infos corrects par défaut) :

~~~ shell
git config --global user.name "Your name here"
git config --global user.email "your_email@example.com"
~~~

On va mettre vim comme éditeur par défaut pour renseigner les commit :

~~~ shell
git config --global core.editor vim
~~~

> **Nota Bene :** Vous n'utiliserez que très peu l'éditeur par défaut une fois que vous ferez vos commit avec l'option `-m`

On met de la couleur dans le terminal par défaut : 

~~~ shell
git config --global color.ui true
~~~

> **Nota Bene :** 
> Vous pouvez mettre votre [éditeur favori](https://docs.github.com/en/github/using-git/associating-text-editors-with-git) bien sur, mais `vim` sera toujours présent quelque soit l'endroit où au aurez besoin de faire un commit (genre un serveur distant). Il est donc bien d'avoir quelque notions de vim et de les utiliser de temps en temps, d'où cette configuration.

Pour éviter d'avoir un pager lors des `git log` :
~~~ shell
git config --global pager.log false
~~~

Si l'on ne met pas cette option, les logs seront automatiquement passé à `more` par défaut pour paginer les résultats. 

> **Nota Bene :**
> On obtiendrait le même résultat sans utiliser la config ci-dessus en utilisant l'argument de git `--no-pager`, par exemple :`git --no-pager log`. Notez que `--no-pager` est un argument de git, pas de sa commande `log`, il est donc placé avant celle-ci.

## config minimale github

Créez vous un compte github si ce n'est déjà fait. Github va vous permettre de travailler en groupe et de montrer ce que vous savez faire, c'est un peu votre *book* de développeur.

Donc :

  - utilisez votre nom/prénom ou un pseudo présentable
  - utiliser une adresse mail que vous lisez
  - ne mettez dessus que les projets que vous pourriez mettre sur votre cv.
  
Rien ne vous empêche d'avoir d'autres comptes github pour vos projets plus perso mais celui-là c'est votre vitrine légale numérique.

Pour que vous puissiez facilement avoir accès à ce compte, 
[ajouter votre clé publique dans github](https://docs.github.com/en/github/authenticating-to-github/adding-a-new-ssh-key-to-your-github-account).

Vous pourrez donner votre clé publique pour être ajouté comme contributeur d'un projet. C'est un moyen pratique de gérer les personnes d'un projet.

# git

## But 

Utilisation courante de git/github grâce à un petit projet web. On suppose que vous avez fait la partie concernant l'initialisation de git et de github.

## création du projet git

Munissez vous d'un terminal et placez vous dans un dossier vierge :

~~~ shell
mkdir mon_projet_web
cd mon_projet_web 
~~~

On peut maintenant initialiser un projet git :

~~~ shell
git init
~~~

## le dossier *.git*

> [**Dans la doc**](https://git-scm.com/book/fr/v2/Les-tripes-de-Git-Plomberie-et-porcelaine) 


La commande précédente a initialisé `git` en créant un dossier caché *.git*. Git ne fonctionne que comme ça, tout est mis dans ce dossier. Chez moi, il ressemble à ça (j'ai utilisé la commande `tree -a` pour afficher l'arborescence et les fichiers cachés) :


~~~ shell
.
└── .git
    ├── HEAD
    ├── config
    ├── description
    ├── hooks
    │   ├── applypatch-msg.sample
    │   ├── commit-msg.sample
    │   ├── fsmonitor-watchman.sample
    │   ├── post-update.sample
    │   ├── pre-applypatch.sample
    │   ├── pre-commit.sample
    │   ├── pre-merge-commit.sample
    │   ├── pre-push.sample
    │   ├── pre-rebase.sample
    │   ├── pre-receive.sample
    │   ├── prepare-commit-msg.sample
    │   └── update.sample
    ├── info
    │   └── exclude
    ├── objects
    │   ├── info
    │   └── pack
    └── refs
        ├── heads
        └── tags

9 directories, 16 files

~~~

Le fichier de configuration est également décrit [dans ce post](https://www.daolf.com/posts/git-series-part-1/). En deux mots :
  - *HEAD* : la branche courant, pour l'instant **Master** (vérifiez le en lisant le fichier avec la commande `cat`)
  - *config* : le fichier de configuration. 
  - *description* : descriptiopn du projet, pas vraiment utilisé
  - *hooks/* : contient des scripts que l'on peu utiliser à chaque qu'une commande git particulieère est utilisée. C'est une utilisation avancée de git, qui permet par exemple de lancer tous les tests à chaque push, etc.
  - *info/exclude/* un *.gitignore* pour tout le projet.
  - *objects/* : contient votre projet actuel et passé en plein de petits bouts. Pour l'instant il n'y a rien.
  - *refs/* : contient les commit. Pour l'instant il n'y a rien.

## fonctionnement de git

Le but de git est de garder un historique d'un projet, en conservant les fichiers du projets et leurs modifications au cours du temps. Cet historique est composé de **commit** qui stock l'état d'un projet à un instant donné. Plus précisément il stocke la différence en l'état précédent et le nouvel état, formant un graphe direct et acyclique (si je jargonne)

Pour démarrer cet historique faisons notre premier commit. 

### premier commit 

Pour cela, il faut que l'on ait quelque chose à stocker.  Créons un petit fichier *index.html* à la racine de notre projet (donc ne soyez plus dans le dossier *.git*) :

~~~ html
<!doctype html>
<html>
<head>
    <meta charset="utf-8"/>
    <title>My homepage</title>
</head>
<body>
<h1>Hello World !</h1>
</body>
</html>
~~~

Pour faire un *commit* (stocker l'état d'un projet) il faut commencer par dire à git ce que l'on veut *"commiter*, ici notre fichier *index.html* :

~~~ shell
git add index.html
~~~

On place le fichier *index.html* courant dans le **stage** c'est à dire l'endroit où son mis les fichier qui seront inclus dans le *commit*. Pour voir tout ça, la commande `status` est super utile :


~~~ shell
git  status
~~~

Cette commande dit chez moi (et en couleur) :

~~~ shell
Sur la branche master

Aucun commit

Modifications qui seront validées :
  (utilisez "git rm --cached <fichier>..." pour désindexer)
	nouveau fichier : index.html
~~~

On a bien un nouveau fichier que l'on veut garder. On peut fait notre premier commit :


~~~ shell
git  commit
~~~

Cette commande va lancer l'éditeur que vous avez configuré (`vim` si vous avez suivi mes recommandations) et va vous demander de décrire votre commit. Cette étape est **obligatoire** et **très importante**, ne mettez donc pas de message fantaisiste : décrivez en une ligne ce que vous avez fait. 
Ici, par exemple : *"first commit"*. Sauvez et sortez de `vim`, vous avez fait votre premier commit. On le voit en tapant la commande `git status` (qui dit que tout est ok, que le stage est vide et que l'on a aucun fichier non suivi par git). 

La commande `git log` vous donne un historique des *commit* avec le nom, l'heure et le message. Chez moi ça donne :


~~~ shell
commit 3b8c0a8836050e58ec8cf8bd24f3d06b0bf39613 (HEAD -> master)
Author: François Brucker <francois.brucker@gmail.com>
Date:   Sat Sep 19 14:35:41 2020 +0200

    First commit !
~~~

### les objets

> [**Dans la doc**](https://git-scm.com/book/fr/v2/Les-tripes-de-Git-Les-objets-de-Git) 

Git va tout (oui tout) stocker dans le dossier `.git/objects` sous la forme d'un fichier compressé de nom égal à sa valeur de hash [SHA-1](https://fr.wikipedia.org/wiki/SHA-1) sur 40 octets.

> **Nota Bene :** Il est possible mais hautement improbable que 2 fichiers différents aient la même valeur de hash SHA-1. Dans ce cas là git sera perdu. Mais bon, que cela arrive c'st rare, et dans un même projet c'est encore plus rare.... Voir n'est pas encore arrivé.

Chez moi j'ai, avec la commande `tree objects` exécutée dans le dossier git :

~~~ shell
objects
├── 3b
│   └── 8c0a8836050e58ec8cf8bd24f3d06b0bf39613
├── 4b
│   └── 825dc642cb6eb9a060e54bf8d69288fbee4904
├── aa
│   └── e16b7870ad8867b12184215adf9063afc800c1
├── ab
│   └── 3401bd309f7e474cba48b2ecc06c09543a1e0d
├── info
└── pack
~~~

Ce dossier est la base de donnée de notre projet. Chaque objet est stocké avec une signature SHA-1 de 40 octets, les deux premiers étant le nom du dossier, les 38 autres le nom du fichier.

Si je veux savoir ce qu'il y a dans le fichier *ab/3401bd309f7e474cba48b2ecc06c09543a1e0d* du dossier objet, je tape : `git cat-file -p ab3401bd309f7e474cba48b2ecc06c09543a1e0d` et j'obtiens :

~~~ html

<!doctype html>
<html>
<head>
    <meta charset="utf-8"/>
    <title>My homepage</title>
</head>
<body>
<h1>Hello World !</h1>
</body>
</html>
~~~

C'est notre fichier html ! Les autres objets correspondent à l'arborescence de projet (pour l'instant un unique nœud, notre commit) et le commit en lui même. Il aura un autre nom chez vous, mais chez moi c'est celui de nom *3b/8c0a8836050e58ec8cf8bd24f3d06b0bf39613* (c'est le numéro donné dans le commit). 

### Les références 

Le dossier référence contient les références des commits de toutes les branches et ou tags de notre projet. Nous n'avons qu'une seule branche, nommée *master* commit des différentes branches. En regardant ce qu'il y a dans le fichier `refs/heads/master` je retrouve bien le numéro de commit.

On peut accéder à tout dans git en utilisant ces numéros (en entier ou  les 4 ou plus premiers chiffres). Par exemple si jeu veux voir le log de mon commit de numéro *3b8c0a8836050e58ec8cf8bd24f3d06b0bf39613*, je peux taper `git log 3b8c0a8836050e58ec8cf8bd24f3d06b0bf39613`, `git log 3b8c` ou encore `git log 3b8c0a8`


## avancer dans l'arbre

Modifions notre fichier *index.html* :

~~~ html
<!doctype html>
<html>
<head>
    <meta charset="utf-8"/>
    <title>Ma maison page</title>
</head>
<body>
<h1>Hello World !</h1>
<h2>et bonjour Monde !</h2>
</body>
</html>
~~~


La commande `git status` nous donne ce qui a changé :

~~~ shell 

Sur la branche master
Modifications qui ne seront pas validées :
  (utilisez "git add <fichier>..." pour mettre à jour ce qui sera validé)
  (utilisez "git restore <fichier>..." pour annuler les modifications dans le répertoire de travail)
	modifié :         index.html

aucune modification n'a été ajoutée à la validation (utilisez "git add" ou "git commit -a")
~~~

Un fichier a été modifié. Comme on a pas de nouveaux fichiers, et que l'on veut juste mettre à jour les fichiers déjà suivis, on peut utiliser l'argument `-a` de la commande `git commit` qui place dans le stage tous les fichiers suivi et modifiés. On ajoute un autre argument, `-m`, qui permet d'ajouter le message de commit directement dans la commande sans passer par l'éditeur. 

~~~ shell
git commit -a -m"add french"
~~~

On peut voir les logs (avec en prime deux nouvelles options, une de git pour ne pas avoir de pager une option de log pour  juste afficher  le message et le numéro du commit) : `git log --pretty=oneline`. J'obtiens :

~~~ shell
11f5564cda69451538ff8036c1eb92834a585884 (HEAD -> master) add french
3b8c0a8836050e58ec8cf8bd24f3d06b0bf39613 First commit !
~~~


### ajout de fichiers

Ajoutons un fichier css à notre projet et faisons les liens avec le fichier html.

*main.css* : 

~~~ css

h1 {
  color: olive;
}

~~~

et le fichier *index.html* modifié :

~~~ html

<!doctype html>
<html>
<head>
    <meta charset="utf-8"/>
    <title>Ma maison page</title>
    
    <link href="main.css" rel="stylesheet">
</head>
<body>
<h1>Hello World !</h1>
<h2>et bonjour Monde !</h2>
</body>
</html>
~~~


La commande `git status` m'indique qu'il existe un fichier non suivi (*main.css*) et que le fichier *index.html* a été modifié :

~~~ shell
Sur la branche master
Modifications qui ne seront pas validées :
  (utilisez "git add <fichier>..." pour mettre à jour ce qui sera validé)
  (utilisez "git restore <fichier>..." pour annuler les modifications dans le répertoire de travail)
	modifié :         index.html

Fichiers non suivis:
  (utilisez "git add <fichier>..." pour inclure dans ce qui sera validé)
	main.css

aucune modification n'a été ajoutée à la validation (utilisez "git add" ou "git commit -a")

~~~


Faites un commit de tout ça (en n'oubliant pas d'ajouter *main.css* au stage avant le commit car l'option `-a` n'ajoute pas automatiquement au stage les fichiers non suivis) :

~~~ shell
git add main.css
git add index.html

git status
# on vérifie bien tout avant le commit
git commit -m"add css and link to html"
git status
# on vérifie que tout s'est bien passé.
~~~

> **Nota Bene :** Prenez l'habitude de faire un `git status` avant et après chaque commit, histoire d'être sur que l'on ne va rien oublier dans le commit.


Un `git log --oneline` nous montre que l'on a 3 commits (notez que l'option `--oneline` ne garde que les 7 premiers chiffres de chaque commit).


diff avant le commit pour voir la diff avec ce qui a été enregistré.

### historique

Vous pouvez voir ce qu'il y avait dans chaque commit, [cette doc](https://git-scm.com/book/fr/v2/Les-bases-de-Git-Visualiser-l%E2%80%99historique-des-validations) vous montre plein de chouettes exemples. En particulier : `git log -p` qui montre ce que l'on a fait avec chaque commit. Le [format de git diff](https://www.oreilly.com/library/view/git-pocket-guide/9781449327507/ch11.html) est un format étonnamment lisible qui montre distinctement les différences entre les versions. 


### diff

On peut également voir les différences entre le dernier commit et ce que l'on a fait en utilisant la commande [`git diff`](https://git-scm.com/docs/git-diff/fr).

Commençons par modifiez nos fichiers *main.css* et *index.html* :

On ajoute une règle pur les `<h2>` dans *main.css* :
~~~ css
h2 {
  color: blue;
}
h1 {
  color: olive;
}
~~~

Egt un petti paragraphe dans *index.html* :

~~~ html
<!doctype html>
<html>
<head>
    <meta charset="utf-8"/>
    <title>Ma maison page</title>
    
    <link href="main.css" rel="stylesheet">
</head>
<body>
<h1>Hello World !</h1>
<h2>et bonjour Monde !</h2>
<p>Comment allez-vous ? </p>
</body>
</html>
~~~


La commande `git diff` nous indique les différences entre le dernier commit et ce qeu je n'ai pas encore mis en stage. Donc ici `git diff` nous donne les différences pour *main.css* et *index.html* :

~~~ shell
diff --git a/index.html b/index.html
index b73fc14..17c8556 100644
--- a/index.html
+++ b/index.html
@@ -9,5 +9,6 @@
 <body>
 <h1>Hello World !</h1>
 <h2>et bonjour Monde !</h2>
+<p>Comment allez-vous ? </p>
 </body>
 </html>
diff --git a/main.css b/main.css
index 4a4e8ca..aca9293 100644
--- a/main.css
+++ b/main.css
@@ -1,3 +1,6 @@
+h2 {
+  color: blue;
+}
 h1 {
   color: olive;
 }

~~~

Mettons le fichier index.html en stage (`git add index.html`) et refaisons la commande `git diff` :

~~~ shell
diff --git a/main.css b/main.css
index 4a4e8ca..aca9293 100644
--- a/main.css
+++ b/main.css
@@ -1,3 +1,6 @@
+h2 {
+  color: blue;
+}
 h1 {
   color: olive;
 }

~~~

Nous n'avons bien plus que les différences avec *main.css*. 



Allez commitons tout ça : `git commit -a -m"h2 rule in css and p in html"`. Notez que le fichier *main.css* a bien été ajouté au stage avant le commit grâce à l'argument `-a`. Vérifiez le avec `git status` voir même un `git diff`.


> **Nota Bene : ** la commande `git diff --cached` permet de faire le diff en prenant en compte le stage. Vous avez donc un diff entre le dernier commit et ce que vous avez fait depuis.


### modifier le dernier commit

Il arrive parfois (souvent) de se rendre compte juste après un commit que l'on a pas tout envoyé (le `git status` n'est pas clean) ou que l'on a fait une faute dans le message accompagnant le commit. C'est pour ça qu'il existe l'argument `--amend` à commit qui vous permet de modifier le dernier commit que vous avez fait. 

[Lisez la doc](https://git-scm.com/book/fr/v2/Utilitaires-Git-R%C3%A9%C3%A9crire-l%E2%80%99historique) pour voir comment faire. C'est super utile pour tous ceux qui, comme moi, ont un peu la tête en l'air.


## .gitignore

Il est impératif qu'avant chaque commit il ne reste aucun fichier non suivi. Cependant, certains fichiers sont pré&sent dans le dossier mais on ne veut pas les inclure dans le projet git. On peut citer :

  - les fichiers *.DS_STORE* des macs,
  - les fichiers des IDE, comme les ficheirs *.idea* de intellij
  - les fichiers de bibliothèques, comme le dossier *node_modules* lorsque l'on fait du web
  - ...

Pour que git ignore ces fichiers on utilise un fichier *.gitignore*) qui liste ces fichiers. Son [format](https://git-scm.com/docs/gitignore) est à la fois simple et efficace. On peut même avoir un fichier *.gitignore* par dossier du projet, donc utilisez le !

Vous trouverez plein d'[exemples de .gitingore](https://github.com/github/gitignore), je vous conseille ne pas mettre plein de choses dont vous n'avez pas besoin. Ajoutez des lignes au *.gitingore* uniquement lorsque vous en avez besoin.

Par exemple, après avoir supprimé un fichier via le finder sur mon mac, `git status` me donne ça :

~~~ shell
Sur la branche master
Fichiers non suivis:
  (utilisez "git add <fichier>..." pour inclure dans ce qui sera validé)
	.DS_Store

aucune modification ajoutée à la validation mais des fichiers non suivis sont présents (utilisez "git add" pour les suivre)

~~~ 

On va donc créer un fichier *.gitingore* contenant uniquement la ligne `.DS_STORE`, l'ajouter au stage et refaire un `git status` pour obtenir : 

~~~ shell
Sur la branche master
Modifications qui seront validées :
  (utilisez "git restore --staged <fichier>..." pour désindexer)
	nouveau fichier : .gitignore
~~~

On fini par l'ajouter au projet par un commit : `git commit -m"add .gitignore"`.

## branches

Les [branches](https://git-scm.com/book/fr/v2/Les-branches-avec-Git-Les-branches-en-bref) de git permettent d'avoir plusieurs histoires possible de mon projet.

La principale utilisation des branches en développement est :
  
  - l'ajout de nouvelles fonctionnalités. La fonctionnalité n'est ajoutée au master qu'une fois finie. .
  - la correction de bug. Une fois le bug corrigé, on ajoute la correction au master.


Ceci nous assure que la branche `master` est **TOUJOURS** un projet fonctionnel. 

A part ces branches temporaires, on a parfois besoin de branches plus pérennes comme :

  - la gestion des versions différentes de l'application à maintenir
  - une branche qui contient le build d'un site web statique par exemple.

La commande `git branch` nous indique les branches que nous avons. Pour l'instant nous n'avons que la branche par défaut : `master`.

### créer une branche

Nous allons créer une branche pour voir s'il est possible d'ajouter du javascript à notre projet : `git branch js`. 

Si l'on refait la commande `git branch`, on voit qu'on a deux branches et qu'on est toujorus sur la branche `master`. Allons vers la branche `js` avec la commande : `git checkout js` 

On peut maintenant tranquillement ajouter du js à notre projet :

  - On ajoute le fichier *main.js*
    ~~~ javascript
    let paragraph = document.getElementById("couleur");

    paragraph.addEventListener("mouseenter", function( event ) {   
      event.target.style.color = "purple";
    }, false);

    paragraph.addEventListener("mouseleave", function( event ) {   
      event.target.style.color = "black";
    }, false);
    ~~~

  - et on modifie le fichier *index.html* :
    ~~~ html
    <!doctype html>
    <html>
    <head>
        <meta charset="utf-8"/>
        <title>Ma maison page</title>
        
        <link href="main.css" rel="stylesheet">
    </head>
    <body>
    <h1>Hello World !</h1>
    <h2>et bonjour Monde !</h2>
    <p id="couleur">Comment allez-vous ? </p>
    
    <script src="main.js"></script>
    </body>
    </html>
    ~~~
    
On peut maintenant commiter le tout (en commençant pas ajouter les fichiers *main.js* et *index.html* au stage bien sur avec la commande `git add main.js index.html
`) : `git commit m"add js"`.

Un `git log --oneline` nous montre bien que l'on est maintenant sur une nouvelle branche :

~~~ shell
f7907be (HEAD -> js) add js
35609dd (master) add .gitignore
7d2fd72 h2 rule in css and p in html
a3c3fdc add css and link to html
11f5564 add french
3b8c0a8 First commit !
~~~


### voir des branches

Si l'on revient à la branche `master` avec la commande `git checkout master` on voit que le fichier *main.js* a disparu et que le fichier *index.html* est remis à sa position sans le js.


Faisons une modification du fichier *index.html* de la branche master en ajoutant une phrase au paragraphe :
~~~ html
<!doctype html>
<html>
<head>
    <meta charset="utf-8"/>
    <title>Ma maison page</title>

    <link href="main.css" rel="stylesheet">
</head>
<body>
<h1>Hello World !</h1>
<h2>et bonjour Monde !</h2>
<p>Comment allez-vous ?  Bien ou quoi ?</p>
</body>
</html>
~~~

Et on commit le tout : `git commit -am"parlons jeune"`

On remarque que la commande `git log --oneline` ne montre que l'histoire du dernier commit, on ne montre donc pas la modification de la branche `js` qui est inutile pour notre dernier commit.

Pour voir tous les log, on peut ajouter l'argument `--all`. Du coup : `git log --oneline --all` donne :

~~~ shell
a2ac886 (HEAD -> master) parlons jeune
f7907be (js) add js
35609dd add .gitignore
7d2fd72 h2 rule in css and p in html
a3c3fdc add css and link to html
11f5564 add french
3b8c0a8 First commit !

~~~

Et si l'on veut voir le graphe des dépendances on peut ajouter l'argument `--graph` : `git log --oneline --all --graph` :

~~~ shell
* a2ac886 (HEAD -> master) parlons jeune
| * f7907be (js) add js
|/  
* 35609dd add .gitignore
* 7d2fd72 h2 rule in css and p in html
* a3c3fdc add css and link to html
* 11f5564 add french
* 3b8c0a8 First commit !
~~~


### réconcilier les branches

Si l'on veut maintenant mettre notre branche expérimentale (`js`) dans la branche `master`, il va falloir réconcillier les branches. Cela peut se faire de nombreuses manière mais la méthode couramment utilisée actuellement est celle du [rebase](https://www.miximum.fr/blog/git-rebase/)

Nous allons donc procéder comme suit : 

  1. depuis la branche `js`, on va la faire commencer à la fin de `master`
  2. on va "*merger*" la branche `js` à la suite de la branche `master`.

On aura donc à la fin un joli historique qui fait comme si j'avais ajouter mon `js` à la suite du `master` sans autres branches.

#### git rebase

Sur la branche `js` on excute la commande : `git rebase master` et on obtient le résultat : 

~~~ 
Fusion automatique de index.html
CONFLIT (contenu) : Conflit de fusion dans index.html
error: impossible d'appliquer f7907be... add js
Resolve all conflicts manually, mark them as resolved with
"git add/rm <conflicted_files>", then run "git rebase --continue".
You can instead skip this commit: run "git rebase --skip".
To abort and get back to the state before "git rebase", run "git rebase --abort".
impossible d'appliquer f7907be... add js

~~~

En essayant d'ajouter les derniers commits de master au début de js, git a un soucis. Il n'arrive pas à le faire tout seul. Il va falloir l'aider.

Son soucis est dans le ficier *index.html*. Regardons le :

~~~ html
<!doctype html>
<html>
<head>
    <meta charset="utf-8"/>
    <title>Ma maison page</title>

    <link href="main.css" rel="stylesheet">
</head>
<body>
<h1>Hello World !</h1>
<h2>et bonjour Monde !</h2>
<<<<<<< HEAD
<p>Comment allez-vous ?  Bien ou quoi ?</p>
=======
<p id="couleur">Comment allez-vous ? </p>

<script src="main.js"></script>
>>>>>>> f7907be... add js
</body>
</html>
~~~

Horreur, c'est tout cassé. Mais au final c'est compréhensible. Le haut est `HEAD` (donc master) et le bas c'est ce que j'ai (la branche `js`). Pour que les deux soient cohérent on modifie le fichier pour qu'il intègre nos modifications conjointes  :

~~~ html
<!doctype html>
<html>
<head>
    <meta charset="utf-8"/>
    <title>Ma maison page</title>

    <link href="main.css" rel="stylesheet">
</head>
<body>
<h1>Hello World !</h1>
<h2>et bonjour Monde !</h2>
<p id="couleur">Comment allez-vous ?  Bien ou quoi ?</p>

<script src="main.js"></script>
</body>
</html>
~~~

On peut ensuite l'ajouter au stage pour signifier à git qu'on a résolu son problème : `git add index.html` et on continue jusqu'à la fin ou jusqu'au nouveau problème : `git rebase --continue`. Il n'y a plus d'erreur et on arrive dans `vim` pour donner le message de commit. On laisse celui par défaut et on obtient la jolie liste de commit suivant (`git log --oneline --all --graph`):

~~~ 
* fe850ac (HEAD -> js) add js
* a2ac886 (master) parlons jeune
* 35609dd add .gitignore
* 7d2fd72 h2 rule in css and p in html
* a3c3fdc add css and link to html
* 11f5564 add french
* 3b8c0a8 First commit !
~~~

On est passé de ça :

~~~
A---B---C---D ← master
         \
          F---G ← js
~~~

à ça :

~~~
A---B---C---D ← master
             \
               F'---G' ← js
~~~

Il ne nous reste plus qu'à fusionner `js` dans `master` (ce qui devrait se faire sans soucis puisqu'elles se suivent). Pour cela :

  1. on se place sur la branche `master` : `git checkout master`
  2. on fusionne la branche `js` sur `master` : `git merge js`

Un `it log --oneline --all --graph` montre que les deux branches sont identique, on peut maintenant supprimer la branche `js` : `git branch -d js`

#### merge

"*Merger*" revient à fusionner une branche dans une autre. Si les deux branches ne sont pas linéairement dépendante, par exemple comme ça : 

~~~
A---B---C---D ← master
         \
          F---G ← js
~~~

Le résultat du merge sera : 

~~~
A---B---C---D---H ← master
         \     /
          F---G ← js
~~~

Ce qui induit des "boucle" et n'est pas pratique lorsque l'on veut connaître l'historique du projet. Une droite c'est mieux pour voir ce qu'il s'est passé. Dans l'exemple ci-dessus, un même fichier a pu être modifié en D et en G avant d'être fusionné.

On évitera donc au maximum un merge comme ça et on ne l'utilisera que si les branches sont linéairement dépendante comme çà :

~~~
A---B---C---D ← master
             \
              E---F ← js
~~~

Rendant l'historique lisible et le merge facile (c'est le rebase qui pourra être compliqué)


# github

[github](https://github.com/) est un endroit où l'on peut stocker ses projets. Ces projets seront identiques aux projets que vous avez sur votre machine (un projet git contient tout le temps tout l'historique de celui-ci) mais leurs état sera la référence pour tous les contributeur du projet. On appelle cet endroit *origin*. 

> **Nota Bene : ** A priori rien de différentie ce repository d'un autre, juste une convention qui déscide qu'un des repository d'un projet sera l'origin.

## Initalisation d'un projet

Il y a deux façon d'initialiser un projet sur github :

  - le projet existe déjà sur github et je le *clone* chez moi : [la doc github pour le cloning](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository)
  - le projet existe en dehors de github et je veux le mettre sur github : [la doc d'import d'un projet dans github](https://docs.github.com/en/github/importing-your-projects-to-github/adding-an-existing-project-to-github-using-the-command-line)
origin

### clone

Vous allez cloner le projet du cours qui est là : https://github.com/FrancoisBrucker/cours_informatique

  1. placez vous dans le dossier parent où vous voulez que votre projet soit
  2. `git clone git@github.com:FrancoisBrucker/cours_informatique.git` 
  
Un dossier *cours_informatique* a été créé. Regardez le fichier *.git/config* de ce projet :

~~~
[core]
	repositoryformatversion = 0
	filemode = true
	bare = false
	logallrefupdates = true
	ignorecase = true
	precomposeunicode = true
[remote "origin"]
	url = git@github.com:FrancoisBrucker/cours_informatique.git
	fetch = +refs/heads/*:refs/remotes/origin/*
[branch "master"]
	remote = origin
	merge = refs/heads/master
~~~

Par rapport au projet précédent, deux entrées ont fait leurs apparitions :

  - "origin" : qui est le dépôt origin de notre projet maintenant, sur [github](https://github.com/).
  - "master" qui est la branche principale sur le projet origin.

### ajouter un projet existant à github

Ajoutons notre petit projet web à github :

  1. créez un *repository* sur github
  2. on va ajouter à la main l'origin et le master dans le projet sur notre ordinateur. Pour moi, avec *my_web_test* comme nom de projet ça donne (il suffit de copier/coller ce qeu nous donne github après la création du projet) :
    - origin : 
        - `git remote add origin git@github.com:FrancoisBrucker/my_web_test.git`
        - on se place dans la branche de notre projet qui va être le master et on tape `git branch -M master` si elle ne s'appelle pas encore master.
  3. on pousse tout notre projet sur github : `git push --set-upstream origin master`. Cette commande a à la fois pousser tout notre projet sur github et placé le master de l'origin par défaut. Il suffira ensuite de taper `git push` pour que ce soit equivalent à `git push origin master`.


## récupérer les données du serveur origin

On utilise la commande `git pull` (ou `git pull origin master` si l'on a pas défini une branche par défaut).

Pour que cette commande fonctionne il faut que l'origin soit plus loin en commit que vous et que n'ayez pas fait de modification par rapport à l'histoire de l'origin (vous devez juste être en retard, pas autre part)

**Attention :** Le `git pull` fera un merge par défaut, brisant la jolie linéarité de l'historique. Il faut, comme pour la synchronisation des branche faire un rebase. Je vous conseille la lecture de [cet article](https://delicious-insights.com/fr/articles/bien-utiliser-git-merge-et-rebase/) qui explique bien comment faire. 

Pour se fixer les idées, on ne fera jamais un `gill pull` depuis l'origin, mais un : `git pull --rebase=preserve`. Ceci permet de :

  - faire un rebase de l'origin sur votre branche locale
  - de préserver les merge (fusion) de branches déjà présentes (et qui donc, si elles existent, ont une fonction *sémantique* dans votre projet)
  
  Pour ne pas avoir à se soucier de toujours ajouter ces options aux git pull, on en fait des options globales :
  
  ~~~ shell
  git config --global pull.rebase preserve
  ~~~

Vous pourrez ensuite faire des `git pull` tout seul et ils seront rebasé par défaut et préserveront les merges existant. Le meilleur des deux monde en somme.


## envoyer ses données à l'origin

Pour envoyer ses données à l'origin il faut que vous soyez en avance sur lui. Donc que l'origin se trouve à un endroit du passé de votre historique. Il doit être en retard par rapport à vous, pas autre part.


Il y a alors  deux façons de faire, que l'on soit un contributeur authentifié du projet (on utilise alors push sur la branche comme on le ferait en local) ou pas (on fait un push mais il faut demander la permission au propriétaire du projet de la publier. C'est ce que l'on appelle un *pull-request*)

### push

Si une *origin* de notre projet est déterminée, `git push` envoie les derniers commits sur celle-ci. 

### pull request

Si l'on a cloné un projet et que l'on est pas un de ses contributeur mais que l'on aimerait tout de même contribuer (comme vous devrez/pouvez le faire pour ce cours), vous pouvez faire une [pull request](http://thelia-school.com/faire-une-pull-request-sur-un-projet-thelia/faire-une-pull-request.html), c'est à dire envoyez vos modification au responsable du projet pour qu'il l'intègre s'il le veut au projet.


## synchronisation

Si l'origin et votre dossier local n'est pas synchronisé, il faut faire un rebase comme pour les branches pour la synchronisation puisse se faire.


# mettre en production

Pour mettre un site en production, il suffit de cloner son projet git et de pull les dernières versions du projet.

On a parfois une branche dédiée qui s'appelle production, mais souvent la branche master suffit.


# revenir en arrière dans l'historique

Il arrive parfois qu'on a complètement raté un truc et que l'on veuille revenir en arrière dans le projet. C'est super car c'est justement là où git est fort.


Attention cependant, ces opérations modifient l'historique du projet, chose que l'on aime pas trop faire. Il est donc recommandé de ne faire ça que sur des commits qui n'ont pas été publiés sur l'origin.


Je ne vais ici que résumer les possibilités. Allez voir sur 
[cette vidéo](https://www.youtube.com/watch?v=ZY5A7kUR0S4) pour avoir un apperçu de ce que l'on peut faire en situation, ou encore 
[cette doc](https://delicious-insights.com/fr/articles/git-reset/), plus velue.

Pour l'instant l'historique de notre projet est (`git log --oneline`) :

~~~
fe850ac (HEAD -> master, origin/master) add js
a2ac886 parlons jeune
35609dd add .gitignore
7d2fd72 h2 rule in css and p in html
a3c3fdc add css and link to html
11f5564 add french
3b8c0a8 First commit !
~~~

> **Nota Bene :** c'est queand on veut faire ce genre de chose ou que l'on cherche quand un bug a été introduit dans le projet que l'on est bien content d'avoir mis des message de commit explicite.

Il y a 3 commandes git qui permettent de gérer l'historique [reset, restore et revert](https://git-scm.com/docs/git#_reset_restore_and_revert), chacune a ses spécificités et ses utilités. 

> **Nota Bene : ** la commande `git reflog` montre tous les commits du projet. Cela peut être super utile si on a fait un `git reset` à un ancien commit et que l'on veut finalement revenir à un endroit dans le futur par rapport à ce commit.

On va voir plusieurs cas pratiques : 

  - revenir au dernier commit. Le dernier commit est appelé *HEAD* par git. 
    - supprimer  des modifications faites à un fichier pour revenir à sa version *HEAD* : `git restore index.html` par exemple reprend la version du `index.html` du dernier commit de l'historique.
    - vider le stage : `git reset` (ou `git reset HEAD nom_de-fichier` pour un stager un unique fichier).
    - revenir au dernier commit et supprimer toutes les modification faites  : `git reset --hard`. Attention cela supprime du code...
 
  - revenir à un commit plus éloignés. On peut y acceder par son numéro ou par une reférence par rapport au dernier commit (nommé aussi HEAD). Ainsi HEAD signifie le dernier commit, HEAD~1 l'avant dernier, HEAD~2 l'antépénultième et ainsi de suite.
    - regarder un ancien endroit dans le projet : `git checkout 7d2fd72` par exemple crée une nouvelle branche temporaire (nommée *HEAD détachée*) pour voir à quoi ressemblait notre projet au commit *7d2fd72* (on a bien une règle h2 à notre css). Si l'on a rien modifié, un simple `git checkout master` reviendra à l'état courant du projet. Si l'on a modifié des fichiers, il faut commencer par revenir à l'état initial
    - revenir à un commit plus lointain : 
      - `git reset numéro_commit` reviendra au commit déterminé mais laissera vos modifications.
      - `git reset numéro_commit --hard` reviendra au commit déterminé mais supprimera vos modifications. Attention vous allez perdre des modifications !
  - remettre un seul fichier à un état antérieur : `git checkout 7d2fd72 index.html` prend le fichier dans l'état où il était au commit précisé, l'importe à l'état actuel et le met dans le stage, prêt à être commité. Si on ne veut plus de ce fichier, on peut revenir à l'état initial en important le fichier du master : `git checkout master index.html`
  - undo un commit : `git revert 7d2fd72` va créer un commit qui défait un ancien commit (ce commit pouvant être aussi loin que l'on veut). Cela ne change pas l'historique en supprimant le commit undoé, ça rajoute un commit qui le undo.

# ressources
  - [githug](https://github.com/Gazler/githug) apprenez git par l'exemple.
  - initialisation git/github par défaut :
    - [doc officielle](https://git-scm.com/book/en/v2/Getting-Started-First-Time-Git-Setup)
    - [git et github](https://kbroman.org/github_tutorial/pages/first_time.html) 
  - guide général :
    - [sympa et en français](https://www.miximum.fr/blog/decouvrir-git/)
    - [guide de Karl Broman](https://kbroman.org/github_tutorial/). Très bien fait et va au but.
    - [pro git](https://git-scm.com/book/en/v2). Y'a tout. Peut-être parfois un peu trop. Mais si on a un problème il y a forcément la solution là dedans.
    - [git magic](http://www-cs-students.stanford.edu/~blynn/gitmagic/intl/fr/index.html). En français. Très intéressant à suivre également, il donne des infos différente du tuto de Karl Broman.
    - playlist youtube :
      - [coding train playlist](https://www.youtube.com/playlist?list=PLRqwX-V7Uu6ZF9C0YMKuns9sLDzK6zoiV). Sympa à écouter et faire. Passe pas mal de temps au début avec github.
      - [grafikart](https://www.youtube.com/watch?v=rP3T0Ee6pLU&list=PLjwdMgw5TTLXuY5i7RW0QqGdW0NZntqiP). En français s'il vous plait.
    - [version control with git](https://www.amazon.fr/Version-Control-Git-collaborative-development-ebook/dp/B008Y4OR3A). Un très bon livre qui explique en détail le fonctionnement de git. 
  - commandes :
    - [toutes les commandes](https://git-scm.com/docs/git#_git_commands)
    - [commandes courante](https://www.hostinger.fr/tutoriels/commandes-git/)
    - [une cheat sheet](https://training.github.com/downloads/fr/github-git-cheat-sheet.pdf)
  - misc :
      - du git en 3 parties [partie 1](https://www.daolf.com/posts/git-series-part-1/)
      - tout ce que vous avez toujours voulu savoir sur [rebase t quand l'utiliser](https://delicious-insights.com/fr/articles/bien-utiliser-git-merge-et-rebase)
      
