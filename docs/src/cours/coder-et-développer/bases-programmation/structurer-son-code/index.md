---
layout: layout/post.njk

title: Structurer son code

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---


Lorsque l'on veut plus que juste utiliser des méthodes et fonctions déjà existante, il faut structurer son code en parties utilisables indépendamment, que ce soit sous la forme de code (bloc, fonctions, modules) ou de données (conteneurs).

Nous n'utiliserons plus directement l'interpréteur pour nos futurs code. En effet, créer des bloc directement avec l'interpréteur est un calvaire car il est fait pour exécuter une ligne après l'autre alors qu'un bloc nécessite plusieurs lignes.

{% info %}
Utilisez un projet vscode (ou à la la limite un notebook ou Spyder) pour exécuter les divers exemples et exercices. [Utiliser directement l'interpréteur pour écrire des blocs](./#interpréteur-blocs) qui vont s'étendre sur plusieurs lignes est pénible.
{% endinfo %}

## Bloc

Si python ne pouvait qu'exécuter ligne à ligne un code on ne pourrait pas faire grand chose. Le principe des programmes est de pouvoir grouper les instructions en bloc.

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

L'indentation permet **toujours** de s'y retrouver.

## Exécution conditionnelle et répétition de blocs

{% aller %}
[Blocs](blocs){.interne}
{% endaller %}

## Créer ses propres fonctions

Si un bloc de code est exécuté plusieurs fois à l'identique, on aimerait aussi pouvoir nommer ce groupe pour **pouvoir le réutiliser juste en appelant son nom**. C'est possible avec les fonctions.

{% aller %}
[Création de fonctions](creation-fonctions){.interne}
{% endaller %}

## Créer ses propres modules

{% aller %}
[Création de modules](creation-modules){.interne}
{% endaller %}

## <span id="interpréteur-blocs"></span>Blocs et interpréteur

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
