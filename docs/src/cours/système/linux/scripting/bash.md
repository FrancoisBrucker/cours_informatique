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

> TBD : $0, $1, $@

## Fonctions

> TBD fonction qui rendent des entier (retour d'instruction et que le reste c'est des sorties standards)

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

Bash permet également d'utiliser une construction utilisant [`[[ expression ]]`](https://tldp.org/LDP/abs/html/testconstructs.html#DBLBRACKETS) qui rend certains tests plus clair mais est spécifique à bash et ne fonctionnera pas avec d'autres shell (`[[` n'est pas une commande, c'est une instruction interne à bash) :

```shell

if [[ $answer -eq  "42"]]; then
echo "Youpi !"
fi
```

Préférez les constructions avec `[` ou test, plus portable

{% lien %}
[Créer ses test patterns](https://tldp.org/LDP/abs/html/testconstructs.html)
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