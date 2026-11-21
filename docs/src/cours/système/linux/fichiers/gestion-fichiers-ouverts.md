---
layout: layout/post.njk

title: Gestion des fichiers ouverts

eleventyComputed:
    eleventyNavigation:
        key: "{{ page.url }}"
        title: "{{ title | safe }}"
        parent: "{{ '../' | siteUrl(page.url) }}"
---


Dans un système unix ce sont les process qui ouvrent des fichiers, mais le noyaux en garde en sous-main le contrôle pour permettre à des process différents de se partager les ressources ouvertes.

## Process

Chaque process doit garder une liste des fichiers qu'il a ouvert et peut donc utiliser.

A chaque fichier ouvert est associé un numéro nommé Un [descripteur de fichier (*file descriptor*)](https://fr.wikipedia.org/wiki/Descripteur_de_fichier). Les différents fichiers ouvert par un process donné sont accessibles via leurs file descriptor dans leurs `/proc`{.fichier} :

```shell
ls -la /proc/$$/fd
```

Tout process a toujours 3 file descriptors :

- 0 qui est stdin
- 1 qui est stdout
- 2 qui est stderr
- 255 uniquement si vous utilisez bash (utilisé pour ses besoins internes)

Ces fichiers ouverts sont des redirections vers le [fichier tty](https://www.malekal.com/quest-ce-que-tty-comment-utiliser-commande-tty-sur-linux/) correspondant.

{% exercice %}
Les fichiers `stdin`{.fichier}, `stdout`{.fichier} et `stderr`{.fichier}  présent dans `/dev/`{.fichier} sont des liens.

Vers quoi pointent-ils ?
{% endexercice %}
{% details "solution" %}
vers les files descriptor de `/proc/self/`{.fichier} qui est le process actuellement entrain d'être exécuté (et il change de nombreuses fois par secondes...).

A chaque lecture du fichier `/proc/self/`{.fichier}, le noyau va donner le process actuellement entrain d'être exécuté, c'est à dire celui qui lit le dossier. Ainsi, si vous exécutez la commande :

```shell
ls -l /proc/self
```

Cela vous affichera le process du `ls` entrain de lire `/proc/self`.

De la même manière si vous écrivez :

```c
echo "coucou" >> /dev/stdout
```

C'est dans le stdout de echo que vous écrivez (et c'est donc identique à écrire `echo "coucou"`).

{% enddetails %}

{% faire %}
Ouvrez deux terminaux :

1. vérifiez que les 3 FD ne pointent pas vers le même tty
2. écrivez dans le stdout de l'un à partir de l'autre.
{% endfaire %}

Vous pouvez connaître leurs informations dans le dossier `fdinfo` :

```shell
ls -la /proc/$$/fdinfo/1
```

### Fichiers ouverts

{% lien %}
[Commande lsof](https://www.youtube.com/watch?v=Gr2IbTZdnvI)
{% endlien %}

Si vous utilisez la commande `lsof -p $$` vous verrez que process ouvre plus de fichiers que les fide descriptors numériques (qui sont des entrées/sorties) :

```shell
$ lsof -p $$
COMMAND    PID     USER   FD   TYPE DEVICE SIZE/OFF    NODE NAME
bash    928549 fbrucker  cwd    DIR   0,24        4 5241736 /proc/928549/fd
bash    928549 fbrucker  rtd    DIR    8,2     4096       2 /
bash    928549 fbrucker  txt    REG    8,2  1415800  655454 /usr/bin/bash
bash    928549 fbrucker  mem    REG    8,2  8321104  662997 /usr/lib/locale/locale-archive
bash    928549 fbrucker  mem    REG    8,2  1641496  663748 /usr/lib/aarch64-linux-gnu/libc.so.6
bash    928549 fbrucker  mem    REG    8,2   195784  658635 /usr/lib/aarch64-linux-gnu/libtinfo.so.6.3
bash    928549 fbrucker  mem    REG    8,2   187776  663741 /usr/lib/aarch64-linux-gnu/ld-linux-aarch64.so.1
bash    928549 fbrucker  mem    REG    8,2    27004  664116 /usr/lib/aarch64-linux-gnu/gconv/gconv-modules.cache
bash    928549 fbrucker    0u   CHR  136,1      0t0       4 /dev/pts/1
bash    928549 fbrucker    1u   CHR  136,1      0t0       4 /dev/pts/1
bash    928549 fbrucker    2u   CHR  136,1      0t0       4 /dev/pts/1
bash    928549 fbrucker  255u   CHR  136,1      0t0       4 /dev/pts/1
```

Il y a :

- le dossier où est le shell (ici `/proc/928549/fd`{.fichier})
- le fichier exécuté bash lui-même !
- les bibliothèques partagées utilisées par le programme bash
- les fichiers de communications stdin, stdout, stderr et 255.

{% faire %}

1. ouvrez un fichier texte avec `less`
2. trouver son PID avec `ps aux | grep less`
3. voir ses fichiers ouverts

{% endfaire %}

On peut également faire le contraire et regarder quel process ouvre tel fichier en utilisant la commande [`fuser`](https://www.digitalocean.com/community/tutorials/how-to-use-the-linux-fuser-command) :

```shell
$ fuser -v /usr/bin/bash
                     UTIL.       PID ACCÈS  COMMANDE
/usr/bin/bash:       fbrucker  928549 ...e. bash
```

### Limites

Un process particulier ne peut pas forcément ouvrir autant de fichier. Par défaut, la limite est 1024. Comme annoncée dans le fichier limits du process :

```shell
$ cat /proc/$$/limits
Limit                     Soft Limit           Hard Limit           Units     
Max cpu time              unlimited            unlimited            seconds   
Max file size             unlimited            unlimited            bytes     
Max data size             unlimited            unlimited            bytes     
Max stack size            8388608              unlimited            bytes     
Max core file size        0                    unlimited            bytes     
Max resident set          unlimited            unlimited            bytes     
Max processes             7422                 7422                 processes 
Max open files            1024                 1048576              files     
Max locked memory         257257472            257257472            bytes     
Max address space         unlimited            unlimited            bytes     
Max file locks            unlimited            unlimited            locks     
Max pending signals       7422                 7422                 signals   
Max msgqueue size         819200               819200               bytes     
Max nice priority         0                    0                    
Max realtime priority     0                    0                    
Max realtime timeout      unlimited            unlimited       
```

Vous pouvez aussi utiliser la commande : `ulimit -a` et ses différentes options pour particulariser la limite à chercher. Exemple `ulimit -n`.

## Noyau

{% lien %}
[FD et FT](https://www.youtube.com/watch?v=rW_NV6rf0rM&list=PLhy9gU5W1fvUND_5mdpbNVHC1WCIaABbP&index=21)
{% endlien %}

Le noyau maintient à jour une table globale contenant tous les fichiers ouverts par tous les process. Cette table, nommé ***file table*** contient :

- le type d'accès au fichier : lecture ou écriture
- un lien vers le fichier : inode pour un fichier classique ou un dossier, socket, etc
- la position dans le fichier
- le nombre de *file descriptor* pointant vers cette structure

Chaque *file descriptor* est alors associé à un élément de la *file table*.

```
process             noyau
  FD         Table         
              T1  ---------> inode/socket/pipe/...
  23 -        T2 
       \        
        \     Ti  ---
         \            \
  42  ----->  Fj   ------->  Vk
```

Plusieurs file descriptor (d'un même process ou de process différents) peuvent pointer vers le même élément de la table, et plusieurs élément de la table peuvent ouvrir le même fichier.

La table est initialisée au démarrage et contient toutes les structures, le type de fichier étant libre. Il y a donc un nombre maximum de fichier qui peuvent être ouvert en même temps pour un système.

{% info %}
On peut bien sur connaître le nombre de fichier actuellement ouvert : `cat /proc/sys/fs/nr_open` et le nombre de fichier maximum `cat /proc/sys/fs/file-max`. Chez moi cela donne :

```shell
$ cat /proc/sys/fs/nr_open
1048576
$ cat /proc/sys/fs/file-max
9223372036854775807
```

{% endinfo %}

## Fork

Lors de la création de nouveaux process, les files descriptors sont dupliqués :

1. l'enfant à le même nombre de file descriptor que son parent
2. les file descriptors de l'enfant pointent vers les même élément de la table que son parent
