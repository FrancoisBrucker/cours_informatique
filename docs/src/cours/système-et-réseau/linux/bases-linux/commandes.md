---
layout: layout/post.njk

title: Commande

eleventyNavigation:
    order: 1

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---


> [liste des instructions courantes shell (bash)](https://github.com/RehanSaeed/Bash-Cheat-Sheet)

Les commandes sont les instructions que l'on exécute dans un shell. Elles sont faites pour être :

- spécialisées : elles ne font qu'un seule chose
- paramétrables : des options permettent de changer son comportement par défaut
- automatisables : elles ne demandent (presque) jamais de confirmation de la part de l'utilisateur

Elles sont exécutées :

- dans le **dossier courant** du shell
- avec un process enfant du shell

Une commande unix peut être utilisée de multiple manière. Le format d'utilisation standard est son nom suivi par des arguments séparées par des espaces. Par exemple :

- `ls` : exécution de la commande [ls](https://linux.die.net/man/1/ls)
- `ls ~` : exécution de la commande [ls](https://linux.die.net/man/1/ls) avec un paramètre

Les arguments d'une commande peuvent être :

- des options : commence par un `-`
- des paramètres : ne commencent pas par un `-`

L'exécution d'une commande par le shell se fait plaçant la commande, ses paramètres et ses options dans une liste où le 1er élément est la commande, suivie de ses arguments dans l'ordre d'entrée. Le premier élément de cette liste est exécuté et la liste est passée en paramètre de celle-ci.

{% exercice %}
La commande [echo](http://www.man-linux-magique.net/man1/echo.html) affiche ses paramètres séparés par un espace puis va à la ligne.

Quel est le résultat de la commande `echo coucou      !` ?
{% endexercice %}
{% details "solution" %}

La commande a deux paramètres :

- `coucou`
- `!`

Elle va donc afficher `coucou !` puis aller à la ligne.

{% enddetails %}

Pour distinguer les paramètres des options on fait précéder :

- une option courte, c'est à dire composé d'un caractère, par `-` : `ls -l`
- une option longue, c'est à dire composé d'un mot, par `--` : `ls --all`

L'intérêt des options courtes est qu'on peut les combiner en ne les faisant précéder que d'un `-`. Par exemple `ls -lh` est équivalent à `ls -l -h`. La plupart des options longues ont leur pendant court, mais ce n'est pas toujours le cas.

Enfin, certaines options nécessitent un paramètre qui doit être donné juste après celle ci. Exemple : `ls -hI "I*" ~` va fonctionner (on peut également les "coller" à l'option, comme ça : `ls -hI"I*" ~`) alors que `ls -Ih "I*" ~` non. Lorsque le paramètre Le paramètre des options longues peut être donné avec un `=`, par exemple : `ls ~ -h --ignore="I*"`

La plupart des commandes fonctionnent sous différents systèmes unix (Linux, Macos, Bsd, ...). Le fonctionnement général de chaque commande est dicté par la norme [POSIX](https://fr.wikipedia.org/wiki/POSIX) mais des variations existent (en particulier les extensions à POSIX dépendent de l'implémentation de la commande et donc du système unix utilisé) il est crucial de se référer à l'aide de son système.

{% note %}
La commande `man paramètre` permet d’accéder au manuel du nom de la commande passée en paramètre.

Par exemple `man ls`, ou encore `man man` pour accéder au manuel de `man`.

Le synopsis de la commande permet de donner toutes ses utilisation possible. Son format est [déterminée par une norme POSIX](https://pubs.opengroup.org/onlinepubs/9699919799/basedefs/V1_chap12.html) :

- **en gras** : doit être tapé exactement de la même manière
- *en italique* : à remplacer par les bon arguments
- `[-abc]` : toutes les options sont optionnelles
- `-a|-b` : les options -a et -b ne peuvent être utilisées en même temps
- <u>souligné</u> : l'argument est répétable

Ceci se combine :

- [<u>souligné</u>] : répétable et optionnel
- [expression [argument]] : l'expression est optionnelle et peut être utilisée avec ou sans argument
{% endnote %}

La plupart des commandes donnent une aide succincte avec l'option `-h` ou `--help`. Par exemple `ls --help`.

{% exercice %}
Comment faire pour que la commande echo n'aille pas à la ligne à la fin de son exécution ?
{% endexercice %}
{% details "solution" %}
C'est l'option `-n`.

Attention il faut la mettre en 1er argument, sinon cela ne fonctionne pas.

{% enddetails %}

On peut chaîner les commandes avec `;`. Par exemple : `ls ~; echo Fichiers de home`

{% note %}

Stopper une commande avec ctrl+C qui envoie le signal `SIGINT`

{% endnote %}

## Commandes classiques

Linux/Ubuntu possède une grande variété de commandes par défaut (tous les fichiers du dossier `/usr/bin`). Certaines demandent des droit d'administrations mais la plupart sont utilisables par tous les utilisateurs.

{% lien %}
<https://haydenjames.io/linux-commands-frequently-used-by-linux-sysadmins-part-1/>
{% endlien %}

### Indispensables

Un certains nombre de commandes sont indispensable à connaître (pas à maîtriser).

- `man`
- `cd`
- `ls`
- `cat`, `less` (ou `more`)
- `touch`
- `echo`
- `rm` et `rmdir`
- `mv`
- `grep`
- `sed`, `awk` (au moins à quoi ils peuvent servir)
- `find` (au moins à quoi ça peut servir)

{% exercice %}
Utilisez grep pour connaître le shell de l'utilisateur `root`. Il se trouve dans le fichier `/etc/passwd`
{% endexercice %}
{% details "solution" %}

```shell
grep root /etc/passwd
```

{% enddetails %}

{% exercice %}
Une des commandes ci-dessus n'est pas dans `/usr/bin`. Laquelle ?
{% endexercice %}
{% details "solution" %}

```shell
ls /usr/bin/cd
ls: impossible d'accéder à '/usr/bin/cd': Aucun fichier ou dossier de ce type
```

Alors que les autres commandes fonctionnent :

```shell
ls /usr/bin/cd
ls: impossible d'accéder à '/usr/bin/cd': Aucun fichier ou dossier de ce type
```

{% enddetails %}

### Utiles

- [curl](https://www.youtube.com/watch?v=APtOavXTv5M&list=PLShDm2AZYnK1SdG3dufPdCqk08sOahUBP&index=9)
- [dd](https://www.youtube.com/watch?v=hsDxcJhCRLI)
- [gzip et bzip2](https://www.computernetworkingnotes.com/linux-tutorials/how-to-use-gzip-and-bzip2-linux-commands-explained.html)
- [jq](https://lzone.de/cheat-sheet/jq)

{% note %}
Il est possible que certaines de ces commandes n'existent pas chez vous. Installez-les.
{% endnote %}

## Retour d'une commande

Lorsqu'une commande unix ne rend aucun retour visible, c'est que tout s'est bien passé.

Chaque commande va rendre un entier, appelé ***code de sortie***, par défaut invisible sur la ligne de commande. Cet entier vaut :

- 0 si tout s'est bien passé
- un entier strictement positif s'il y a une une erreur (l'entier caractérise l'erreur)

La valeur de retour de la dernière commande exécutée dans le shell est stockée dans la variable spéciale `$?`

{% exercice %}
Quel est le retour de `ls /` ? Et de `ls /root` ?

Que signifie ces retours ?
{% endexercice %}
{% details "solution" %}

Une fois la commande exécutée, on tape `echo $?` pour connaître son code de sortie.

- `ls /` rend 0
- `ls /root` rend 2 (si on a pas exécuté la commande en temps que root bien sur)

Le code de retour est déterminé dans le manuel.

{% enddetails %}

On peut utiliser ce mécanisme en utilisant les opérateurs logiques [`&&` et `||`](https://kyleshevlin.com/using-and-and-or-in-bash-scripts) :

- ET logique : `commande1 && commande2` : la `commande2` ne sera exécutée que si le code de sortie de la `commande1` est un succès (vaut 0)
- OU logique : `commande1 || commande2` : la `commande2` ne sera exécutée que si le code de sortie de la `commande1` est un échec (vaut >0)

{% attention %}
En shell, 0 vaut pour un succès et le reste est un échec. Ainsi, La commande `true` rend 0 et `false` rend 1.

Ceci diffère de la  programmation classique où 0 vaut faux et le reste vaut vrai.
{% endattention %}

Ceci permet de chaîner conditionnellement des commandes.

{% exercice %}
Quelle est la différence entre :

- `cd ~/truc ; touch toto`
- `cd ~/truc && touch toto`
{% endexercice %}
{% details "solution" %}
Le premier va créer un fichier `toto` dans truc s'il existe ou dans le répertoire courant sinon, le second crée le fichier toto dans truc s'il existe.

{% enddetails %}
{% exercice %}
Que fait :

```shell
ls ~/truc || mkdir ~/truc ; cd ~/truc
```

{% endexercice %}
{% details "solution" %}
Ca créer le dossier `~/truc`{.fichier} s'il n'existe pas. Puis aller dans le dossier `~/truc`{.fichier}

Si truc existe et est un fichier. Il va cependant y avoir un soucis...
{% enddetails %}

## Grouper des commandes

{% lien %}
[Grouper des commandes](https://www.gnu.org/software/bash/manual/html_node/Command-Grouping.html)
{% endlien %}

On peut grouper de commandes de deux façons :

- `{ cmd1; cmd2; }` : les commandes sont exécutées dans le shell courant
- `(cmd1 ; cmd2 ; ...)` : un shell enfant est crée pour exécuter les commandes dans la parenthèse. Ceci permet d'isoler ces exécutions

Notez que c'est bien l'accolade qui est début et la fin de l'instruction de groupement, il faut les prendre comme des commandes spéciales :

- il faut faire suivre l'accolade ouvrante d'un espace
- il faut faire précéder l'accolade fermante d'un point-virgule

{% exercice %}
Quelle est la différence entre les deux instructions suivantes :

1. `cd /; { ls; cd; }`
2. `cd /; ( ls; cd; )`

{% endexercice %}
{% details "solution" %}
On ne conserve pas les dossiers courants dans un sous-shell. ON est donc toujours dans `/` à la fin du second jeu d'instructions.
{% enddetails %}

La création d'un shell enfant pour exécuter des commandes est un principe fondamental en unix. Il permet de compartimenter les exécutions de commandes comme on la vue dans l'exercice précédent.

## <scan id="meta-caracteres"></span>Interactions avec le shell

{% lien %}
[Les métacaractères du shell](https://www.youtube.com/watch?v=4W5NG3jZXHU&list=PLQqbP89HgbbbD0WSKRR90R5yjmTpSNNIl&index=6)
{% endlien %}

Le shell va interpréter certains caractères, nommé ***métacaractères*** avant même que la commande ne soit exécuté. Vous en connaissez déjà au moins deux, l'espace qui sépare les arguments d'une commande et `$?`, mais il en existe une foules d'autres. Parmi eux, les plus courant sont :

- l'espace pour séparer les arguments
- toute une série commençant par `$` :
  - `$?` : le code de sortie de la dernière commande
  - `$$` : le PID du shell courant
  - `$(expression)` : pour exécuter l'expression et donner son affichage comme argument. Par exemple `echo $(expr 3 + 4)`. C'est bien ce qui est affiché qui est rendu, pas son code de sortie.
  - `$((arithmétique))` : pour [exécuter des opérations arithmétiques](https://www.gnu.org/software/bash/manual/bash.html#Shell-Arithmetic), par exemple `echo $((3+4))`
  - `${variable}` : pour afficher le contenu d'une variable, par exemple `echo ${PAH}`
- expression régulières pour les fichiers du dossiers courant (la fin de la vidéo introductive y est consacrée)
  - `*` : `echo .*` va afficher tous les fichier du dossier courant commençant par un `.`. Notez bien que ce remplacement est effectué avant l'exécution de `echo` qui ne voit qu'une suite de paramètres
  - `?` : un caractère. Par exemple `cd ~; echo Vid?os`
  - `[caractères]` un caractère parmi la liste. Par exemple `cd ~; echo [vV]id?os`

On peut inhiber cette interférence du shell dans nos commandes de trois façons :

- par un `\` pour inhiber le métacaractère qui suit. Par exemple `echo \*`. Attention ne marche pas si le métacaractère est composé de deux caractères, par exemple `echo \$(expr 3 + 4)` ne fonctionne pas car la parenthèse n'est pas inhibée.
- par des `' '` qui inhibent tous les métacaractères. Par exemple `echo 'bonjour      !'` ou `echo '$?'`
- par des `" "` qui inhibent tous les métacaractères **sauf** ceux commençant par `$`. Par exemple `echo "bonjour      !"` ou `echo "$?"`

{% attention %}
Vous verrez parfois <span>&#96;</span>commandes<span>&#96;</span>, qui est équivalent à `$(commandes)`.

Par exemple :

```shell
echo `expr 3 + 4`
```

Qui est équivalent à :

```shell
echo $(expr 3 + 4)
```

J'ai tendance à préférer cette dernière notation qui est selon moi plus clair. On a déjà assez à faire avec `"` et `'`
{% endattention %}
  
## I/O

> TBD en faire plus. Car les `|`, `>` et `>>` c'est pas clair.

{% lien %}

- <https://linuxhint.com/bash_stdin_stderr_stdout/>
- <https://www.youtube.com/watch?v=zMKacHGuIHI>

{% endlien %}

Toute commande à 3 flux qui lui sont connectés :

- l'entrée standard, *stdin*, qui est par défaut le clavier
- la sortie standard, *stdout*, qui est par défaut l'écran
- l'erreur standard, *stderr*, qui est par défaut l'écran

```
stdin -> process --> stdout
                 \
                  -> stderr
```

### Lecture de l'entrée standard

```shell
wc
```

Il lit l'entrée standard. Stopper la commande avec ctrl+C arrêter tout et interrompt la commande. Il faut terminer l'entrée standard en lui faisant lire la séquence de contrôle EOF ctrl+D.

### Redirection de la sortie vers une autre commande

{% note "**Commande**" %}
La redirection de la sortie vers l'entrée se fait via le *pipe* : `|`.
{% endnote %}

> TBD expliciter les commandes ci-dessous.

Le très utilisé :

```shell
cat /etc/passwd | less
```

Ou plus compliqué :

```shell
cat /etc/passwd | cut -d : -f 1 | lolcat
```

### Pipe et tee

> TBD créer ses propres pipe avec `mkfifo`
> TBD faire mieux. Mettre dans une partie à part. Un peu comme un cheveux sur la soupe là.
> TBD dire que la sortie de l'un va dans l'autre.

```
----> stdin   |pipe|  stdout ----> 
```

Une seule sortie mais l'entrée peut venir de plusieurs endroits par des redirections :

```
-  
  \
----> stdin   |pipe|  stdout ----> 
  /
-
```

Un tee permet d'avoir 2 sorties, stdout et une sortie vers un fichier

```
----> stdin   |pipe|  stdout ----> 
                              \
                                -> fichier
```

### redirection de la sortie vers un fichier

{% note "**Commande**" %}
La redirection de la sortie vers un **nouveau** fichier se fait avec : `>`.
{% endnote %}

```shell
echo "toto" > truc
```

{% note "**Commande**" %}
La redirection de la sortie vers **la fin** d'un fichier existant se fait avec : `>>`.
{% endnote %}

```shell
echo "toto" >> truc
```

### Redirection de l'erreur

```shell
ls /truc 2>&1 | lolcat
```

[tee](https://linuxize.com/post/linux-tee-command/) pour :

- sauver un résultat intermédiaire dans une chaîne
- sauver et voir le stdout

### car particulier de l'affichage à l'écran

Souvent les commandes savent si leur stdout est dirigé vers un terminal (doit être affiché à l'écran) ou un fichier, et vont se comporter différemment selon le cas.

Par exemple va lister les fichier les uns à la suite ds autres pour une sortie écran et un par ligne pour une sortie fichier ou pipe

```shell
$ ls
Bureau     Images   Musique  snap             temp  truc
Documents  Modèles  Public   Téléchargements  test  Vidéos
$ ls > ls.result
$ cat ls.result 
Bureau
Documents
Images
ls.result
Modèles
Musique
Public
snap
Téléchargements
temp
test
truc
Vidéos
```

Si on "*voir*"  ce qui se passe si on redirige vers un fichier, on peut rediriger vers `cat` :

```shell
$ ls | cat
Bureau
Documents
Images
ls.result
Modèles
Musique
Public
snap
Téléchargements
temp
test
truc
Vidéos

```

## Exercice

> TBD en faire des petits commandes à suivre.

On aura besoin de tout ce qu'on a appris

```
hexdump -C < /dev/random
```

```
xxd < /dev/random
```

```
base64 </dev/random | head -c 100 
```

```
base64 </dev/random 2>/dev/null | head -c 100
```

```
base64 </dev/random | head -c 100 ; echo
```

```shell
echo "hasard : "$(base64 </dev/random 2>/dev/null| head -c 100)
```
