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

## Note

- 2 tests de 15min sur papier les 2ème et 3ème lundi (8h-8h15)
- un projet à rendre sur github la dernière semaine

## Partie I : le système

> Durée 3h plus questions

### Cours

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

#### Le terminal

{% aller %}

1. [terminal](/cours/système-et-réseau/bases-système/terminal/){.interne}
2. exécuter l'interpréteur python comme programme (différent de spider). Le code python exécuté via l'interpréteur et pas directement par le système

{% endaller %}

#### Interpréteur python

{% aller %}

1. [versions de python](/cours/coder-et-développer/version-python/){.interne}
2. [comprendre son exécution grace au debugeur](/cours/coder-et-développer/debugger/){.interne},  
3. [Variables (locales), pile et _stackframe_](/cours/coder-et-développer/données-mémoire/){.interne}
4. [virtualenv](/cours/coder-et-développer/environnements-virtuels/){.interne} pourquoi et comment

{% endaller %}

### TD

{% aller %}

1. installez vscode et faites le tutoriel du cours
2. Utilisez les exercices de la partie [on s'entraîne](/cours/coder-et-développer/projet-codes/){.interne} pour :
   1. comprendre comment fonctionne le débogueur
   2. installez un environnement virtuel par projet

{% endaller %}

## Partie II : développement

1. tests :
   1. [lire et écrire du code](/cours/coder-et-développer/écrire-code/){.interne}
   2. s'il y a bien une chose que ne doit pas faire une IA, c'est écrire vos tests !
2. classes et objets

## Partie III : gestion des sources

1. principes
2. github, git app
3. git interne

<!-- > TBD note avec commit pertinent sur un petit projet -->

## Liens

Basé sur les cours :

{% lien %}

- [Coder et développer en python](/cours/coder-et-développer){.interne}
- [Système et réseau](/cours_informatique/cours/système-et-réseau){.interne}
  {% endlien %}
