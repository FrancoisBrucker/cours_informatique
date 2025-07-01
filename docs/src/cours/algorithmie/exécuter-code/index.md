---
layout: layout/post.njk

title: Exécuter du Code

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---


> TBD comme mmix pour les sauts. Utiliser un registre.
> TBD introduire les registre bien plus tôt qu'actuellement.
> TBD dire que le pseudo code c'est des fonctions binaires finies et des boucles. sur des variables tableau binaire.
> du coup c'est des and/or/not et des boucles avec des données sous la forme de tableaux binaires.
> TBD ajouter mémoire car variables de taille quelconque ne fonctionne pas.


Le [pseudo-code](../écrire-algorithmes/pseudo-code/) permet d'écrire des programmes sur papier que l'on peut exécuter dans sa tête aidé d'un papier et d'un crayon. Les langages de programmation permettent d'exécuter du code sur un ordinateur un utilisant un [langage de programmation](https://fr.wikipedia.org/wiki/Langage_de_programmation).

Pour la plupart d'entre eux, il est facile de transcrire le pseudo-code en code pouvant être exécuté, on a alors l'implication suivante :

{% note "**Proposition**" %}
Tout ce qui peut s'écrire en pseudo-code peut s'exécuter sur un ordinateur.
{% endnote %}

Mais se pose alors 2 questions :

1. Comment ?
2. Est-ce que tout ce qui s'exécute sur un ordinateur peut s'écrire sous la forme d'un pseudo-code rendant les deux notions équivalentes ?

Pour répondre à ces deux questions, il nous faut commencer par montrer que le pseudo-code est équivalent à un autre langage, le pseudo-assembleur, comportant bien moins d'instructions et qui sera plus facile à implémenter physiquement.

## Exécuter du code

### <span id="pseudo-assembleur"></span>Pseudo-assembleur

{% aller %}
[Pseudo-assembleur](./pseudo-assembleur){.interne}
{% endaller %}

Le pseudo-assembleur a permit de montrer qu'il faut peu de choses pour pouvoir écrire et exécuter du code :

1. une mémoire finie pour stocker et gérer des données
2. une structure de contrôle et de flux permettant d'exécuter le code ligne à ligne

### Architecture de Von Neumann

L'architecture de Von Neumann montre que l'on peut rassembler ces deux entités en une seule :

{% aller %}
[Architecture de Von Neumann](./von-neumann){.interne}
{% endaller %}

### MMIX

Nous n'avons montré que le principe d'un pseudo-assembleur et de son utilisation dans un modèle de Von Neumann, juste assez pour nous convaincre que l'on peut exécuter du code.

