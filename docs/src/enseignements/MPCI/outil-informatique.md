---
layout: layout/post.njk 
title: "S1 : Ordinateur comme outil"

eleventyNavigation:
  order: 1

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title }}"
    parent: "{{ '../' | siteUrl(page.url) }}"

---

Pour parodier [full metal jacket](https://www.youtube.com/watch?v=fr_hvg7tNbQ) :

> Ça, c'est mon ordi. Il y en a beaucoup comme ça, mais lui, c'est le mien. Mon ordi, c'est mon meilleur ami.

Le but de cette séance est de vous donner les connaissances nécessaire pour avoir un ordinateur pour le développement.

## Utiliser le réseau

Connectez vous [au réseau Éduroam](https://www.eduroam.fr/) qui est le réseau des université européennes.

- login : votre adresse mail
- mot de passe : celui de l'ent AMU

Sous Linux vous pouvez cocher : *aucun certificat CA requis*.

## Connaissances minimales du système d'exploitation

### But

{% aller %}
[But d'un système d'exploitation](/cours/système-et-réseau/bases-système/bases/but){.interne}
{% endaller %}

### Installations système complémentaires

- **sous Linux/Ubuntu**, cela vaut le coup de lire le tuto ci-après qui liste différents paquets utiles : [post-installation](/cours/système-et-réseau/linux/bases-linux/post-installation/){.interne}
- **sous mac** installez <https://brew.sh/> qui vous permettra d'installer de nombreux package unix : [installer brew](/cours/système-et-réseau/bases-système/système-installation/brew/){.interne}.

### Dossiers et fichiers

{% aller %}
[Naviguer dans un système de fichiers](/cours/système-et-réseau/bases-système/bases/interactions/fichiers-navigation/){.interne}
{% endaller %}

## Ordinateur pour le développement en python

Vous aurez besoin d'installer python et un logiciel pour programmer :

{% aller %}
[Installer python et un interpréteur](/cours/coder-et-développer/bases-programmation/interpréteur/){.interne}
{% endaller %}

## Autre logiciels utiles

On ne donne ici que les moyens d'installer les logiciels. La façon des les utiliser sera expliquée par les enseignants des matières concernées.

### Développement et code

Vous aurez besoin de coder dans quasi toutes les matières. La bonne nouvelle c'est que les logiciels que l'on vous demande d'installer pour les cours d'informatiques (vscode et python, que vous avez déjà du installer) suffisent.

### Documents scientifiques

#### Latex

{% lien %}
- [Page Wikipedia de $\LaTeX$](https://fr.wikipedia.org/wiki/LaTeX)
- [Ressources sur Tex et Latex](https://www.tug.org/)
- [latex en ligne](https://www.overleaf.com/)
{% endlien %}

Produire des documents scientifiques se fait difficilement avec Word, de part la multiplicité des formules à écrire. La communauté scientifique préfère utiliser le logiciel Latex qui produit, à partir de fichiers textes, des documents pdf de qualité.

Latex est cependant un vieux programme, la gestion des packages à installer et les différentes étapes de *compilation* respirent les années 1980. Il vaut mieux installer le maximum de choses tout de suite histoire de ne pas avoir de paquets manquants. Ceci se fait en installant une [distribution](https://fr.wikipedia.org/wiki/Distribution#Informatique) Latex.

Installation de :

{% details "sous Windows 11" %}
Suivez la *easy install* de l'installation de la distribution TexLive :

<https://www.tug.org/texlive/windows.html>

{% enddetails %}

{% details "sous Linux/Ubuntu" %}
Suivez la *easy install* de l'installation de la distribution TexLive :

```
sudo apt install texlive-full
```

{% attention %}
C'est long (plus de 5GB à télécharger)
{% endattention %}
{% enddetails %}
{% details "sous Macos" %}
C'est la distribution MacTex qu'on installe. Deux possibilités pour le faire :

- par téléchargement via le site : <https://www.tug.org/mactex/>
- via brew : `brew install --cask mactex`{.language-}

{% enddetails %}

Pour utiliser latex, rien de tel qu'un bon tuto :

{% lien %}
<https://www.tuteurs.ens.fr/logiciels/latex/>
{% endlien %}

#### Typst

{% lien %}

- [typst](https://typst.app/#start)
- [installer typst chez vous](https://github.com/typst/typst)

{% endlien %}

Le petit nouveau qui fait (presque) tout comme son grand frère.

### Graphiques

Créer des graphiques scientifique est une science, voir un art. Avoir de bons outils pour le faire aide grandement.

{% lien %}
<http://www.gnuplot.info/>
{% endlien %}

Installation :

{% details "sous Windows 11" %}

1. allez dans le dossier contenant la dernière version de gnuplot sur [sourceforge](https://sourceforge.net/projects/gnuplot/files/gnuplot/). Chez moi c'est 5.4.8
2. téléchargez le fichier `.exe`. Chez moi c'est `gp548-win64-mingw.exe`{.fichier}
3. une fois téléchargé, vous pouvez cliquer dessus pour l'installer

{% lien %}
[un tuto](https://www.youtube.com/watch?v=GaXXpQXB4pg) d'utilisation de Latex.
{% endlien %}
{% enddetails %}

{% details "sous Linux/Ubuntu" %}
Un paquet à installer :

```
sudo apt install gnuplot
```

{% enddetails %}
{% details "sous Macos" %}
Avec brew :

```
brew install gnuplot
```

{% enddetails %}

Une fois le la logiciel installé, vous pourrez tester s'il fonctionne en :

1. tapant `gnuplot`{.language-} dans un terminal
2. dans le logiciel, tapez la commande : `plot exp(-x**2 /2)`{.language-} puis appuyez sur la touche entrée. Vous devriez voir une fenêtre s'afficher avec un graphique représentant la courbe $y=\text{exp}(\frac{-x^2}{2})$.
3. vous pouvez quitter le programme en tapant la commande `quit`{.language-}

{% lien %}
[Un petit tutorial](https://www.cs.hmc.edu/~vrable/gnuplot/using-gnuplot.html) d'utilisation de gnuplot.
{% endlien %}

### Mathématiques

{% lien %}
<https://www.geogebra.org/>
{% endlien %}

Vous pouvez utiliser les application directement sur le site en lançant l'application voulue depuis [le site](https://www.geogebra.org/download). Vous pouvez aussi l'installer :

{% details "sous Windows 11" %}
Téléchargez l'application GeoAlgebra Classique 5 depuis [le site](https://www.geogebra.org/download).
{% enddetails %}

{% details "sous Linux/Ubuntu" %}

```
sudo apt install geogebra
```

{% enddetails %}
{% details "sous Macos" %}
Deux possibilités :

- Téléchargez l'application GeoAlgebra Classique 5 depuis [le site](https://www.geogebra.org/download
- via brew : `brew install --cask geogebra`{.language-} et vous aurez même une version plus récente

{% attention %}
Comme Geogebra n'est pas une application signée, Macos ne vous laissera pas l'ouvrir automatiquement. Lors du premier lancement uniquement, vous devrez faire la procédure pour [Ouvrir une app Mac provenant d’un développeur non identifié](https://support.apple.com/fr-fr/guide/mac-help/mh40616/mac). Une fois cette manipulation effectuée, vous pourrez lancer l'application normalement.
{% endattention %}

{% enddetails %}
