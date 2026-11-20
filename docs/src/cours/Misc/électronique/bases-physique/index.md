---
layout: layout/post.njk

title: Bases physiques et de l'électronique

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Pour pouvoir 

## Relais

{% note %}
[Le steampunk](https://www.youtube.com/watch?v=WOfmZLnXY8w) de l'informatique
{% endnote %}

Le O et le 1 dont on va avoir besoin va être du courant.


Base d'un relais est un électro-aimant :

![relais 1](relais-1.1.png) 

On lui adjoint une diode (voir plus bas pour ce que c'est) pour dissiper la charge lorsque l'on coupe l'alimentation (le circuit se ferme alors sur la diode et permet de limiter la tension à la tension de la diode (typiquement .7V) et de dissiper l'énergie emmagasinée dans la bobine) :

![relais 1](relais-1.2.png)

Enfin le mécanisme de relais en lui-même :

![relais 2](relais-2.png)

- sans courant en A une barre de métal fait une connexion entre com et repos,
- si on alimente A, l'électro-aimant fait baisser la barre et elle connecte maintenant com à travail.

Ingénieux, non ! C'est Shannon qui a le premier montré la faisabilité  de créer un réseau booléen en utilisant des relais.

{% lien %}
[A Symbolic Analysis of Relay and Switching Circuits (Shannon, 1938)](https://en.wikipedia.org/wiki/A_Symbolic_Analysis_of_Relay_and_Switching_Circuits){.externe}
{% endlien %}

Par exemple une porte NON (_NOT_) :

- générateur de courant en com
- entrée : A
- sortie : repos

Ou une porte NON-ET (_NAND_) :

- entrées : com et A
- sortie : travail

## Transistor à jonctions

{% note %}
[Le Giscardpunk](https://www.youtube.com/watch?v=KKhnDzRgsW8) de l'informatique
{% endnote %}

électronique analogique.

N'étant pas électronicien et encore moins physicien, je vais rester à la surface de l'explication. Je suppose juste que vous savez ce qu'est une charge et une tension.

### Semi-conducteurs : Diode PN

{% lien %}
[La jonction PN expliquée avec des chiens de traîneaux](https://www.youtube.com/watch?v=QHGcE1_NjBw&list=PLKV-I2qagq68bc0Aq9Ivy0Dh-A-ma08Oz&index=1){.externe}
{% endlien %}

La base de la jonction PN est un cristal de silicium dopé (avec ajout de) au Bore, Aluminium ou Gallium pour la couche P et au Phosphore, Arsenic ou Antimoine pour la couche N. 

![atomes](./si-PN.png)

Comme vous le voyez, les atomes de Silicium ont 4 électrons sur leur couche de valence, les atomes de type P en ont 3 et ceux de type n, 5. Un cristal est formé d'atomes qui si partagent les électrons sur la couche de valence :

![cristal](./cristal.png)

Un couche de Valence aime avoir [8 électrons](https://fr.wikipedia.org/wiki/R%C3%A8gle_de_l%27octet). Si elle en a moins elle va avoir tendance à vouloir en attraper un autre, si elle en a trop elle aura envie de les donner. Pour nos cristaux :

- un atome de silicium sera stable,
- un atome de type P aura un électron en moins.
- un atome de type N aura un électron en trop,


De façon globale la charge d'un cristal est de 0. 

Lorsque l'on colle un cristal dopé en P avec un cristal dopé en N on obtient une diode :

![cristal](./diode-NP.png)

À la jonction entre le cristal P et le cristal N les électrons surnuméraires de la couche N se déplacent vers les places libres des cristaux de la couche P. Au total la charge du cristal est toujours nulle, mais dans la région du milieu ces déplacements d'électrons ont généré une différence de potentielle (une charge + lorsqu'un électron est parti et une charge - lorsqu'un électron est arrivé)qu'on appelle tension de seuil (typiquement 0.7V pour une diode au silicium). Ceci ne peut pas prendre tout le cristal car à la jonction le potentiel négatif de la région P empêche les électron de passer naturellement.

On peut en revanche agrandir ou diminuer ce potentiel via un générateur de tension qui va "pousser" ou tirer les électrons d'un côté ou de l'autre en passant de trou en trou, chaque trou laissé libre étant remplacé par un autre électron :

![tension diode](./diode-tension.png)

Si la tension est négative la barrière augmente jusqu'à prendre toute la place. Dans le cas contraire, une tension positive, la barrière diminue jusqu'à disparaître lorsque la tension appliquée est la tension de seuil. À ce moment là la diode devient passante : un courant passe à travers le circuit. 

![diode passante](./diode-passante.png)

Les électrons passent de la cathode à l'anode fournissant un courant positif de l'anode à la cathode. Notez que si la diode est passante, son intensité peut être aussi grande que l'on veut mais sa tension ne peut être supérieure à la tension de seuil.

On utilise une diode pour bloquer la circulation du courant dans un sens (comme pour le relais). 

### Transistors NPN

{% lien %}
[Le transistor bipolaire](https://www.youtube.com/watch?v=Zjw7Prg5244&list=PLKV-I2qagq68bc0Aq9Ivy0Dh-A-ma08Oz&index=2){.externe}
{% endlien %}

Un transistor à jonction utilise le principe de la diode en ajoutant une couche supplémentaire. Il existe ainsi deux type de transistors à jonctions les PNP et les NPN. Nous allons montrer le principe pour les NPN utilisé en électronique, mais le principe est le même pour les PNP. Sa construction reprend celle de la diode, c'est un collage d'un cristal P entre deux cristaux N :

![transistor NPN](./transistor-NPN.png)


Un transistor à jonction est un amplificateur de courant.

C'est le transistor utilisé pour les circuits. Les bascules se font en tension (+5V) mais doivent être converties en courant (via des résistances pull-up ou pull-down) puisque la commande d'un transistor à jonction est le courant de base.


> TBD schéma en utilisant 


> TBD résistance et courant

## Transistor à effet de champ

{% note %}
[Le cyberpunk](https://www.youtube.com/watch?v=aIYp4ArokzE) de l'informatique
{% endnote %}

numérique MOSFET : NMOS et PMOS 

{% lien %}
[Le transistor MOSFET](https://www.youtube.com/watch?v=Zjw7Prg5244&list=PLKV-I2qagq68bc0Aq9Ivy0Dh-A-ma08Oz&index=3){.externe}
{% endlien %}

> TBD le mosfet utilisé comme ohm pour générer des tensions
> TBD ohmique si dans un circuit, saturation que dans les effets transitoirs
> TBD que des tensions. Sans courant en régime stable

1. <https://www.youtube.com/watch?v=docgmTprR5o>
2. <https://www.youtube.com/watch?v=wGrkczNxEh0&list=PLQms29D1RqeKb21acQ481DRiDH28sE0vN&index=1>
3. <https://www.youtube.com/watch?v=1rZyGL1K5QI>
4. <https://www.youtube.com/watch?v=HjneAhCy2N4>


en français : <https://www.youtube.com/watch?v=31hyLr07obo>
en anglais :
- defs : <https://www.youtube.com/watch?v=HxfoFFK_zBc&list=PLXb3r5ny8_1X7Ph5vivwAmILwI42OVv94&index=1>
- MOSFET : defs <https://www.youtube.com/watch?v=iF-fd_jDjEw&list=PLXb3r5ny8_1X7Ph5vivwAmILwI42OVv94&index=25>

