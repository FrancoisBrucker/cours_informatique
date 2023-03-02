---
layout: layout/post.njk 
title:  "Projet numérologie : partie 1 / niveau 4 / préparation"
category: cours
author: "François Brucker"
---

> [numérologie]({% link cours/web/projets/numérologie/index.md %}) / [partie 1]({% link cours/web/projets/numérologie/partie-1-front/index.md %}) / [niveau 4]({% link cours/web/projets/numérologie/partie-1-front/niveau-4/index.md %}) / [préparation]({% link cours/web/projets/numérologie/partie-1-front/niveau-4/1-preparation.md %})
{.chemin}

Initialisation du projet git.

## prérequis

Suivez les parties [installation]({% link cours/git_et_github/index.md %}#installation) et [configuration]({% link cours/git_et_github/index.md %}#configuration) du cours [git et github]({% link cours/git_et_github/index.md %}).

Vous être prêt à utiliser git.

> vous pourrez lire [le cours git]({% link cours/git_et_github/index.md %}), en particulier les usages de git, cela vous donnera une plus grande connaissance de ce que l'on va faire.

## initialisation du projet

Avant de commencer notre projet on va créer un nouveau *repository* sur github qui s'appellera "numérologie".

Suivez ce [tuto](https://docs.github.com/en/get-started/quickstart/create-a-repo) pour créer le projet numérologie. Vous devriez obtenir une page du genre :

![projet github fraichement créé]({{ "/assets/cours/web/numérologie/partie-1-niveau-4-projet-github.png" | relative_url }}){:style="margin: auto;display: block}

Editez ensuite le fichier readme.md pour y a jouter la ligne :

```text
Voyez la vie en base 10.
```

En vas de la page, vous voyez la page pour commiter ses changements, cliquez sur le bouton vert *Commet changes*.

Il nous reste maintenant à cloner le projet sur notre ordinateur. Suivez [ce tuto]({% link cours/git_et_github/git_commands.md %}#clone-projet) pour pour le faire.

> Lorsque vous allez cloner votre projet, il va créer un dossier *"numérologie"* dans lequel sera votre projet.
{:.attention}

## ajout du fichier

Suivez la partie [préparation du niveau 1]({% link cours/web/projets/numérologie/partie-1-front/niveau-1/1-preparation.md %}) jusqu'à la fin.

## premier commit

Lorsque l'on fait des commit avec git, on va toujours avoir le même workflow :

1. `git status` : pour vérifier ce qui est nouveau
2. `git add --all` : pour ajouter les nouveau fichiers (ou on ajoute juste les nouveaux fichiers voulus)
3. `git commit -am"message de commit"` : pour enregistrer les modifications et inclure un message qui résume ce qu'on a fait

Le message du commit doit être informatif. Cela permettra de voir ce qui a été fait lorsque l'on regardera l'historique des commits.

> Il ne faut pas qu'un commit regroupe trop de changements sinon ça ne sert à rien : il faut qu'un commit regroupe une unité thématique, une chose sur laquelle on travaillait et qui est finie, ou quelque chose sur laquelle on a bien avancé.

Commençons le workflow pour l'état actuel de notre projet :

### git status

Le résultat de `git status` :

```shell
On branch main
Your branch is up to date with 'origin/main'.

Untracked files:
  (use "git add <file>..." to include in what will be committed)
    mes_tests.js

nothing added to commit but untracked files present (use "git add" to track)
```

Il y a un nouveau fichier, `mes_test.js` qui n'a pas encore été ajouté. Tous les fichiers non encore ajouté doivent être ajouté au projet on ajoute donc tout en une fois en tapant la commande :

```shell
git add --all
```

> S'il existe des fichiers que ne veut pas ajouter dans le projet, autant les mettre dans le fichier [.gitignore](https://git-scm.com/docs/gitignore)

Le `git status` dit maintenant :

```shell
On branch main
Your branch is up to date with 'origin/main'.

Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
    new file:   mes_tests.js
```

Il n'y a plus rien à ajouter. On peut faire le commit : `git commit -am"ajout des tests"`. Le résultat de cette commande est alors :

```shell
[main 78ef52e] ajout des tests
 1 file changed, 3 insertions(+)
 create mode 100644 mes_tests.js
```

et le `git status` :

```shell
git status                     
On branch main
Your branch is ahead of 'origin/main' by 1 commit.
  (use "git push" to publish your local commits)

nothing to commit, working tree clean
```

On a fini notre commit. Tous les changements ont été conservé localement.

> En toute logique, on aurait pu uniquement taper la commande : `git commit -m"ajout des tests"` car il n'y avait pas de fichiers modifiées, mais la commande `git commit -am"message"` sera une commande que nous taperons par défaut, donc autant l'utiliser pour nous la mettre dans les doigts.

### synchronisation avec le serveur

`git push` va envoyer les modification au serveur. Selon le mode d'authentifications, vous aurez besoin soit de votre clé ssh, soit d'un token pour vous connecter à github.

Vous pouvez regarder la page du projet numérologie sur le site de github, vous devriez voir le fichier ajouté.
