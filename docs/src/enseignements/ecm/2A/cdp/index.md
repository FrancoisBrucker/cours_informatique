---
layout: layout/post.njk
templateEngineOverride: njk, md

title: "Coder et développer en python"
tags: ["enseignement", "ECM"]

eleventyNavigation:
  order: 0

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

24 heures de cours pour apprendre le python objet, les bases de la gestion des sources avec git et la programmation par les tests.

<!-- TBD 

Modifier le plan pour l'année prochaine. Mettre l'environnement virtuel en fin de 2A, partie IV

voir ce qui passe pour les 1A et décaler le I et II (le faire sans test mais y mettre l'interpréteur et le debogueur. Ajouter un tuto pour qu'il puisse montrer ce qu'est une variable. l'exécution d'une commande et d'une fonction) 

## Partie I : le système

> TBD Ca c'est JEMNEP

> TBD ici programme python et interpréteur
> débogueur pour voir comment il s'exécute.
> le chemin pour savoir où exécuter son python.
> installer des modules (ici numpy ou matplotlib) sur un python spécifique

## Partie II : un algorithme

> TBD ici JEMNEP : input ≠ return et les fonctions. Un programme qui fait tout
>
> TBD ici tests et installation de pytest sur le python du système

## Partie III : un programme

> TBD ici JEMNEP : deux fichiers ou on sépare main et fonctions. On dit pourquoi
> TBD ici dépendances puis prog objet
> TBD en 3A on ajoute design et TDD

## Partie IV : Le projet

> TBD ici JEMNEP : un zip et le fichier requirement.txt + readme
> TBD ici git pour le projet
> puis virtualenv pour la gestion des dépendances.

-->

## Note

