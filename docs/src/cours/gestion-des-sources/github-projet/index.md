---
layout: layout/post.njk
title: Projet github

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

On va utiliser l'interface de github pour mettre en œuvre les principales fonctionnalités d'un système de gestion des sources :

- faire des commit
- gérer des branches
- fusionner des branches en résolvant des conflits
- voir l'historique du projet
- comment ajouter des membres à un projet

{% info %}
L'[aide de github](https://docs.github.com/en/get-started) est très bien faite (la traduction en français est cependant automatique, donc souvent approximative), n'hésitez pas à y jeter un coup d'œil.
{% endinfo %}

## Créer un projet

1. ![créer un projet](github-créer-un-projet-1.png)
2. ![options du projet](github-créer-un-projet-2.png)

Résultat : ![options du projet](github-créer-un-projet-3.png)

Les _commit_ sont les mises à jour du projet.

{% note %}

Chaque **_commit_** est associé à une **_branche_** (ici `main`) et est obligatoirement constitué de :

- du nom de la personne qui a effectué le commit, ici `Test-cours-ecm`
- du numéro du commit, ici `da919d7` (donné automatiquement).
- d'un message (d'une ligne) décrivant le commit, ici `initial commit`

{% endnote %}
{% info %}
Voir [ce doc](https://www.designveloper.com/blog/hash-values-sha-1-in-git/) pour voir comment git associe chaque commit à un sha pour le retrouver.
{% endinfo %}

## Faire des commits

### Ajout de fichiers

1. ![ajout de fichier](github-ajout-fichier-1.png)
2. ![texte dans l'interface](github-ajout-fichier-2.1.png)
3. ![le commit](github-ajout-fichier-2.2.png)
4. ![le résultat](github-ajout-fichier-3.png)

{% info %}
On a utilisé <https://gitmoji.dev/> pour le commit. Mettre un émoji en premier caractère du message permet de facilement identifier le but du commit.
{% endinfo %}

Notre projet a maintenant 2 commits. En cliquant sur le texte _32 commits"_, on voit l'historique de notre projet sur la branche principale (`main`) :

![historique](github-historique-main.png)

En cliquant sur le numéro de commit, on voit le détail de celui-ci :

![historique](github-historique-main-détail.png)

Nous rentrerons plus en détails de ce tout cci signifie un peut plus tard. Mais La façon dont est représenté le commit suit la syntaxe des [GNU `diffutils`](https://www.gnu.org/software/diffutils/manual/diffutils.html). Pour nous :

1. on a modifié le fichier `programme.txt`{.fichier}
2. `@@ -0,0 +1, 6 @@` : on a supprimé aucune ligne et on a ajouté les lignes 1 à 6.
3. à droite on voit les lignes ajoutées en vert avec un `+` devant elles

### Modifier un fichier

Nous allons maintenant modifier le fichier `readme.md`{.fichier} qui est aussi un fichier texte écrit au format [Markdown]({{ "/tutoriels/format-markdown.md"  }}). POur que ce fichier soit agréable à la lecture, github le compile en html, mais — en vrai — c'est juste du texte.

1. ![cliquer pour accéder au fichier `readme.md`](github-modification-readme-1.png)
2. ![cliquer pour éditer le fichier `readme.md`](github-modification-readme-2.png)
3. ![édition du fichier `readme.md`](github-modification-readme-3.png)
4. ![modification du fichier `readme.md`](github-modification-readme-4.1.png)
5. ![commit du fichier `readme.md`](github-modification-readme-4.2.png)

Notre nouveau commit :

1. Notre fichier modifié est maintenant ![fichier](github-modification-readme-5.1.png)
2. Son historique montre qu'il a été modifié par 2 commit ![fichier](github-modification-readme-5.2.png)
3. Le dernier commit a modifié son contenu ![fichier](github-modification-readme-5.3.png)

L'index qui permet de voir les différences entre ce qu'on a sauvegarder et ce qu'on va ajouter. L'index est transparent pour l'instant mais plus on progressera plus il sera visible.

> TBD voir le diff.

## Changer de branche

Je suis content de mon projet, mais soit :

- j'aimerai tester des modifications sans être sûr de les conserver
- j'aimerai corriger un bug mais sa correction risque de prendre un peu de temps

De plus, je ne voudrai pas juste travailler dans mon coin et tout commiter une fois que ce sera fini car :

- le travail risque de prendre du temps et plusieurs commits
- si je travaille dans mon coin, lorsque j'aurai fini, les autres membres du projets auront certainement modifié le code.

La solution à ce problème consiste à ajouter **une branche** au projet.

### Création d'une nouvelle branche

1. ![branches](github-branches-1.png)
2. On clique :
   - pour ajouter une nouvelle branche : ![ajout d'une branche](github-branches-2.1.png)
   - on indique son nom et la branche à copier : ![paramètres de la branche](github-branches-2.2.png)
3. On peut maintenant changer de branche :
   - on retourne à la page de gestion de projet et on voit qu'on a 2 branches : ![plusieurs branches](github-branches-3.1.png)
   - passage sur une autre branche : ![passage à la nouvelle branche](github-branches-3.2.png)

### Travail sur la nouvelle branche

1. ajout d'un fichier : ![ajout fichier](github-feature-1.png)
2. modification d'un fichier : ![modification](github-feature-2.png)

On obtient alors les commits sur la branches feature :

![commits sur la branche feature](github-feature-3.png)

Les 3 premiers commits sont communs à la branche main (allez dans _"insights/network"_ pour voir le graphe de dépendances) :

![graphe de dépendances](github-feature-4.png)

Pour bien voir que les branches sont indépendantes, ajoutons un commit sur la branche main, en modifiant le fichier `programme.txt`{.fichier} :

![ajout commit dans la branche main](github-feature-5.png)

Le graphe de dépendance à maintenant deux histoires qui divergent :

![graphe de dépendances suite](github-feature-6.png)

### Fusion de branches

Notre feature est terminée, nous voulons ajouter ses modifications dans la banche main. Ceci n'est pas possible directement car il y a également eu des modifications dans la branche main.

Il faut amener les modifications de la branche `feature` dans la branche `main` sans tout casser. Git permet de faire ceci avec deux opérations :

- merge
- rebase

#### merge

La situation actuelle est celle-ci :

```text
main : A -> B -> C -> F
                  \
feature :          -> D -> E

```

Et nous voulons arriver à ceci :

```text
main : A -> B -> C -> F ----> G
                  \          /
feature :           -> D -> E

```

Il faut fusionner (`merge`) la branche `feature` dans la branche `main` puis supprimer `feature` car elle n'est plus utile.

Pour cela :

1. on va créer une `pull request` : ![pull request](github-merge-1.png)
2. ce qu'on veut : ![pull request](github-merge-2.png)
3. ce n'est pas possible de faire ça automatiquement car il y a des mélanges de lignes : ![pull request diff](github-merge-3.png) L'ajout de fichier s'est passé sans problème en revanche, git le fait tout seul.
4. On clique sur `create pull request` pour créer la requête : ![requête créée](github-merge-4.png)
5. En cliquant sur la requête, on voit qu'elle ne peut être résolue automatiquement : ![requête conflits](github-merge-5.1.png)
6. Qui sont dans le fichier `programme.txt`: ![requête conflits diff](github-merge-5.2.png)
7. Chaque conflit (il peut y en avoir plusieurs par fichier) est toujours représenté comme ça :

```text
<<<<<< [nom d'une branche ou d'un commit]
[contenu de la branche]
====== autre branche
[contenu de l'autre branche]
>>>>>> [nom de l'autre branche ou de l'autre commit]
```

Résoudre un confit consiste à choisir une branche ou à faire un mélange des branches pour arriver à un texte sans les `<<<<<<`, `>>>>>>` et `=====`. Puis cliquez sur `mark as resolved Pour notre problème : ![résolution](github-merge-6.png)

Une fois la fusion exécutée, notre graphe de dépendance est :

![graphe de dépendance après fusion](github-merge-7.png)

On peut alors supprimer la branche `feature` qui ne nous est plus d'aucune utilisée. On ne peut donc plus faire de commits sur cette branche, mais son existence est conservée dans l'historique :

![graphe de dépendance suppression de la branche](github-merge-8.png)

#### annuler un commit

L'opération `revert` permet de revenir en arrière et d'annuler un commit ou un _"pull request"_ (le commit fautif n'est pas supprimé).

{% note %}
Supprimer un commit n'est pas une opération recommandée lorsque des collaborateur ont pu avoir accès à celui-ci. Cela les désynchroniseraient. On préfère faire un `commit revert` qui crée un commit qui revient en arrière : on ne supprime pas le commit fautif, on l'annule en refaisant le contraire de ce qu'il a fait. Ceci assure que les utilisateurs restent synchronisés.

{% endnote %}

Nous allons ici _annuler_ notre pull request :

1. ![pull request revert 1](github-revert-1.png)
2. ![pull request revert 2](github-revert-2.png)
3. ![pull request revert 3](github-revert-3.png)

Nous venons de créer une `pull request` pour supprimer une pull request. On peut maintenant la résoudre :

![pull request revert 4](github-revert-4.png)

Et on se retrouve comme avant le merge, avec un graphe de dépendance encore un peu plus compliqué :

![pull request revert 5](github-revert-5.png)

Git se débrouille tout seul

### Rebase

Pour éviter des fusions de branches inutiles et conserver un historique aussi linéaire que possible, à la place de fusionner un pull request, vous pouvez effectuer un rebase.

Pour que cela soit possible, il faut que vous modifiez les préférences de votre projet :

![préférences](./préférences-projet.png)

Puis scrollez jusqu'à la partie sur les pull request pour cocher les diverses options disponibles :

![préférences](./préférences-rebase.png)

{% lien %}
[documentation github](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/configuring-pull-request-merges/configuring-commit-rebasing-for-pull-requests)
{% endlien %}

> TBD faire un modification (demander à un élève de le faire et de prendre n screen de la modif effectuée)

Si vous cliquez sur le triangle à droite du bouton vous verrez le pop-up :

![merge pull request](./merge-defaut.png)

Choisissez rebase :

![rebase pull request](./rebase-pull-request.png)

Puis appliquez la pull request. Si vous retournez dans la vision des commits et des branches, vous verrez que votre pull request a été ajouté linéairement :

> TBD un screen

{% attention "**À retenir**" %}
Préférer toujours faire un rebase lorsque c'est possible, un historique linéaire est toujours mieux qu'une succession de fusions pour pouvoir plus tard s'y retrouver lorsqu'il faudra corriger un bug.
{% endattention %}

## Ajouter des collaborateurs au projet

C'est très facile :

1. ![ajout-1](github-ajout-1.png)
2. ![ajout-2](github-ajout-2.png)
3. sur le compte invité, on peut accepter l'invitation : ![ajout-3](github-ajout-3.png)
4. de retour dans l'interface du projet, on voit les collaborateurs : ![ajout-4](github-ajout-4.png)

Toutes les personnes peuvent maintenant ajouter et modifier des fichiers.
