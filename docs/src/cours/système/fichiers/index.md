---
layout: layout/post.njk

title: Fichiers Unix

eleventyComputed:
    eleventyNavigation:
        key: "{{ page.url }}"
        title: "{{ title | safe }}"
        parent: "{{ '../' | siteUrl(page.url) }}"
---

Accéder (en lecture ou en écriture) à un ensemble de données peut se faire de deux façons :

- ***accès direct*** : on peut accéder à chaque donnée indépendamment
- ***accès séquentiel*** : on peut accéder qu'à un échantillon de donnée à chaque instant.

Le principal représentant de la première catégorie d'accès est l'accès à la mémoire RAM (Random Access Memory). On accède à tout élément de la mémoire, un byte, via son adresse, que l'on lire ou modifier.

Le principal représentant de la seconde catégorie est l'accès disque ou réseau : on ne peut accéder aux données que via deux fonctions : une fonction de lecture qui renvoie un ensemble de donnée et une fonction d'écriture qui écrit un ensemble de données.

Ces deux moyens d'accès ont chacun des avantages et ds inconvénients selon le type ou la structure de données manipulée :

- **accès direct** :
  - avantages :
    - chaque donnée est identifiée (son adresse)
    - accès rapide à n'importe quelle donnée
  - inconvénient : l'ensemble des données accessibles est forcément fini et constant
- **accès séquentiel** :
  - avantage :
    - accès aux données sous la forme d'un flux (*stream*) possiblement infini
    - les fonctions de lecture et écriture peuvent être *intelligentes*
  - inconvénient : il faut souvent plusieurs lectures pour accéder à une donnée particulière

On privilégiera l'accès direct lorsque l'on cherche à accéder **rapidement** à une donnée parmi un nombre constant de donnée, c'est à dire pour les accès mémoires, et l'accès séquentiel pour tout le reste.

{% note "**Définition**" %}
Dans le monde unix, une donnée pouvant être accédée de façon séquentielle est un ***fichier***. On y accède via 5 méthodes :

- ***open*** qui prépare le fichier à être accédé **soit** en lecture **soit** en écriture
- ***close*** qui termine l'accès au fichier
- ***read*** qui retourne des données du fichier
- ***write*** qui envoie des données au fichier
- ***seek*** qui se positionne à un endroit particulier dans le fichier
{% endnote %}
{% info %}
La méthode **seek** permet d'accéder à une donnée particulière, comme on le ferait avec une donnée à accès direct, mais :

- elle prend usuellement beaucoup plus de temps
- elle peut ne pas être définie selon le type de fichier
{% endinfo %}

Cette définition permet d'utiliser un fichier pour :

- lire/écrire des données sur le disque dur : des fichiers "classique"
- faire des accès réseaux
- demander des informations au noyaux
- ...

L'utilisation d'un fichier est identique quelque soit le type de fichier :

1. on commence par ouvrir le fichier en lecture ou en écriture avec la méthode **open**.
2. selon la méthode d'ouverture, on peut alors lire (avec la méthode **read**) ou écrire (avec la méthode **write**) des données. Le nombre de données lues ou écrite dépend du type de fichier.
3. une fois terminé, on clôt le fichier en utilisant la méthode **close**.

