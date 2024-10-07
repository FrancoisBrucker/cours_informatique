---
layout: layout/post.njk

title: Instructions

eleventyNavigation:
    order: 1

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Les instructions que peuvent exécuter un core vont dépendre de son modèle. Il existe deux grandes familles qui se distinguent par le choix des opérations qu'elles permettent :

- [architecture CISC](https://fr.wikipedia.org/wiki/Microprocesseur_%C3%A0_jeu_d%27instruction_%C3%A9tendu) (intel et AMD). Possèdent un grand nombre d'instructions, chaque instruction étant complexe. Ceci permet de dédier de la circuiterie à chaque instruction pour en accélérer son exécution.
- [architecture RISC](https://fr.wikipedia.org/wiki/Processeur_%C3%A0_jeu_d%27instructions_r%C3%A9duit) (ARM et Apple). Un petit nombre d'instructions simples. Le petit jeu d'instruction uniformisé en [pipeline](https://en.wikipedia.org/wiki/Classic_RISC_pipeline) permet théoriquement d'avoir une instruction par cycle. De plus la simplicité de chaque opération rend ces processeurs économe en énergie.

On s'accorde à dire que le RISC est plus rapide mais consomme plus que le RISC :

- le CISC est l'architecture reine des ordinateurs de bureaux
- le RISC est présent dans quasi tous les téléphones portables et tablettes

Les développement récents tendent à brouiller un peu ces différences, chaque architecture empruntant à l'autre ses points forts (le CISC scinde certaines de ses instructions pour gagner en consommation et le RISC propose quelques instructions complexes pur les optimiser).

De nombreuses personnes pensent que l'avenir est aux puces RISC et que leur utilisation dans les devices mobiles n'est que le début. Par exemple apple et ses nouvelles puces M pour toutes leurs machines, ou encore Angelina Jolie et sa phrase mythique :

> [*"RISC architecture is gonna change everything"*](https://www.youtube.com/watch?v=yVo9_h3-zwQ) (Angelina Jolie parlant de son portable dans [Hackers (1995)](https://en.wikipedia.org/wiki/Hackers_(film))).

{% aller %}
[RISK vs CISC](https://www.youtube.com/watch?v=a4kgtygCZBc) et [ARM vs x86](https://www.youtube.com/watch?v=AADZo73yrq4). Et une comparaison avec le petit dernier [RISC-V](https://www.youtube.com/watch?v=Ps0JFsyX2fU)
{% endaller %}

Pour la suite de ce cours, nous allons cependant uniquement nous occuper d'architecture [x86-64](https://en.wikipedia.org/wiki/X86-64), donc CISC car la majorité des pc en sont équipés.

{% lien %}
[Instructions x86_64](https://www.felixcloutier.com/x86/)
{% endlien %}

## Registres

Les [registres](https://fr.wikipedia.org/wiki/Registre_de_processeur) sont la mémoire dont dispose un core. Cette mémoire est très rapide, donc très chère : il n'y en a que peu.

Un registre est un espace mémoire de 64b ou le core stocke les paramètres et les résultats de ses instructions.

Par exemple l'instruction :

```
ADD RAX, 42
```

Va ajouter 42 à la valeur du registre `RAX` puis placer le résultat dans le registre `RAX`.

On peut aussi :

```
ADD RAX, RDX
```

Qui va ajouter la valeur du registre `RDX` à la valeur du registre `RAX` puis placer le résultat dans le registre `RAX`.

Ou encore :

```
ADD RAX, [RDX]
```

Qui va ajouter la valeur (64bits) à l'adresse du registre `RDX` à la valeur du registre `RAX` puis placer le résultat dans le registre `RAX`.

{% lien %}
Toutes les façons de faire ADD : [la commande ADD](https://www.felixcloutier.com/x86/add).
{% endlien %}

Il y a un petit nombre de [registres x86-64](https://en.wikibooks.org/wiki/X86_Assembly/X86_Architecture#x86_Architecture). Les registres 64b commencent par `R`.

### Registres généraux

Il en existe 14 de 64b. Ils sont utilisées dans une grande variété de cas.

#### Paramètres

- RAX (accumulateur)
- RBX (adresse donnée)
- RCX (compteur)
- RDX (données)

#### Déplacement de données

- RSI (adresse source)
- RDI (adresse destination)

#### génériques

de R8 à R15 (registres fourre-tout).

#### Décomposition des registres

Les registres généraux se divisent en bouts plus petits. Par exemple le registre RAX se décompose en :

- EAX (les 32 premiers bits)
- AX (les 16 premiers bits)
- AL (les 8 premiers bits) et AH (les 8 suivants)

### Instruction pointer

Il s'appelle RIP qui contient l'adresse de la **prochaine** instruction à exécuter.

### Gestion de la pile

Deux registres de gestion de la pile :

- RSP (adresse pile courante)
- RBP (adresse pile base)

### Registre d'états (flag)

Le registre [RFLAGS](https://en.wikipedia.org/wiki/FLAGS_register) est un registre d'états qui permet de rendre compte d'*états* arrivant en plus de l'instruction.

C'est une structure de donnée de type [bit field](https://en.wikipedia.org/wiki/Bit_field) : chaque état est codé par un bit du registre : si l'état est présent ce bit vaut 1, sinon il vaut 0.

Par exemple si le résultat de l'opération précédente vaut 0, le 6ème bit de ce registre vaut 1 (c'est le [zéro flag](https://en.wikipedia.org/wiki/Zero_flag)).

Ces états permettent de faire les instructions if/then/else en laguage machine en utilisant des [instructions de saut conditionnels](https://www.felixcloutier.com/x86/jcc).

### Autre registres

Il existe également des registres de segments :

- qui ne sont plus utilisés : SS, CS, DS et ES.  Ils restent présent pour des raisons de compatibilité mais valent tout le temps 0
- FS et GS qui sont utilisés uniquement par le système d'exploitation mais ne participent à aucune instruction

## opcode

Chaque instruction possède un code permettant de l'identifier de façon unique. On appelle ceci l'opcode. Il diffère non seulement pour chaque commande mais également pour chaque usage de la commande (chaque usage de la [commande ADD](https://www.felixcloutier.com/x86/add) aura un opcode différent).

Le passage d'une instruction assembleur à l'opcode n'est pas triviale :

{% lien %}

- [Construire l'opcode d'une instruction](https://wiki.osdev.org/X86-64_Instruction_Encoding)
- liste de [toutes les instructions x86-64](http://ref.x86asm.net/)

{% endlien %}

Heureusement, il existe des site pour nous aider :

{% faire %}
Utilisez [ce site](https://defuse.ca/online-x86-assembler.htm) ci-après pour connaître l'opcode de l'instruction `ADD RAX, 42` :

Attention au fait qu'il faut que vous soyez en x64, RAX n'étant pas défini en 32bits.
{% endfaire %}
{% faire %}
Que fait l'instruction : `MOV RAX, 0` ? Et celle ci : `XOR RAX, RAX` ?

Quel est l'instruction à privilégier ?
{% endfaire %}
{% details "solution" %}
Les deux instructions font la même chose, elles place 0 dans `RAX`. Mais la seconde à un opcode plus court que la première, c'est pourquoi vous verrez souvent la seconde instruction lorsque vous décompilez du code.
{% enddetails %}
