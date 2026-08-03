---
layout: layout/post.njk

title: Ordinateur, programmes et OS

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

<!-- TBD 

intro : ordi / os et programmes. 

-->

## Ordinateur

Le but d'un [ordinateur](https://fr.wikipedia.org/wiki/Ordinateur) est de permettre à des utilisateurs d'exécuter des applications :

{% note2 "**Définition**" %}
Un **_ordinateur_** est composé de multiples composants physiques qui interagissent entre eux via [une carte mère](https://fr.wikipedia.org/wiki/Carte_m%C3%A8re) :

- le [**_processeur_**](https://fr.wikipedia.org/wiki/Processeur) qui exécute des instructions sur des variables appelés **_registre_** pouvant contenir 64[bit](https://fr.wikipedia.org/wiki/Bit) d'information (il existe des registres génériques que l'on peut utiliser de façon interchangeable pour de nombreuses instructions et des registres spécialisés dans une tâche bien précise).
- de la mémoire que l'on sépare en 2 grande catégories :
  - [**_la mémoire vive_**](https://fr.wikipedia.org/wiki/M%C3%A9moire_vive) : un espace de stockage rapide, mais volatile (se vide lorsque l'on éteint l'ordinateur). Peut-être vu comme un grand tableau $M$ ou chaque case contient 1[Byte](https://fr.wikipedia.org/wiki/Byte) (un Byte est un entier entre 0 et 255 et est stocké sur 8 bits). Le processeur peut lire 8 Bytes consécutifs de la mémoire et les placer dans un de ses registres ou écrire un de ses registre dans 8 cases consécutives de la mémoire (en fait, ceci n'est possible que pour les adresses multiples de 8 : $M[8\cdot i:8\cdot (i +1)]$ pour tout $i$ pour des raisons d'efficacité). Comme on peut accéder à tout élément de la mémoire sans contrainte, cette mémoire est appelée _RAM_ (pour Random Access Memory)
  - [**_la mémoire de masse_** ou de stockage](https://fr.wikipedia.org/wiki/M%C3%A9moire_de_masse), non volatile. On ne peut pas toujours accéder à tout byte du tableau de stockage indépendamment, il faut utiliser un protocole. Ces devices sont plus lent que la RAM mais sont non volatiles. Par exemple :
    - disques durs : plus lent que la mémoire mais non volatile
    - USB : encore plus lent qu'un disque dur mais déplaçable facilement
- [des **_périphériques_**](https://fr.wikipedia.org/wiki/P%C3%A9riph%C3%A9rique_informatique), appelés **_device_**, qui composent tout les autres composants :
  - [carte réseau](https://fr.wikipedia.org/wiki/Carte_r%C3%A9seau) : encore plus lent que l'USB mais accessible de partout
  - [interfaces](https://fr.wikipedia.org/wiki/Interactions_homme-machine) :
    - dont on peut uniquement lire des données (périphériques d'entrée) : clavier/souris
    - dont on peut uniquement envoyer des données (périphériques de sortie) : écran/imprimante
    - entrée/sortie : volant avec retour de force

{% endnote2 %}
{% info %}
[Unités et ordres de grandeur en informatique](/cours/misc/unités-ordres-grandeur){.interne}
{% endinfo %}

Le schéma (très) simplifié suivant décrit un ordinateur :

![un ordinateur](./schema-ordinateur.png)

Ce schéma s'applique à une vaste gamme d'ordinateur : ordinateur fixe ou portable, mobile, tablette, _etc_. Ce qui va différentier ce que l'on peut faire avec est certes lié aux périphériques installées et aux capacités du processeur, mais aussi et surtout du système d'exploitation utilisé pour exécuter des applications.

## Programmes

Un programme est une suite d'instructions exécutée l'une après l'autre par le processeur. Ce processus (dont nous verrons (bien) plus tard le fonctionnement détaillé nommé [_fetch-decode-execute_](https://en.wikipedia.org/wiki/Instruction_cycle#Summary_of_stages)) est contraint par le schéma de l'ordinateur :

1. le seul endroit où peut être stocké un programme est en mémoire : chaque instruction du processeur doit être associé à un nombre binaire. 
2. le processeur doit connaître la prochaine instruction qu'il doit exécuter : un de ses registres spécialisé nommé **_pointeur d'instruction_** (d’abréviation _IP_) contiendra toujours l'adresse en mémoire de la **prochaine** instruction à exécuter.

{% note2 "**Définition**" %}
Exécuter un programme sur un ordinateur de fait en suivant les étapes suivantes :

1. initialisation :
   1. charger en mémoire la suite d'instructions à effectuer
   2. placer dans le registre  `IP` du processeur l'adresse en mémoire de la première instruction à executer
2. boucle d'exécution du programme :
   1. étape **_fetch_** : 
      1. lire à l'adresse mémoire de `IP` la prochaine instruction à exécuter (pour les processeurs intel x86, cette instruction peut prendre entre 1 et 15 byte en mémoire), qui devient l'instruction courante
      2. incrémente `IP` de la taille de l'instruction courante (la valeur de `IP` est l'adresse par défaut de l'instruction suivant l'instruction courante)
   2. étape **_decode_** : prépare l'instruction courante à être exécuté en chargeant ses paramètres dans des registres si nécessaire
   3. étape **_execute_** : le processeur exécute l'instruction courante
3. si l'instruction courante n'était pas l'instruction de fin de programme, on retourne à l'étape 2. pour effectuer une nouvelle boucle d'exécution du programme

{% endnote2 %}

La définition ci-dessus amène quelques commentaires. 

Tout d'abord **les registres du processeur  sont les seuls moyens de communication du processeurs** et servent à beaucoup de choses :

Comme `IP` doit contenir l'adresse en mémoire de la prochaine instruction à exécuter, sa taille limite la taille maximale de la mémoire qu'un ordinateur peut utiliser.

{% exercice %}
Pour une taille de registre de 64b, quelle est la taille mémoire maximale en terabyte ($10^{12}$ byte)
{% endexercice %}
{% details "corrigé" %}
Une case mémoire contient 1B et un nombre de 64b peut être associé en notation binaire à $2^64$ entiers différents. La taille mémoire maximales est donc $2^{64}$Byte, ce qui correspond à $10^{64/\log_2(10)} \simeq 10^{19}$ Byte, donc plus de $10^7$ terabyte. 

Il y a de la marge pour nos ordinateurs actuels...
{% enddetails %}

De plus, un programme doit être stocké en mémoire de l'ordinateur pour être exécuté : à chaque instruction est associée une suite finie de 0 et de 1 stockée en mémoire. Par exemple considérons l'instruction 
valide pour un processeur x86 intel consistant à placer la constante 42 dans les 64bits du registre générique `RAX`. Elle s'écrit en [assembleur](https://fr.wikipedia.org/wiki/Assembleur) (le language des processeurs) ainsi  :

```
MOV RAX, 42
```

Et est codée en [langage machine](https://fr.wikipedia.org/wiki/Langage_machine) (l'encodage dans la mémoire) sur 10 bytes (on a utilisé ici la notation décimale, un byte correspondant aux entier allant de 0 255) : $72\\;\\;184\\;\\;42\\;\\;0\\;\\;0\\;\\;0\\;\\;0\\;\\;0\\;\\;0\\;\\;0$ de valeurs binaires : 

```
01001000  10111000  101010  00000000  00000000  00000000  00000000  00000000  00000000  00000000
```

- $72\\;\\;184$ correspond au numéro de l'instruction : _"place un entier sur 64b dans le registre `RAX`"_ 
- $42\\;\\;0\\;\\;0\\;\\;0\\;\\;0\\;\\;0\\;\\;0\\;\\;0$ correspond à l'entier $0\\;\\;0\\;\\;0\\;\\;0\\;\\;0\\;\\;0\\;\\;0\\;\\;42 = 42$ en notation [petit-boutisme](https://fr.wikipedia.org/wiki/Boutisme#Petit-boutisme) (on écrit les bytes d'un nombre de droite à gauche dans les processeurs intel)

Si on reprend le cycle d'exécution de cette instruction :

1. fetch : 
   1. le registre `IP` est placé au début de l'instruction. Son code est $72\\;\\;184\\;\\;42\\;\\;0\\;\\;0\\;\\;0\\;\\;0\\;\\;0\\;\\;0\\;\\;0$ qui correspond à l'instruction _"place 42 dans le registre `RAX`_ qui devient l'instruction courante
   2. le registre `IP` est incrémenté de 10
2. decode : l'entier 42 est placé dans un registre tampon du processeur utilisé pour stocker les paramètres
3. exécution : la valeur du registre tampon est placé dans le registre `RAX`

{% exercice %}
Effectuez le cycle d'exécution pour l'instruction `ADD RBX, RAX` de code $72\\;\\;137\\;\\;195$ qui ajoute le contenu de `RAX` au registre `RBX`
{% endexercice %}
{% details "corrigé" %}

1. fetch : 
   1. le registre `IP` est placé au début de l'instruction. Son code est $72\\;\\;137\\;\\;195$ qui correspond à l'instruction _"ajoute `RAX` à `RBX`_ qui devient l'instruction courante
   2. le registre `IP` est incrémenté de $3$
2. decode : rien à faire
3. exécution : la valeur du registre `RAX` est ajoutée au registre `RBX`

{% enddetails %}


L'assembleur est très proche du langage machine. Il y a une transcription directe entre une instruction en langage assembleur et son code en langage machine. Par exemple notre instruction `ADD RBX, RAX` qui correspond au code machine $72\\;\\;137\\;\\;195$ se transcrit ainsi :

- $72$ est appelé _opcode_ est détermine la taille des registres que l'on va utiliser. Ici des registres de taille 64 bit (`RAX` signifie en effet les 64 bits du registre `A`. Dans certains cas, on pourra utiliser qu'une partie de celui-ci : les 32 premiers bit en écrivant `EAX`, les 16 premiers en utilisant `AX`, ou encore les 8 premiers en utilisant `AL`.)
- $137$ est l'instruction proprement dite et correspond au fait d'ajouter la valeur d'un registre dans un autre
- $195$ qui vaut $11000011$ en binaire se décompose en :
  - $11$ qui correspond au fait que l'on veut manipuler 2 registres
  - $000$ qui correspond au registre `A` (ici `RAX`)
  - $011$ qui correspond au registre `B` (ici `RBX`)

{% exercice %}
Comment ajouter 42 au registre `RAX` en assembleur ?
{% endexercice %}
{% details "corrigé" %}

On peut exécuter le programme :

```
MOV RBX, 3
ADD RAX, RBX
```

{% enddetails %}


Enfin, toutes ces instructions dépendant du processeur utilisé par l'ordinateur ! Nous avons utilisé ici des jeux d'instructions pour des processeurs de type x64 (les PC). Ces instructions seraient tout à fait différente pour un programme s'exécutant sur un mac par exemple.

{% attention2 "**À retenir**" %}
Un programme dépend du processeur utilisé car les instructions de chaque type de processeur (PC, MAC, mobile) va être différente.
{% endattention2 %}

Mais c'est encore pire que ça. Lorsqu'un processeur veut accéder à un device comme le disque dur il faudra qu'il parle son langage et ce langage va être différent selon le type de device (on ne parle pas à un écran comme on parle à une clé USB) et même selon la marque du device (deux écrans de marque différentes vont avoir des langages différents) : si l'on change de clavier il faut possiblement changer son programme !

{% attention2 "**À retenir**" %}
Un programme dépend non seulement du processeur utilisé mais également des différents devices de l'ordinateur sur lequel il est exécuté.
{% endattention2 %}

Ce n'est pas raisonnable d'avoir à modifier son programme si l'on change une partie de son ordinateur, c'est pourquoi on n'exécute jamais un programme directement sur un ordinateur, on passe via un système d'exploitation dont le but est de gérer les différences entre matériels.

## Système d'exploitation

> TBD ici
> 
<!-- tbd

ICI théorème fondamentale de l’ingénierie logicielle

parler de système d'exploitation : exploite/utilise l'ordinateur.
parler de language machine : spécifique au processeur
parler d'application : programme exécutable spécifique au système d'exploitation

-->

Pour que chaque application n'ait pas à tout gérer (accès au processeur, à la mémoire, au disque dur, au réseau, ...) comme on le ferait avec un circuit imprimé par exemple, on utilise un [système d'exploitation](https://fr.wikipedia.org/wiki/Syst%C3%A8me_d%27exploitation) (ou **_OS_** pour _operating system_) comme intermédiaire. L'architecture d'un ordinateur et les systèmes d'exploitations ont co-évolué. Les besoins des uns modifiant l'architecture des autres et réciproquement. Nous allons présenter ici les principes d'un OS de bureau (W11, Linux Ubuntu, MacOS) actuel.


> TBD ici 
> 
> TBD déplacer les utilisateur/root etc dans la partie II.2 (II.1 = dossiers et fichiers, II.2 = utilisateurs et droits)
> 
On suppose ici que vous savez minimalement interagir avec votre système d'exploitation en exécutant des applications via un menu ou l'explorateur de fichiers.

- programme = numéro de l'instruction instruction processeur
- au démarrage on charge un endroit du disque dur en mémoire et on exécute ces instructions (codées sur 8 bytes, 64 bits) une à une
- l'instruction sur un endroit du disque dur : montrer liste x86
-


> Parler d'indirection entre Ordi - os - programme. Ne pas parler de noyau ni d'horloge
> TBD tout se suite parler de la carte mère qui réveille le noyau. Dire qu'un OS c'est un noyau, des drivers et des format application pour les programmes (co un driver d'exécutable). Noyau est processeur dépendant.

Le but d'un [ordinateur](https://fr.wikipedia.org/wiki/Ordinateur) est de permettre à des utilisateurs d'exécuter des applications. Pour que chaque application n'ait pas à tout gérer (accès au processeur, à la mémoire, au disque dur, au réseau, ...) comme on le ferait avec un circuit imprimé par exemple, on utilise un [système d'exploitation](https://fr.wikipedia.org/wiki/Syst%C3%A8me_d%27exploitation) (ou **_OS_** pour _operating system_) comme intermédiaire :

> TBD supprimer utilisateur et parler directement ici du théorème fondamental de l'ingénierie
> TBD remplacer logiciels par applications
> 
![os](./os.png)

### Matériel et logiciel

Le but premier d'un système d'exploitation est ainsi de faire le lien entre le [matériel](https://fr.wikipedia.org/wiki/Mat%C3%A9riel_informatique) (_hardware_) et le [logiciel](https://fr.wikipedia.org/wiki/Logiciel) (_software_).

#### Matériel

Le **_matériel_** comporte tous les éléments physique d'une machine :

- processeur
- mémoire
- disques dur
- clavier, souris, écran
- carte réseau
- ...

Que l'on peut regrouper en trois grandes catégories :

- processeur
- mémoire
- les [périphériques](https://en.wikipedia.org/wiki/Peripheral) ou _devices_ qui regroupent tout le reste. C'est ce qui se branche sur la [carte mère](https://fr.wikipedia.org/wiki/Carte_m%C3%A8re)

{% note "Accès matériel" %}

Chaque device va avoir son fonctionnement propre (un clavier ne fonctionne pas pareil qu'un disque dur et deux cartes réseaux de constructeurs différents vont fonctionner différemment). Pour permettre une utilisation simple de ces périphériques, un logiciel demande l'accès au matériel via des fonctions données par le système d'exploitation, nommés [appel système](https://fr.wikipedia.org/wiki/Appel_syst%C3%A8me) qui sont tout le temps le même pour une catégorie de périphérique donné. Le système d'exploitation accède quand à lui accède directement au matériel via des [drivers](https://fr.wikipedia.org/wiki/Pilote_informatique) propre à chaque device.

{% endnote %}

#### Logiciel

Les logiciels, que d'un point de vue système on appelle [**process**](<https://fr.wikipedia.org/wiki/Processus_(informatique)>) ou **processus** auront besoin pour fonctionner d'accéder au matériel mais également de cohabiter entre eux : un ordinateur va toujours avoir plusieurs logiciels en fonctionnement en même temps. C'est aussi le rôle d'un système d'exploitation que de faire en sorte que cette cohabitation se passe bien :

{% note "Logiciels concurrents" %}
Un système d'exploitation permet l'exécution de process :

- de façon [concurrente](https://fr.wikipedia.org/wiki/Programmation_concurrente) (on peut écrire dans un gdoc tout en écoutant de la musique)
- de façon sécurisée : le gdoc ne peut accéder aux variables de l'application jouant de la musique
  {% endnote %}

Il n'y aura toujours qu'un seul processus actif à chaque instant, mais comme on change souvent de processus actif, on a l'impression qu'ils s'exécutent en même temps.

{% info %}
[Parallèle vs concurrent](https://www.youtube.com/watch?v=r2__Rw8vu1M) :

- concurrent : le début d'un process est entre la début et la fin de l'autre
- parallèle : en même temps. Ceci est possible si on a plusieurs cœur ou plusieurs processus sur la machine
  {% endinfo %}

Que les processus soient concurrent ou parallèle, c'est le rôle du système d'exploitation de gérer cela.

### Couches Systèmes

Un système d’exploitation n'est pas monolithique, il est constitué de multiples parties qui forment un tout cohérent. L'organisation logicielle d'un ordinateur (ou plus généralement tout système logiciel assez important) est constitué de _couches_, comme le stipule le

{% note "**[théorème fondamental de l’ingénierie logicielle](https://en.wikipedia.org/wiki/Fundamental_theorem_of_software_engineering)**" %}

On peut régler tous les problèmes en ajoutant une couche d'indirection

{% endnote %}

```
       compliqué
A --------------------> B
   simple      simple
A --------> C --------> B
```

Ce principe universel est une instanciation de la [deuxième partie du discours de la méthode](https://fr.wikipedia.org/wiki/Discours_de_la_m%C3%A9thode#Deuxi%C3%A8me_partie) : il faut diviser chaque difficulté en autant de parties facile à résoudre séparément.
D'un point de vue ingénierie, ceci permet en plus de clairement les responsabilités de chaque couche, une maintenance plus aisée.

Un ordinateur et son utilisation peut être séparé quatre couches :

1. Matériel
   - mémoire RAM
   - devices
2. Noyau
   - drivers matériels
   - gestion de la mémoire
   - ordonnancement des processus
3. process
   - interface graphique
   - terminal
   - ...
4. utilisateurs
   - qui à le droit de faire quoi

{% note %}

Seul le noyau a accès au matériel et a un contrôle total de la machine. On distingue deux états d'une machine :

- le _kernel mode_ : le noyau travail
- le _user mode_ : un process travaille
  {% endnote %}
  {% lien %}
  [User et Kernel mode sous windows 11](https://learn.microsoft.com/fr-fr/windows-hardware/drivers/gettingstarted/user-mode-and-kernel-mode)
  {% endlien %}

La machine doit tourner le plus souvent possible en _user mode_ car toute mauvaise action en kernel mode peut potentiellement être désastreux (plantage de la machine, effacement de données, etc). Un système d'exploitation ne peut être uniquement composé d'un noyau, ce serait inefficace (rien ne pourrait être exécuté en parallèle) et dangereux (le moindre bug logiciel ou matériel ferait tout planter) :

{% note %}

Un système d'exploitation est constitué de 3 couches :

- **le** [noyau](https://fr.wikipedia.org/wiki/Noyau_de_syst%C3%A8me_d%27exploitation)
- **des** [interfaces logicielles](<https://en.wikipedia.org/wiki/Interface_(computing)#Software_interfaces>) qui permettent d'accéder aux devices (comme accéder à une clé usb)
- **des** [démons](<https://fr.wikipedia.org/wiki/Daemon_(informatique)>) qui gèrent l'environnement (le fait de réagir à l'insertion d'une clé usb dans l'ordinateur par exemple)

{% endnote %}

Les démons et les interfaces sont des process comme les autres. Ils sont cependant exécutés par un utilisateur spécial, souvent nommé [`root`](https://fr.wikipedia.org/wiki/Utilisateur_root), qui est le [super-utilisateur](https://fr.wikipedia.org/wiki/Utilisateur_root) et est le représentant utilisateur du système.

<span id="démarrage"></span>

La distinction entre user et kernel mode se fait directement au démarrage de la machine :

1. boot de l'ordinateur en kernel mode
2. exécution d'un [chargeur d'amorçage (_bootloader_)](https://fr.wikipedia.org/wiki/Chargeur_d%27amor%C3%A7age)
3. charge le noyau
   1. vérification du matériel
   2. vérification des sous-systèmes : réseau, ...
4. passage en user mode puis charge les démons et les interfaces
5. login

À partir de l'étape 4, l'ordinateur est en user mode. Il ne passe en kernel que :

- via un appel système d'un processus
- lorsque l'on change de processus actif

{% attention "À retenir" %}
La partie noyau du système d'exploitation ne fonctionne pas tout le temps, elle ne s'active **que** lors d'un appel système ou lors du changement de processus actif.
{% endattention %}

Si tous les process du user mode pouvaient effectuer tous les appels systèmes sans restriction cela poseraient d'énormes problèmes de sécurité (un process pourrait accéder à toute la mémoire, en particulier celle réservée à d'autres process par exemple) c'est pourquoi chaque process n'a qu'un nombre restreint de possibilités (on appelle ceci [des droits](<https://fr.wikipedia.org/wiki/Droit_d%27acc%C3%A8s_(informatique)>)) gérés via la notion d'utilisateurs.

### Utilisateurs et groupes

Du point de vue du système d'exploitation un utilisateur est une entité permettant d'exécuter des processus. L'utilisateur qui se connecte à l'ordinateur au login est donc un parmi beaucoup d'autres, la plupart n'étant pas associé à une personne physique. Les utilisateurs sont ensuite placés dans des groupes, chaque groupe ayant des droits particuliers.

{% note %}
Un utilisateur peut utiliser uniquement les éléments (logiciel, fichier, dossier, ...) qui lui appartiennent ou qui appartiennent à ses groupes.
{% endnote %}

Il existe de nombreux groupes et utilisateurs utilisés par le système pour segmenter (et donc sécuriser) les utilisations. Parmi eux, un utilisateur et un groupe se détachent car ils ont plus de droit que les autres.

#### Utilisateur `root`

L'utilisateur `root` est l'utilisateur lié au système d'exploitation. Il est le propriétaire des process (démons) et interfaces du système d'exploitation. Cet utilisateur a ainsi tous les droits (peut aller partout, réserver autant de mémoire qu'il veut, etc).

Comme **Tout** processus a un propriétaire, l'existence de cet utilisateur est garantie.

#### Groupe des administrateurs systèmes

{% lien %}
[administrateur système](https://fr.wikipedia.org/wiki/Administrateur_syst%C3%A8me)
{% endlien %}

Le groupe des administrateurs systèmes permet de modifier des paramètres systèmes d'exécuter ou stopper des démons et d'installer de nouveaux logiciels. Ces utilisateurs ont moins de pouvoirs que root qui peut tout faire mais permettent d'administrer le système au quotidien.

Cela permet, si nécessaire, d'installer ou de configurer son système sans être connecté en tant que root en utilisant [la commande sudo](https://www.linuxtricks.fr/wiki/sudo-utiliser-et-parametrer-sudoers) sous Linux par exemple.

