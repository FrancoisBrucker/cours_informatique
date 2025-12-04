---
layout: layout/post.njk

title: Bases de programmation et du langage python
authors:
  - François Brucker
  - Pierre Brucker

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Nous montrerons dans ce cours les bases du codage en utilisant le langage de programmation [python](<https://fr.wikipedia.org/wiki/Python_(langage)>) dont le site est : <https://www.python.org/>

Nous verrons comment est structuré un langage informatique et comment écrire puis exécuter du code.

Ce n'est pas un cours d'informatique proprement dit, nous ne ferons quasiment pas d'algorithmie par exemple et il n'y a aucun prérequis informatique à avoir. Le but est de pouvoir exécuter (de la façon la plus optimale possible) des lignes de code pour obtenir un résultat concret (qui n'aura souvent rien à voir avec de l'informatique).

## Partie I : Variables et objets

Coder revient à manipuler des objets via des variables. Nous allons ici définir ces terme et expliciter les différents moyens mis en oeuvre par python (et par extension tous les langages) pour le faire.

### Principes

Avant d'écrire des programmes en python, on commence par s'intéresser à ses mécanismes internes en comprenant ce qu'est une instruction python et ce que'on peut faire avec.

{% aller %}
[Principes](principes){.interne}
{% endaller %}

### Exécuter du code python

On a utilisé un interpréteur externe (sur le site <https://basthon.fr/>) pour l'instant. Son utilisation n'est pas tès satisfaisante pour l'instant puisqu'il faut copier/coller chaque ligne dans l'interpréteur.

La façon classique d'exécuter du code python est d'utiliser un intermédiaire entre l'interpréteur et son code. Nous allons montrer deux façons classiques de le faire.

#### Notebooks

[Les Notebooks](https://jupyter.org/) sont des solutions pratiques lorsque l'on veut exécuter rapidement un petit bout de code ou une série de bouts de codes plus ou moins indépendant : lorsque l'on utilise l'outil informatique pour faire des maths ou de la physique par exemple ; ou encore lorsque l'on fait de la data science.

{% lien %}
Deux possibilités simples d'acceder à des notebook :

- <https://basthon.fr/> (qui est géré par l'éducation nationale)
- <https://colab.google/> (qui est géré par google)

{% endlien %}

Leur utilisation est particulièrement adaptée pour rédiger et partager des comptes-rendus.

{% aller %}
[Notebooks](notebooks){.interne}
{% endaller %}

#### Spyder

{% lien %}
<https://www.spyder-ide.org/>
{% endlien %}

Spyder est un éditeur lié à un interpréteur python. L'application est très utilisée lorsque l'on commence à apprendre la programmation. Et permet d'écrire des programmes tout en conservant un unique interpréteur accessible par une console.

Il fonctionne à la fois comme un notebook ou comme un interpréteur.

{% attention %}
La commande `Run file` exécute son code dans un nouvel interpréteur **puis** le fusionne avec l'interpréteur courant.

Ce fonctionnement est déroutant...
{% endattention %}

Si vous voulez faire du développement sérieusement, je vous conseille d'utiliser plutôt la combinaison éditeur + interpréteur ci-dessous.

### <span id="installation-développement"></span>Installer et utiliser un interpréteur python

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

{% info %}
Pour tester le code de cette partie utilisez [l'éditeur vscode](éditeur-vscode){.interne}.
{% endinfo %}

### Blocs de code

Si python ne pouvait qu'exécuter ligne à ligne un code on ne pourrait pas faire grand chose. Le principe des programmes est de pouvoir grouper les instructions en blocs.

{% note "**Définition**" %}

Les **_blocs_** en python permettent de grouper des lignes de code qui seront exécutées ensemble sous certaines conditions. Un bloc est toujours défini de la même manière :

- Ce qui va identifier le bloc pour son exécution (une condition, son nombre d'exécution, son nom) et se finit par un `:`{.language-}
- Les instructions le constituant.

{% endnote %}

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

{% attention "**À retenir**" %}
L'indentation permet **toujours** de s'y retrouver.
{% endattention %}
{% details "blocs dans l'interpréteur" %}
<span id="interpréteur-blocs"></span>

Lorsque l'on crée un bloc avec l'interpréteur, après la première ligne qui défini le bloc (la ligne avec le `:`{.language-}.
), l'interpréteur passe en _mode bloc_ (il écrit `...` en début de ligne) ce qui permet d'écrire son bloc (en n'oubliant pas l'indentation). Une fois le bloc terminé, pour faire repasser l'interpréteur en mode normal et exécuter le bloc on appuie juste sur la touche entrée pour insérer ue ligne vide.

Par exemple l'exemple suivant crée un bloc qui écrit `coucou`{.language} indéfiniment directement dans l'interpréteur :

```python
>>> while True:
...     print("coucou")
...
```

Le même bloc écrit dans un notebook puis exécuté aurait été écrit comme ça :

```python
while True:
    print("coucou")
```

{% enddetails %}

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

## Partie III : Structures des données

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
