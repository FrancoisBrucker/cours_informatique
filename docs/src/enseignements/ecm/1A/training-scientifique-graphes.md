---
layout: layout/post.njk
templateEngineOverride: njk, md

title: "Training scientifique : Théorie des graphes"
tags: ['enseignement', 'ECM']

eleventyNavigation:
  order: 0

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

<!-- début résumé -->

Une semaine pour s'initier à la théorie des graphes. Outre un intérêt scientifique et théorique certain, la théorie des graphes permet de résoudre un nombre important de problèmes concrets courant pour un ingénieur.

Ce cours est séparer en trois parties, contenant chacune un volet théorique  où et un volet applicatif où seront mis en œuvre et en python le concepts théoriques abordés.

<!-- fin résumé -->

Cet enseignement est basé sur [l'introduction à la théorie des graphes]({{ "/cours/graphes"  }}) dont il reprend la structure mais n'entre pas dans tous les détails. Nous nous focaliserons sur trois problèmes :

1. connexité et cycles
2. chemins de poids minimums
3. flots

## <span id="partie-1"></span> Partie 1 : préparation

Pour pouvoir écrire agréablement du code python qui fonctionne, il est nécessaire d'avoir des logiciels efficaces installés sur son ordinateur et — surtout — savoir s'en servir.

Pour la partie code de ce cours, il est **indispensable d'avoir un environnement python qui fonctionne**.  Vous pouvez utiliser spyder, jupyter notebook ou tout autre ide que vous avez utilisé en prépa.

{% faire %}
Assurez vous d'avoir un environnement python qui fonctionne.
{% endfaire %}

### Configuration recommandée

Il vous est cependant recommandé, si l'informatique vous intéresse, d'installer et d'utiliser un python et un éditeur de texte professionnel. Pour cela, suivez les 3 parties suivantes :

1. [Installation de python]({{ '/tutoriels/installation-python'  }}) et de [vscode]({{ '/tutoriels/vsc-installation-et-prise-en-main'  }})
2. [Installer les plugins python de vscode]({{ '/tutoriels/vsc-python'  }})
3. [Un projet pour s'entraîner]({{ '/cours/algorithme-code-théorie/code/projet-hello-dev' }})

### Prérequis

Les prérequis de ce cours sont minimaux, il faut avoir une connaissance moyenne du language python et des connaissances minimales de l'organisation de son ordinateur. Si vous n'avez pas ces prérequis ou que vous voulez vérifier que vous les avez suivez les tutoriels suivants :

1. [Avoir un système en état de marche]({{ '/tutoriels/installation-nouveau-système'  }})
2. [Savoir naviguer dans un système de fichiers]({{ '/tutoriels/fichiers-navigation'  }})
3. Il pourra de plus être très utile de :
   * [Savoir ouvrir une fenêtre terminal]({{ '/tutoriels/terminal'   }})
   * [D'installez brew si vous êtes sous mac]({{ '/tutoriels/brew'   }})
4. [Connaissances minimales en python]({{ '/cours/utiliser-python'  }})

## Partie 2 : Cours

### Lundi

* graphes : partie [Structure]({{ "/cours/graphes" }}#structure) du cours de graphe
* problème théorique : [chemins eulérien]({{ "/cours/graphes/parcours-eulériens" }})
* application : [Mots de Bruijn]({{ "/cours/graphes/projet-mots-bruijn" }})

### Mardi

* graphes et algorithmes : partie [Problème de la partie chemins de longueur minimum]({{ "/cours/graphes" }}#chemin-problèmes)
* applications :
  * [Projet chemins de longueur minimum]({{ "/cours/graphes/projet-chemins-min" }})
  * [Projet graphe géographique]({{ "/cours/graphes/projet-graphe-géographique" }})

### Vendredi

* graphes : [flots]({{ "/cours/graphes/flots" }})
* [projet modélisation]({{ "/cours/graphes/projet-flots-modélisation" }})
