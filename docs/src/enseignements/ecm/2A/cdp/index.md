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

Connectez vous [au réseau Éduroam](https://www.eduroam.fr/){.externe} qui est le réseau des université européennes pour vos travaux en TD/TP.

- login : votre adresse mail
- mot de passe : celui de l'ent ECM

Sous Linux suivez les instructions de : <https://cat.eduroam.org/>{.externe}

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
[Rappels](/cours/coder-et-d%C3%A9velopper/apprendre-programmation/concepts/)
{% endaller %}


Pour terminer cette partie, utilisez [un interpréteur en ligne](https://console.basthon.fr/){.externe} ou [spyder](https://www.spyder-ide.org/){.externe} pour vous rafraîchir la mémoire en python :

{% aller %}
[84 monolignes en python](/cours/coder-et-développer/apprendre-programmation/concepts/mono-lignes/)
{% endaller %}

Vous devriez être capable de comprendre toutes les solutions et (dans le meilleur des cas) d'en faire une grande partie.

## <span id="partie-1"></span>Partie I : Projets informatique 

### Interpréteur python et IDE

> 1h cours

{% aller %}
1. Interagir avec le système :
   1. [Naviguer dans un système de fichiers](/cours/système/interagir-avec-système/fichiers-dossiers/)
   2. [Terminal](/cours/système/interagir-avec-système/terminal/)
2. [Installer un interpréteur et un IDE](/cours/coder-et-développer/apprendre-programmation/coder-projets/outils/)
{% endaller %}
{% info %}
[Installer des paquets](/cours/système/interagir-avec-système/gestionnaire-paquets/)
{% endinfo %}

### Principe de conduite d'un projet informatique

> 2h TD (1h en autonomie)

Les deux principes fondamentaux lorsque l'on développe un projet informatique est de séparer le programme principal des fonctions et de conserver les tests qui nous on permis de vérifier qu'elles fonctionnent :

{% aller %}
1. Séparer code et fonctions en [créant ses propres modules](/cours/coder-et-développer/apprendre-programmation/coder-projets/écrire-code/création-modules/)
2. [Tester ses fonctions](/cours/coder-et-développer/apprendre-programmation/coder-projets/outils/)

{% endaller %}

Pour aller plus loin, comment trouver des bugs de façon efficace :

{% aller %}
[Utiliser le débogueur pour corriger son code](/cours/coder-et-développer/apprendre-programmation/coder-projets/écrire-code/débogueur/)
{% endaller %}

### À vous

> 2h TP

Les 3 exercices se suivent et prennent les mêmes exemples. Faite un exemple au complet (fonction puis création module puis test) avant de passer à un autre.

{% aller %}

1. [Création de fonctions](/cours/coder-et-développer/apprendre-programmation/concepts/projet-codes/)
2. [Séparation main/fonctions](/cours/coder-et-développer/apprendre-programmation/coder-projets/écrire-code/projet-création-modules/)
3. [On ajoute des tests](/cours/coder-et-développer/apprendre-programmation/coder-projets/écrire-code/projet-codes-tests/)

{% endaller %}

Pour aller plus loin :

{% aller %}
[exercices divers](/cours/coder-et-développer/apprendre-programmation/coder-projets/exercices-tests/)
{% endaller %}
{% info %}
Vous aurez besoin d'utiliser des fichiers, donc lisez [la partie consacrée aux fichiers du cours](/cours/coder-et-développer/apprendre-programmation/coder-projets/gestion-données/fichiers/)
{% endinfo %}


### À rendre

> 2h DM à rendre sur Moodle

Lisez la partie du cours suivant et faire le rendu qu'il faudra déposer sur Moodle :

{% aller %}
1. [Bonnes pratiques et mantra](/cours/coder-et-développer/apprendre-programmation/coder-projets/écrire-code/bonnes-pratiques/)
2. [Mise en œuvre d'un projet informatique](/cours/coder-et-développer/apprendre-programmation/coder-projets/écrire-code/projet-informatique/)
{% endaller %}


{% faire "**Travail à rendre** "%}
Faite le [Projet pourcentage](/cours/coder-et-développer/apprendre-programmation/coder-projets/écrire-code/projet-pourcentages/). 
{% endfaire %}
{% attention %}
 Le travail (code + réponse aux questions) est à rendre [sur Moodle](https://moodle.centrale-med.fr/course/view.php?id=1523){.externe} **avant mercredi 16/09 à 8h00**.
{% endattention %}
{% info %}
Vous rendrez un dossier contenant :
- le code (uniquement les fichiers `.py`{.fichier} (main, fonctions et tests), pas le dossier `__pycache__`{.fichier} par exemple,)
- un ficher texte `réponses.md`{.fichier} où vous aurez répondu aux questions. Vous utiliserez [le format markdown](/cours/coder-et-développer/apprendre-programmation/coder-projets/écrire-code/projet-informatique/#doc).
{% endinfo %}



## Partie II : Classes et objets

{% prerequis "**À lire avant la séance**" %}
[Tout est objet en python](/cours/coder-et-développer/apprendre-programmation/programmation-objet/introduction/)
{% endprerequis %}

### Classe et objets en python

> 2h cours

{% aller %}
1. [Classes et objets](/cours/coder-et-développer/apprendre-programmation/programmation-objet/classes-et-objets/)
2. [Des dés](/cours/coder-et-développer/apprendre-programmation/programmation-objet/projet-objets-dés/)
{% endaller %}


> 2h TP (1h en autonomie)

{% aller %}
[Projet cartes](/cours/coder-et-développer/apprendre-programmation/programmation-objet/projet-objets-cartes/)
{% endaller %}

### Rendre ses objets plus conviviaux

> 1h CM

{% aller %}

1. [Améliorer ses objets](/cours/coder-et-développer/apprendre-programmation/programmation-objet/améliorer-ses-objets/)
2. [Des dés améliorés](/cours/coder-et-développer/apprendre-programmation/programmation-objet/projet-objets-dés-amélioration/)

{% endaller %}

> 1h TP

{% aller %}
[Projet Cartes améliorées](/cours/coder-et-développer/apprendre-programmation/programmation-objet/projet-objets-cartes-amélioration/)
{% endaller %}

### À rendre

> 2h DM à rendre sur github et ne mettre sur Moodle qu'un fichier texte contenant le lien vers le dépôt github.

{% prerequis "**Travail préparatoire**" %}
Mettre son code à disposition via un [Dépôt](/cours/gestion-des-sources/dépôt/) sur github.
{% endprerequis %}


{% faire "**Travail à rendre** "%}
[Projet Fractran](/cours/coder-et-développer/apprendre-programmation/programmation-objet/projet-fractran/)
{% endfaire %}
{% attention %}
 Le travail est à rendre **sur github** et en mettant le lien vers le déport [sur Moodle](https://moodle.centrale-med.fr/course/view.php?id=1523){.externe} **avant mercredi 23/09 à 8h00**.
{% endattention %}

## Partie III : Composition/agrégation et héritage

### Composition et agrégation

> 2h cours

{% aller %}
1. [Composition et agrégation](/cours/coder-et-développer/apprendre-programmation/programmation-objet/composition-agrégation/)
2. [Des compositions de dés](/cours/coder-et-développer/apprendre-programmation/programmation-objet/projet-composition-aggrégation-dés/)
{% endaller %}

> 2h TP (1h en autonomie)

{% aller %}
[Projet cartes et bataille](/cours/coder-et-développer/apprendre-programmation/programmation-objet/projet-agrégation-cartes/)
{% endaller %}

### Héritage

> 1h cours

{% aller %}
1. [Héritage](/cours/coder-et-développer/apprendre-programmation/programmation-objet/héritage/)
2. [Dés spécifiques](/cours/coder-et-développer/apprendre-programmation/programmation-objet/projet-objets-dés-héritage/)
{% endaller %}

> 1h TP

{% aller %}
[Projet héritage](/cours/coder-et-développer/apprendre-programmation/programmation-objet/projet-héritage/)
{% endaller %}

### À rendre

> 3h+ DM à rendre sur github et ne mettre sur Moodle qu'un fichier texte contenant le lien vers le dépôt github.


{% prerequis "**Travail préparatoire**" %}
1. [création d'un environnement virtuel](/cours/coder-et-développer/apprendre-programmation/gestion-dépendances/environnements-virtuels/) pour ses projets
2. mettre son code à disposition via un [Dépôt](/cours/gestion-des-sources/dépôt/) sur github.

{% endprerequis %}

{% faire %}

Rendre le projet [Bataille Navale](/cours/coder-et-développer/apprendre-programmation/programmation-objet/projet-bataille-navale/). 

Les consignes sont :

- le projet doit se trouver sur github
- mettre de la couleur dans vos sorties en utilisant le module <https://github.com/termcolor/termcolor>{.externe}
- il doit fonctionner avec un environnement virtuel : le fichier `requirements.txt`{.fichier} est requis


{% endfaire %}
{% attention %}
 Le travail est à rendre **sur github** et en mettant le lien vers le dépôt [sur Moodle](https://moodle.centrale-med.fr/course/view.php?id=1523){.externe} **avant mercredi 23/11 à 8h00**.
{% endattention %}

## Pour aller plus loin

Vous l'avez sans doute vu, ce cours est une extraction d'un cours plus vaste sur le développement logiciel (mais parfois encore en bordel et toujours en chantier). Ce cours est vaste et part de zéro pour arriver plus loin, si vous voulez y jeter un œil, il est disponible ici :

{% lien %}
[Coder et développer](/cours/coder-et-développer/)
{% endlien %}
