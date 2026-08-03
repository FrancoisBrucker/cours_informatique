---
layout: layout/post.njk

title: Variables shell

eleventyNavigation:
    order: 1

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

On montre ici la création de variables avec les shell de type `sh` qui sont très utilisés comme [bash](https://www.gnu.org/software/bash/) (le shell par défaut sous des distribution Linux comme Ubuntu ou Debian), [zsh](https://www.zsh.org/) (le shell par défaut sous mac) ou [ksh](http://www.kornshell.com/) (le shell par d´´faut d'OpenBSD).

## Création de variables

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

On ne fait que écrire le contenu de la variable, on peut en faire ensuite ce que l'on veut :

```shell
❯ liste=ls
❯ ${liste}
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

On peut modifier/créer plusieurs variables en les séparant par des espaces (pas un `;` qui est le métacaractère shell de séparation de commande):

```
V1=v1 V2=v2 commande
```

## Supprimer une variable

Avec `unset` :

```
toto=titi
echo ${toto}
unset toto
echo ${toto}
```

## Visualisation des variables

Avec la commande shell [`set`](https://www.gnu.org/software/bash/manual/html_node/The-Set-Builtin.html).

## Existence d'une variable

Il n'y a pas de réel moyen de savoir si une variable existe ou pas. Par exemple `echo ${n_existe_pas}` ne produira pas d'erreur, le métacaractère `${n_existe_pas}` étant juste remplacé par la chaîne vide.

## Affecter une variable

> <https://www.gnu.org/savannah-checkouts/gnu/bash/manual/bash.html#Quoting>

### Commande

```shell
var=$(ls)
```

> TBD comme ` `. Mais je n'aime pas l'utiliser

C'est exécuté dans un sous shell et on récupère la sortie standard. Pas besoin du `$`, la sortie est juste affichée. Ce genre d'astuce permet de faire ce genre de choses :

```
(cd ..;ls)
```

### Arithmétique

```shell
var=$((1 + 3))
```

### Chaîne de caractères

```shell
echo "$((3+4))"
```

```shell
echo '$((3+4))'
```
