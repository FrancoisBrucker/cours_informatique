---
layout: layout/post.njk

title: Vsc et terminal

eleventyNavigation:
  prerequis:
    - "../../../bases-programmation/éditeur-vscode/"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Les différentes manières d'invoquer un terminal avec [visual studio code](https://code.visualstudio.com/). C'est un condensé de la documentation officielle qui bien plus complète :

{% lien %}

<https://code.visualstudio.com/docs/editor/integrated-terminal>
{% endlien %}

## Palette de commande

Si vous tapez `>terminal` dans [la palette de commande](../prise-en-main#palette-de-commande){.interne}, vous verrez toutes les commandes qui ont terminal dans leur nom. Il y a des commandes spécifiques à un langage (javascript, python, etc) et certaines très générales comme : _Open New External Terminal_ qui ouvre un terminal dans le dossier de votre projet.

## <span id="terminal-intégré"></span> Intégration dans vscode

### Ouvrir un terminal

On peut ouvrir un terminal dans : _menu Terminal > nouveau Terminal_ :

![nouveau terminal](./vscode-nouveau-terminal.png)

Ce qui donne quelque chose du type :

![terminal dans vscode](./vscode-terminal.png)

Les différents panels du dessus du terminal (`PROBLEMES`, `OUTPUT`, `CONSOLE DE DEBOGAGE` et `TERMINAL`) dans vscode sont des sorties d'autres processus.

on reste donc 99% du temps sur `TERMINAL` (qui est en sur-brillance).

### Supprimer un terminal

On peut supprimer (en cliquant sur la poubelle) et créer (_menu Terminal > Nouveau terminal_) autant de terminal que l'on le veut. On peut aussi juste fermer la fenêtre du terminal en cliquant sur la croix.

### Créer un nouveau terminal

Notez bien que _menu Affichage > Terminal_ ouvre le terminal courant, il n'en recrée pas un. C'est donc la commande à utiliser par défaut pour garder l'historique de ses commandes en utilisant la flèche du haut, qui remets la dernière commande utilisée.

Lorsque vous voulez créer un nouveau terminal, c'est dans _menu Terminal > Nouveau Terminal_.

## Exécuter du python via le terminal

Vous pouvez utiliser le terminal pour exécuter vos programmes python.

{% faire %}
Ouvrez ou refaite [le projet d'introduction vscode et python](../../../bases-programmation/éditeur-vscode/python)
{% endfaire %}

Remarquez que lorsque [vous exécutez le code](../../../bases-programmation/éditeur-vscode/python/#exécuter-programme), vscode exécute une ligne de commande dans le terminal :

```
nom-du-programme-python fichier-à-exécuter
```

Une fois le programme exécuté, vscode vous laisse dans le terminal. Vous pouvez alors facilement re-exécuter votre programme **en tapant sur la flèche du haut** sur votre clavier. Ceci à pour effet de rappeler la commande précédente pour l'exécuter à nouveau en appuyant sur la touche entrée.

<div id="exécuter-programme"></div>

{% note %}
Cette technique est utile pour connaître l'interpréteur utilisé par vscode.

1. commencez par exécuter un programme python avec le triangle
2. tapez la flèche du haut pour rappeler la commande

Vous aurez alors la commande :

```
nom-du-programme-python fichier-à-exécuter
```

Vous pouvez alors :

- soit copier le `nom-du-programme-python` pour l'utiliser dans un autre terminal
- soit supprimez la fin de la commande (le nom du fichier à exécuter) pour ne garder que le programme python utilisé.

{% endnote %}

Nous allons refaire ce processus à la main.

{% faire %}
Ouvrez un [terminal dans vscode](../terminal){.interne} : _menu Affichage > Terminal_.
{% endfaire %}

{% faire %}
Déterminer votre `nom-du-programme-python`, puis exécutez le dans un autre terminal.
{% endfaire %}

![interpréteur](python-interpreteur.png)

Dans l'interpréteur (à côté des `>>>`, qu'on appelle [invite de commande ou prompt](https://fr.wikipedia.org/wiki/Interface_en_ligne_de_commande)) :

{% faire %}
Tapez :

```python
print("Bonjour monde !")
```

Puis appuyez sur la touche entrée.
{% endfaire %}

Vous devriez avoir quelque chose du genre à la sortie :

![hello world](python-hello-world-interpreteur.png)

Ca a l'air d'avoir marché. La ligne de code a affiché à l'écran `Bonjour Monde`, puis l'invite de commande est revenue (une fois l'instruction exécutée, on attend la suivante).

Pour quitter l'interpréteur python :

{% faire %}
Tapez `quit()` puis appuyez sur la touche entrée.
{% endfaire %}

l’intérêt d'utiliser le terminal est que l'on peut :

- utiliser la flèche du haut du clavier pour rappeler la commande précédente. Cela va plus vite que de se déplacer sur le triangle
- on peut exécuter le code sans être sur l'onglet du fichier à exécuter

{% faire %}
Exécutez le fichier `main.py`{.language-} via le terminal en respectant la forme générale d'une exécution d'un code python :

{% endfaire %}
