---
layout: layout/post.njk

title: "Erreurs courantes : Pendu"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---


## Description d'une fonction

La description d'une fonction (entre `"""`{.language-}) est inutile. Le code **doit** se suffire à lui-même pour être lisible et compris. Si ce n'est pas le cas, c'est que vous avez mal codé !

La description de chaque fonction n'est utile que si vous faire une bibliothèque (une suite de fonctions qui devront être utilisées par d'autres sans qu'ils aient à connaître leurs codes). Ici, vous faite du code qui sera exécuté ou utilisé par vous et les autres membres de l'équipe de développement (ou le correcteur, ici moi) : la description ou les commentaires **doivent** être inutiles : faites du code lisible.

## Listes

On préférera toujours utiliser `L.append(i)`{.language-} plutôt que `L = L + [i]`{.language-} car `append`{.language-} est une méthode en $\mathcal{O}(1)$ opérations alors `+` crée une nouvelle liste et est donc en $\mathcal{O}(n)$ où $n$ est la taille de la liste `L`{.language-}.

## Comparaison de booléens

On ne teste pas si un booléen est vrai ou faux, on utilise directement sa valeur.

- On écrit : `assert est_une_lettre("i", "victoire")`{.language-}
- ~~On écrit pas `assert est_une_lettre("i", "victoire") == True`{.language-}~~

En effet, les deux formes sont équivalentes puisque une comparaison avec `==`{.language-} rend `True`{.language-} ou `False`{.language-} mais la seconde est plus compacte et moins redondante.

De même (vu souvent), à la place d'écrire :

```text
Si f() == Vrai alors:
    return Vrai
sinon:
    return Faux
```

écrivez :

```text
return f()
```

## Import

Deux fautes de style reviennent assez souvent :

- `from truc import *`{.language-}
- `import contrôle as ctr`{.language-}

Ne faites aucune des deux, c'est [Bad Karma](https://www.youtube.com/watch?v=2dRIHt2SJHE) (et c'est très très mal !) : ça vous sautera à la figure tôt ou tard.

{% attention "**Pourquoi c'est mal**" %}

- `from truc import *`{.language-} : **on ne sais pas ce que l'on importe**. Le traçage des fonctions n'est pas clair et tôt ou tard ça va vous sauter à la figure en important des choses que vous ne voulez pas importer
- `import contrôle as ctr`{.language-}. Je ne vois pas l'avantage de cette chose. Vous vous tirez au moins 3 fois une balle dans le pied :
  1. **Ce n'est pas plus court**. Car, pourquoi ne pas avoir écrit `import contrôle as c`{language-} ? C'est **encore** plus court... On gagne carrément 2 caractères à chaque utilisation du module ! De quoi finir à 12h14 à la place de 12h15 (royal !).. Ou tant qu'à gagner des lettres autant directement renommer le fichier `contrôle.py`{fichier} en `ctr.py`{.fichier}. On aurait eu encore moins de choses à écrire (juste `import ctr`{language-}, soit carrément 12 caractères de moins !)
  2. **c'est moins lisible**. Vous devez pouvoir lire votre code sans avoir besoin de réfléchir aux significations des variables. Votre esprit doit être concentré sur la compréhension de l'algorithmie. Vous gagnez 10 microsecondes à l'écriture (et encore, voir ci-après) mais vous perdez 2 secondes à chaque lecture pour vous rappeler la signification de `ctr`{.language-}.
  3. **vous empêchez votre éditeur de vous aider** avec la complétion automatique qui rend un nom explicite est plus facile à compléter qu'une abréviation.

{% endattention %}

## Variable différent d'une chaîne de caractère

Ne confondez pas la variable ou le paramètre d'une fonction `x`{.language-} avec une chaîne de caractères contenant le caractère x, notée `'x'`{.language-}.
