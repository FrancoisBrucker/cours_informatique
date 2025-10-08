---
layout: layout/post.njk

title: Projet git

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

> TBD factoriser ce qu'on a déjà vu. Il y a des redites.

Bases de l'utilisation de git. On va utiliser git/github grâce à un petit projet web et en profiter pour expliquer le fonctionnement interne de git.

## Création du projet git

Munissez vous d'un terminal et placez vous dans un dossier vierge :

```shell
mkdir mon_projet_web
cd mon_projet_web
```

On peut maintenant initialiser un projet git :

```shell
git init
```

## le dossier `.git`{.fichier}

{% lien "**Documentation**" %}
<https://git-scm.com/book/fr/v2/Les-tripes-de-Git-Plomberie-et-porcelaine>
{% endlien %}

La commande précédente a initialisé `git` en créant un dossier caché `.git`{.fichier}. Git ne fonctionne que comme ça, tout est mis dans ce dossier. Chez moi, il ressemble à ça :

```shell
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
```

{% info %}
J'ai utilisé la commande `tree -a` pour afficher l'arborescence et les fichiers cachés.
{% endinfo %}

En deux mots le dossier de configuration du projet git contient :

- `HEAD`{.fichier} : la branche courant, pour l'instant **Master** (vérifiez le en lisant le fichier avec la commande `cat`)
- `config`{.fichier} : le fichier de configuration.
- `description`{.fichier} : description du projet, pas vraiment utilisé
- `hooks/`{.fichier} : contient des scripts que l'on peu utiliser à chaque qu'une commande git particulière est utilisée. C'est une utilisation avancée de git, qui permet par exemple de lancer tous les tests à chaque push, etc.
- `info/exclude/`{.fichier} un _.gitignore_ pour tout le projet.
- `objects/`{.fichier} : contient votre projet actuel et passé en plein de petits bouts. Pour l'instant il n'y a rien.
- `refs/`{.fichier} : contient les commit. Pour l'instant il n'y a rien.

## Fonctionnement de git

Le but de git est de garder un historique d'un projet, en conservant les fichiers du projets et leurs modifications au cours du temps. Cet historique est composé de **commit** qui stock l'état d'un projet à un instant donné. Plus précisément il stocke la différence en l'état précédent et le nouvel état, formant un graphe direct et acyclique (si je jargonne)

Pour démarrer cet historique faisons notre premier commit.

### Premier commit

Pour cela, il faut que l'on ait quelque chose à stocker. Créons un petit fichier `index.html`{.fichier} à la racine de notre projet (donc ne soyez plus dans le dossier `.git`{.fichier}) :

```html
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8" />
    <title>My homepage</title>
  </head>
  <body>
    <h1>Hello World !</h1>
  </body>
</html>
```

Pour faire un _commit_ (stocker l'état d'un projet) il faut commencer par dire à git ce que l'on veut _"commiter"_, ici notre fichier `index.html`{.fichier} :

```shell
git add index.html
```

On place le fichier `index.html`{.fichier} courant dans le **stage** c'est à dire l'endroit où son mis les fichier qui seront inclus dans le _commit_. Pour voir tout ça, la commande `status` est super utile :

```shell
git status
```

Cette commande dit chez moi (et en couleur) :

```shell
Sur la branche main

Aucun commit

Modifications qui seront validées :
  (utilisez "git rm --cached <fichier>..." pour désindexer)
  nouveau fichier : index.html
```

On a bien un nouveau fichier que l'on veut garder. On peut fait notre premier commit :

```shell
git commit
```

