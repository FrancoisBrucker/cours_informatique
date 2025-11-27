---
layout: layout/post.njk

title: Shell scripting

eleventyNavigation:
    order: 1

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---


> sh cheat sheet : <joedog.org/articles-cheat-sheet/>
> <https://stackoverflow.com/questions/5725296/difference-between-sh-and-bash>
> <https://stackoverflow.com/a/5725402>
> <https://www.commandlinux.com/man-page/man1/sh.1.html>

Les principes d'un bon script sont (voir [classic shell scripting](https://www.amazon.fr/Classic-Shell-Scripting-Arnold-Robbins/dp/0596005954)) :

1. faire **une seule chose** et sans blabla
2. prendre et rendre du texte pas de fichiers binaires
3. utiliser les entrés/sorties standard
4. vos entrées et vos sorties doivent avoir le même format
5. "*laisser quelqu'un d'autre faire les choses compliquées*" : utiliser d'autres commandes unix

{% attention "À retenir" %}

Essayer d'être portable. On fait du du sh pour pouvoir être exécuté partout.

{% endattention %}

> TBD faire exemple du rot13 tout au long de ce cours

Taper des commandes = script. Comme python. Il faut trouver un moyen de faire des bouts de commandes sans les executer a=à la fin d'une ligne. Python fait des blocs. shell fait autrement. De plus, tout est orienté commandes sans pratiquement aucune surcouche du shell (on le verra avec les if/then/else qui fonctionnent bien différemment du reste des langages de programmation)

