---
layout: layout/post.njk 
templateEngineOverride: njk, md

title: Méthode de développement
tags: ['enseignement', 'ECM']

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---


24 heures de cours pour apprendre le python objet, les bases de la gestion des sources avec git et la programmation par les tests. C'est la suite de ce que vous avez fait en 1A avec JEMNEP et I1 de MIE en 2A. Donc revenez en arrière s'il vous manque des connaissances.

> TBD pour l'instant, je remets toutes les étapes ici.

## Partie I

> Identique au 2A [Méthode de développement I1-MIE](/enseignements/ecm/2A/cdp/){.interne}

Pour la prochaine fois, trois groupes :

- [poetry](https://python-poetry.org/)
- [uv](https://docs.astral.sh/uv/)
- module et package python : comment les utiliser

Préparer un exposé de 5min chacun + support avec biblio et principales fonctionnalités.

## Partie II

> Début Identique au 2A [Méthode de développement I1-MIE](/enseignements/ecm/2A/cdp/){.interne}

Puis :

{% aller %}

1. [design pattern](/cours/coder-et-développer/programmation-objet/design-patterns/){.interne}
2. [code coverage](/cours/coder-et-développer/couverture-de-code/){.interne}
3. [TDD](/cours/coder-et-développer/projet-TDD/){.interne}

{% endaller %}

Pour la prochaine fois, trois groupes :

- design pattern
- tests dans d'autres langages (java, js ou ts, ...)
- test pattern et refactoring pattern
- mock et tests

Préparer un exposé de 5min chacun + support avec biblio et principales fonctionnalités.

## Partie III

> TBD garder les tutos projets pour que je puisse les récupérer (je les ai perdu et j'ai besoin de les garder à jour). Il y a aussi des TDB, faites les et ajouter des screenshot que je puisse les inclure dans le cours.

{% aller %}

[Gestion du code source](/cours/gestion-des-sources/){.interne}

{% endaller %}

<!-- > TBD git (bases cette année)
> TBD ci/cd (pour l'année prochaine) 
> - <https://www.youtube.com/watch?v=KnSBNd3b0qI&list=PLnFWJCugpwfwQgjlSg_-csiJbpBIze2qa>
> - le faire avec github actions ? Au temps 2 Sur leur serveur ? -->

<!-- TBD voir ce qui passe pour les 1A et décaler le I et II (le faire sans test mais y mettre l'interpréteur et le debogueur. Ajouter un tuto pour qu'il puisse montrer ce qu'est une variable. l'exécution d'une commande et d'une fonction) 

## Partie II : un algorithme

> TBD ici JEMNEP : input ≠ return et les fonctions. Un programme qui fait tout
>
> TBD ici tests et installation de pytest sur le python du système
> TBD voir la gestion des variables grace au débogueur.

## Partie III : un programme

> TBD ici JEMNEP : deux fichiers ou on sépare main et fonctions. On dit pourquoi
> TBD ici dépendances puis prog objet
> TBD en 3A on ajoute design et TDD

## Partie IV : Le projet

> TBD ici JEMNEP : un zip et le fichier requirement.txt + readme
> TBD ici git pour le projet
> puis virtualenv pour la gestion des dépendances.

-->

<!-- ## Partie I : Système

> L'environnement dans lequel on code.

### Utiliser son Système d'exploitation

> [JEMNEP](/enseignements/ecm/1A/jemnep/){.interne}

#### Utiliser le réseau

Connectez vous [au réseau Éduroam](https://www.eduroam.fr/) qui est le réseau des université européennes.

- login : votre adresse mail
- mot de passe : celui de l'ent ECM

Sous Linux vous pouvez cocher : *aucun certificat CA requis*.

#### Avoir un système opérationnel

Outils et logiciels très utiles pour l'utilisation raisonnée de son système.

- **sous Windows**, ayez un compte sur le [microsoft store](https://apps.microsoft.com/home?hl=fr-FR&gl=FR).
- **sous mac** installez <https://brew.sh/> qui vous permettra d'installer de nombreux package unix : [installer brew](/cours/système-et-réseau/bases-système/système-installation/brew/){.interne}.
- **sous Linux/Ubuntu**, cela vaut le coup de lire le tuto ci-après qui liste différents paquets utiles : [post-installation](/cours/système-et-réseau/linux/bases-linux/post-installation/){.interne}

Si votre système est vieux et que vous l'utiliser sans vous en occuper depuis longtemps, cela peut valoir le coup d'en faire une nouvelle installation. Ceci est optionnel si votre système fonctionne.

{% info %}
Cette étape est **optionnelle**. Ne la faites que si votre ordinateur commence à avoir des comportement erratique, signe d'un système malade.
{% endinfo %}
{% aller %}
[installation d'u nouveau système](/cours/système-et-réseau/bases-système/système-installation/){.interne}
{% endaller %}

### Connaissances minimales du Système d'Exploitation

> [JEMNEP](/enseignements/ecm/1A/jemnep/){.interne}

{% aller %}

[But d'un système d'exploitation](/cours/système-et-réseau/bases-système/bases/but){.interne}
{% endaller %}

{% aller %}
[Programmes et bibliothèques](/cours/système-et-réseau/bases-système/bases/interactions/fichiers-exécutable/){.interne}
{% endaller %}

### Dossiers et fichiers

#### Notion de chemin

> [JEMNEP](/enseignements/ecm/1A/jemnep/){.interne}

{% aller %}

[Naviguer dans un système de fichiers](/cours/système-et-réseau/bases-système/bases/interactions/fichiers-navigation/){.interne}

{% endaller %}

#### Terminal

> 3A

1. le [terminal](/cours/système-et-réseau/bases-système/terminal/){.interne} pour exécuter des programmes et naviguer dans le système de fichiers
2. le (power)shell
3. Exécution d'un programme grâce au path

## Partie II : coder un algorithme

### Exécuter du python

> TBD suivre le cours.
> TBD 
> 1. interpréteur (avec basthon) :
>     1. comprendre les langages interprété vs compilé
>     2. comprendre les variables et les objets
> 2. interpréteur ligne à ligne exécution. Pas pratique si plusieurs lignes -> spyder/notebook pour :
>     1. faire des fonctions avec spyder ou un notebook. différence entre print et return
>     2. comprendre les variables locales
> 3. Mais pas bien car ordre ds cellules important, on est pas sur que la prochaine exécution sera identique à l'ancienne : il faut refaire un interpréteur à chaque exécution.
>     1. installation d'un python puis on regarde si ça marche avec un terminal (en 1A ici on ouvre un terminal et on explique ce que c'est). En 3A on fait marcher le tout en : 1. trouver ou est le python ; on fait des chemins pour y arriver.
>     2. pour exécuter du python il va falloir créer des fichiers et les envoyer dans un interpréteur. On utilise un programme pour nous aider : vscode

### Coder un algorithme

> ici cours par défaut.
> TBD ajouter des choses sans tests dans un seul fichier pour comprendre comment tout ça fonctionne juste avec vscode.
> débogueur pour voir comment il s'exécute.

> le chemin pour savoir où exécuter son python avec vscode et son terminal intégré.

### Installer des modules

> installer des modules :
>   1A. numpy ou matplotlib :
>   2A. pytest
>   3A. code coverage.
> TBD en 2A on ajoute pytest en installant le module pytest

> TBD ici programme python et interpréteur



> TBD c'est un découpage du cours [coder et développer](/cours/coder-et-développer/){.interne}

#### Principes

L'interpréteur python est un programme dont le but est d'exécuter du code python qu'on lui passe. Il doit exister sur votre système, mais pour l'instant on va l'utiliser via le web.

{% aller %}
[interpréter du python](/cours/coder-et-développer/bases-programmation/principes/){.interne}
{% endaller %}





### TBD




#### Ordinateur pour le développement en python

Vous aurez besoin d'installer python et un logiciel pour programmer :

{% aller %}
[Installer python et un interpréteur](/cours/coder-et-développer/bases-programmation/interpréteur/){.interne}
{% endaller %}

#### Coder en python

> But : avoir confiance dans le code produit

{% aller %}

1. [lire et écrire du code](/cours/coder-et-développer/écrire-code/){.interne}
2. [comprendre et corriger un programme grace au debogeur](/cours/coder-et-développer/debugger/){.interne},  
3. [variables (locales), pile et _stackframe_](/cours/coder-et-développer/données-mémoire/){.interne}

{% endaller %}

#### Interpréteur python

> But : gérer les dépendances d'un projet entre développeurs. Tout le monde doit avoir les mêmes bibliothèques (nom et versions) installées.

{% aller %}

1. [versions de python](/cours/coder-et-développer/version-python/){.interne}
2. [virtualenv](/cours/coder-et-développer/environnements-virtuels/){.interne}
   1. pourquoi et comment avec vscode
   2. **[3A] :** à la main

{% endaller %}

#### Exécution (pas à pas) d'un programme

### TD

{% aller %}

1. faites les tutoriels du cours :
   1. de vscode
   2. lire et écrire en python
   3. débogueur
   4. faites un environnement virtuel, installez matplotlib et [faites le tutoriel](/cours/coder-et-développer/bases-programmation/matplotlib/){.interne} dans un vscode
2. Utilisez les exercices de la partie [on s'entraîne](/cours/coder-et-développer/projet-codes/){.interne} pour :
   1. installer un environnement virtuel par projet
   2. comprendre comment fonctionne le débogueur
   3. faire un code qui fonctionne

{% endaller %}

> TBD test : interpréteur vs programme / variable locale vs globale

### À faire


## Partie II : principes de développement

- [vscode](/cours/coder-et-développer/bases-programmation/éditeur-vscode/){.interne} (parties prise en main et utilisation de python)
- **[3A] :** [code coverage](/cours/coder-et-développer/couverture-de-code/){.interne}
- **[3A] :** modules et packages, exécution de ses propres packages
- [on s'entraîne](/cours/coder-et-développer/projet-codes/){.interne}

## Partie III : projets

1. tests :
   1. [lire et écrire du code](/cours/coder-et-développer/écrire-code/){.interne}
   2. s'il y a bien une chose que ne doit pas faire une IA, c'est écrire vos tests !
2. classes et objets
3. **[3A] :** design patterns
4. **[3A] :** programmation par les tests

## Partie IV : gestion des sources

1. principes
2. github, git app
3. git interne

## Liens

Basé sur les cours :

{% lien %}

- [Coder et développer en python](/cours/coder-et-développer){.interne}
- [Système et réseau](/cours_informatique/cours/système-et-réseau){.interne}

{% endlien %}
 -->