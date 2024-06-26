---
layout: layout/post.njk
title: "Projet numérologie / partie 1 : front / niveau 2 / préparation"

authors:
    - "François Brucker"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

<!-- début résumé -->

Ajout d'outils de gestion de projet.

<!-- fin résumé -->

## Prérequis

Suivez la partie [préparation du niveau 1](../../niveau-1/1-preparation){.interne} jusqu'à la fin.

## Code

Nous allons avoir plusieurs dossiers dans le projet, chacun étant dédié à une partie spécifique (test, user stories, code, ...). La partie relative au site sera placé dans un dossier `site`{.fichier} dans le dossier du projet.

## Outils de gestion de projet

Les outils de gestion de projet que l'on va voir ici sont destinés à être utilisé pour un projet allant d'1 développeur à une petite équipe de développement. Toutes ces méthodes sont éprouvées.Vous ne pourrez vous considérer comme développeur que lorsque vous utiliserez ces méthodes de façon fluide.

### User stories

Lorsque l'on code un site, une page web ou n'importe quoi d'autre il faut que l'on sache comment ça va être utilisé.

Notre site doit répondre à un certains nombre de besoins identifiés et qui doivent être facilement assouvis. Pour cela on rédige des [**user stories**](https://fr.wikipedia.org/wiki/R%C3%A9cit_utilisateur) (au moins une par besoin) qui vont décrire comment un utilisateur ayant un besoin précis va l'assouvir avec notre code. Souvent ces besoins utilisateurs sont liées à un ou plusieurs **tests fonctionnels** qui vont décrire précisément comment un
utilisateur va faire pour réaliser sa user story.

{% info %}
Nous verrons dans les niveaux supérieurs comment automatiser ces tests. Pour l'instant on va juste les conserver pour s'en rappeler.
{% endinfo %}

### Todos

Lorsque vous n'êtes pas en TD où on vous dit exactement quoi faire, réaliser un projet peut être assez déroutant. Il y a trop de choses à faire et à se rappeler.

Nous allons utiliser ici une gestion ds tâches à faire sous la forme de todos. On va lister tout ce qu'il faut faire pour réaliser le projet et à chaque fois réaliser la tâche la plus facile à faire. Cette liste est dynamique, on va ajouter et supprimer plein de tâches lors du projet.

{% note %}
L'essentiel est de conserver la tâche courante et tout ce que l'on pense devoir encore faire avant la réalisation du projet.
{% endnote %}

### Tests unitaires

Coder, c'est rajouter des bugs dans un programme. Normalement tout développeur va vérifier plus ou moins bien que ce qu'il vient juste d'écrire fonctionne, puis une fois vérifié va supprimer les tests : **C'est complètement stupide !**. En effet :

* lorsqu'il modifiera son code, il devra tout recommencer (trouver des tests, les réaliser, puis à nouveau tout effacer)... Et plus il refera cette opération moins il testera
* lorsque le code qu'on écrit devient gros, c'est les interactions entre les parties qui va poser problème, pas juste le code qu'on vient d'écrire. En toute logique il faut donc tester toute l'application à chaque ligne de code écrite.

{% note %}
Nous allons ici juste prendre en compte le problème, c'est aux niveaux ultérieurs lorsque vous maîtriserez des outils de gestion de projet que l'on automatisera tout ça.
{% endnote %}

## Écrire du texte avec markdown

Écrire les user stories et gérer nos todos ne peut se faire qu'en écrivant du texte structuré (avec des chapitres, des titres, des listes, etc).  On ne peut cependant pas se permettre d'ouvrir un gdoc ou un word à chaque fois :

* ça prend trop de temps
* les users stories et les todos font partie du projet, il doivent pouvoir être géré avec un gestionnaire de sources

Heureusement, il existe plusieurs *langages* qui permettent d'écrire du texte structuré dans un éditeur de texte et qui sont jolis même en texte. Nous allons utiliser le [markdown]({{"/tutoriels/format-markdown" | url}}).

### Fichiers de user stories

{% faire %}
Ajoutez un dossier `user-stories`{.fichier} à votre projet.
{% endfaire %}

Vous pouvez ajouter ce dossier avec l'explorateur de fichier de ordinateur ou directement avec vscode :

1. *menu Affichage > Explorateur* pour amener le gestionnaire de fichier de vscode.
2. cliquez sur le nom de dossier du *workspace* (`numérologie-niveau-X`{.fichier})
3. une fois le dossier sélectionné, vous pouvez cliquer sur l'icône du dossier avec un petit +
4. écrivez "user-stories" puis appuyez sur entrée

#### Actions sur le site

Créez un fichier nommé `connaître-son-numero.md`{.fichier} à l'intérieur du dossier `user-stories`{.fichier} (cliquez droit sur le nom du dossier, puis "new file") où vous écrirez :

```
# Connaître son numéro

## Page générale

1. je rentre mon nom dans un champ texte : François puis j'appuie sur la touche entrée.
2. En dessous du champ texte, on affiche alors Bonjour François, votre numéro est le X

## Style 

X est écrit en gros au milieu de la page. Avec, si possible une fonte rigolote.
```

Créez un fichier nommé `url-numero.md`{.fichier} à l'intérieur du dossier `user-stories`{.fichier} (cliquez droit sur le nom du dossier, puis "new file") où vous écrirez :

```
# Url du numéro

<http://localhost/prénom/XXXX>

Le retour de cette url doit être le numéro associé au prénom : XXXX
```

{% info %}
Remarquez quand vous tapez entrée après avoir écrit le premier item ça passe de suite à 2 ? C'est markdown all in one qui est à la manœuvre.
{% endinfo %}

Dans la palette de commande (*menu Affichage > Palette de commandes...*), regardez tout ce que l'on peut faire en tapant "markdown".

{% faire %}
Par exemple essayez : *Markdown All in One: Print current document to html*
{% endfaire %}

Votre markdown a magiquement été transformé en un joli html que vous pouvez ouvrir avec votre navigateur préféré (c'est tellement beau que j'en ai les larmes aux yeux). Vous pouvez supprimer ce fichier html en lui cliquant droit dessus puis : *delete file*.

{% note %}
Ces user stories sont importantes pour garder en mémoire le but qu'on se fixe. Il ne faut pas hésiter à en ajouter, les modifier au cours du projet.
{% endnote %}

### <span id="todos"></span> Todos

{% faire %}
Créez un dossier `todos`{.fichier} et à l’intérieur de celui-ci un fichier `todos.md`{.fichier}
{% endfaire %}

On va ajouter nos liste des taches à faire, et marquer ces tâches effectuées lorsqu'elles sont réalisées. Le projet sera fini lorsqu'il n'y aura plus de tâche dans le todo.

{% info %}
On nettoiera de temps en temps le fichier en supprimant les lignes effectuée pour garder une taille raisonnable de fichier.
{% endinfo %}

Fichier `todos/todos.md`{.fichier} :

```
# Todos

On mettra un 'X' dans la checkbox pour l'item courant
on ~~barrera~~ lorsque cette item sera réalisé

* [ ] associer un chiffre à un nom
* [ ] créer un champ texte dans un fichier html
* [ ] récupérer en html le contenu d'un champ texte lorsque l'on appuie sur la touche entrée
* [ ] modifier l'arbre DOM avec du texte
* [ ] récupérer un info de l'url et la traiter
```

## Fin

On est prêt, on peut commencer la suite.
