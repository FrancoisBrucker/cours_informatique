---
layout: layout/post.njk
templateEngineOverride: njk, md

title: "Coder et développer en python"
tags: ['enseignement', 'ECM']

eleventyNavigation:
  order: 0

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

24 heures de cours pour apprendre le python objet, les bases de la gestion des sources avec git et la programmation par les tests.

## Partie I : le système

### Cours

1. système :
   1. [principes](/cours/système-et-réseau/bases-système/système-principes/){.interne} 
   2. [dossier, fichier, programme et bibliothèques](/cours/système-et-réseau/bases-système/système-interaction/){.interne}
2. programmes :
   1. [vscode](/cours/coder-et-développer/bases-programmation/éditeur-vscode/){.interne} comme exemple de programme (où, fichier de conf lib, utilisateur et projet)
   2. [terminal](/cours/système-et-réseau/bases-système/terminal/){.interne}
   3. interpréteur python comme programme (différent de spider). Exécution grace au path Voir ses dépendances. Le code python exécuté via l'interpréteur et pas directement par le système
3. interpréteur python : 
   1. [versions de python](/cours/coder-et-développer/version-python/){.interne}
   2. [comprendre son exécution grace au debugeur](/cours/coder-et-développer/debugger/){.interne}, 
   3. [installer des dépendances pip](/cours/coder-et-développer/bases-programmation/modules-python/){.interne} 
   4. [virtualenv](/cours/coder-et-développer/environnements-virtuels/){.interne} pourquoi et comment

### TD

- [vscode](/cours/coder-et-développer/bases-programmation/éditeur-vscode/){.interne} (parties prise en main et utilisation de python)
- [on s'entraîne](/cours/coder-et-développer/projet-codes/){.interne}

## Partie II : développement

1. tests :
   1. [lire et écrire du code](/cours/coder-et-développer/écrire-code/){.interne}
   2. s'il y a bien une chose que ne doit pas faire une IA, c'est écrire vos tests !
2. classes et objets
3. design patterns
4. programmation par les tests

## Partie III : gestion des sources

1. principes
2. github, git app
3. git interne

## Liens

Basé sur les cours :

{% aller %}
- [Coder et développer en python](/cours/coder-et-développer){.interne}
- [Système et réseau](/cours_informatique/cours/système-et-réseau){.interne}
{% endaller %}
