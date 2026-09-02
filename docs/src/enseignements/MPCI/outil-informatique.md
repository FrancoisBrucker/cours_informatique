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

## <span id="eduroam"></span>Utiliser le réseau

[Le réseau Éduroam](https://www.eduroam.fr/) est le réseau des université européennes. Il est disponible partout (pour vous à AMU et à l'ECM) et est gratuit. 

{% faire %}
Connectez vous au  réseau WIFI éduroam : 

- **login** : votre adresse mail
- **mot de passe** : celui de l'ent AMU

{% endfaire %}
{% info %}
Sous Linux vous pouvez cocher : *aucun certificat CA requis*.
{% endinfo %}

## Connaissances minimales du système d'exploitation

Les bases nécessaire pour pouvoir appréhender le fonctionnement d'un ordinateur et pouvoir l'utiliser au quotidien :

{% aller %}
- [Bases d'un système d'exploitation](/cours/système/ordinateur-programmes-OS/){.interne}
- [le terminal](../terminal/bases/){.interne}.
- [gestionnaire de paquets](/cours/système/interagir-avec-système/gestionnaire-paquets/){.interne}
{% endaller %}


## Logiciels à installer pour l'informatique

On va lister ici des logiciels qui vous seront utiles en informatique, mais pas que.

### spyder

{% lien %}
<https://www.spyder-ide.org/>
{% endlien %}

Le logiciel que vous utiliserez pour faire du python en S1.

- sous Windows et Macos : utilisez le lien donné sur le site
- sous Linux. Dans un terminal tapez la commande : `sudo apt install spyder` (il vous faudra peut-être aussi installer le paquet ` python3-spyder-kernels` mais essayez sans et dites mois si ça marche)

Pour vérifier que ça fonctionne, lisez la partie du cours qui y est consacrée :

{% aller %}
[Éditeur Spyder](/cours/coder-et-développer/apprendre-programmation/concepts/fondements-programmation/exécuter-code/#spyder){.interne}
{% endaller %}
{% info %}
Retrouvez sous windows et Linux comment suivre la visite guidée (pour l'instant il y a un TBD car je n'ai qu'un mac)
{% endinfo %}

### vscode

{% lien %}
<https://code.visualstudio.com/>
{% endlien %}

{% aller %}
[Prise en main de vscode](/cours/coder-et-développer/apprendre-programmation/coder-projets/outils/éditeur-vscode/prise-en-main/){.interne}
{% endaller %}

### Interpréteur python

{% aller %}
[Installer un interpréteur Python](/cours/coder-et-développer/apprendre-programmation/coder-projets/outils/interpréteur-installation/){.interne}
{% endaller %}


## Autre logiciels utiles

On ne donne ici que les moyens d'installer les logiciels. La façon des les utiliser sera expliquée par les enseignants des matières concernées.

### Documents scientifiques

Produire des documents scientifiques se fait difficilement avec Word, de part la multiplicité des formules à écrire. La communauté scientifique préfère utiliser le logiciel Latex qui produit, à partir de fichiers textes, des documents pdf de qualité.


#### Markdown

Ne nécessite pas à proprement parler de logiciel, c'est une façon d'écrire du texte. 

{% lien %}
- [tutoriel markdown](https://grafikart.fr/tutoriels/markdown-377)
- [plugin vscode](https://marketplace.visualstudio.com/items?itemName=yzhang.markdown-all-in-one)
{% endlien %}

#### Typst

L'outil actuel pour créer ses documents scientifiques.

{% lien %}

- [typst](https://typst.app/#start)
- [installer typst chez vous](https://github.com/typst/typst)
- [plugin vscode](https://marketplace.visualstudio.com/items?itemName=myriad-dreamin.tinymist)
{% endlien %}

#### Latex

Le prédécesseur de typst.

{% lien %}

- [Page Wikipedia de $\LaTeX$](https://fr.wikipedia.org/wiki/LaTeX)
- [Ressources sur Tex et Latex](https://www.tug.org/)
- [latex en ligne](https://www.overleaf.com/)
- [plugin vscode](https://marketplace.visualstudio.com/items?itemName=James-Yu.latex-workshop)

{% endlien %}

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

Il existe un plugin vscode :

{% lien %}
<>
{% endlien %}

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
Téléchargez l'application GeoAlgebra Classique 5 depuis [leur site](https://www.geogebra.org/download)

{% attention %}
Comme Geogebra n'est pas une application signée, Macos ne vous laissera pas l'ouvrir automatiquement. Lors du premier lancement uniquement, vous devrez faire la procédure pour [Ouvrir une app Mac provenant d’un développeur non identifié](https://support.apple.com/fr-fr/guide/mac-help/mh40616/mac). Une fois cette manipulation effectuée, vous pourrez lancer l'application normalement.
{% endattention %}

{% enddetails %}
