---
layout: layout/post.njk
title: "Projet numérologie / partie 1 : front / niveau 1 / préparation"

authors:
    - "François Brucker"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

<!-- début résumé -->

Numérologie partie 1 - niveau 1 : Préparation.

<!-- fin résumé -->

Avant de se lancer à corps perdu dans le développement et le code, vérifions que nous avons tous les outils nécessaires.

## Outils

D'après les prérequis du projet, vous avez :

* [vscode](https://code.visualstudio.com/)
* [node](https://nodejs.org/en/) que vous pouvez exécuter dans [un terminal](/cours/coder-et-développer/ordinateur-développement/terminal/){.interne}

## Projet

Commencez par vos familiariser avec vscode si ce n'est déjà fait grâce à [ce tutoriel](/cours/coder-et-développer/éditeur-vscode/prise-en-main/){.interne}. On supposera par la suite que vous avez lu et fait les installations de ce tutoriel.

Nous allons préparer le projet dans lequel nous allons coder. Ceci se fait avec vscode en ouvrant un dossier. Ce dossier sera le départ de votre projet et s'appelle *workspace*.

1. Commencez par créer le dossier `numérologie`{.fichier}
2. dans vscode, choisissez : "*Menu File > open*" puis naviguez jusqu'à votre dossier `numérologie`{.fichier}. On vous demande si vous faites confiances aux auteurs, puisque c'est vous dites oui.

{% info %}
Lorsque l'on code et que l'on ne veut pas de problèmes en développement, les noms de fichiers doivent êtres sans espaces et sans accents.
{% endinfo %}

On va créer notre premier fichier javascript : *menu Fichier > Nouveau Fichier* et sauvez le de suite : *menu Fichier > Enregistrer* avec le nom `mes_tests.js`{.fichier}.

Vscode à compris que c'était du javascript, il l'écrit dans la barre de statut (la dernière ligne, en bleu, de la fenêtre vscode, voir [user interface](https://code.visualstudio.com/docs/getstarted/userinterface)). Commençons notre voyage dans le monde merveilleux de la programmation web serveur, en écrivant notre premier programme javascript dans le fichier `numérologie/"mes_tests.js`{.fichier} :

```javascript
let nom = "monde"

console.log("bonjour " + nom + " !")
```

{% faire %}
Puis sauvez le fichier (*menu Fichier > Enregistrer*).
{% endfaire %}

### Exécution du code

Tapez ">terminal" dans [la palette de commande](/cours/coder-et-développer/éditeur-vscode/prise-en-main/#palette-de-commande){.interne} (*menu Affichage >  Palette de commandes...*)/ et choisissez la commande *Open New External Terminal*.

Un nouveau terminal s'ouvre directement dans le dossier de votre projet. Magique non ?

{% faire %}
Vous pouvez maintenant exécuter votre fichier en tapant dans ce nouveau terminal : `node mes_tests.js`.
{% endfaire %}

N'oubliez pas non plus [le terminal de vscode](/cours/coder-et-développer/éditeur-vscode/terminal/){.interne}, ouvrez le (*"menu Affichage > Terminal"*) et exécutez votre code comme précédemment.
