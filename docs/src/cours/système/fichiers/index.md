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
- ***seek*** qui permet de gérer la position dans le fichier
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

## Gérer ses fichiers

### EOF

{% lien %}
[EOF](https://www.baeldung.com/linux/eof)
{% endlien %}

Lorsque l'on est entrain d'écrire dans un fichier, on peut envoyer le signal `EOF` (*End Of File*) pur indiquer que l'on a plus rien à écrire, au moins pour l'instant.

Réciproquement, lorsque l'on lit un fichier, si l'on reçoit le signal EOF, cela signifie que le fichier n'a plus de données à nous faire lire pour l'instant.

{% note %}
Si vous écrivez au clavier, la combinaison de touche `ctrl+D` envoie le signal EOF
{% endnote %}
{% faire %}
Si vous utilisez la commande `cat`, elle va lire l'entrée standard et la répéter.

Si au milieu d'une ligne vous tapez la combinaison de touche `ctrl+D`, le signal EOF est envoyé et votre bout de ligne est affiché.  

Vous pouvez continuer à taper des choses, le lien entre `stdin` et `cat` n'est pas rompu. Ce n'est que si vous envoyez deux signaux `EOF` de suite que le lien est stoppé.
{% endfaire %}

Le signal EOF est une information envoyé au process qui lit le fichier comme quoi il n'y a plus rien à lire. Le process peut alors choisir soit  d'attendre d'avoir de nouveau des choses à lire, soit stopper la lecture.

{% faire %}

1. créez un fichier vide `test`{.fichier} avec la commande `touch test`
2. dans un terminal lisez le fichier avec la commande `tail -f` qui lit les 10 dernières lignes du fichier eet ne stope pas la lecture à la fin (lisez le man)
3. dan un autre terminal ajoutez ds lignes à votre fichier (par exemple avec la commande `echo "coucou" >> test`)
4. vous devriez voir la ligne s'afficher dans le terminal exécutant la commande `tail -f`

{% endfaire %}
{% info %}
Cette technique est très utilisée lorsque l'on veut visualiser en direct le comportement d'un serveur web par exemple via son [fichier de log](https://en.wikipedia.org/wiki/Logging_(computing)).
{% endinfo %}

### Buffers

{% lien %}
[buffers de stdin/out/err](https://www.pixelbeat.org/programming/stdio_buffering/)
{% endlien %}

La plupart des fichiers sont *bufferisés*, c'est à dire qu'ils n'envoient leurs données que par paquet, et ce pour des raisons de performances ou de praticité.

Sans buffer, les données sont directement envoyées au programme une par une :

```
              stream
fichier | ------------- | programme
```

Un buffer stocke les données lues (une à une ou par paquet) :

```
              stream
fichier | ------------- | buffer | 
                        |--------|
                        |---     | ......... | programme
                                             |
```

Et une fois plein ou qu'une condition est remplit  :

```
              stream
fichier | ------------- | buffer | 
                        |--------|
                        |--------| ......... | programme
                                             |
```

Il envoie toutes ses données stockées au programme (on appelle ça un flush) en une fois :

```
              stream
fichier | ------------- | buffer | 
                        |        |            
                        |        | .......... | programme
                                              | --------------
```

Si vous regardez par exemple les fichiers de `/dev`{.fichier}, ce sont des fichiers de type bloc. C'est à dire que l'envoi des données se fait par paquet pour limiter les accès disques.

Ceci est aussi vrai des fichiers `stdin` et `stdout` qui n'envoient leurs données qu'une fois le caractère '\n' reçu (une fois que la touche enter est appuyée). Ces buffer sont dit de type *line*

{% faire %}
Si vous utilisez la commande `cat`, elle va lire l'entrée standard et la répéter.
La lignée tapée depuis `stdin` ne sera envoyée à `cat` qu'une fois le caractère '\n' reçu. Si vous tapez ctrl+c au milieu d'une ligne rien n'est envoyé
{% endfaire %}

Ceci est pratique puisque cela permet dans le cadre du shell :

- d'éditer et corriger ses lignes si besoin
- chaque entrée est une commande et peut être traitée directement

En revanche., le fichier stderr n'est pas bufferisé. Comme il doit traiter des erreurs, tout ce qui y est écrit doit être directement visible.

On peut contrôler les buffers des fichiers standards :

- en shell avec la commande [stdbuf](https://www.gnu.org/software/coreutils/manual/html_node/stdbuf-invocation.html#stdbuf-invocation).
- en **C** en utilisant la fonction [setbuf](https://man7.org/linux/man-pages/man3/setbuf.3.html) si on a ouvert le fichier avec [fopen](../fichiers-C)

Vider le buffer pour tout envoyer est appelé *flush*. On peut le faire explicitement en envoyant le signal EOF, mais cela peut parfois déconnecter la lecture/écriture. En **C**, on peut aussi explicitement le faire  en utilisant la commande [fflush](https://koor.fr/C/cstdio/fflush.wp).

### En shell

{% aller %}
[Fichiers en shell](fichiers-shell){.interne}
{% endaller %}

### Appels systèmes

{% aller %}
[Appels systèmes fichiers](fichiers-syscall){.interne}
{% endaller %}