Cette commande va lancer l'éditeur que vous avez configuré (`vi` si vous avez suivi mes recommandations) et va vous demander de décrire votre commit. Cette étape est **obligatoire** et **très importante**, ne mettez donc pas de message fantaisiste : décrivez en une ligne ce que vous avez fait.
Ici, par exemple : _"first commit"_. Sauvez et sortez de `vi`, vous avez fait votre premier commit. On le voit en tapant la commande `git status` (qui dit que tout est ok, que le stage est vide et que l'on a aucun fichier non suivi par git).

La commande `git log` vous donne un historique des _commit_ avec le nom, l'heure et le message. Chez moi ça donne :

```shell
commit 3b8c0a8836050e58ec8cf8bd24f3d06b0bf39613 (HEAD ->  main)
Author: François Brucker <francois.brucker@gmail.com>
Date:   Sat Sep 19 14:35:41 2020 +0200

    First commit !
```

### Les objets

{% lien "**Documentation**" %}
<https://git-scm.com/book/fr/v2/Les-tripes-de-Git-Les-objets-de-Git>
{% endlien %}

Git va tout (oui tout) stocker dans le dossier `.git/objects`{.fichiers} sous la forme d'un fichier compressé de nom égal à sa valeur de hash [SHA-1](https://fr.wikipedia.org/wiki/SHA-1) sur 40 octets.

{% info %}
Il est possible mais hautement improbable que 2 fichiers différents aient la même valeur de hash SHA-1. Dans ce cas là git sera perdu. Mais bon, que cela arrive c'st rare, et dans un même projet c'est encore plus rare.... Voir n'est pas encore arrivé.
{% endinfo %}

Chez moi j'ai, avec la commande `tree objects` exécutée dans le dossier git :

```shell
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
```

Ce dossier est la base de donnée de notre projet. Chaque objet est stocké avec une signature SHA-1 de 40 octets, les deux premiers étant le nom du dossier, les 38 autres le nom du fichier.

Si je veux savoir ce qu'il y a dans le fichier `ab/3401bd309f7e474cba48b2ecc06c09543a1e0d`{.fichier} du dossier `objet`{.fichier}, je tape : `git cat-file -p ab3401bd309f7e474cba48b2ecc06c09543a1e0d` et j'obtiens :

```html
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8" />
    <title>My homepage</title>
  </head>
  <body>
    <h1>Hello World !</h1>
  </body>
</html>
```

C'est notre fichier html ! Les autres objets correspondent à l'arborescence de projet (pour l'instant un unique nœud, notre commit) et le commit en lui même. Il aura un autre nom chez vous, mais chez moi c'est celui de nom `3b/8c0a8836050e58ec8cf8bd24f3d06b0bf39613`{.fichier} (c'est le numéro donné dans le commit).

### Les références

Le dossier référence contient les références des commits de toutes les branches et ou tags de notre projet. Nous n'avons qu'une seule branche, nommée `main` commit des différentes branches. En regardant ce qu'il y a dans le fichier `refs/heads/main` je retrouve bien le numéro de commit.

On peut accéder à tout dans git en utilisant ces numéros (en entier ou les 4 ou plus premiers chiffres). Par exemple si jeu veux voir le log de mon commit de numéro `3b8c0a8836050e58ec8cf8bd24f3d06b0bf39613`, je peux taper `git log 3b8c0a8836050e58ec8cf8bd24f3d06b0bf39613`, `git log 3b8c` ou encore `git log 3b8c0a8`

## Avancer dans l'arbre

Modifions notre fichier `index.html`{.fichier} :

```html
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8" />
    <title>Ma maison page</title>
  </head>
  <body>
    <h1>Hello World !</h1>
    <h2>et bonjour Monde !</h2>
  </body>
</html>
```

La commande `git status` nous donne ce qui a changé :

```shell

Sur la branche main
Modifications qui ne seront pas validées :
  (utilisez "git add <fichier>..." pour mettre à jour ce qui sera validé)
  (utilisez "git restore <fichier>..." pour annuler les modifications dans le répertoire de travail)
  modifié :         index.html

aucune modification n'a été ajoutée à la validation (utilisez "git add" ou "git commit -a")
```

Un fichier a été modifié. Comme on a pas de nouveaux fichiers, et que l'on veut juste mettre à jour les fichiers déjà suivis, on peut utiliser l'argument `-a` de la commande `git commit` qui place dans le stage tous les fichiers suivi et modifiés. On ajoute un autre argument, `-m`, qui permet d'ajouter le message de commit directement dans la commande sans passer par l'éditeur.

```shell
git commit -a -m"add french"
```

On peut voir les logs (avec en prime deux nouvelles options, une de git pour ne pas avoir de pager une option de log pour juste afficher le message et le numéro du commit) : `git log --pretty=oneline`. J'obtiens :

```shell
11f5564cda69451538ff8036c1eb92834a585884 (HEAD -> main) add french
3b8c0a8836050e58ec8cf8bd24f3d06b0bf39613 First commit !
```

### Ajout de fichiers

Ajoutons un fichier css à notre projet et faisons les liens avec le fichier html.

Fichier `main.css`{.fichier} :

```css
h1 {
  color: olive;
}
```

et le fichier `index.html`{.fichier} modifié :

```html
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8" />
    <title>Ma maison page</title>

    <link href="main.css" rel="stylesheet" />
  </head>
  <body>
    <h1>Hello World !</h1>
    <h2>et bonjour Monde !</h2>
  </body>
</html>
```

La commande `git status` m'indique qu'il existe un fichier non suivi (_main.css_) et que le fichier _index.html_ a été modifié :

```shell
Sur la branche main
Modifications qui ne seront pas validées :
  (utilisez "git add <fichier>..." pour mettre à jour ce qui sera validé)
  (utilisez "git restore <fichier>..." pour annuler les modifications dans le répertoire de travail)
  modifié :         index.html

Fichiers non suivis:
  (utilisez "git add <fichier>..." pour inclure dans ce qui sera validé)
  main.css

aucune modification n'a été ajoutée à la validation (utilisez "git add" ou "git commit -a")

```

Faites un commit de tout ça (en n'oubliant pas d'ajouter _main.css_ au stage avant le commit car l'option `-a` n'ajoute pas automatiquement au stage les fichiers non suivis) :

```shell
git add main.css
git add index.html

# on vérifie bien tout avant le commit
git status

# on commit
git commit -m"add css and link to html"

# on vérifie que tout s'est bien passé.
git status
```

{% note %}
Prenez l'habitude de faire un `git status` avant et après chaque commit, histoire d'être sur que l'on ne va rien oublier dans le commit.
{% endnote %}

Un `git log --oneline` nous montre que l'on a 3 commits (notez que l'option `--oneline` ne garde que les 7 premiers chiffres de chaque commit).

diff avant le commit pour voir la diff avec ce qui a été enregistré.

### Historique

Vous pouvez voir ce qu'il y avait dans chaque commit, [cette doc](https://git-scm.com/book/fr/v2/Les-bases-de-Git-Visualiser-l%E2%80%99historique-des-validations) vous montre plein de chouettes exemples.

En particulier : `git log -p` qui montre ce que l'on a fait avec chaque commit. Le [format de git diff](https://www.oreilly.com/library/view/git-pocket-guide/9781449327507/ch11.html) est un format étonnamment lisible qui montre distinctement les différences entre les versions.

### Diff

On peut également voir les différences entre le dernier commit et ce que l'on a fait en utilisant la commande [`git diff`](https://git-scm.com/docs/git-diff/fr).

Commençons par modifiez nos fichiers `main.css`{.fichier} et `index.html`{.fichier} :

On ajoute une règle pur les `<h2>` dans `main.css`{.fichier} :

```css
h2 {
  color: blue;
}
h1 {
  color: olive;
}
```

Et un petit paragraphe dans `index.html`{.fichier} :

```html
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8" />
    <title>Ma maison page</title>

    <link href="main.css" rel="stylesheet" />
  </head>
  <body>
    <h1>Hello World !</h1>
    <h2>et bonjour Monde !</h2>
    <p>Comment allez-vous ?</p>
  </body>
</html>
```

La commande `git diff` nous indique les différences entre le dernier commit et ce qeu je n'ai pas encore mis en stage. Donc ici `git diff` nous donne les différences pour `main.css`{.fichier} et `index.html`{.fichier} :

```shell
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

```

Mettons le fichier index.html en stage (`git add index.html`) et refaisons la commande `git diff` :

```shell
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

```

Nous n'avons bien plus que les différences avec _main.css_.

Allez commitons tout ça : `git commit -a -m"h2 rule in css and p in html"`. Notez que le fichier _main.css_ a bien été ajouté au stage avant le commit grâce à l'argument `-a`. Vérifiez le avec `git status` voir même un `git diff`.

{% note %}
La commande `git diff --cached` permet de faire le diff en prenant en compte le stage. Vous avez donc un diff entre le dernier commit et ce que vous avez fait depuis.
{% endnote %}

### Modifier le dernier commit

{% lien "**Documentation**" %}
<https://git-scm.com/book/fr/v2/Utilitaires-Git-R%C3%A9%C3%A9crire-l%E2%80%99historique>
{% endlien %}

Il arrive parfois (souvent) de se rendre compte juste après un commit que l'on a pas tout envoyé (le `git status` n'est pas clean) ou que l'on a fait une faute dans le message accompagnant le commit. C'est pour ça qu'il existe l'argument `--amend` à commit qui vous permet de modifier le dernier commit que vous avez fait.

## Fichier `.gitignore`{.fichier}

Il est impératif qu'avant chaque commit il ne reste aucun fichier non suivi. Cependant, certains fichiers sont pré&sent dans le dossier mais on ne veut pas les inclure dans le projet git. On peut citer :

- les fichiers `.DS_STORE`{.fichier} des macs,
- les fichiers des ide, comme les fichiers `.vscode`{.fichier} de vscode
- les fichiers de bibliothèques, comme le dossier _node_modules_ lorsque l'on fait du web
- ...

Pour que git ignore ces fichiers on utilise un fichier _.gitignore_) qui liste ces fichiers. Son [format](https://git-scm.com/docs/gitignore) est à la fois simple et efficace. On peut même avoir un fichier _.gitignore_ par dossier du projet, donc utilisez le !

Vous trouverez plein d'[exemples de `.gitignore`{.fichier}](https://github.com/github/gitignore), je vous conseille ne pas mettre plein de choses dont vous n'avez pas besoin. Ajoutez des lignes au `.gitignore`{.fichier} uniquement lorsque vous en avez besoin.

Par exemple, après avoir supprimé un fichier via le finder sur mon mac, `git status` me donne ça :

```shell
Sur la branche main
Fichiers non suivis:
  (utilisez "git add <fichier>..." pour inclure dans ce qui sera validé)
  .DS_Store

aucune modification ajoutée à la validation mais des fichiers non suivis sont présents (utilisez "git add" pour les suivre)

```

On va donc créer un fichier `.gitignore`{.fichier} contenant uniquement la ligne `.DS_STORE`{.fichier}, l'ajouter au stage et refaire un `git status` pour obtenir :

```shell
Sur la branche main
Modifications qui seront validées :
  (utilisez "git restore --staged <fichier>..." pour désindexer)
  nouveau fichier : .gitignore
```

On fini par l'ajouter au projet par un commit : `git commit -m"add .gitignore"`.

## Branches

{% lien "**Documentation**" %}
<https://git-scm.com/book/fr/v2/Les-branches-avec-Git-Les-branches-en-bref>
{% endlien %}

Les branches de git permettent d'avoir plusieurs histoires possible de mon projet.

La principale utilisation des branches en développement est :

- l'ajout de nouvelles fonctionnalités. La fonctionnalité n'est ajoutée au main qu'une fois finie. .
- la correction de bug. Une fois le bug corrigé, on ajoute la correction au main.

Ceci nous assure que la branche `main` est **TOUJOURS** un projet fonctionnel.

A part ces branches temporaires, on a parfois besoin de branches plus pérennes comme :

- la gestion des versions différentes de l'application à maintenir
- une branche qui contient le build d'un site web statique par exemple.

La commande `git branch` nous indique les branches que nous avons. Pour l'instant nous n'avons que la branche par défaut : `main`.

### Créer une branche

Nous allons créer une branche pour voir s'il est possible d'ajouter du javascript à notre projet : `git branch js`.

Si l'on refait la commande `git branch`, on voit qu'on a deux branches et qu'on est toujours sur la branche `main`. Allons vers la branche `js` avec la commande : `git switch js`

On peut maintenant tranquillement ajouter du js à notre projet :

- On ajoute le fichier _main.js_

  ```javascript
  let paragraph = document.getElementById("couleur");

  paragraph.addEventListener(
    "mouseenter",
    function (event) {
      event.target.style.color = "purple";
    },
    false
  );

  paragraph.addEventListener(
    "mouseleave",
    function (event) {
      event.target.style.color = "black";
    },
    false
  );
  ```

- et on modifie le fichier _index.html_ :

  ```html
  <!DOCTYPE html>
  <html>
    <head>
      <meta charset="utf-8" />
      <title>Ma maison page</title>

      <link href="main.css" rel="stylesheet" />
    </head>
    <body>
      <h1>Hello World !</h1>
      <h2>et bonjour Monde !</h2>
      <p id="couleur">Comment allez-vous ?</p>

      <script src="main.js"></script>
    </body>
  </html>
  ```

On peut maintenant commiter le tout (en commençant pas ajouter les fichiers _main.js_ et _index.html_ au stage bien sur avec la commande `git add main.js index.html`) : `git commit -m"add js"`.

Un `git log --oneline` nous montre bien que l'on est maintenant sur une nouvelle branche :

```shell
f7907be (HEAD -> js) add js
35609dd (main) add .gitignore
7d2fd72 h2 rule in css and p in html
a3c3fdc add css and link to html
11f5564 add french
3b8c0a8 First commit !
```

### Voir des branches

Si l'on revient à la branche `main` avec la commande `git switch main` on voit que le fichier `main.js`{.fichier} a disparu et que le fichier `index.html`{.fichier} est remis à sa position sans le js.

Faisons une modification du fichier `index.html`{.fichier} de la branche `main` en ajoutant une phrase au paragraphe :

```html
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8" />
    <title>Ma maison page</title>

    <link href="main.css" rel="stylesheet" />
  </head>
  <body>
    <h1>Hello World !</h1>
    <h2>et bonjour Monde !</h2>
    <p>Comment allez-vous ? Bien ou quoi ?</p>
  </body>
</html>
```

Et on commit le tout : `git commit -am"parlons jeune"`

On remarque que la commande `git log --oneline` ne montre que l'histoire du dernier commit, on ne montre donc pas la modification de la branche `js` qui est inutile pour notre dernier commit.

Pour voir tous les log, on peut ajouter l'argument `--all`. Du coup : `git log --oneline --all` donne :

```shell
a2ac886 (HEAD -> main) parlons jeune
f7907be (js) add js
35609dd add .gitignore
7d2fd72 h2 rule in css and p in html
a3c3fdc add css and link to html
11f5564 add french
3b8c0a8 First commit !
```

Et si l'on veut voir le graphe des dépendances on peut ajouter l'argument `--graph` : `git log --oneline --all --graph` :

```shell
* a2ac886 (HEAD -> main) parlons jeune
| * f7907be (js) add js
|/
* 35609dd add .gitignore
* 7d2fd72 h2 rule in css and p in html
* a3c3fdc add css and link to html
* 11f5564 add french
* 3b8c0a8 First commit !
```

### Réconcilier les branches

Si l'on veut maintenant mettre notre branche expérimentale (`js`) dans la branche `main`, il va falloir réconcilier les branches. Cela peut se faire de nombreuses manière mais la méthode couramment utilisée actuellement est celle du [rebase](https://www.miximum.fr/blog/git-rebase/)

Nous allons donc procéder comme suit :

1. depuis la branche `js`, on va la faire commencer à la fin de `main`
2. on va "_merger_" la branche `js` à la suite de la branche `main`.

On aura donc à la fin un joli historique qui fait comme si j'avais ajouter mon `js` à la suite du `main` sans autres branches.

#### Git rebase

Sur la branche `js` on exécute la commande : `git rebase main` et on obtient le résultat :

```text
Fusion automatique de index.html
CONFLIT (contenu) : Conflit de fusion dans index.html
error: impossible d'appliquer f7907be... add js
Resolve all conflicts manually, mark them as resolved with
"git add/rm <conflicted_files>", then run "git rebase --continue".
You can instead skip this commit: run "git rebase --skip".
To abort and get back to the state before "git rebase", run "git rebase --abort".
impossible d'appliquer f7907be... add js
```

En essayant d'ajouter les derniers commits de `main` au début de js, git a un soucis. Il n'arrive pas à le faire tout seul. Il va falloir l'aider.

Son soucis est dans le fichier `index.html`{.fichier}. Regardons le :

```html
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8" />
    <title>Ma maison page</title>

    <link href="main.css" rel="stylesheet" />
  </head>
  <body>
    <h1>Hello World !</h1>
    <h2>et bonjour Monde !</h2>
    <<<<<<< HEAD
    <p>Comment allez-vous ? Bien ou quoi ?</p>
    =======
    <p id="couleur">Comment allez-vous ?</p>

    <script src="main.js"></script>
    >>>>>>> f7907be... add js
  </body>
</html>
```

Horreur, c'est tout cassé. Mais au final c'est compréhensible. Le haut est `HEAD` (donc `main`) et le bas c'est ce que j'ai (la branche `js`). Pour que les deux soient cohérent on modifie le fichier pour qu'il intègre nos modifications conjointes :

```html
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8" />
    <title>Ma maison page</title>

    <link href="main.css" rel="stylesheet" />
  </head>
  <body>
    <h1>Hello World !</h1>
    <h2>et bonjour Monde !</h2>
    <p id="couleur">Comment allez-vous ? Bien ou quoi ?</p>

    <script src="main.js"></script>
  </body>
</html>
```

On peut ensuite l'ajouter au stage pour signifier à git qu'on a résolu son problème : `git add index.html` et on continue jusqu'à la fin ou jusqu'au nouveau problème : `git rebase --continue`. Il n'y a plus d'erreur et on arrive dans `vim` pour donner le message de commit. On laisse celui par défaut et on obtient la jolie liste de commit suivant (`git log --oneline --all --graph`):

```text
* fe850ac (HEAD -> js) add js
* a2ac886 (main) parlons jeune
* 35609dd add .gitignore
* 7d2fd72 h2 rule in css and p in html
* a3c3fdc add css and link to html
* 11f5564 add french
* 3b8c0a8 First commit !
```

On est passé de ça :

```text
A---B---C---D ← main
         \
          F---G ← js
```

à ça :

```text
A---B---C---D ← main
             \
               F'---G' ← js
```

Il ne nous reste plus qu'à fusionner `js` dans `main` (ce qui devrait se faire sans soucis puisqu'elles se suivent). Pour cela :

