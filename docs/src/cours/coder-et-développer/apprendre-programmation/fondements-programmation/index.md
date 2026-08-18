---
layout: layout/post.njk

title: Bases de programmation
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


On a vue dans la partie système (le prérequis) qu'un programme s'exécute via un processeur, instruction par instruction. Presque plus personne ne crée de programmes directement en langage machine, on utilise des langages dit _évolués_ composées d'instructions spécifiques à celui-ci. Un programme d'un langage évolué est alors une suite d'instructions. 

{% note2 "**Définition**" %}
Pour qu'un programme puisse être exécuté par le processeur d'un ordinateur chacune de ses instructions doit être traduite en instructions machine avant son exécution. Il existe trois stratégies pour cela :

- convertir le programme en entier avant exécution. Les langages appliquant cette stratégie sont dit **_langages compilés_** et regroupe des langages comme le Go ou le Rust (ou des dinosaures comme le C ou le C++).
- convertir les instructions une à une au cours de l'exécution du programme. Les langages appliquant cette stratégie sont dit **_langages interprétés_**, ou encore **_langages de script_** et regroupe des langages comme le python ou le javascript par exemple (ou encore le Ruby)
- méthode hybride : convertir le programme en entier avant exécution dans un langage un peu plus évolué que le langage machine appelé [bytecode](https://fr.wikipedia.org/wiki/Bytecode). Le java ou le C# sont des langages appliquant cette stratégie.

{% endnote2 %}

Selon l'usage que l'on veut en faire on utilisera l'un ou l'autre de ces langages :

- langages compilés :
  - **avantages** : la compilation permet de vérifier que tout le programme est correct avant exécution et on peut optimiser le langage machine produit pour le système ou le processeur utilisé.
  - **inconvénients** : l'étape de compilation est à faire après toute modification du code source et le programme compilé ne fonctionne que sur un système et un processeur donné.
- langages interprété :
  - **avantages** : il n'y a pas de différence entre le code source et le programme à exécuter. On peut modifier puis exécuter rapidement du code
  - **inconvénients** : nécessite un programme, appelé [interpréteur](https://fr.wikipedia.org/wiki/Interpr%C3%A8te_%28informatique%29), qui fait la transcription instruction par instruction
- bytecode : combine les avantage/inconvénient des deux 
  - **avantages** : le bytecode est portable (indépendant du système et du processeur) et l'étape de compilation permet d'optimiser le code presque autant qu'avec un langage compilé.
  - **inconvénients** : nécessite une étape de compilation un programme, et doit être exécuté par un programme appelé [machine virtuelle](https://fr.wikipedia.org/wiki/Machine_virtuelle#Machine_virtuelle_de_haut_niveau)


{% attention2 "**À retenir**" %}
Il n'y a pas de mauvaise stratégie, il faut utiliser le langage adapté à notre situation/projet :

- petits projets ou code devant être modifié souvent : langage de script
- gros projets sur la durée devant être exécuté sur de nombreuses machines différentes : bytecode
- projets dont la vitesse d'exécution est primordiale : langages compilés

En plus de cela, chaque langage va bien sur avoir sa spécificité, mais rappelez-vous :

> Plus on veut du code rapide (ou optimisé) plus on va passer du temps a l'écrire et moins il sera portable.

{% endattention2 %}


Nous utiliserons ainsi ici [le langage python](<https://fr.wikipedia.org/wiki/Python_(langage)>) qui est un langage interprété très simple à utiliser. Ce sera l'idéal pour comprendre et assimiler toutes les méthodes et techniques principales en développement.

> TBD mettre notebook dans la partie analyse des données : (notebook de basthon) mais surtout collab (re print et exemple avec graphique matplotlib)

## Exécuter du code python avec un interpréteur

{% aller %}
[Utiliser un interpréteur](./interpréteur-principes){.interne}
{% endaller %}


## Élément de langage

> TBD écrire du code exécutable.

### Variables et objets

> stocker et retrouver ses petits

> manipuler des objets via des opérations et des néthodes
> 
### Fonctions et modules

> manipuler des objets via des fonctions
> groupement de fonctions dans des 

## Partie I : Variables et objets

Coder revient à manipuler des objets via des variables. Nous allons ici définir ces terme et expliciter les différents moyens mis en oeuvre par python (et par extension tous les langages) pour le faire.

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
