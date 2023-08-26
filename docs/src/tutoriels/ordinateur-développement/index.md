---
layout: layout/post.njk

title: Ordinateur pour le développement
tags: ['tutoriel', 'vsc', 'terminal', 'système']
authors: 
    - François Brucker

eleventyComputed:
    eleventyNavigation:
        key: "{{ page.url }}"
        title: "{{ title | safe }}"
        parent: Tutoriels
---

Utiliser son ordinateur pour le développement nécessite quelques connaissances et outils pour que tout se passe au mieux. Rien d'insurmontable, mais si on ne le fait pas on a vite un système instable où rien de marche comme il faudrait.

Il faut résister à la tentation de faire n'importe quoi en espérant que ça passe car, au bout du compte, on perd plus de temps à réparer qu'on en gagne à installer sans préparation.

{% info %}
On regardera comment faire sous 3 systèmes d'exploitations :

* Windows 11
* Macos
* Linux/Ubuntu (si vous êtes avec une autre distribution, vous devriez savoir vous déb rouiller tout seul)
{% endinfo %}

## Préparation

### Compte utilisateur

Votre compte utilisateur avec lequel vous allez faire du développement (qui peut être votre compte principal) doit posséder quelques propriétés qui vont vous faire gagner du temps :

* doit être un ***compte administrateur*** (pouvant exécuter la commande [`sudo`](https://www.linuxtricks.fr/wiki/print.php?id=480) si vous êtes sous Linux)
* votre nom de compte ne doit contenir ***ni espace ni accent***

Si votre compte ne satisfait pas les deux critères ci-dessus :

{% faire %}
Création d'un compte administrateur :

* [sous Windows 11](https://support.microsoft.com/fr-fr/windows/cr%C3%A9er-un-compte-d-administrateur-ou-d-utilisateur-local-dans-windows-20de74e0-ac7f-3502-a866-32915af2a34d)
* [sous Macos](https://support.apple.com/fr-fr/guide/mac-help/mchl3e281fc9/mac)
* [sous Linux/Ubuntu](https://guide.ubuntu-fr.org/desktop/user-add.html)
{% endfaire %}

### Installation d'un nouveau système

Cette étape est **optionnelle**, mais souvent très utile si vous avez votre ordinateur depuis longtemps et que vous y avez installé plein de choses de façon anarchique sans trop savoir ce que vous faisiez.

{% aller %}
[Installation d'un nouveau système](installation-nouveau-système){.interne}
{% endaller %}

## Applications indispensables

Quelques applications sont indispensables pour utiliser son ordinateur pour le développement. Nous allons présenter ici les plus importantes, installées par défaut et que tout utilisateur doit avoir constamment sous la main.

### Un navigateur

Il en existe de nombreux et tout système en a un par défaut ([edge](https://fr.wikipedia.org/wiki/Microsoft_Edge), [safari](https://fr.wikipedia.org/wiki/Safari_(navigateur_web)) ou [firefox](https://fr.wikipedia.org/wiki/Mozilla_Firefox)).

### Un outil de compression/décompression de fichiers

Compresser ou décompresser des fichiers est indispensable. Un outil de compression est déjà installé pour les trois systèmes. Pour l'utiliser depuis un explorateur de fichier, il suffit de cliquer droit sur le dossier ou le fichier que vous voulez compresser et choisissez l'item `compresser` du menu.

### Un éditeur de texte à tout faire

On a souvent besoin de lire ou d'éditer un fichier texte rapidement, que ce soit lire un readme, éditeur un fichier de configuration, corriger rapidement un faute dans un fichier Latex, etc.

Nous en donnons 3, un par système d'exploitation qui ont l'avantage d'être directement utilisable et qui possèdent une interface graphique.

{% details "sous Windows 11" %}
Je conseille d'installer [notepad++](https://notepad-plus-plus.org/)

{% enddetails %}
{% details "sous Macos" %}
Je conseille d'utiliser la version gratuite (ou de payer le logiciel si vous l'utilisez beaucoup ou avec besoin des fonctionnalités avancées que la version payante propose) de [bbedit](http://www.barebones.com/products/bbedit/).

{% enddetails %}
{% details "sous Linux/Ubuntu" %}
Par défaut, Ubuntu installe l'application `Éditeur de texte` qui permet d'éditer et de modifier des fichiers textes.

{% enddetails %}

## Connaissances indispensables

### Système de Fichiers

Savoir comment est organisé le disque dur de votre ordinateur

{% aller %}
[Naviguer dans un système de fichiers](../fichiers-navigation){.interne}
{% endaller %}

### Utilisation du Terminal

Le terminal permet d'exécuter rapidement des commandes.

{% aller %}
[Terminal](../terminal){.interne}
{% endaller %}

## Outils utiles

Les outils ci-après ne sont pas stricto-sensu obligatoire, mais les avoir va fluidifier vos développements.

### <span id="gestionnaire-package"></span>Un gestionnaire de package

Sous Linux et Macos, l'installation d'applications Unix se fait via l'utilisation d'un gestionnaire de package.

{% details "sous Macos" %}

N'installez **aucun logiciel unix** sous mac à la main. Utilisez toujours [brew](https://brew.sh/index_fr) pour le faire.

{% faire %}
Suivez les instructions du tutoriel suivant pour installer le gestionnaire.
{% aller %}
[tutoriel brew](../brew){.interne}
{% endaller %}
{% endfaire %}

{% enddetails %}
{% details "sous Linux/Ubuntu" %}

{% faire %}
Suivez les instructions du tutoriel suivant pour savoir comment utiliser ces deux applications.

{% aller %}
[tutoriel apt et snap](../apt-snap){.interne}
{% endaller %}

{% endfaire %}

{% enddetails %}

### Un IDE générique

Un [IDE](https://fr.wikipedia.org/wiki/Environnement_de_d%C3%A9veloppement) permet de créer rapidement des projets. Il en existe de nombreux, allant du très générique au très particulier.

Actuellement, l'éditeur générique en vogue est [vscode](https://code.visualstudio.com/)

{% aller %}
Suivez le tutorial pour [l'installation de vscode](../vsc-installation-et-prise-en-main){.interne}
{% endaller %}
