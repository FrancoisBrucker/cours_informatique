---
layout: layout/post.njk

title: "Projet : distribuer du code"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Nous allons créer un projet sous github pour que le monde entier puisse l'utiliser s'il le désire.

{% info %}
L'[aide de github](https://docs.github.com/en/get-started) est très bien faite (la traduction en français est cependant automatique, donc souvent approximative), n'hésitez pas à y jeter un coup d'œil.
{% endinfo %}

## Le code

Pour se fixer les idées utilisons ce projet :

{% faire %}
1. Téléchargez le dossier suivant contenant un projet python de 3 fichiers : [le projet Numérologie](https://download-directory.github.io?url=https://github.com/FrancoisBrucker/cours_informatique/tree/main/docs/src/cours/gestion-des-sources/besoins-d%C3%A9p%C3%B4t/projet-d%C3%A9pot/num%C3%A9rologie/num%C3%A9rologie-v1?filename=projet-numérologie-v1)
2. Créez un projet vscode avec ces différents fichiers et exécutez le fichier `main.py`{.fichier}
{% endfaire %}
{% faire %}
Une fois le fichier `main.py`{.fichier} exécuté, **remarquez** qu'un dossier `__pycache__`{.fichier} a été créé. Il correspond à l'import du module `num`{.language-} par le programme principal.
{% endfaire %}


## <span id="création"></span>Créer un projet

1. ![créer un projet](github-créer-un-projet-1.png)
2. ![options du projet](github-créer-un-projet-2.png)

Résultat : ![options du projet](github-créer-un-projet-3.png)

Félicitation vous avez fait votre premier commit !

Chaque **_commit_** est associé à une **_branche_** (ici `main`) et est obligatoirement constitué de :

- du nom de la personne qui a effectué le commit, ici `Test-cours-ecm`
- du numéro du commit, ici `da919d7` (donné automatiquement).
- d'un message (d'une ligne) décrivant le commit, ici `initial commit`

### Fichier `readme.md`{.fichier}

Le fichier n'est cependant pas celui qu'on veut :

{% faire %}
Éditez le fichier `README.md`{.fichier} :

![éditer readme](./editer-readme.png)

Puis cliquez sur le gros bouton vert `commit changes` pour voir apparaître cette fenêtre :

![commit readme](./commit-readme.png)

Puis cliquez sur `commit changes`.
{% endfaire %}

Un deuxième commit !

### Upload des fichiers

Il nous reste à mettre les fichiers sur le dépôt :

{% faire %}
Sur la page de votre projet, à gauche du bouton vert `code`, il y a un menu déroulant `add file`. Cliquez dessus et uploadez les 3 fichiers pythons :

![upload](./upload.png)

Puis commitez vos ajouts.
{% endfaire %}
{% attention %}
Il e faut pas uploader le dossier `__pycache__`{.fichier} qui est créé à l'exécution : 

**On ne met sur github que les fichiers sources de votre projet, pas les fichiers générés.**

{% endattention %}

Sur la page de votre projet, sur la droite, vous voyez un lien `activity`. En cliquant dessus vous voyez les différents commits effectués :

![liste commis](./liste-commits.png)

## Tag

En cliquant sur le lien tag sur la fenêtre :

![tag](./tag.png)

On vous proposera de créer une nouvelle release. 

{% faire %}
1. commencez par créer un nouveau tag que vous nommerez `release-1`
2. donnez un titre à notre release, par exemple `1.0`
3. commitez votre release !

{% endfaire %}

Ceci a créé une release, notre 1.0. Pour la voir, cliquez sur le lien release :

![lien release](./lien-release.png)

## V2

Après quelque temps de travail, on est arrivé à une nouvelle version publiable :

{% faire %}
1. Téléchargez le dossier suivant contenant un projet python de 3 fichiers : [le projet Numérologie](https://download-directory.github.io?url=https://github.com/FrancoisBrucker/cours_informatique/tree/main/docs/src/cours/gestion-des-sources/besoins-d%C3%A9p%C3%B4t/projet-d%C3%A9pot/num%C3%A9rologie/num%C3%A9rologie-v2?filename=projet-numérologie-v2)
2. Créez un projet vscode avec ces différents fichiers et exécutez le fichier `main.py`{.fichier}
{% endfaire %}

Il nous faut mettre à jour le projet sur github :

{% faire %}
Ulpoadez les fichiers de la v2.
{% endfaire %}

La fenêtre principale de votre projet doit ressembler à quelque chose du type :

![v2 upload](./upload-v2.png)

Vous remarquerez que :

- on a maintenant 4 commit
- que le fichier `teste.json`{.fichier} a été ajouté
- que le fichier `main.py`{.fichier} a été modifié
- que les deux autres fichiers (`num.py`{.fichier} et `test_num.py`{.fichier}) n'ont pas changé entre les deux versions.

Voyons ce qui a changé dans le fichier `main.py`{.fichier} :

{% faire %}

Cliquez sur le lien `main.py`{.fichier} depuis la fenêtre principale du projet :

![main](./v2-main.png)
{% endfaire %}

Vous devriez voir le fichier `main.py`{.fichier} que vous avez uploadé.
   
{% faire %}
Cliquez sur le lien history :

![main](./v2-main-history.png)
{% endfaire %}

Vous devriez voir les différents commits où ce fichier a été modifié.

{% faire %}
Cliquez sur le numéro du dernier commit :

![main](./v2-main-commit.png)
{% endfaire %}
{% info %}
Voir [ce doc](https://www.designveloper.com/blog/hash-values-sha-1-in-git/) pour voir comment git associe chaque commit à un sha pour le retrouver.
{% endinfo %}


Vous devriez voir un "_diff_" entre la v1 et la v2 pour le commit :

- en rouge ce qui a disparu
- en vert ce qui a été ajouté

Et ce pour chaque fichier mis à jour pour ce commit.

On termine en faisant une seconde release :

{% faire %}
Faite la release v2 du projet. Vous utiliserez **un autre** tag que pour la v1 ainsi qu'un nouveau titre.
{% endfaire %}

