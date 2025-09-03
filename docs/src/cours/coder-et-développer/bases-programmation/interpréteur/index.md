---
layout: layout/post.njk

title: Installer et utiliser un interpréteur

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Les logiciels et outils nécessaires pour écrire et exécuter du code python.

## Interpréteur python

Commençons par installer un interpréteur indépendant de l'application utilisée pour coder. Selon le système d'exploitation, la méthode d'installation est un peu différente :

{% details "sous Windows 11" %}
Utilisez le Microsoft store.

{% lien %}
[Tutoriel d'installation](https://learn.microsoft.com/fr-fr/windows/python/beginners#install-python)
{% endlien %}
{% enddetails %}

{% details "sous Linux/Ubuntu" %}
Python est installé par défaut, mais il ne contient pas le module pip permettant d'installer de nouveaux modules à python. Pour installer pip, tapez dans [un terminal](../ordinateur-développement/terminal){.interne} :

```
sudo apt install python3-pip
```

De plus, le python d'installé ne contient pas non plus le module [Tkinter](https://docs.python.org/fr/3/library/tkinter.html). Ceci pose des problèmes lorsque l'on veut utiliser le [module turtle](https://docs.python.org/fr/3/library/turtle.html).

Pour installer une version de python avec Tkinter, tapez dans [un terminal](../ordinateur-développement/terminal){.interne} :

```
sudo apt install python3-tk
```

Enfin, la commande pour taper python est `python3`. Pour avoir le même comportement que sous windows où cette commande s'appelle juste `python`, vous pouvez installer :

```
sudo apt install python-is-python3
```

Vous pourrez uniquement taper `python` dans un terminal pour exécuter l'interpréteur python,
{% enddetails %}

{% details "sous Macos" %}

De même que sous Linux/Ubuntu, python est installé par défaut, mais pas le module [Tkinter](https://docs.python.org/fr/3/library/tkinter.html). Ceci pose des problèmes lorsque l'on veut utiliser le [module turtle](https://docs.python.org/fr/3/library/turtle.html).

Il va falloir installer python avec [brew](../ordinateur-développement/brew){.interne} puis. Dans [un terminal](../ordinateur-développement/terminal){.interne} tapez :

```
brew install python-tk
```

Enfin, la commande pour taper python est `python3`. Pour avoir le même comportement que sous windows où cette commande s'appelle juste `python`, vous pouvez taper dans un terminal :

```shell
echo "alias python=python3" >> ~/.zshrc
```

{% enddetails %}

## Éditeur de code

Une fois l'interpréteur installé, on va l'utiliser _via_ [un IDE](https://fr.wikipedia.org/wiki/Environnement_de_d%C3%A9veloppement). Il existe plusieurs choix possible, mais le plus utilisé actuellement est vscode :

{% aller %}
[Éditeur vscode](éditeur-vscode){.interne}
{% endaller %}

Vscode utilise le terminal pour exécuter ses programmes python. C'est une pratique courante dans le monde unix mais iun peu plus exotique sous windows. Prenez le temps de lire le tutoriel suivant pour l'utiliser efficacement.

{% aller %}
[Utiliser le terminal de vscode](terminal-vscode){.interne}
{% endaller %}

## Modules python

Un interpréteur tout neuf vient presque nu. Il ne possède aucun des modules mis à disposition d'environnement tels que anaconda ou Spyder. Mais ce n'est pas grave, nous allons les installer nous même !

{% aller %}
[Installer des modules](modules-python){.interne}
{% endaller %}
