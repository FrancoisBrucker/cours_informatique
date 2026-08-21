---
layout: layout/post.njk

title: Coder des projets

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

- ici fichiers
- tests etc
- créer ses propres modules

> TBD ici formalisation des espaces de nommage avec les classes...

La première partie nous a appris les concepts fondamentaux d'un langage de programmation à objet et nous a permis d'écrire et d'exécuter un (petit) programme python. Cette partie nous permettra de passer à l'échelle en créant des programmes sur plusieurs fichiers et à traiter des données.


## Installer son propre interpréteur

> TBD ici vscode + installation de son python.

## <span id="développer"></span>Gestion des données

Avant de pouvoir écrire des programmes conséquents il faut comprendre comment est organisé votre ordinateur et pouvoir minimalement interagir avec son système d'exploitation. Donc lisez la partie consacrée aux bases d'un système d'exploitation avant de continuer :

{% prerequis "**Connaissances système minimales**" %}

[Utiliser son système d'exploitation](/cours/système-et-réseau/bases-système){.interne}

{% endprerequis %}
{% info "**Etape optionnelle**"%}

L'installation d'un nouveau système est une étape optionnelle, mais si vous avez votre ordinateur depuis longtemps sans vraiment vous en occuper, ou que vous avez des erreurs étranges, il peut-être nécessaire de faire une nouvelle installation.

{% endinfo %}

### Installer des modules externes

Même si python vient avec de nombreux modules d'installés il arrive toujours un moment où l'on devra installer des modules développés par d'autres personnes :

{% aller %}
[Installer des modules](./modules-externes-python/){.interne}
{% endaller %}


### Stockage des données

#### En mémoire

{% aller %}
[Données en mémoire](données-mémoire){.interne}
{% endaller %}

#### Chaîne de caractères

{% aller %}
[Encodage Unicode](encodage-unicode){.interne}
{% endaller %}

#### Sur des fichiers

{% aller %}
[Fichiers](fichiers){.interne}
{% endaller %}

## Écrire du code

### Corriger son code

Le débogueur, qui permet d'exécuter ligne à ligne du code python est non seulement un excellent outil pour corriger son code, mais également un très bon outil d'apprentissage puisqu'il vous permettra d'assimiler plus rapidement ces notions de variables, d'objets et d'espaces de noms :

{% aller %}
[Déboguer son code](débogueur){.interne}
{% endaller %}

### Écrire du code maintenable

Il faut essayer de limiter au maximum la création de bug et, surtout, éviter qu'ils réapparaissent à la suite d'une modification de code.

Mais plutôt que de corriger il vaut mieux éviter que les bugs arrivent

{% aller %}
[Tester son code](tests-unitaires){.interne}
{% endaller %}

{% aller %}
[On s’entraîne : écrire des tests](projet-codes-tests){.interne}
{% endaller %}

### Écrire du code lisible

{% aller %}
[Écrire et exécuter du code](écrire-code){.interne}
{% endaller %}

### On s'entraîne à écrire du code propre qui fonctionne

#### Un projet complet

{% aller %}
[Projet pourcentage](projet-pourcentages){.interne}
{% endaller %}

#### On vérifie qu'on sait faire

{% aller %}
[exercices](exercices-tests){.interne}
{% endaller %}
