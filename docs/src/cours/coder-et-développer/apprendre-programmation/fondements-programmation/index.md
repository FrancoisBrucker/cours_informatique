---
layout: layout/post.njk

title: Fondements de la programmation (avec python)
authors:
  - François Brucker
  - Pierre Brucker

eleventyNavigation:
    prerequis:
        - "/cours/système/ordinateur-programmes-OS/"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Nous allons voir dans cette partie tout ce qui est nécessaire pour exécuter et créer son propre code python. Tout ce que l'on verra ici est applicable pour tous les langages de programmation.

_Python_ est un [langage de programmation](https://fr.wikipedia.org/wiki/Langage_de_programmation) inventé en 1991 par [Guido van Rossum](https://fr.wikipedia.org/wiki/Guido_van_Rossum). C'est comme une langue mais en beaucoup plus simple car :

- il n'y a pas d'exception
- il y a très peu de vocabulaire de base
- il est structuré en lignes et non en phrase

Son but est de faire faire des choses à un ordinateur.

## Exécuter du code python

On ne peut cependant pas directement donner un texte écrit en python (qu'on appelle **_code_** ou **_programme_**) à un ordinateur pour qu'il l'exécute car celui-ci ne comprend que le [langage machine](https://fr.wikipedia.org/wiki/Langage_machine), on passe par un intermédiaire, un programme nommé **_interpréteur python_**.

{% aller %}
[Exécuter du code python](./exécuter-code/){.interne}
{% endaller %}

## Éléments du langage

> TBD ici remonter commentaire plus haut
> code = manipuler des objets.
> et faire 2 parties : les objets (créer et manipuler des objets)

Faire faire des choses à un ordinateur nécessite de communiquer avec lui via des instructions qui sont structurés comme un langage. Nous allons montrer ici les fondement de tout langage de programmation.



{% aller %}
[Écrire du code python](./écrire-code/){.interne}
{% endaller %}

## Structurer son code

> TBD que faire des opérations on ne peut pas faire grand chose. 
> exécution conditionnelles et grouper des instructions entre elles.
> 
Nous avons vu comment 


### Fonctions et modules

> manipuler des objets via des fonctions
> groupement de fonctions dans des 

## Partie I : Variables et objets


### Principes

Avant d'écrire des programmes en python, on commence par s'intéresser à ses mécanismes internes en comprenant ce qu'est une instruction python et ce que'on peut faire avec.

{% aller %}
[Principes](principes){.interne}
{% endaller %}


<!-- TBD 

Faire des exercices : 

- utilisation de modules et de fonctions de python
- les différents imports possibles

-->


### Exécuter du code python


### <span id="installation-développement"></span>Installer et utiliser un interpréteur python

> installer un interpréteur
> vscode ou pycharm dans un second temps


Jusqu'à présent on a utilisé des interpréteurs externes pour exécuter notre code. Si l'on cherche à créer ses propres programmes, il est préférable d'avoir un interpréteur sur propre ordinateur. Ceci sera plus rapide et permettra à terme d'être paramétrable à l'envie.

{% aller %}
[Installer un interpréteur python](interpréteur){.interne}
{% endaller %}

Une fois l'interpréteur installé, plutôt que de l'utiliser directement, on utilise un éditeur de texte spécialisé dans l'écriture de code : [un IDE](https://fr.wikipedia.org/wiki/Environnement_de_d%C3%A9veloppement). Il existe plusieurs choix possible, mais le plus utilisé actuellement est vscode.

{% aller %}
[Éditeur vscode](éditeur-vscode){.interne}
{% endaller %}

La principale différence entre un éditeur de texte et un notebook est que l'interpréteur est re-exécuté à chaque exécution : il ne garde rien en mémoire de la précédente exécution du code. Ceci permet de faire du code rép´table où toutes les informations sont uniquement contenues dans le fichier que l'on exécute.

## Partie II : Structures du code

Lorsque l'on veut plus que juste utiliser des méthodes et fonctions déjà existantes, il faut structurer son code en parties utilisables indépendamment, que ce soit sous la forme de code (bloc, fonctions) ou de données (conteneurs).

{% attention2 "**À retenir**" %}
Dans tous les exemple de code qui suivront, lorsque l'on écrira du code python, il faudra pour l'exécuter l'écrire dans un fichier. Ne seront visible à l'exécution que les affichages à l'écran. Par exemple le résultat du code :

```python
print(21 * 2)
```

Sera l'affichage à l'écran de 42. Le code suivant n'écrira rien à l'écran :

```python
21 * 2
```

L'objet produit, un entier valant 42, n'est pas utilisé.

{% endattention2 %}
{% info %}
Il y a donc deux type d'exemples de code :

- ceux commençant par un `>>>`{.language-} dont le but est d'être directement exécuté dans [un interpréteur](./principes/interpréteur/){.language-} et dont on verra directement le résultat de chaque instruction,
- les programmes dont le but est d'être exécuté via un éditeur comme vscode par exemple et qui consisteront la grande majorité des exemples donnés
{% endinfo %}

### <span id="blocs"></span> Blocs de code

Si python ne pouvait qu'exécuter ligne à ligne un code on ne pourrait pas faire grand chose. Le principe des programmes est de pouvoir grouper les instructions en blocs.

{% note2 "**Définition**" %}

Les **_blocs_** en python permettent de grouper des lignes de code qui seront exécutées ensemble sous certaines conditions. Un bloc est toujours défini de la même manière :

- Ce qui va identifier le bloc pour son exécution (une condition, son nombre d'exécution, son nom) et se finit par un `:`{.language-}
- Les instructions le constituant.

{% endnote2 %}

Pour séparer les blocs les un des autres, et savoir ce qui le définit, le langage Python utilise l'indentation (4 espaces par défaut): un bloc est donc une suite d'instructions ayant la même indentation.

```text
type_de_bloc:
    instruction 1
    instruction 2
    ...
    instruction n
```

Ces différents blocs sont pratiques car ils vont nous permettre :

- d'exécuter des blocs conditionnellement
- de répéter des blocs

Les blocs peuvent bien sur se combiner :

```text
bloc A:
    instruction 1 du bloc A
    bloc B:
        instruction 1 du bloc B
        ...
        instruction m du bloc B
    instruction 2 du bloc A
    ...
    instruction n du bloc A
```

{% attention2 "**À retenir**" %}
L'indentation permet **toujours** de s'y retrouver.

{% endattention2 %}
{% info %}
<span id="interpréteur-blocs"></span>

Lorsque l'on crée un bloc avec l'interpréteur, après la première ligne qui défini le bloc (la ligne avec le `:`{.language-}.
), l'interpréteur passe en _mode bloc_ (il écrit `...` en début de ligne) ce qui permet d'écrire son bloc (en n'oubliant pas l'indentation). Une fois le bloc terminé, pour faire repasser l'interpréteur en mode normal et exécuter le bloc on appuie juste sur la touche entrée pour insérer ue ligne vide.

Par exemple l'exemple suivant crée un bloc qui écrit `coucou`{.language} indéfiniment directement dans l'interpréteur :

```python
>>> while True:
...     print("coucou")
...
```

Le même bloc écrit dans un éditeur puis exécuté aurait été écrit comme ça :

```python
while True:
    print("coucou")
```

{% endinfo %}

#### Instructions conditionnelles

{% aller %}
[Exécution conditionnelle de blocs](bloc-condition){.interne}
{% endaller %}

#### Répétitions

{% aller %}
[Répétition de blocs](bloc-répétition){.interne}
{% endaller %}

#### Exercice

{% exercice %}
Utilisez ce que vous avez appris pour vérifier la [conjecture de Syracuse](https://fr.wikipedia.org/wiki/Conjecture_de_Syracuse) pour les 100 premiers entiers.
{% endexercice %}
{% details "solution" %}

```python

for x in range(100):
    while x > 1:
        if x % 2  == 0:
            x /= 2
        else:
            x = 3 * x + 1
```

{% enddetails %}

### Fonctions

Si un bloc de code est exécuté plusieurs fois à l'identique, on aimerait aussi pouvoir nommer ce groupe pour **pouvoir le réutiliser juste en appelant son nom**. C'est possible avec les fonctions.

{% aller %}
[Création de fonctions](creation-fonctions){.interne}
{% endaller %}


<!-- TBD 

Faire des exercices : faire des fonctions

-->

## Partie III : Structures de données

### <span id="conteneurs"></span>Conteneurs

Les conteneurs sont des objets contenant d'autres objets. Ils permettent de structurer ses données.

{% aller %}
[Conteneurs](conteneurs){.interne}
{% endaller %}

### Mutable et non mutable

{% attention %}
La notion de mutabilité d'un objet est cruciale à comprendre. Elle permet du code clair et optimisé (aucun objet n'est copié) mais est la cause de nombre d'erreurs a priori incompréhensibles si on ne l’appréhende pas bien.
{% endattention %}
{% aller %}
[Objets mutables et non mutables](mutable-immutable){.interne}
{% endaller %}


<!-- TBD 

Faire des exercices : listes et dictionnaires.

-->


## Partie IV : Structures du programme

Structurer son programmes en fichiers.

### Modules

{% aller %}
[Création de modules](creation-modules){.interne}
{% endaller %}

### Espace de nommage

La base de cette séparation en unités fonctionnelles séparée est l'espace de nommage. Nous l'avons déjà entre-aperçu lorsque l'on a parlé de modules et de fonctions, nous allons ici rentrer dans les détails et expliciter comment python trouve un objet associé à un nom.

{% aller %}
[Espace de nommage](espace-nommage){.interne}
{% endaller %}

{% aller %}
[Espace de nommage et fonctions](fct-espace-nommage){.interne}
{% endaller %}
