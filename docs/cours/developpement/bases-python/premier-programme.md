---
layout: page
title:  "Bases de python : premier programme"
author: "François Brucker"
---

[développement]({% link cours/developpement/index.md %}) / [bases de python]({% link cours/developpement/bases-python/index.md %}) / [premier programme]({% link cours/developpement/bases-python/premier-programme.md %})


## projet vsc

Créez un dossier nommé *"cours-python"* sur votre ordinateur, et ouvrez le avec vscode (*menu Fichier > ouvrir...*). Une fois que vous avez dit que vous faisiez confiance au développeur de ce projet, fermez l'onglet *Welcome*. Vous pouvez même fermer l'explorer en cliquant sur l'icone en sur-brillance dans la barre d'activité de [l'interface vsc](https://code.visualstudio.com/docs/getstarted/userinterface).

Nous allons commencer par utiliser le [le terminal intégré]({% post_url tutos/editeur/vsc/2021-09-14-vsc-terminal %}#terminal-integre) de vscode pour exécuter nos premiers programmes python avant d'écrire nos programmes de plusieurs lignes.

## interpréteur python et espace de noms

Ouvrez un terminal dans vscode (le [terminal]({% post_url /tutos/systeme/2021-08-24-terminal %}) permet d'exéctuer des commandes de votre système) : *menu Affichage > Terminal*.

Vous pouvez ensuite taper `python` sous windows ou `python3` sous linux et mac pour rentrer dans l'interpréteur python :

![interpreteur]({{ "/assets/cours/developpement/python-interpreteur.png" | relative_url }}){:style="margin: auto;display: block}

L'interpéteur est le cœur de python. Tout programme python est exécuté de la même manière :

1. on entre une ligne de code dans l'interpréteur
2. l'interpréteur exécute cette ligne dans son *espace de noms global* (*global namespace*)
3. une fois la ligne exécutée, l'interpréteur redonne la main à l'utilisateur
4. retour à la l'étape 1.

Un *espace de noms* est un endroit où seront stockées les différentes variables par exemple. C'est tout ce dont il faut se souvenir pour les futures lignes de code. A chaque fois que l'on exécute l'interpréteur, un nouvel *espace de noms global* est crée et une fois que l'on stoppe l'interpréteur, cet *espace* est détruit.

> Le fait qu'un espace de nom existe est crucial pour pouvoir utiliser des variables et le fait qu'il soit créé au début du programme (au lancement de l'interpréteur) détruit une fois le programme terminée (une fois que l'interpréteur s'arrête) permet d'assurer qu'un programme donnera toujours le même résultat (si l'espace de noms etait toujours le même il resterait des variables d'un ancien programme dans un nouveau...).

### une première ligne de python

Dans l'interpréteur (à côté des `>>>`, qu'on appelle [invite de commande ou prompt](https://fr.wikipedia.org/wiki/Interface_en_ligne_de_commande)), tapez :

```python
print("Bonjour monde !")
```

Puis appuyez sur la touche entrée. Vous devriez avoir quelque chose du genre à la sortie :

![hello world]({{ "/assets/cours/developpement/python-hello-world-interpreteur.png" | relative_url }}){:style="margin: auto;display: block}

Ca a l'air d'avoir marché. La ligne de code a affiché à l'écran `Bonjour Monde`, puis l'invite de commande est revenue (une fois l'instruction exécutée, on attend la suivante).

### commentaires

Essayons maintenant de taper ça :

```python
# print("Bonjour monde !")
```

Ca a l'air de n'avoir rien fait. C'est parce que le caractère `#` est considéré comme un début de commentaire. Tout ce qui suit ce caractère est ignoré.

> **pour aller plus loin** :
> Vous devriez pouvoir répondre aux questions suivante à la fin de cette partie. Pourquoi est-ce que :
>
> * `print#("Bonjour monde !")` rend `<built-in function print>`
> * `print("Bonjour #monde !")` rend `Bonjour #monde !`

### quitter l'interpréteur

```python
`quit()`
```

## exécution d'un fichier dans l'interpréteur

Créez un fichier *"programme.py"* (*menu Fichier > New File* puis sauvez le immédiatement *menu Fichier > Save*).

> Si vous n'avez pas encore configuré python, vscode va vous demander de configurer son [environnement python]({% post_url /tutos/systeme/2021-08-24-terminal %}).

Tapez dans le fichier ouvert  dans vscode :

```python
print("Bonjour monde !")
```

Vous pouvez alors l'exécuter :

* dans le terminal en tapant : `python3 programme.py`
* en cliquant sur [le triangle en haut à droite de la fenêtre vsc](https://code.visualstudio.com/docs/python/python-tutorial#_run-hello-world)

Remarquez que lorsque vous exécutez votre programme via la seconde solution, cela crée un nouveau terminal qui s'appelle *Python*.

![hello world]({{ "/assets/cours/developpement/python-interpreteur-execution-python.png" | relative_url }}){:style="margin: auto;display: block}

> L'interpréteur python utilisé pour la seconde méthode est celui du paramètre `python.defaultInterpreterPath` qui devrait être le même que lorsque vous tapez juste `python` dans un terminal.

