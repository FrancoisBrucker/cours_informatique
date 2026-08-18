---
layout: layout/post.njk

title: Utiliser un interpréteur Python
authors:
  - François Brucker
  - Pierre Brucker

eleventyNavigation:
    prerequis:
        - "/cours/système/ordinateur-programmes-OS/"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---


> TBD utiliser un interpreteur = TFIL

Commençons par le commencement et voyons comment exécuter du code python chez soit.

> interpréteur (comme javascript) python -> interp -> exécution machine (diff des langages exécutés golang)
> ici : envoyer sur systeme 1 : systeme et execution de code. Principes.
> utiliser print() et x = 34 (affectation variables)
> 
>  Différentes façon d'exécuter du python
>
> basthon
> spyder

On a utilisé un interpréteur externe (sur le site <https://basthon.fr/>) pour l'instant. Son utilisation n'est pas tès satisfaisante pour l'instant puisqu'il faut copier/coller chaque ligne dans l'interpréteur.

La façon classique d'exécuter du code python est d'utiliser un intermédiaire entre l'interpréteur et son code. Nous allons montrer deux façons classiques de le faire.


#### Spyder


{% lien %}
<https://www.spyder-ide.org/>
{% endlien %}

Spyder est un éditeur lié à un interpréteur python. L'application est très utilisée lorsque l'on commence à apprendre la programmation. Et permet d'écrire des programmes tout en conservant un unique interpréteur accessible par une console.

Il fonctionne à la fois comme un notebook ou comme un interpréteur.

{% attention %}
La commande `Run file` exécute son code dans un nouvel interpréteur **puis** le fusionne avec l'interpréteur courant.

Ce fonctionnement est déroutant...
{% endattention %}

Si vous voulez faire du développement sérieusement, je vous conseille d'utiliser plutôt la combinaison éditeur + interpréteur ci-dessous.

<!-- TBD

Montrer que le run file est étrange avec une fonction.
Déf dans le fichier puis exécution dans l'interpréteur.
Il faudra refaire le même exemple avec vscode et montrer que ça ne marche pas. On a un terminal pas un interpréteur. Il faut tout faire dans le fichier -->

