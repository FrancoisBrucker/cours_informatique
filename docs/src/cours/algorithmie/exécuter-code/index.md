---
layout: layout/post.njk

title: Exécuter du Code

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

[Un programme](../bases-théoriques/définition/#règles-générales) est un algorithme qui ne s'arrête pas forcément. On les décrit en algorithmie avec du [pseudo-code](../écrire-algorithmes/pseudo-code/) mais lorsque l'on veut exécuter ses programmes sur un ordinateur, on est obligé de transcrire le pseudo-code dans un langage de programmation (on utilisera le python dans ce cours) puis de l'exécuter sur un ordinateur.

Nous allons voir dans cette partie qu'écrire du code ou du pseudo-code est équivalent.

## Langage machine universel

> Abus de langage (lol). Le but est de trouver un langage permettant de faire tout ce que fait le pseudo code avec les règles les plus simple possibles
>
Nous allons pour cela commencer par donner une version alternative et équivalente au pseudo-code, nommé **_assembleur_**, qui nous permettra de faire un pont entre pseudo-code et code.

L'assembleur est une sorte de pseudo-code nécessitant moins de syntaxe que [le pseudo-code classique](../écrire-algorithmes/pseudo-code/), mais tout aussi expressif comme nous allons le voir.

Le pseudo-code est en effet constitué de nombre de facilités dont on peut se passer.

### Objets

{% note "**Définition**" %}
Les objets manipulés par le langage machine universel sont des suites finies de "0" et de "1".
{% endnote %}

Un objet `o`{.language-} utilisé par le langage machine est une suite de "0" et de "1". On doit pouvoir affecter une variable :

```python
o = 1011001
```

On doit pouvoir accéder à un de ses bit comme un tableau, qu'on lit de **droite à gauche** :

```python
    76543210
o = 11010100

o[0] = 0
o[1] = 0
o[2] = 1
o[3] = 0
o[4] = 1
o[5] = 0
o[6] = 1
o[7] = 1
```

Et connaître sa taille `l(o) = 8`{.language-}
Enfin, on doit pouvoir interpréter un objet comme un entier :

- positif (on dit **_unsigned_**) en utilisant la représentation binaire de l'objet : `u(o) = 212`
- relatif (on dit **_signed_**) en utilisant [le complément à deux](https://fr.wikipedia.org/wiki/Compl%C3%A9ment_%C3%A0_deux) : `s(o) = -44`

Remarquez que le complément à deux dépend de la taille de la suite, ce qui semble contre intuitif mais sera justifié par la suite.
Il existe une autre possibilité, moins utilisée car moins pratique algorithmiquement, qui est de dédier un bit au signe usuellement celui le plus à gauche.

{% note "**Définition**" %}
Le bit le plus à gauche, donc celui d'indice le plus élevé, est appelé **_bit de poids fort_**.
{% endnote %}

On a vu que [tout objet d'un algorithme](../bases-théoriques/définition/#paramètres-binaires) pouvait être représenté par une suite finie de "0" et de "1" donc :

{% note "**Proposition**" %}
Un programme et le langage machine universel utilisent les mêmes objets.
{% endnote %}

### Opérations

Le pseudo-code doit permettre de faire les opérations arithmétiques courantes sur les objets :

- plus, moins, fois et divisé pour les entiers relatifs et les approximations des réels
- plus, moins, fois et divisé pour les approximations de réels
- concaténation des chaines de caractères

L'intérêt d'utiliser des suites binaires est que toutes les opérations arithmétiques peuvent se réaliser avec les deux opérations logiques suivantes :

- `copie(x)`
- `SHIFT(x, y)` rend un objet contenant la concaténation de y0...0 ajout de s(x) 0 à droite de y si s(x) > 0 et de -s(x) 0 à gauche si s(x) < 0
- `NAND(x, y)` : opérateur logique NON ET.

En effet, il est possible d'[obtenir toutes les opérations logiques avec NAND](https://en.wikipedia.org/wiki/NAND_logic) et l'opération SHIFT permet d'ajouter des bits à gauche ou à droite d'un objet (si on veut ajouter des 1 on peut fait NOT(SHIFT(x, NOT(y))))

Ou 1 ou 2 paramètre et une sortie.

### Structures de contrôles

> Saut conditionnel

### Fonctions

> Dans la mémoire directement. Variable = adresse du début de l'objet.
> mémoire infinie
> 

> 

### Lier Variables et objets

Comme on a que la mémoire qui est une suite de 0 et de 1 pour stocker les objets et les variables//
> TBD exemple de 2 objets un qui fait hello et l'autre qui fait -3.
> 
Pour chaque objet il faut pouvoir connaitre la taille
> savoir distinguer un nombre d'un objet : connaitre sa taille. l'endrait dans la mémoire
> 
> connaitre la taille d'un objet

### Opérations

#### Bit à bit

#### Arithmétiques

dérivées des

#### Registres

> ce qui amène a avoir que NOT et ADD comme opération. Le montrer 
> arithmétique et bit à bit
> saut
> paramètre des opérations dans des "Registres" il y en a peu.


## Architecture de Von Neumann

> code = nombres en mémoire. Exemple MMIX de knuth (langage théorique)
> associe un registre spéciale pour l'adresse du code. On le place utiusllement avant les variables.

tas (mémoire)
pile : variables (adresses vers)
constantes
code

Code et variables dans la même mémoire

> Théoriquement infinie, même si en pratique comme Tout algorithme n'a besoin que d'un nombre fini d'opérations Si on a autant de cases mémoire que nombre d'opérations c'est comme si la mémoire était infinie.
>
> 
> On donne une taille de 8b par usage. Et les entiers sont sur 64b par défaut (mais peuvent avoir d'autres taille 8b à 128b et souvent 32b pour les entiers courants)

> Donc attention, la taille des objets manipulés est (presque) toujours plus grande que la taille d'une case mémoire qui est, poids de l'histoire, fixée à 8b.

> Pour nos ordis :
> - des cases de 8bits et 
> - adresse sur 64b et donc 2^64 cases mémoires.
> - cela fait XXX terabyte
> - pour 8GHz cela fait 2^64 opérations et un programme qui peut durer XXX siècles


## Implémentation

> plus que NAND pour gagner du temps. Optimisation RISC ou CISC
> 
> dire que juste un programe là. Il y plus d'un preogramme en vrai : cf cours ssteme
> Processeur x64 et RISK
> MMIX
> Taille des registre = 64b
>  mémoire finie et découpée en cases. 8b par défaut
> - Pour ne pas avoir à retenir les positions des variables en mémoire qui peuvent changer d'une
> exécutionà lautre, on procède à une indirection avec la pile : on connait la position dans la pile et dans la pile est contenue l'adresse de la variable
> 
> Pile et variables locales par durée de vie. Faire exemple
> - appel de fonctions call et ret
> - appel au système
> - taille finie
> objet taille fixe, et pas infini pour être traité directement dans un registre.
> Si on a des entiers plus gros il faut combiner en une structure plus compliquée
> Variables temporaire dans la pile.
> On peu empiler et dépiler

> peut être vu comme un pseudo-code "minimal"

> TBD le plus minimal c'est la machine de turing, mais d'un point de vue opérationel il est minimal car c'est ce qui est appelé assembleur.
> faire les call avec des jump
> à la fin dire qu'il y a souvent plusieurs autres méthodes dans les langages machines pour aider (donner exemple, sub, mul, gestion approximation de réel, call/ret et surtout la pile qu'on verra bien plus tard.), mais on peut tout faire avec ce qu'on a la.
> 
> Passer d'un pseudo code à un langage machine simple et montrer sn équivalence. Ceci permettra de montrer plus facilement que des langages sont équivalents.
> Langage simplifié où les variables n'existent pas et le boucles sont remplacés par des saut. Tout langage informatique peut être transcrit en langage machine
> instructions finie et 1 ou deux paramètres et une sortie dans des variables fixées et de taille fixé disons 64bits appelées registres.
> variables = un grand tableaux de cases de taille fixée. Disons 64bits

Y arriver à partir du pseudo-code : fait de façon formelle par Knuth et son langage universel MMIX.

> TBD Faire exemple avec Fibonacci ?

Variables :

> 1. uniquement entiers relatifs
> 2. uniquement entiers binaires
> 3. uniquement addition et -x comme opération.
> 4. uniquement entiers binaires 64bits (sinon tableaux). Positifs et négatifs. Addition avec flag si ça dépasse. faire exemple d'une addition sur plusieurs mots
> 5. uniquement entiers binaires positifs (non signé).  Négatif = complément à deux. Et on remplace le -x par NOT

> TBD tout algorithme va s'arrêter et donc peut rentrer dans une machine physique avec une mémoire assez grande. Si N opérations -> n accès à une variable utilisé -> N cases mémoires  -> on découpe l'espace en log2(n) pour qu'une case mémoire soit suffisant pour stocker l'adresse de la case mémoire.
> Actuellement 64bits -> taille mémoire de X terra. -> si 4GHz alors temps execution XX sec On y est pas encore...

Structures :

> 6. pas de boucles, que des labels
> 7. pas de variables. Que la mémoire
> 8. opérations via des registres pour les paramètres et les résultats des opérations (transfert mémoire registre), plus quelques registres généraux/sp´´cifique

Programme :

> 8. pas de code que des nombres. Avec un numéro de fin.
> 9. Programme = entier : code puis variables (voir <https://en.wikipedia.org/wiki/CMD_file_(CP/M)> plus compliqué aujourd'hui mais même principe)

> TBD ne pas parler de pile. Juste de la structure.

<https://fr.wikibooks.org/wiki/Programmation_Assembleur/x86>

<https://fr.wikipedia.org/wiki/MMIX> <https://mmix.cs.hm.edu/>

<https://www.technologuepro.com/microprocesseur/jeu-instructions-8086-8088.htm>

<https://www.youtube.com/watch?v=665rzOSSxWA>



Transcrit en code.
et les opérations fait en circuit.

Attention, il y a le système en plus (qui est aussi un programme) qui gère plusieurs exécution des programmes. Cela rajoute une couche de complexité mais à chaque moment il n'y a qu'un seul programme qui tourne en même temps par processeur. 
> TBD donner exemple de l'organisation de la mémoire pour un programme et dire ce qu'il se passe pour deux programme : échange de mémoire. Puis emmener vers la partie système si besoin de précision.

### Circuits

## Langages et pseudo-code

On va montrer que les langages informatiques (ou en tout cas une grande partie) sont équivalents au pseudo-code. Pour cela on va procéder en deux temps :

1. on va commencer par montrer que l'on peut simuler un pseudo-code avec un langage : un langage informatique sera plus puissant que le pseudo-code
2. on montrera que l'on peut simuler un langage avec le pseudo-code ce qui montrera que le pseudo-code est plus puissant que tout langage informatique.

Pour certains langages informatiques, comme le python ou le java par exemple, il est clair que l'on peut facilement écrire tout pseudo-code sous la forme d'un programme 

### Langage ≥ pseudo-code

> il faut montrer que l'on peut faire tout ce que fait un pseudo-code.
> 
> TBD souvent clair. comme le python, parfois moins clair et là il faudra voir un modèle équivalent au pseudo-code. Exemple de l'assembleur : que somme et test et pas de boucle mais des labels. En plus taille fixe, aussi possible.



### Langage ≤ pseudo-code

compilation vers langage machine.

Un langage informatique est décrit en utilisant [une grammaire formelle](https://fr.wikipedia.org/wiki/Grammaire_formelle) qui permet d'écrire des lignes de code.

{% lien %}
[Grammaire de python](https://docs.python.org/fr/3.11/reference/grammar.html)
{% endlien %}

Chaque ligne de la grammaire peut être transformé en pseudo-code _via_ un [analyseur syntaxique](https://fr.wikipedia.org/wiki/Analyse_syntaxique).

{% lien %}
[Analyse syntaxique de python](https://docs.python.org/fr/3/reference/lexical_analysis.html)
{% endlien %}

Comme l'analyse syntaxique peut-être décrite par un algorithme en pseudo-code, on en déduit que tout langage décrit par une grammaire formelle peut-être exécuté par un algorithme écrit en pseudo-code et donc :

{% note "**Proposition**" %}
Tout langage informatique
{% endnote %}
> TBD plan
> pseudo-code <=> langage (via compilateur : chaque langage est décrit par une grammaire <https://docs.python.org/fr/3.11/reference/grammar.html>
> <https://fr.wikipedia.org/wiki/Analyse_syntaxique> facile à fire. C'est pourquoi créer des programme est facile. Mais il ne font pas tous quelque chose et même parfois plantent (s'il font des division par 0 par exemple)
> TBD faire un exemple
> Si on peut écrire un interpréteur en pseudo-code, le langage est contenu dans ce qu'on peut faire en pseudo-code) <=> asm (pas de boucles) <=> taille fixe <=> von neumann
> 
> #### Langages informatiques

> TBD : le plus clair car le pseudo code s'écrit presque directement, par exemple en python
> TBD pas exécuté directement. Traduit en un autre langage compréhensible par ce qui va l'exécuter.
> TBD : compilé en langage machine (montrer des exemples). Souvent actuellement en byte code (module dis en python pour le voir <https://docs.python.org/fr/3/library/dis.html> ou <https://www.fevrierdorian.com/carnet/pages/python-sous-le-capot-chapitre-1-fonctionnement-de-la-vm-cpython.html>) qui est lui-même exécuté par une machine virtuelle.

> TBD :
> 1. interprété (python, js)
> 2. compilé :
>   1. pour la machine : C
>   2. bytecode : java, wasm
> 3. [ésotérique](https://fr.wikipedia.org/wiki/Langage_de_programmation_exotique) : brainfuck

## Exécution automatique de programme

### Modèle de Von Neumann

> TBD : le langage des processeurs
> assembleur = transcription. Mais c'est déjà une interprétation
> nom => nombre, saut
> mais aussi le système va ajouter des chose pour être exécuté (elf)
> une mémoire pour le code puis les variables : faire le dessin
> 
### Circuits logique

> TBD : <https://www.youtube.com/@CoreDumpped/videos>. <https://www.amazon.fr/Code-Language-Computer-Hardware-Software/dp/0137909101/ref=sr_1_1>
> TBD un processeur est codé en porte logiques,
>
> TBD tout est basé sur les opérations booléennes, logiques car algorithme = fonction booléenne.

> <https://people.csail.mit.edu/rrw/week1.pdf>
> <https://cs.brown.edu/people/jsavage/book/pdfs/ModelsOfComputation_Chapter9.pdf>
> sert pour la dé-randomisation : <https://www.youtube.com/watch?v=mZck0N_T9Cs>
> 
> Gros : <https://en.wikipedia.org/wiki/Circuit_complexity#History>
> TBD circuit logiques ?
>
### Compilation

> TBD :
> - chaque instruction est transformée à la volée en instruction : interprété comme python
> - compiler pour la machine en assembleur : C ou le Rust
> - compiler en autre chose : java