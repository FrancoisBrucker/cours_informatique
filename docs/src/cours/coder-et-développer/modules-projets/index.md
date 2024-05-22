---
layout: layout/post.njk

title: Modules et projet

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Tout projet informatique va dépendre de modules extérieurs pour son exécution. Ces modules vont être de deux ordres :

- ceux liés à l'exécution du programme, comme pyglet, matplotlib ou encore numpy
- ceux liés au développement comme pytest


> TBD C'est un vrai soucis. plusieurs projet avec de`s modules pythons incompatibles, ou des modules inutiles pour certains projets. 
> TBD : pour éviter les soucis. il faut n'avoir que les modules utiles pour chaque projet.
Environnement d'exécution.

> dépendances dans un projet

#### Environnements virtuels


> TBD venv

<https://stackoverflow.com/questions/41573587/what-is-the-difference-between-venv-pyvenv-pyenv-virtualenv-virtualenvwrappe>
> <https://code.tutsplus.com/understanding-virtual-environments-in-python--cms-28272t>
<https://python-guide-pt-br.readthedocs.io/fr/latest/dev/virtualenvs.html>
<https://python-poetry.org/>
<https://linuxfr.org/news/python-partie-7-environnements-virtuels>

#### poetry

plutôt que de mettre les python alternatifs dans le projet, il les place tous au même endroit.

> Gestions des dépendances d'un projet.
