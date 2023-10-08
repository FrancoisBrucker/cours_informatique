---
layout: layout/post.njk

title: Gestion du build

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---


## Makefile simple

{% lien %}

[Introduction à make](https://www.youtube.com/watch?v=a8mPKBxQ9No)

{% endlien %}

La video précédente nous a permis d'écrire le fichier `Makefile`{.fichier} suivant dans le dossier de notre projet :

```
CC=clang
CFLAGS=-Wall -Wextra -pedantic -std=c2x

all: main

main: main.o celcius.o
	$(CC) $(CFLAGS) main.o celcius.o

main.o: main.c
	$(CC) $(CFLAGS) -c main.c

celcius.o: celcius.c
	$(CC) $(CFLAGS) -c celcius.c

clean:
	rm *.o a.out
```

{% attention "**danger !**" %}
L'indentation des makefile est la **tabulation**.

- Oui c'est complètement idiot
- Non on ne peut pas faire autrement

Heureusement, si vous utilisez un IDE, il reconnaîtra que vous faire un Makefile et utilisera bien les tabulations.
{% endattention %}

On utilise un makefile de façon simple. Dans un terminal, tapez `make` (qui est équivalent à `make all`, car c'est la première règle du fichier `Makefile`{.fichier}):

```
$ make      
clang -Wall -Wextra -pedantic -std=c2x -c main.c
clang -Wall -Wextra -pedantic -std=c2x -c celcius.c
clang -Wall -Wextra -pedantic -std=c2x main.o celcius.o
```

La règle `all` dépend des règles `main.o` et `celcius.o` qu'il faut donc faire avant :

- la 1ère ligne correspond à l'exécution de la règle `main.o`
- la 2nde ligne correspond à l'exécution de la règle `celcius.o`
- la 3ème ligne correspond à l'exécution de la règle `all` qui est un prérequis de la règle `all` qui est la règle par défaut.

Si on retape la commande `make`, on remarque un changement :

```
$ make      
clang -Wall -Wextra -pedantic -std=c2x main.o celcius.o
```

Seule la règle main a été exécutée. Ceci est normal car [une règle](https://www.gnu.org/software/make/manual/html_node/Rule-Syntax.html) est définie :

```
noms : prérequis
	commande
```

Si `noms` et `prérequis` sont des noms de fichiers : on exécute la règle `noms` que si un des fichiers de `prérequis` est plus récent (ou a été modifié plus récemment que) un des fichiers de `noms`.

Dans notre cas :

- `all` et `main` ne sont as ds fichiers, elles seront donc toujours exécutées
- `main.o` a été crée à l'exécution de make précédente, le fichier est donc plus récent que `main.c` dot elle dépend : cette règle ne sera pas exécutée
- `celcius.o` a été crée à l'exécution de make précédente, le fichier est donc plus récent que `celcius.c` dot elle dépend : cette règle ne sera pas exécutée

Vérifions ceci en changeant la date de modification du fichier `celcius.c`{.fichier} puis en re-exécutant `make` :

```
$ touch main.c
$ make        
clang -Wall -Wextra -pedantic -std=c2x -c main.c
clang -Wall -Wextra -pedantic -std=c2x main.o celcius.o
```

La règle `celcius.o` a bien été exécutée en plus de la règle `main`.

Pour faire une compilation fraîche, on commence par effacer tout résidu de la compilation précédente avant de refaire un make :

```
$ make clean
rm *.o a.out
$ make      
clang -Wall -Wextra -pedantic -std=c2x -c main.c
clang -Wall -Wextra -pedantic -std=c2x -c celcius.c
clang -Wall -Wextra -pedantic -std=c2x main.o celcius.o
$ ./a.out
98.60 
310 
```

## Variables Makefile

Grace aux variables, il n'est pas nécessaire d'expliciter toutes les règles :

{% lien %}
[variables de make](https://www.youtube.com/watch?v=G5dNorAoeCM)
{% endlien %}

On obtient le fichier `Makefile`{.fichier} suivant, bien plus simple et portable :

```
CC=clang
CFLAGS=-Wall -Wextra -pedantic -std=c2x

OBJECTS=main.o celcius.o 
NAME=celcius

all: $(NAME)

$(NAME): $(OBJECTS)
	$(CC) $(CFLAGS) -o $@ $^

%.o: %.c %.h
	$(CC) $(CFLAGS) -c $^

clean:
	rm *.o $(NAME)
```

Il suffit de renseigner :

- la variable `OBJECTS` avec les différents `.o` nécessaires
- la variable `NAME` avec le nom du programme final

## Documentation

Ce qu'on a appris devrait suffire pour 99.9% de vos besoins, mais au cas ou :

- [documentation de make](https://www.gnu.org/software/make/manual/)
- [Analyse d'un makefile](https://www.youtube.com/watch?v=l5KqE0DMG-Q)
- [Guide du makefile](https://makefiletutorial.com/#top)
