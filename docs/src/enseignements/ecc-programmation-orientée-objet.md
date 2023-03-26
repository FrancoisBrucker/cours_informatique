---
layout: layout/post.njk 
title: Programmation Orientée Objet en Python

tags: ['formation', 'ECC']

eleventyNavigation:
  key: ECC
  parent: Enseignements
  order: 2

---

Cet enseignement est organisé en 3 types d'enseignements :

* 1 séance d'autonomie pour s'auto-former
* 5 séances de cours pour acquérir de nouvelles connaissances
* 8 séances machines pour s'entraîner, accompagné d'un professeur ou d'un corrigé

A l'issue de cet enseignement, l'élève aura de solides connaissance en programmation orientée objet et saura mener à bien un projet de développement en python.

## Notation

La notation de cet enseignement sera composée d'un projet à rendre par équipe de 4 élèves maximum.

## Programme

En plusieurs parties.

### <span id="partie-0"></span> Partie 0 : prérequis

{% note %}
Vérifiez que vous avez les prérequis pour suivre l'enseignement. S'il vous manque des connaissances, suivez les tutoriels et si vous avez encore des doutes après ça, n’hésitez pas à me contacter.
{% endnote %}

Les prérequis de ce cours sont minimaux, il faut avoir une connaissance moyenne du language python et des connaissances minimales de l'organisation de son ordinateur. Si vous n'avez pas ces prérequis ou que vous voulez vérifier que vous les avez suivez les tutoriels suivants :