1. on se place sur la branche `main` : `git switch main`
2. on fusionne la branche `js` sur `main` : `git merge js`

Un `it log --oneline --all --graph` montre que les deux branches sont identique, on peut maintenant supprimer la branche `js` : `git branch -d js`

#### Merge

"_Merger_" revient à fusionner une branche dans une autre. Si les deux branches ne sont pas linéairement dépendante, par exemple comme ça :

```text
A---B---C---D ← main
         \
          F---G ← js
```

Le résultat du merge sera :

```text
A---B---C---D---H ← main
         \     /
          F---G ← js
```

Ce qui induit des "boucle" et n'est pas pratique lorsque l'on veut connaître l'historique du projet. Une droite c'est mieux pour voir ce qu'il s'est passé. Dans l'exemple ci-dessus, un même fichier a pu être modifié en D et en G avant d'être fusionné.

On évitera donc au maximum un merge comme ça et on ne l'utilisera que si les branches sont linéairement dépendante comme çà :

```text
A---B---C---D ← main
             \
              E---F ← js
```

Rendant l'historique lisible et le merge facile (c'est le rebase qui pourra être compliqué)

## Revenir en arrière dans l'historique

Il arrive parfois qu'on a complètement raté un truc et que l'on veuille revenir en arrière dans le projet. C'est super car c'est justement là où git est fort.

