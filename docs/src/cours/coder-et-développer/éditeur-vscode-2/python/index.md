---
layout: layout/post.njk

title: Vsc et python

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

## Paramètres

{% attention %}
Cette partie est optionnelle.

Elle n'est utile que si vous voulez changer le comportement par défaut de vscode et python.
{% endattention %}

Le lien entre vscode et python se fait par l'intermédiaires de [paramètres](https://code.visualstudio.com/docs/getstarted/settings) :

{% details "sous mac" %}

Allez dans : _menu Code > préférences > paramètres_

{% enddetails %}
{% details "sous windows et Linux" %}

Allez dans : _menu Fichier > préférences > paramètres_

{% enddetails %}

Pour trouver les paramètres liés à python, une fois dans l'onglet paramètres, choisissez _extensions > python_ dans le menu de gauche. Les préférences vscode consistent en des variables (_ID du paramètre_) à positionner selon ses envies, chaque variable modifiant un comportement de vscode.

{% attention %}
Il y a deux fois les mêmes préférences : **utilisateur** et **espace de travail**. Assurez vous de modifier les préférences **utilisateur**.
{% endattention %}

Il y a deux préférences qui sont liées à l'interpréteur python :

- **Default Interpreter Path** dont l'ID est `python.defaultInterpreterPath`. C'est le chemin vers l’interpréteur python.
- **Conda Path** dont l'ID est `python.condaPath`. C'est le chemin vers le programme `conda` si vous utilisez la version anaconda de python.

{% info %}
Vous pouvez directement chercher le paramètre en tapant son nom dans la barre de recherche.
{% endinfo %}