1. [Avoir un système en état de marche]({{ '/tutoriels/installation-système'  }})
2. [Savoir naviguer dans un système de fichiers]({{ '/tutoriels/fichiers-navigation'  }})
3. Il pourra de plus être très utile de :
   * [Savoir ouvrir une fenêtre terminal]({{ '/tutoriels/terminal'   }})
   * [D'installez brew si vous êtes sous mac]({{ '/tutoriels/brew'   }})
4. [Connaissances minimales en python]({{ '/cours/coder-en-python'  }})

### <span id="partie-1"></span> Partie 1 : préparation

{% note %}
Le but de cette partie constituée d'**une séance d'autonomie** (le 23 septembre) est d'installer les différents logiciels nécessaires sur son ordinateur et de savoir les utiliser pour coder un projet un python.
{% endnote %}

Pour pouvoir écrire agréablement du code python qui fonctionne, il est nécessaire d'avoir des logiciels efficaces installés sur son ordinateur et — surtout — savoir s'en servir.

Programme de la séance :

1. [Installation de python]({{ '/tutoriels/installation-python'  }}) et de [vscode]({{ '/tutoriels/vsc-installation-et-prise-en-main'  }})
2. [Installer les plugins python de vscode]({{ '/tutoriels/vsc-python'  }})
3. [Un projet pour s'entraîner]({{ '/cours/algorithme-code-théorie/code/projet-hello-dev' }})

### <span id="partie-2"></span> Partie 2 : Classes et objets

{% note %}
Le but de cette partie constituée de **deux séances de cours** (les 26 et 27 septembre) et d'**une séance machine** (le 27 septembre) est de comprendre les notions d'objets et de classes pour pouvoir les implémenter en python.
{% endnote %}

#### <span id="partie-2-cours"></span> Cours

Deux séances de cours pour couvrir trois sujets :

1. [Mémoire et espace de noms]({{ '/cours/algorithme-code-théorie/code/mémoire-espace-noms' }})
2. [Classes et objets]({{ '/cours/algorithme-code-théorie/code/programmation-objet/classes-et-objets' }})
3. [Coder ses objets]({{ '/cours/algorithme-code-théorie/code/programmation-objet/coder-ses-objets' }})

#### Séance machine

Première mise en œuvre des exemple du cours et premières expérimentations :

[projet : coder des objets]({{ '/cours/algorithme-code-théorie/code/programmation-objet/projet-code-objets' }})

### <span id="partie-3"></span> Partie 3 : héritage

{% note %}
Le but de cette partie constituée de **deux séances de cours** (les 11 et 12 octobre) et de **deux séances machines** (les 12 et 13 octobre) est de comprendre la notion d'héritage qui est présente dans la plupart des langages objets.
{% endnote %}

#### <span id="partie-3-cours"></span> Cours

Deux séances de cours :

1. [Composition et agrégation]({{ '/cours/algorithme-code-théorie/code/programmation-objet/composition-agrégation' }})
2. [héritage]({{ '/cours/algorithme-code-théorie/code/programmation-objet/héritage' }})

#### Séances machine

1. [projet : composition et agrégation]({{ '/cours/algorithme-code-théorie/code/programmation-objet/projet-composition-agrégation' }})
2. [projet héritage]({{ '/cours/algorithme-code-théorie/code/programmation-objet/projet-héritage' }})

### Partie 4 : Test Driven Development

{% note %}
Le but de cette partie constituée de **deux séances machines** (du 21 novembre au 2 décembre) est de se familiariser avec la programmation par les tests en suivant un projet de bout en bout.
{% endnote %}

Deux séances machines en autonomie pour vos familiariser avec la *Programmation par les tests* (Test driven development en anglais). Cette méthode de développement fondamentale vous permet de coder de façon robuste et évolutive. Toutes les solutions sont données sous balise *spoiler*.

{% faire %}
Pendant ces deux séances, suivez le [projet Test Driven Development]({{ '/cours/algorithme-code-théorie/code/programmation-objet/projet-TDD' }}) et faites les différents exercices du par vous même puis comparez vos solutions au corrigé.
{% endfaire %}

{% attention %}
Cette méthode **doit être apprise et comprise** pour être efficace.

Si vous vous contentez de suivre la séance sans comprendre et sans essayer par vous même, cela ne fonctionnera pas et vous ne ferez que perdre votre temps.
{% endattention %}

### <span id="partie-5"></span> Partie 5 : Programmation événementielle

{% note %}
Cette partie est constituée d'**une séance de cours** (le 5 décembre) et de **deux séances machines** (les 6 et 7 décembre).
{% endnote %}

#### <span id="partie-5-cours"></span> Cours

1. [Programmation évènementielle]({{ '/cours/algorithme-code-théorie/code/programmation-évènementielle' }})

#### <span id="partie-5-machine"></span> Séances machine

1. [Projet Programmation évènementielle]({{ '/cours/algorithme-code-théorie/code/projet-programmation-évènementielle' }})

## <span id="PROJET-NOTÉ"></span> Projet Noté

**A rendre pour le 5 janvier 2023.**

1. le code (on doit pouvoir taper `python main.py` pour lancer le jeu)
2. les tests dans un fichier `test_snake.py`{.fichier} (on doit pouvoir taper `python -m pytest` pour exécuter les tests)
3. un ficher comportant :
   * une documentation de votre projet
   * les différentes étapes du projet que vous avez effectuées (les différents todos)

{% attention %}
SI je trouve des similitudes entre différents groupes ou que je trouve votre code sur internet, votre projet ne sera pas noté.
{% endattention %}

### Sujet

Création d'un [jeu du snake](https://fr.wikipedia.org/wiki/Snake_(genre_de_jeu_vid%C3%A9o))

* à chaque update (toutes les 1/10 secondes), le snake avance dans une des quatre directions haut, bas, gauche ou droite. Initialement, la tête du snake est placée au milieu de l'écran et il se déplace vers le haut.
* lorsque l'on appuie sur une touche de direction, la direction du snake change. On ne peut cependant pas aller à l'opposé de la direction actuelle
* lorsque l'on appuie sur la touche espace, le jeu se met en pause (le snake s'arrête de bouger et le score s'arrête d'augmenter). En appuyant sur la barre d'espace, le jeu redémarre.

Initialement, le jeu est en pause. Il faut appuyer sur la barre d'espace pour que le snake se déplace. La direction par défaut est vers le haut.

Le snake est composé de carrés de 20 pixels de long qui se suivent en se touchant par un côté. Initialement, le snake est constitué de 3 carrés.

Position initiale du snake (□ est la tête du snake) :

```text
 □
 O
 O
```

A chaque déplacement le 1er carré se déplace de 20 pixels dans la direction de déplacement, les carrés suivant se plaçant là où était le carré précédent (attention, le snake ne peut pas reculer).

Exemple. Position initiale du snake composé de 6 carrés (0 est la tête du snake) :

```text
  O□
  O
OOO
```

Déplacement vers le haut (de 20pixels) :

```text
   □
  OO
  O
 OO
```

Le jeu s'arrête si :

* le snake sort de l'écran
* un carré composant le snake se superpose avec un autre après un déplacement.

Le score augmente de 1 toutes les secondes où le snake est vivant et que le jeu n'est pas en pause. Initialement, le score vaut 0 et est affiché en haut à droite de l'écran.

Toutes les 5 secondes vont apparaître à l'écran (à une position aléatoire mais pas sur le snake) des disques de rayon 40 pixels. Lorsque le snake passe dessus, son score augmente de 5 et sa taille augmente de 5 carrés (le snake va grossir de 1 carré à chacun des 5 déplacements suivants) :

Exemple de grossissement du snake.

Position initiale :

```text
 OO□
```

On veut faire augmenter la taille du snake de 2 carrés. On suppose également que le snake se déplace vers le haut.

Après le 1er déplacement, le snake à grossi de 1 carré (X est le nouveau carré) :

```text
   □
 XOO
```

Après le 2ème déplacement, le snake a encore grossi de  carré (X est le nouveau carré) :

```text
   □
   O
 XOO
```

Finalement, le snake se déplace *normalement*. Par exemple, s'il continue de se déplacer vers le haut :

```text
   □
   O
   O
  OO
```

etc...

### Bonus/Malus/vies

Ajoutez à votre projet :

* des vies à votre snake
* des bonus qui diminuent la taille
* des bonus qui augmentent le score
* des malus qui font mourir le snake lorsque qu'il passe dessus

Vous expliciterez dans votre rapport comment vous avez fait pour implémenter ces différentes chose.

### Organisation du projet

Vous devez créer autant de classes que nécessaires pour votre projet. Il devra au moins avoir :

* votre rapport doit contenir les noms des membres de votre groupe.
* une classe `Snake`{.language}
* les 2 classes `Bonus`{.language} et `Malus`{.language} doivent hériter d'un même ancêtre

Vous devrez bien séparer ce qui a trait à l'interface pyglet (qi n'est pas pas testé) et ce est de l'ordre de l’interaction entre les différents objets (qui est testé).