- 2 tests de 15min sur papier les 2ème et 3ème lundi (8h-8h15)
- [un projet à rendre](./#projet-final){.interne} sur github la dernière semaine

## Partie I : le système

<!-- TBD

l'année prochaine mettre lire et écrire du code avant debogueur puis virtualenv dans la partie gérer un projet

en 1A un fichier avec tout puis 2 fichiers avec des imports
en 2A 3 fichier main/fct et test. 
 
 -->
### Cours

> Durée 3h plus questions

#### Utiliser le réseau

Connectez vous [au réseau Éduroam](https://www.eduroam.fr/) qui est le réseau des université européennes.

- login : votre adresse mail
- mot de passe : celui de l'ent ECM

Sous Linux vous pouvez cocher : *aucun certificat CA requis*.

#### Connaissances minimales du système d'exploitation

{% aller %}
[But d'un système d'exploitation](/cours/système-et-réseau/bases-système/bases/but){.interne}
{% endaller %}

#### Installations système complémentaires

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

#### Dossiers et fichiers

{% aller %}
[Naviguer dans un système de fichiers](/cours/système-et-réseau/bases-système/bases/interactions/fichiers-navigation/){.interne}
{% endaller %}

#### Ordinateur pour le développement en python

Vous aurez besoin d'installer python et un logiciel pour programmer :

{% aller %}
[Installer python et un interpréteur](/cours/coder-et-développer/bases-programmation/interpréteur/){.interne}
{% endaller %}

#### Interpréteur python

{% aller %}

1. [versions de python](/cours/coder-et-développer/version-python/){.interne}
2. [virtualenv](/cours/coder-et-développer/environnements-virtuels/){.interne} pourquoi et comment avec vscode

{% endaller %}

#### Exécution (pas à pas) d'un programme

{% aller %}

1. [comprendre et corriger un programme grace au déboguer](/cours/coder-et-développer/debugger/){.interne},  
2. [variables (locales), pile et _stackframe_](/cours/coder-et-développer/données-mémoire/){.interne}

{% endaller %}

> TBD debug avec un environnement virtuel : <https://m-ruminer.medium.com/vscode-and-debugging-python-in-virtual-environments-d975125b455c>
> doc <https://code.visualstudio.com/docs/python/debugging>

### TD

{% aller %}

1. faites les tutoriels du cours :
   1. de vscode
   2. du débogueur
   3. faites un environnement virtuel, installez matplotlib et [faites le tutoriel](/cours/coder-et-développer/bases-programmation/matplotlib/){.interne} dans un vscode
2. Utilisez les exercices de la partie [on s'entraîne](/cours/coder-et-développer/projet-codes/){.interne} pour :
   1. installer un environnement virtuel par projet
   2. comprendre comment fonctionne le débogueur
   3. faire un code qui fonctionne

{% endaller %}

## Partie II : développement

### Écrire du code

{% aller %}
[lire et écrire du code](/cours/coder-et-développer/écrire-code/){.interne}
{% endaller %}

> À retenir : S'il y a bien une chose que ne doit pas faire une IA, c'est écrire vos tests !

### Un programme comme imbrications d'objets

#### Concevoir des classes et des objets

{% aller %}

1. [Classes et objets](/cours/coder-et-développer/programmation-objet/classes-et-objets/){.interne}
2. [Coder ses objets](/cours/coder-et-développer/programmation-objet/coder-ses-objets/){.interne}

{% endaller %}

#### Améliorer ses objets

{% aller %}

[Améliorer l'utilisabilité de ses objets](/cours/coder-et-développer/programmation-objet/améliorer-ses-objets/){.interne}

{% endaller %}

#### Combiner ses objets entre eux

{% aller %}

[Composition et agrégation d'objets](/cours/coder-et-développer/programmation-objet/composition-agrégation/){.interne}

{% endaller %}

#### Héritage

{% aller %}

1. [Héritage](/cours/coder-et-développer/programmation-objet/héritage/){.interne}
2. [on s'entraîne](/cours/coder-et-développer/programmation-objet/projet-héritage/){.interne}

{% endaller %}

### TD

Vous pouvez faire dans l'ordre ou choisir un sujet (cartes ou dés) puis le faire en entier.

{% aller %}

0. Écrire ses tests :
   1. [projet hello dev](/cours/coder-et-développer/écrire-code/tutoriel-hello-dev/){.interne}
   2. [projet "pourcentages"](/cours/coder-et-développer/écrire-code/projet-pourcentages/){.interne}
1. Coder des objets :
   1. [projet dés](/cours/coder-et-développer/programmation-objet/projet-objets-dés/){.interne}
   2. [projet cartes](/cours/coder-et-développer/programmation-objet/projet-objets-cartes/){.interne}
2. Améliorer ses objets :
   1. [améliorer les dés grâce aux accesseurs](/cours/coder-et-développer/programmation-objet/projet-objets-dés-accesseur/){.interne}
   2. [améliorer les cartes en protégeant ses attributs](/cours/coder-et-développer/programmation-objet/projet-objets-cartes-value-object/){.interne}
3. Combiner les objets entres-eux :
   1. [composer des dés](/cours/coder-et-développer/programmation-objet/projet-composition-dés/){.interne}
   2. [composer des cartes](/cours/coder-et-développer/programmation-objet/projet-agrégation-cartes/){.interne}

{% endaller %}

## Partie III : gestion des sources

<!-- > TBD test
1. mise en oeuvre des tests unitaires
2. intérêt des tests unitaire dans le développement d'un projet
3. intérêt de la programmation objet dans le développement d'un projet

 -->

### Cours

{% aller %}

[Gestion des sources](/cours/gestion-des-sources/){.interne} (jusqu'à la partie outils) :

1. [principes](/cours/gestion-des-sources/principes){.interne}
2. usage : 
   1. [configuration](/cours/gestion-des-sources/usage-quotidien/){.interne}
   2. [bonnes pratiques](/cours/gestion-des-sources/bonnes-pratiques/){.interne}
   
{% endaller %}

### TD

{% aller %}

1. [Découverte de github](/cours/gestion-des-sources/github/){.interne}
2. [SCM avec Github](/cours/gestion-des-sources/github-SCM/projet-github-desktop/){.interne}
   
{% endaller %}


## <span id="projet-final"></span>Projet final

À rendre :

{% faire "**Évaluation finale**"%}

Faites [le projet bataille navale](/cours/coder-et-développer/programmation-objet/projet-bataille-navale/) en utilisant tout ce que l'on a vu :

- un environnement virtuel,
- des tests,
- un SCM,
- des commits réguliers.

Ce projet doit avoir :

1. un fichier `.gitignore`
2. un fichier readme pour expliquer comment exécuter votre jeu
3. un fichier `requirement.txt` pour vos dépendances (il doit au moins y avoir `pytest`)
4. au moins un commit par item avec un `?` à faire.

{% endfaire %}
{% attention %}
À rendre pour le 17/11 sur [moodle](https://moodle.centrale-med.fr/mod/assign/view.php?id=53201) **un unique lien** vers un repo de votre github public.
{% endattention %}

<!-- > TBD note avec commit pertinent sur un petit projet
tbd mettre un .gitignore
 -->

## Liens

Basé sur les cours :

{% lien %}

- [Coder et développer en python](/cours/coder-et-développer){.interne}
- [Système et réseau](/cours_informatique/cours/système-et-réseau){.interne}

{% endlien %}