{% lien %}
[The file abstraction in Linux](https://www.youtube.com/watch?v=UJBr211etS4&list=PLhy9gU5W1fvUND_5mdpbNVHC1WCIaABbP&index=19)
{% endlien %}

Un système unix ouvre constamment de très nombreux fichiers. Vous pouvez les voir en utilisant la commande [`lsof` `ls` open file](https://www.redhat.com/sysadmin/analyze-processes-lsof)

{% exercice %}
Combien de fichier sont ouvert sur votre système ?
{% endexercice %}
{% details "solution" %}

```shell
$ lsof | wc -l
```

{% enddetails %}

## Système de fichiers

{% aller %}
[Système de fichiers et fichiers système](système-fichiers){.interne}
{% endaller %}

## Fichiers ouverts

{% aller %}
[Gestion des Fichiers ouvert](gestion-fichiers-ouverts){.interne}
{% endaller %}


> TBD : faire des FD
> - shell
> - C
>
> nouvelle partie fopen en C
> 
## créer des FD shell

{% lien %}
[file descriptor](https://www.youtube.com/watch?v=FuiLk7uH9Jw)
{% endlien %}

On peut en créer d'autres avec `exec` (attention tout doit être collé), qui seront soit :

- associé à des fichiers déjà ouvert
- associé à un nouveau fichier

Par exemple le code suivant qui crée un nouveau file descriptor qui est associé au *fichier* de la sortie standard:

```shell
$ exec 42>&1
$ echo coucou >&42
coucou
ls -la /proc/$$/fd/42
lrwx------ 1 fbrucker fbrucker 64 oct.  13 09:20 /proc/704757/fd/42 -> /dev/pts/0

```

Ou créer un file descriptor associer à un nouveau fichier  :

```shell
$ exec 42>texte
$ echo coucou >&42
$ cat texte 
coucou
$ ls -la /proc/$$/fd/42
l-wx------ 1 fbrucker fbrucker 64 oct.  13 09:20 /proc/704757/fd/42 -> /home/fbrucker/texte

```

Supprimer un file descriptor se fait ensuite avec `exec 42>&-` :

```shell
$ exec 42>&-
$ ls -la /proc/$$/fd/42
ls: impossible d'accéder à '/proc/704757/fd/42': Aucun fichier ou dossier de ce type
```



## utilisation

[lien vers fd](https://www.youtube.com/watch?v=ayMPFUGE_b4&list=PLhy9gU5W1fvUND_5mdpbNVHC1WCIaABbP&index=20)

<https://www.baeldung.com/linux/bash-close-file-descriptors>

buffer : block/line/"unbuffered" (byte buffered)
limite les accès disque/réseau qui sont lent

- stdin, stdout : line (ctrl+c avant la fin d'une ligne de marque rien)
- stderr : unbuffered
- char
- block

> example shell/buffer : <https://unix.stackexchange.com/questions/411263/stdin-unbuffered>
> TBD : buffer/unbuffer (explication claires) <https://groups.google.com/g/comp.unix.programmer/c/qDxLCB7fCmA>
> 
<https://www.pixelbeat.org/programming/stdio_buffering/>
<https://eklitzke.org/stdout-buffering>
<https://www.learntosolveit.com/cprogramming/chapter8/sec_8.2_getchar.html>
> TBD une image là dedans : <https://stackoverflow.com/questions/63218184/buffered-vs-unbuffered-how-actually-buffer-work>

- read : bloquant jusqu'à ce qu'il se passe quelque chose.
- close : on peut réutiliser le même numéro plus tard. Attention dans votre code... Il faut faire attention, comme un free

### shell

> TBD exemple
> fifo et FD : <https://stackoverflow.com/questions/26344446/questions-about-fifos-and-file-descriptor>

EOF pour terminer la lecture. C'est le caractère de numéro 0 '\0'. Ne finit pas nécessairement la lecture (`tail -f` par exemple lorsque l'on lit des logs. Faire un exemple avec terminal)
EOF != de ne rien lire (ça peut venir plus tard)

EOD = ctrl+D
fermeture du programme = ctrl+c (pas pareil)

### En C

<https://www.youtube.com/watch?v=dhFkwGRSVGk>
<https://www.softprayog.in/programming/interprocess-communication-using-fifos-in-linux>
<https://www.geeksforgeeks.org/named-pipe-fifo-example-c-program/>

[dup et dup2](https://www.delftstack.com/fr/howto/c/dup2-in-c/)

fprintf(stdout) = printf (?)

{% lien %}
[file et C](https://www.youtube.com/watch?v=ayMPFUGE_b4&list=PLhy9gU5W1fvUND_5mdpbNVHC1WCIaABbP&index=20)
{% endlien %}
en C : file descriptor différent de file handle.

- [open](https://man7.org/linux/man-pages/man2/open.2.html) -> int
- fopen -> FILE * (type opaque ?)

lecture dans buffer
écriture dans buffer et flush.

> TBD : coder exemple puis utiliser strace pour voir les syscall pour l'ouverture/lecture et fermeture du fichier

{% lien %}
[fopen vs open](https://www.youtube.com/watch?v=BQJBe4IbsvQ)
{% endlien %}

Attention à l'affichage : str a un '\0' à la fin, pas la lecture d'un fichier.
TBD exemple.

lire utf8 caractère par caractère. Commence 
fgetwc ?

### open

- file descriptor
- flags

- marche bien pour stdin/out ou des fichiers de devices

read, write mais pas les deux à la fois (entrée ou sortie du FD)

### fopen

{% lien %}
[structure opaque FILE](https://www.youtube.com/watch?v=bOF-SpEAYgk&list=PLhQjrBD2T381k8ul4WQ8SQ165XqY149WW&index=20)
{% endlien %}

- structure opaque, qui contient le File descriptor, les options d'ouverture, le buffer, etc.
- pour de vrais fichiers
- bufferisé pour la rapidité : attention au flush.

- tout pour fichier avec f devant :
  - fopen, fclose, fread, fwrite, fgetc, fputc, [fseek](https://www.youtube.com/watch?v=EA2MVIgu7Q4) (si plus loin que la fin quel caractère est ajouté ?)
- et deux fonctions formattées : fprintf et fscanf

### mmap

- utilise le iomapping vue dans la partie système.
- [mmap](https://www.youtube.com/watch?v=m7E9piHcfr4)

## lire et écrire du texte

> TBD parler de utf8 dans la partie chaîne de caractères et y faire un renvoi depuis ici
> 
exemple avec poeme chinois :

- fr
- en
- chinois
- 
choisi si utf8 ou utf32 et on s'y colle.

Presque toujours utf8

<https://www.ibm.com/docs/en/zos/2.5.0?topic=functions-mbrtoc32-convert-multibyte-character-char32-t-character>

<https://beej.us/guide/bgc/html/split/unicode-wide-characters-and-all-that.html>


lecture d'un caractère ? 

utf8 -> u32 : pour strlen
u32 -> u8 

<https://en.cppreference.com/w/c/language/character_constant>

## entrées sorties

- pour l'entrée standard : flush lorsque retour à la ligne.
- car ?
- Pour la sortie standard il y a aussi un flush de temps en temps

Des fichiers comme les autres.

entrées sorties read et write <https://stackoverflow.com/questions/15883568/reading-from-stdin>

