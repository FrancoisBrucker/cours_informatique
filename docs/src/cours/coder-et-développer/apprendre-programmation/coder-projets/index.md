---
layout: layout/post.njk

title: Coder des projets

eleventyNavigation:
    prerequis:
        - "/cours/système/interagir-avec-système/"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

La première partie nous a appris les concepts fondamentaux d'un langage de programmation à objet et nous a permis d'écrire et d'exécuter un (petit) programme python. Cette partie nous permettra de passer à l'échelle en créant des programmes sur plusieurs fichiers et à traiter des données.

{% attention %}
Nous allons passer pas mal de temps à créer des fichiers, des dossiers et à utiliser le terminal. **Assurez-vous donc d'avoir lu et compris** les prérequis.
{% endattention %}



- ici fichiers
- tests etc
- créer ses propres modules

> TBD c'est en codant qu'on devient codeur. On se trompe ou on ne comprends pas. On s'arrête on comprend puis on recommence (lean : 0 déchet on stoppe la ligne de prod. Qualité)


## Interpréteur IDE et modules externes

> TBD intro sur bien coder et bons outils.

### <span id="installation-développement"></span>Installer et utiliser un interpréteur python

> installer un interpréteur
> vscode ou pycharm dans un second temps


Jusqu'à présent on a utilisé des interpréteurs externes pour exécuter notre code. Si l'on cherche à créer ses propres programmes, il est préférable d'avoir un interpréteur sur propre ordinateur. Ceci sera plus rapide et permettra à terme d'être paramétrable à l'envie.

{% aller %}
[Installer un interpréteur python](interpréteur-installation){.interne}
{% endaller %}

Une fois l'interpréteur installé, plutôt que de l'utiliser directement, on utilise un éditeur de texte spécialisé dans l'écriture de code : [un IDE](https://fr.wikipedia.org/wiki/Environnement_de_d%C3%A9veloppement). Il existe plusieurs choix possible, mais le plus utilisé actuellement est vscode.

{% aller %}
[Éditeur vscode](éditeur-vscode){.interne}
{% endaller %}

La principale différence entre un éditeur de texte et un notebook est que l'interpréteur est re-exécuté à chaque exécution : il ne garde rien en mémoire de la précédente exécution du code. Ceci permet de faire du code rép´table où toutes les informations sont uniquement contenues dans le fichier que l'on exécute.

## Installer des modules externes

Même si python vient avec de nombreux modules d'installés il arrive toujours un moment où l'on devra installer des modules développés par d'autres personnes :

{% aller %}
[Installer des modules](./modules-externes-python/){.interne}
{% endaller %}


## <span id="développer"></span>Gestion des données

Avant de pouvoir écrire des programmes conséquents il faut comprendre comment est organisé votre ordinateur et pouvoir minimalement interagir avec son système d'exploitation. Donc lisez la partie consacrée aux bases d'un système d'exploitation avant de continuer :

{% prerequis "**Connaissances système minimales**" %}

[Utiliser son système d'exploitation](/cours/système-et-réseau/bases-système){.interne}

{% endprerequis %}
{% info "**Etape optionnelle**"%}

L'installation d'un nouveau système est une étape optionnelle, mais si vous avez votre ordinateur depuis longtemps sans vraiment vous en occuper, ou que vous avez des erreurs étranges, il peut-être nécessaire de faire une nouvelle installation.

{% endinfo %}



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

### Séparer fonctions et exécutions

> TBD créer ses modules.

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
