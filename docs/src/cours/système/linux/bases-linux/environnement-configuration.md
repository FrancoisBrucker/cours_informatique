---
layout: layout/post.njk

title: Environnement et configuration

eleventyNavigation:
    order: 1

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

La gestion des variables d'environnement dépend du shell utilisé. On suppose ici que vous utilisez le shell par défaut sous Linux/Ubuntu : [bash](https://www.gnu.org/software/bash/)

## Variables d'environnement

La personnalisation de son environnement se fait sous la forme de variables. Ces variables servent à deux choses essentiellement :

- personnaliser son shell (par exemple la langue, les chemins vers les exécutables, ...)
- stocker des paramètres pour plus tard (l'ancien dossier courant par exemple)

L'ensemble de ces variables d'environnement sont disponibles avec la commande `env`

### Création de variables

{% lien %}
[liste des variables](https://blog.roxing.net/bash-liste-des-variables)
{% endlien %}

Il faut commencer par créer une variable :

```
var=valeur
```

{% attention %}
[Pas d'espace dans la déclaration de variable en shell](https://utcc.utoronto.ca/~cks/space/blog/unix/BourneShellObscureErrorRoots)
{% endattention %}

Puis on peut l'afficher en précédant sont nom d'un ${} :

```
echo ${var}
```

{% info %}
Il n'est pas nécessaire d'utiliser les `{}` (`echo $var` fonctionne) mais prenez l'habitude de le faire, cela permet :

- d'être plus clair
- décrire des choses comme `echo ${var}2`

{% endinfo %}

Il est possible d'utiliser les variables partout ! Ce sont des méta-caractères du shell et sont donc remplacés par leurs valeurs **avant** l'exécution de la commande. Il est donc envisageable (et c'est souvent fait) de faire ce genre de choses :

```
v=ls
${v}
```

{% exercice %}
Si `toto=titi`
Quelle est la différence entre les commandes suivantes :

- `echo toto`
- `echo $toto`
- `echo $toto2`
- `echo ${toto}2`
- `echo "${toto}"`
- `echo '${toto}'`

{% endexercice %}
{% details "solution" %}
Va afficher :

- `toto`
- `titi`
- ``
- `titi2`
- `titi`
- `${toto}`

{% enddetails %}

Les variables sont utilisables dans tout le shell, mais ne sont pas transmises au process enfant :

```
toto=titi
bash
echo ${toto}
```

Il faut promouvoir les variables en variables d'environnement pour qu'elles soient transmises :

```
toto=titi
export toto
bash
echo ${toto}
```

On peut créer et promouvoir une variable en une seule opération :

```
export toto=titi
```

### supprimer une variable

Avec `unset` :

```
toto=titi
echo ${toto}
unset toto
echo ${toto}
```

### Visualisation des variables

{% lien %}
[env et export](https://www.youtube.com/watch?v=1z6EUUl11qI&list=PLQqbP89HgbbY23Ab_vXGfLXHygquD7cAs&index=2)
{% endlien %}

- `env` (ou `export`) vous donnent l'ensemble des variables d'environnements
- [`set`](https://www.gnu.org/software/bash/manual/html_node/The-Set-Builtin.html) vous donne l'ensemble des variables et  fonctions définies dans bash

### Existence d'une variable

Il n'y a pas de réel moyen de savoir si une variable existe ou pas. Par exemple `echo ${n_existe_pas}` ne produira pas d'erreur, le métacaractère `${n_existe_pas}` étant juste remplacé par la chaîne vide.

### Variables spéciales

- `$PATH`
- `$PWD` `$OLDPATH` (`cd -`)
- `$HOME`

{% exercice %}
La commande `cd` change la variable `$PWD` du shell courant. Ce qui fait que `cd` ne peut-être un fichier exécutable.

Pourquoi ?
{% endexercice %}
{% details "solution" %}
Un fichier exécutable est crée dans un sous shell. Il ne peut donc modifier les variables de son shell parent.
{% enddetails %}

## Modification locale de l'environnement

On peut modifier l'environnement d'exécution d'une commande. Par exemple, pour avoir le manuel de man en anglais  :

```
LANG=C man man
```

On modifie la variable pour le process qui exécutera la commande : comme c'est un process enfant, la variable du shell parent nest pas modifiée.

On peut modifier/créer plusieurs variables en les séparant par des espaces (pas un `;` qui est le métacaractère shell de séparation de commande):

```
V1=v1 V2=v2 commande
```

## Fichiers de configurations de bash

{% lien %}
[dotfiles de bash](http://mywiki.wooledge.org/DotFiles)
{% endlien %}

Plusieurs fichiers sont lus lors de l'exécution du shell :

1. au login sur une nouvelle machine  :
   1. exécution du fichier `/etc/profile`
   2. **si** un fichier `.bash_profile` existe dans votre home **alors** il est exécuté
   3. **sinon si** un fichier  `.bash_login` existe dans votre home **alors** il est exécuté
   4. **sinon si** un fichier  `.profile` existe dans votre home **alors** il est exécuté
2. pour des exécutions non login (c'est à dire pour des enfants du shell bash de login) :
3. lecture du fichier `.bashrc` de votre home

- Le fichier `.profile` est un standard POSIX préférez ce fichier aux autres pour mettre votre configuration de login.
- le fichier `.bashrc` n'est **pas** au login, il est d'usage de le lire à la fin du `.profile`

{% exercice %}
Que fait le fichier `/etc/profile` avec les fichiers du dossier `/etc/profile.d` ?
{% endexercice %}
{% details "solution" %}
Il va les exécuter un à un.
{% enddetails %}

### Que mettre dans les fichiers de conf

- on place dans le `.profile` les éléments qui sont transmis aux enfants donc essentiellement les variables d'environnements, en particulier [la gestion du `$PATH`](https://opensource.com/article/17/6/set-path-linux).
- le fichier `.bashrc` contient tous les éléments qui ne sont pas transmis aux shell enfants, comme les alias ou les définitions de fonctions,

## Fichiers de configurations des applications

{% lien %}
[Où sont rangés les fichiers de configuration](https://wiki.archlinux.org/title/XDG_Base_Directory)
{% endlien %}

Les application vont eux aussi avec des fichiers de configurations. La plupart des applications vont créer un dossier à leur nom dans votre `$HOME/.config`

Si vous avez des exécutables à vous, rangez les dans : `$HOME/.local/bin`, et n'oubliez pas d'ajouter ce dossier à votre PATH.

{% exercice %}
Créez un fichier nommé `bonjour`{.fichier} contenant :

```
#! /usr/bin/env python3
print("bonjour !")
```

Placez le dans votre dossier `$HOME/.local/bin` et faites en sorte de pouvoir l'exécuter de partout en modifiant le path.
{% endexercice %}
{% details "solution" %}

- créer le fichier au bon endroit
- modifier les droits pour le rendre exécutable
- dans le fichier `.profile`, modifier le `$PATH` pour qu'il accepte le chemin `export PATH=${PATH}:${HOME}/.local/bin`

{% enddetails %}

L'organisation des ses fichiers de préférence, appelés les *dotfiles* est un réel sujet. La plupart d'entre nous ont un projet github contenant nos fichiers de conf pour pouvoir les déplacer facilement d'une machine à l'autre :

{% lien %}
[gestion des dotfiles](https://www.youtube.com/watch?v=5oXy6ktYs7I)
{% endlien %}