Attention cependant, ces opérations modifient l'historique du projet, chose que l'on aime pas trop faire. Il est donc recommandé de ne faire ça que sur des commits qui n'ont pas été publiés sur l'origin.

Je ne vais ici que résumer les possibilités. Allez voir sur
[cette vidéo](https://www.youtube.com/watch?v=ZY5A7kUR0S4) pour avoir un aperçu de ce que l'on peut faire en situation.

Pour l'instant l'historique de notre projet est (`git log --oneline`) :

```text
fe850ac (HEAD -> main, origin/main) add js
a2ac886 parlons jeune
35609dd add .gitignore
7d2fd72 h2 rule in css and p in html
a3c3fdc add css and link to html
11f5564 add french
3b8c0a8 First commit !
```

> C'est quand on veut faire ce genre de chose ou que l'on cherche quand un bug a été introduit dans le projet que l'on est bien content d'avoir mis des message de commit explicite.

Il y a 3 commandes git qui permettent de gérer l'historique [reset, restore et revert](https://git-scm.com/docs/git#_reset_restore_and_revert), chacune a ses spécificités et ses utilités.

> la commande `git reflog` montre tous les commits du projet. Cela peut être super utile si on a fait un `git reset` à un ancien commit et que l'on veut finalement revenir à un endroit dans le futur par rapport à ce commit.

On va voir plusieurs cas pratiques :

- revenir au dernier commit. Le dernier commit est appelé _HEAD_ par git.
  - supprimer des modifications faites à un fichier pour revenir à sa version _HEAD_ : `git restore index.html` par exemple reprend la version du `index.html` du dernier commit de l'historique.
  - vider le stage : `git reset` (ou `git reset HEAD nom_de-fichier` pour un stager un unique fichier).
  - revenir au dernier commit et supprimer toutes les modification faites : `git reset --hard`. Attention cela supprime du code...
- revenir à un commit plus éloignés. On peut y acceder par son numéro ou par une référence par rapport au dernier commit (nommé aussi HEAD). Ainsi HEAD signifie le dernier commit, HEAD~1 l'avant dernier, HEAD~2 l'antépénultième et ainsi de suite.
  - regarder un ancien endroit dans le projet : `git switch 7d2fd72` par exemple crée une nouvelle branche temporaire (nommée _HEAD détachée_) pour voir à quoi ressemblait notre projet au commit _7d2fd72_ (on a bien une règle h2 à notre css). Si l'on a rien modifié, un simple `git switch main` reviendra à l'état courant du projet. Si l'on a modifié des fichiers, il faut commencer par revenir à l'état initial
  - revenir à un commit plus lointain :
    - `git reset numéro_commit` reviendra au commit déterminé mais laissera vos modifications.
    - `git reset numéro_commit --hard` reviendra au commit déterminé mais supprimera vos modifications. Attention vous allez perdre des modifications !
- remettre un seul fichier à un état antérieur : `git switch 7d2fd72 index.html` prend le fichier dans l'état où il était au commit précisé, l'importe à l'état actuel et le met dans le stage, prêt à être commité. Si on ne veut plus de ce fichier, on peut revenir à l'état initial en important le fichier du `main` : `git switch main index.html`
- undo un commit : `git revert 7d2fd72` va créer un commit qui défait un ancien commit (ce commit pouvant être aussi loin que l'on veut). Cela ne change pas l'historique en supprimant le commit undoé, ça rajoute un commit qui le undo.