{% lien %}
- [tuto](https://www.youtube.com/watch?v=tK9Oc6AEnR4)
- [un autre tuto](https://www.youtube.com/watch?v=KG97VzMjfMg)

<https://www.gnu.org/software/bash/manual/html_node/>
{% endlien %}

```shell
#! /bin/sh -

```

## Gestion des paramètres

{% lien %}
[Gestion des paramètres d'un script](https://coderwall.com/p/85jnpq/bash-built-in-variables)
{% endlien %}

## Fonctions

{% lien %}

- [Fonctions bash en texte](https://linuxize.com/post/bash-functions/)
- [fonctions bash YouTube](https://www.youtube.com/watch?v=aqvc9kYnz0U&list=PLShDm2AZYnK1SdG3dufPdCqk08sOahUBP&index=2)

{% endlien %}

Les fonctions ne peuvent rendre qu'un entier, c'est leur code de sortie. Pour le reste effectuez vos sorties sur la sortie standard (avec `echo`).

## Structures de contrôle

### if/then

```shell
if 
commandes
then
commandes
fi
```

Avec un else :

```shell
if 
commandes
then
commandes
else
commandes
fi
```

C'est le retour de la dernière commande avant la ligne avec `then` qui décide du branchement :

- s'il vaut 0 on fait le bloc allant de `then` à `else` (ou `fi` s'il n'y a pas de bloc `else`)
- sinon on fait le bloc allant de `else` à `fi`

Par exemple, en utilisant les commandes [`true`](https://man7.org/linux/man-pages/man1/true.1.html) et [`false`](https://man7.org/linux/man-pages/man1/false.1.html) :

```shell
if
true
then
echo oui
else
echo non
fi
```

Ou encore :

```shell
if
false
true
then
echo oui
else
echo non
fi
```

On peut aussi avoir la forme où la première commande peut être placée après le if :

```shell
if true
then
echo oui
else
echo non
fi
```

La forme précédente qui est très pratique lorsque l'on a qu'une seule commande.

{% attention %}
Une commande doit précéder l'instruction `then` si on peut avoir sur une même ligne le if et le then, il faut terminer la commande de test avec un `;` :

```shell
if true; then
echo oui
else
echo non
fi
```

{% endattention %}

La commande [`test`](https://linux.die.net/man/1/test) qui est aussi la commande `[` (oui, `[` est un fichier de `/usr/bin`) permet de faire de nombreux test courant :

{% lien %}
[Utiliser la commande `test` ou `[`](https://www.shellscript.sh/test.html)
{% endlien %}

Bash permet également d'utiliser une construction utilisant [`[[ expression ]]`](https://tldp.org/LDP/abs/html/testconstructs.html#DBLBRACKETS) qui rend certains tests plus clair mais est spécifique à bash et ne fonctionnera pas avec d'autres shell (`[[` n'est pas une commande, c'est une instruction interne à bash). Préférez donc les constructions avec `[` ou `test`, plus portable.

Il est possible de tester de nombreuses choses, allant de conditions logique à l'existence de fichiers :
{% lien %}
[comment réaliser des tests en bash](https://fr.wikibooks.org/wiki/Programmation_Bash/Tests)
{% endlien %}

### boucles for/while/until

{% lien %}
[boucles en bash](https://www.gnu.org/software/bash/manual/html_node/Looping-Constructs.html)
{% endlien %}

Les constructions sont identiques à la construction du if. La seule particularité est la boucle for qui itère sur une suite de mot séparé par des espaces :

```
for x in salut les gars
do                     
echo $x      
done                   
```

Ou, de façon équivalente :

```
for x in salut les gars; do
echo $x      
done                   
```

On utilise parfois la boucle `while` pour lire l'entrée standard, en combinaison avec la commande [`read`](https://www.quennec.fr/trucs-astuces/syst%C3%A8mes/gnulinux/programmation-shell-sous-gnulinux/les-bases-de-la-programmation-shell/la-commande-read) :

```shell
while read line
do
  echo "$line"
done < /dev/stdin
```

Ou le redoutable :

```shell
while read line
do
  echo "$line"
done < "${1:-/dev/stdin}"
```

Qui lit l'entrée standard si le premier paramètre (`$1`) n'est pas positionné. Cela utilise une spécificité de sh pour [gérer les variables](https://github.com/dylanaraps/pure-sh-bible?tab=readme-ov-file#parameter-expansion).

## Variables

### Métacaractères

On a déjà vu [les métacaractères du shell](../../bases-linux/commandes#meta-caracteres), ils commencent par `$` et peuvent être utilisés dans les scripts :

- `$?` : le code de sortie de la dernière commande
- `$$` : le PID du shell courant
- `$(expression)` : pour exécuter l'expression et donner son affichage comme argument. Par exemple `echo $(expr 3 + 4)`. C'est bien ce qui est affiché qui est rendu, pas son code de sortie.
- `$((arithmétique))` : pour [exécuter des opérations arithmétiques](https://www.gnu.org/software/bash/manual/bash.html#Shell-Arithmetic), par exemple `echo $((3+4))`
- `${variable}` : pour afficher le contenu d'une variable, par exemple `echo ${PAH}`

### Variables internes

Des variables créés par le shell et pouvant être utilisé dans les scripts. A utiliser avec parcimonie car cela rend vos scripts spécifiques à bash.

{% lien %}
<https://tldp.org/LDP/abs/html/internalvariables.html>
{% endlien %}

## Process et shell

> TBD mieux faire

Le script est par défaut exécuté dans un nouveau shell. Mais ce n'est pas toujours ce que l'on veut :

- `./truc.sh`{.fichier} exécution dans un nouveau shell enfant
- `source ./truc.sh`{.fichier} exécution ligne à ligne dans le shell actuel
- `. ./truc.sh`{.fichier} exécution ligne à ligne dans le shell actuel (identique à `source`)
- `exec ./truc.sh`{.fichier}` nouveau shell qui remplace le shell existant

Supposons que vous ayez un fichier exécutable `pid.sh`{.fichier} contenant :

```
#! /bin/sh

echo $$
```

1. Le pid du shell courant est accessible avec : `echo $$`
2. Le pid précédent est différent du pid du shell exécutant le script : `./pid.sh`
3. On devrait retrouver le même pid en tapant : `source ./pid.sh`

C'est très utile lorsque l'on exécute un fichier de configuration qui doit s'appliquer au shell courant.

Attention, si vous exécutez `exec ./pid.sh` le shell faisant le echo vq remplacer le shell courant et donc fermer la fenêtre. Pour l'exécuter sans soucis faite le dans un sous-shell :

```shell
$ echo $$
704757
$ bash
$ echo $$
705824
$ exec ./pid.sh 
705824
$ echo $$
704757
```

## Getopt

> TBD <https://labex.io/fr/tutorials/shell-bash-getopt-391993>

## Bash scripting

> TBD étoffer et vérifier que je ne raconte pas de bêtises.
> TBD dans les systèmes actuels sh = bash

- [un cours](https://michael-herbst.com/teaching/advanced-bash-scripting-2017/)
