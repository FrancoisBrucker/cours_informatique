---
layout: layout/post.njk

title: Shell

eleventyNavigation:
    order: 1

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---


Essayer d'être portable. On fait du du bash (voir du sh) pour pouvoir être exécuté partout

- [tuto](https://www.youtube.com/watch?v=tK9Oc6AEnR4)
- [un autre tuto](https://www.youtube.com/watch?v=KG97VzMjfMg)

Taper des commandes = script. Comme python. Il faut trouver un moyen de faire des bouts de commandes san les executer a=à la fin d'une ligne. Python fait des blocs. shell fait autrement. De plus, tout est orienté commandes sans pratiquement aucune surcouche du shell (on le verra avec les if/then/else qui fonctionnent bien différemment du reste des langages de programmation)

<https://www.gnu.org/software/bash/manual/html_node/>

## Gestion des paramètres

{% lien %}
[Gestion des paramètres d'un script](https://coderwall.com/p/85jnpq/bash-built-in-variables)
{% endlien %}

## Fonctions

{% lien %}

- [Fonctions bash en texte](https://linuxize.com/post/bash-functions/)
- [fonctions bash YouTube](https://www.youtube.com/watch?v=aqvc9kYnz0U&list=PLShDm2AZYnK1SdG3dufPdCqk08sOahUBP&index=2)

{% endlien %}

Les fonctions ne peuvent rendre qu'un entier, c'est leur code de sortie. POur le reste effectuez vos sorties sur la sortie standard (avec `echo`).

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

```
while read line
do
  echo "$line"
done < /dev/stdin
```

Ou le redoutable :

```
while read line
do
  echo "$line"
done < "${1:-/dev/stdin}"
```

Qui lit l'entrée standard si le premier paramètre (`$1`) n'est pas positionné. Cela utilise une spécificité de bash pour [gérer les variables](https://www.gnu.org/software/bash/manual/bash.html#Shell-Parameter-Expansion).

## Variables

- Méta-caractères commençant par `$` :
  - `$?` : le code de sortie de la dernière commande
  - `$$` : le PID du shell courant
  - `$(expression)` : pour exécuter l'expression et donner son affichage comme argument. Par exemple `echo $(expr 3 + 4)`. C'est bien ce qui est affiché qui est rendu, pas son code de sortie.
  - `$((arithmétique))` : pour [exécuter des opérations arithmétiques](https://www.gnu.org/software/bash/manual/bash.html#Shell-Arithmetic), par exemple `echo $((3+4))`
  - `${variable}` : pour afficher le contenu d'une variable, par exemple `echo ${PAH}`
- variables internes : <https://tldp.org/LDP/abs/html/internalvariables.html>

## Process et shell

> TBD mieux faire

- `./truc.sh`{.fichier} exécution dans un nouveau shell enfant
- `source ./truc.sh`{.fichier} exécution ligne à ligne dans le shell actuel
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


## Pipe

> TBD créer ses propres pipe avec `mkfifo`

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

## Autres shell

Plusieurs sortes de shell (sh : shell historique, bash : shell par défaut dans Linux, zsh : shell par défaut macos, ...)

perso : mon shell c'est zsh mais les script je les écris en (ba)sh.

- [sh ou bash pour nos scripts ?](https://www.youtube.com/watch?v=8L7cM4q6TL8)

- le script se fait avec le shell le plus courant : bash (présent sous macos)
- [histoire du design sh](https://www.youtube.com/watch?v=FI_bZhV7wpI)

```
curl https://www.gutenberg.org/cache/epub/1184/pg1184.txt 2>/dev/null | wc
```

https://itslinuxfoss.com/how-parse-json-shell-scripting-linux/

## Bibliographie

- [un cours](https://michael-herbst.com/teaching/advanced-bash-scripting-2017/)
