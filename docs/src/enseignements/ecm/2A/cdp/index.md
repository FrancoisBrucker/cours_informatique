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

15h+6h heures de cours pour apprendre le python objet, les bases de la gestion des sources avec git et la programmation par les tests.

{% info %}

Connectez vous [au réseau Éduroam](https://www.eduroam.fr/) qui est le réseau des université européennes pour vos travaux en TD/TP.

- login : votre adresse mail
- mot de passe : celui de l'ent ECM

Sous Linux vous pouvez cocher : *aucun certificat CA requis*.

{% endinfo %}

Tous les exercices et rendu sont fait pour être réalisé sans IA :

{% attention "**IA et code**" %}

Les agents IA sont de formidables accélérateurs en développement, **mais** :

- ils n'inventent rien de neuf : ils ne peuvent répondre qu'à des problèmes déjà résolus,
- ils peuvent (vont parfois) halluciner et donner des solutions qui semblent corrects mais sont fausses en réalité

En temps que développeur **vous avez l'obligation** :

- de préparer le terrain aux agent étant le plus explicite possible dans vos demandes
- de toujours vérifier le code produit
- de connaître le fonctionnement de votre projet et pouvoir modifier le code si nécessaire


Pour cela : 

- vous devez **appendre** le cours 
- **faire vous même** les exercices et les TDs pour assimiler les concepts
- utiliser l'IA dans les projets plus long en vérifiant chaque étape produite

{% endattention %}

## Partie 0 : Vérification des acquis

> 1h cours

{% aller %}
[Rappels](/cours/coder-et-d%C3%A9velopper/apprendre-programmation/concepts/){.interne}
{% endaller %}


Pour terminer cette partie, utilisez [un interpréteur en ligne](https://console.basthon.fr/) ou [spyder](https://www.spyder-ide.org/) pour vous rafraîchir la mémoire en python :

{% aller %}
[84 monolignes en python](/cours/coder-et-développer/apprendre-programmation/concepts/mono-lignes/){.interne}
{% endaller %}

Vous devriez être capable de comprendre toutes les solutions et (dans le meilleur des cas) d'en faire une grande partie.

## <span id="partie-1"></span>Partie I : Projets informatique 

### Interpréteur python et IDE

> 2h cours

{% aller %}
1. Interagir avec le système :
   1. [Naviguer dans un système de fichiers](/cours/système/interagir-avec-système/fichiers-dossiers/){.interne}
   2. [Terminal](/cours/système/interagir-avec-système/terminal/){.interne}
2. [Installer un interpréteur et un IDE](/cours/coder-et-développer/apprendre-programmation/coder-projets/outils/){.interne}
{% endaller %}
{% info %}
[Installer des paquets](/cours/système/interagir-avec-système/gestionnaire-paquets/){.interne}
{% endinfo %}

### Principe de conduite d'un projet informatique

> 2h TD

Le premier principe fondamental est de séparer le programme principal des fonctions :

{% aller %}
1. Séparer code et fonctions en [créant ses propres modules](/cours/coder-et-développer/apprendre-programmation/coder-projets/écrire-code/création-modules/){.interne}
2. On s'entraîne : [Projet : création de modules](/cours/coder-et-développer/apprendre-programmation/coder-projets/écrire-code/projet-création-modules/){.interne}

{% endaller %}

Le second principe fondamental est que les tests des fonctions fonts partie du projet :

{% aller %}
1. [Tester ses fonctions](/cours/coder-et-développer/apprendre-programmation/coder-projets/outils/){.interne}
2. [On s'entraîne à écrire des tests](/cours/coder-et-développer/apprendre-programmation/coder-projets/écrire-code/projet-codes-tests/){.interne}
{% endaller %}

Pour aller plus loin :

{% aller %}
1. [Utiliser le débogueur pour corriger son code](/cours/coder-et-développer/apprendre-programmation/coder-projets/écrire-code/débogueur/){.interne}
2. [exercices divers](/cours/coder-et-développer/apprendre-programmation/coder-projets/exercices-tests/){.interne}
{% endaller %}

### À rendre

> 2h DM à rendre sur moodle

Lisez la partie du cours suivant et faire le rendu qu'il faudra déposer sur moodle :

{% aller %}
1. [Bonnes pratiques et mantra](/cours/coder-et-développer/apprendre-programmation/coder-projets/écrire-code/bonnes-pratiques/){.interne}
2. [Mise en œuvre d'un projet informatique](/cours/coder-et-développer/apprendre-programmation/coder-projets/écrire-code/projet-informatique/){.interne}
{% endaller %}


{% faire "**Travail à rendre** "%}
Faite le [Projet pourcentage](/cours/coder-et-développer/apprendre-programmation/coder-projets/écrire-code/projet-pourcentages/){.interne}
{% endfaire %}
{% attention %}
 Le travail est à rendre [sur moodle](https://moodle.centrale-med.fr/course/view.php?id=1523) **avant mercredi 16/09 à 8h00**.
{% endattention %}


## Partie II : Classes et objets

{% prerequis "**À lire avant la séance**" %}
[Tout est objet en python](/cours/coder-et-développer/apprendre-programmation/programmation-objet/introduction/){.interne}
{% endprerequis %}

### Classe et objets en python

> 2h cours

{% aller %}
1. [Classes et objets](/cours/coder-et-développer/apprendre-programmation/programmation-objet/classes-et-objets/){.interne}
2. [Des dés](/cours/coder-et-développer/apprendre-programmation/programmation-objet/projet-objets-dés/){.interne}
{% endaller %}

### A vous

> 1h TP

{% aller %}
[Projet cartes](/cours/coder-et-développer/apprendre-programmation/programmation-objet/projet-objets-cartes/){.interne}
{% endaller %}

> 2h TD

{% aller %}

1. [Améliorer ses objets](/cours/coder-et-développer/apprendre-programmation/programmation-objet/améliorer-ses-objets/){.interne}
2. [Des dés améliorés](/cours/coder-et-développer/apprendre-programmation/programmation-objet/projet-objets-dés-amélioration/){.interne}


{% endaller %}

#### À rendre

> 2h DM à rendre sur github et ne mettre sur moodle qu'un fichier texte contenant le lien vers le dépôt github.

{% prerequis "**Travail préparatoire**" %}
Mettre son code à disposition via un [Dépôt](/cours/gestion-des-sources/dépôt/){.interne} sur github.
{% endprerequis %}


{% faire "**Travail à rendre** "%}
[Cartes améliorées](/cours/coder-et-développer/apprendre-programmation/programmation-objet/projet-objets-cartes-amélioration/){.interne}
{% endfaire %}
{% attention %}
 Le travail est à rendre **sur github** et en mettant le lien vers le déport [sur moodle](https://moodle.centrale-med.fr/course/view.php?id=1523) **avant mercredi 23/09 à 8h00**.
{% endattention %}

## Partie III : Composition/agrégation et héritage

### Composition et agrégation

> 2h cours

{% aller %}
1. [Composition et agrégation](/cours/coder-et-développer/apprendre-programmation/programmation-objet/composition-agrégation/){.interne}
2. [Des compositions de dés](/cours/coder-et-développer/apprendre-programmation/programmation-objet/projet-composition-aggrégation-dés/){.interne}
{% endaller %}

### À vous

> 2h TP

{% aller %}
[Projet cartes et bataille](/cours/coder-et-développer/apprendre-programmation/programmation-objet/projet-agrégation-cartes/){.interne}
{% endaller %}

### Héritage

> 1h cours

{% aller %}
1. [Héritage](/cours/coder-et-développer/apprendre-programmation/programmation-objet/héritage/){.interne}
2. [Dés spécifiques](/cours/coder-et-développer/apprendre-programmation/programmation-objet/projet-objets-dés-héritage/){.interne}
{% endaller %}

#### À rendre

> 2h+ DM à rendre sur github et ne mettre sur moodle qu'un fichier texte contenant le lien vers le dépôt github.



{% prerequis "**Travail préparatoire**" %}
1. [création d'un environnement virtuel](/cours/coder-et-développer/apprendre-programmation/gestion-dépendances/environnements-virtuels/){.interne} pour ses projets
2. mettre son code à disposition via un [Dépôt](/cours/gestion-des-sources/dépôt/){.interne} sur github.

{% endprerequis %}


{% faire %}

Rendre le projet [Bataille Navale](/cours/coder-et-développer/programmation-objet/projet-bataille-navale){.interne}. 

Les consignes sont :

- le projet doit se trouver sur github
- mettre de la couleur dans vos sorties en utilisant le module <https://github.com/termcolor/termcolor>
- il doit fonctionner avec un environnement virtuel : le fichier `requirements.txt`{.fichier} est requis


{% endfaire %}
{% attention %}
 Le travail est à rendre **sur github** et en mettant le lien vers le déport [sur moodle](https://moodle.centrale-med.fr/course/view.php?id=1523) **avant mercredi 23/11 à 8h00**.
{% endattention %}
