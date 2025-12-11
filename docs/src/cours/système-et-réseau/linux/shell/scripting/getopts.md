---
layout: layout/post.njk

title: paramètres de script

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---


1. sans rien
2. `$1` `$2`
3. `$@` `$#` `$0`
4. `shift` (boucle avec "y'en a des biens")
5. test si des paramètres ou pas
6. faire boucle à la min avec --b et startswith
7. getopts (est-ce posix ?)
8. ajouter l'aide ":" "\?"
9. getopts + paramètres sans argument à la fin
10. getopts + paramètres sans argument partout
11. ajouter l'aide si pas de paramètres par défaut (attention faire des listes)

script final :

```sh

#! /bin/sh

echo $# '-' $@

args=""

while (($#))
do
    while getopts ":hf:" opt 
    do
        case $opt in
            f) echo "f" $OPTIND '-' $OPTARG
                ;;
            h) echo "h" $OPTIND '-' $OPTARG
                ;;
            :) echo "option manquante" $OPTIND '-' $OPTARG
                ;;
            \?) echo "inconnu" $OPTIND '-' $OPTARG
                ;;
        esac
    done
    shift $((OPTIND-1))
    echo $# '-' $@
    if [ $# -gt 0 ]
    then
        args=$args" $1"
        shift
    fi
done

echo "args:"$args"-"
```

Fin (ça rate avec markdown...) :

```shell
if [ $ accolade #args accolade -lt 1 ]
then
    echo "au moins un argument"
fi
 ```
