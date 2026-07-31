---
layout: layout/post.njk

title: Système de fichiers et fichiers système

eleventyComputed:
    eleventyNavigation:
        key: "{{ page.url }}"
        title: "{{ title | safe }}"
        parent: "{{ '../' | siteUrl(page.url) }}"
---


{% lien %}
[Type de fichiers Linux](https://www.n0tes.fr/2015/09/22/Types-fichiers-Linux/)
{% endlien %}

Le système de fichiers de Linux possède plusieurs types de fichiers différents. Ils permettent d'accéder non seulement à des données stockées sur le disque dur, mais également à tout ce qui se passe en interne dans le noyaux et les processus.

Commençons par identifier les fichiers les plus courant, en considérant ce bout de résultat d'un `ls` de mon dossier maison :

```shell
$ ls -la ~
total 148
drwxr-x--- 23 fbrucker fbrucker  4096 oct.  13 08:56 .
drwxr-xr-x  3 root     root      4096 août  24 08:18 ..
-rw-------  1 fbrucker fbrucker 14022 oct.  13 09:04 .bash_history
-rw-r--r--  1 fbrucker fbrucker   220 août  24 08:18 .bash_logout
-rw-r--r--  1 fbrucker fbrucker  3771 août  24 08:18 .bashrc
drwxr-xr-x  2 fbrucker fbrucker  4096 août  24 08:20 Bureau

[snip]
```

Le type de fichier est le 1er élément :

- `-` pour les fichiers *régulier*, comme `.bashrc`{.fichier}
- `d` pour les dossiers, comme `Bureau`{.fichier}

On voit aussi deux dossiers spéciaux `.`{.fichier} et `..`{.fichier} qui permettent de remonter dans la hiérarchie et sont respectivement des [liens physiques](https://doc.ubuntu-fr.org/lien_physique_et_symbolique) vers les dossiers courant et parent.

{% info %}
Un [lien symbolique](https://doc.ubuntu-fr.org/lien_physique_et_symbolique#exemple_de_lien_symbolique) aura un `l` comme premier élément et est un type de fichier spécial, le lien physique **est** le même fichier.
{% endinfo %}

## Fichiers d'accès aux données systèmes

Il existe tout un tas d'autres types de fichiers, qui sont remplis par le noyau lorsque l'on y accède. Par exemple le dossier `/proc`{.fichier} :

{% faire %}
Faire un :

```shell
$ ls /proc
```

Et trouvez le nombre de secondes depuis que votre système est en marche en lisant la mage man de /proc : `man proc` ou `man 5 proc`.
{% endfaire %}
{% details "solution" %}

```shell
$ cat /proc/uptime | cut -d ' ' -f 1
```

{% enddetails %}

Par exemple pour le process du shell courant :

```shell
$ ls -la /proc/$$
```

{% attention %}
[`/proc/$$`{.fichier} vs `/proc/self`{.fichier}](https://chengdol.github.io/2020/02/03/linux-proc-$$-self/)
{% endattention %}

Le dossier `/proc/$$`{.fichier} Contient un dossier `cwd`{.fichier} qui est un fichier spécial (c'est un lien) :

```shell
$ cd ~
$ ls -la /proc/$$/cwd
lrwxrwxrwx 1 fbrucker fbrucker 0 oct.  13 10:18 /proc/704757/cwd -> /home/fbrucker

```

Voyez comment ce dossier change selon l'endroit où l'on est ? Les dossier et fichiers de `/proc`{.fichier} sont crées et modifiés par le noyau. Ils permettent d'accéder directement à toute information relative au système via des fichiers, la plupart du temps texte. Lorsqu'on accède à l'un d'eux, via la commande `cat` par exemple, qui *lit le contenu du fichier* (fonction *read* des fichiers) le noyau renvoie une valeur, le plus souvent texte.

## Fichiers d'I/O

Les entrées et sorties sur les divers disques durs sont *aussi* des fichiers. Ils sont rangés dans le dossier `/dev`{.fichier} (quelques entrées seulement):

```shell
fbrucker@MV-ubuntu:/dev$ ls -la
total 4

brw-rw----   1 root     disk      8,   0 oct.   9 06:18 sda
brw-rw----   1 root     disk      8,   1 oct.   9 06:18 sda1
brw-rw----   1 root     disk      8,   2 oct.   9 06:18 sda2
lrwxrwxrwx   1 root     root          15 oct.   9 06:18 stderr -> /proc/self/fd/2
lrwxrwxrwx   1 root     root          15 oct.   9 06:18 stdin -> /proc/self/fd/0
lrwxrwxrwx   1 root     root          15 oct.   9 06:18 stdout -> /proc/self/fd/1
crw-rw-rw-   1 root     tty       5,   0 oct.   9 06:18 tty
crw--w----   1 root     tty       4,   0 oct.   9 06:18 tty0
crw-rw-rw-   1 root     root      1,   5 oct.   9 06:18 zero

[snip]
```

Ce dossier contient, outre des liens symboliques, des fichiers de **type bloc** (`b`) qui corresponde à des disques durs et des fichiers de **type caractère** (`c`) qui correspondent à des terminaux d'entrée et/ou sortie.

## FIFO

{% lien %}
[FIFO shell](https://www.youtube.com/watch?v=6lik_f1Vp54)
{% endlien %}

```shell
ls -la ma_fifo 
prw-rw-r-- 1 fbrucker fbrucker 0 oct.  16 11:45 ma_fifo
```

Les FIFO sont de type `p` pour pipe. On les appelle en effet aussi pipes (`|`) nommés.

Ils permettent d'utiliser les pipes en-dehors d'un chaînage de commandes et permettent d'avoir plusieurs entrées qui se combinent en une sortie :

```
A >-
     \ 
B >-------> FIFO >---- sortie
      /
C >--
```

{% faire %}

1. Créez une FIFO nommée `ma_fifo`{.fichier} dans votre dossier maison.
2. exécutez la commande `cat ~/ma_fifo`
3. ouvrez un autre terminal et exécutez la commande `cat > ~/ma_fifo`, puis écrivez du texte. Lorsque vous appuyez sur la touche entrée,  vous devriez voir apparaître le texte dans l'autre terminal.

{% endfaire %}