Donald Knuth a formellement décrit un pseudo-assembleur complet dans le modèle de Von Neumann, nommée [MMIX](https://fr.wikipedia.org/wiki/MMIX). Il contient bien plus d'opérations que juste `NAND` et se rapproche en cela d'un véritable assembleur.

Je ne saurais trop vous conseiller d'aller jeter un coup d'œil au site qui explique son fonctionnement, comme toujours avec Knuth, de façon claire et précise :

{% lien %}
<https://mmix.cs.hm.edu/>
{% endlien %}

Une fois que vous serez à l'aise avec cette architecture, vous pourrez vous lancer dans le grand bain et faire vos propres programme en assembleur utilisant des processeurs réels, intel ou arm.

### Processeurs

Ce qui est fascinant, c'est que les choses fonctionnent quasiment à l'identique entre un pseudo-assembleur théorique et le code d'un assembleur pouvant exécuter des instructions sur un processeur ARM ou intel.

La principales différence, outre le fait qu'il y a plus d'opérations que juste `NAND` et plus de registres que 3, est que l'on ne peut pas accéder à tous les bits de la mémoire indépendamment :

1. chaque case mémoire est constitué de 8bits (on appelle ça un byte ou un octet). Ainsi, pour une architecture 64b, on peut adresser au maximum $2^{64}$byte, c'est à dire $8\cdot 2^{64}$bits.
2. on ne peux accéder qu'au adresses qui sont des multiples de S/8, c'est à dite au multiples de 8 pour une architecture de 64b (ce sont des [problèmes d'alignememt](https://fr.wikipedia.org/wiki/Alignement_en_m%C3%A9moire))

Il existe enfin deux grandes catégories de processeurs :

- [CISC](https://fr.wikipedia.org/wiki/Microprocesseur_%C3%A0_jeu_d'instructions_%C3%A9tendu) fabriqué, entre autres par intel, de la famille x64,
- [RISC](https://fr.wikipedia.org/wiki/Processeur_%C3%A0_jeu_d%27instructions_r%C3%A9duit) fabriqué, entre autres, par ARM.

Leurs fonctionnement interne est cependant le même et sont constitués de millions de [transistors](https://fr.wikipedia.org/wiki/Transistor). En effet ces composants électroniques permettent, sur un espace réduit, de faire les 3 choses essentielles pour permettant d'exécuter du pseudo-assembleur dans le modèle de Von Neumann :

- une porte logique `NAND`
- une mémoire
- pouvoir ligne des opcodes

{% lien %}
Trois vidéos de la même chaîne :

- [transistor et code](https://www.youtube.com/watch?v=HjneAhCy2N4)
- [transistor et mémoire](https://www.youtube.com/watch?v=rM9BjciBLmg)
- [transistor et processeur](https://www.youtube.com/watch?v=GYlNoAMBY6o)

Je ne saurais trop vous conseiller de lire le livre [Code](https://www.amazon.fr/Code-Language-Computer-Hardware-Software/dp/0137909101/) qui part du poteau télégraphique pour arriver au 8086 d'intel.
{% endlien %}

Attention, il y a le système en plus (qui est aussi un programme) qui gère plusieurs exécution des programmes. Cela rajoute une couche de complexité mais à chaque moment il n'y a qu'un seul programme qui tourne en même temps par processeur. C'est une autre histoire (renvoyer au cours système)

## Compilation

Un ordinateur peut exécuter du code, transcription du pseudo-assembleur, lui même équivalent à du pseudo-code. On n'écrit cependant pas de gros programme en assembleur, on utilise des langages plus proches du pseudo-code comme le python, le java ou encore le rust, le code écrit dans ces langages est ensuite transformé, on dit compilé, en assembleur lui même ensuite transformé au format binaire directement exécutable sur un processeur.

Cette transcription entre code et assembleur est possible car le pseudo-code est structuré, comme une langue mais sans les exception, par une [une grammaire formelle](https://fr.wikipedia.org/wiki/Grammaire_formelle). Une [analyse syntaxique](https://fr.wikipedia.org/wiki/Analyse_syntaxique) du code permet alors de traduire un pseudo-code d'un langage vers un autre, en particulier l'assembleur.

{% lien %}

- [Grammaire de python](https://docs.python.org/fr/3.11/reference/grammar.html)
- [Analyse syntaxique de python](https://docs.python.org/fr/3/reference/lexical_analysis.html)

{% endlien %}

Ce processus de compilation peut être fait en une fois sur tout le programme, c'est ce qui est fait en C ou en rust par exemple. Le processus de compilation produit un [fichier exécutable](https://fr.wikipedia.org/wiki/Fichier_ex%C3%A9cutable) qui peut ensuite être directement exécuté. L’intérêt de cette méthode est que l'on ne fait le processus de compilation, qui est lent, qu'une seule fois, le problème est que cela dépend du système d'exploitation (un fichier exécutable windows ne fonctionnera pas sur mac et réciproquement)

On peut aussi, c'est ce que font les [langages interprétés](https://fr.wikipedia.org/wiki/Interpr%C3%A8te_(informatique)) comme python par exemple, compiler ligne à ligne le code pour l'exécuter au moment de l'exécution. On a alors besoin que de l'interpréteur (qui lui est un programme compilé), qui se chargera de transcrire puis d'exécuter ligne à ligne le code écrit dans le langage (souvent ce n'est pas directement en assembleur qu'est transcrit le programme mais en [bytecode](https://fr.wikipedia.org/wiki/Bytecode), état intermédiaire entre pseudo-code et langage binaire). L’intérêt de cette méthode est que l'on peut donner directement le code écrit dans le langage sans avoir besoin de le compiler, le problème est que ces programmes sont souvent plus lent à exécuter puisqu'il faut compiler chaque ligne à chaque fois qu'on veut l'exécuter.

{% lien %}

- voir l'assembleur produit à partir d'un code : <https://godbolt.org/>
- [processus de compilation et d'exécution de python](https://www.fevrierdorian.com/carnet/pages/python-sous-le-capot-chapitre-1-fonctionnement-de-la-vm-cpython.html)

{% endlien %}
