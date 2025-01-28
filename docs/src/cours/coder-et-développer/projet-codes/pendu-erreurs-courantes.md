---
layout: layout/post.njk

title: "Erreurs courantes : pendu"
---


{% note %}
Du code est fait pour être exécuté donc vous devez vous assurer que :

- le code rendu est exécutable
- vos tests sont exécutables avec pytest (on peut tolérer un test qui rate si vous expliquez que vous n'avez pas eu le temps de corriger le bug)

Pour cela, vous **devez** lancer régulièrement vos tests **pendant** le test.

{% endnote %}

Ci-après quelques remarques plus ponctuelles

## Trop lent

Vous prenez globalement bien trop de temps à écrire des algorithmes simples : les 3 premières questions doivent être faisable en 15 minutes.

En particulier, les tests à effectuer sont donnés dans l'énoncé sous la forme d'exemples, il vous suffisait de les reprendre en utilisant le formalisme vu lors du [projet pourcentage](../../développement/projet-pourcentages/).

## Format des tests

Les tests **doivent** être fait comme dans le [projet pourcentage](../../développement/projet-pourcentages/). Il faut donc :

- un fichier de test séparé du code et un fichier de test par fichier de code. Le nom de ce fichier doit s'appeler `test_[nom du fichier de code à tester].py`{.fichier}
- pourvoir l'exécuter avec `python -m pytest` dans un terminal (utilisez le nom de l'interpréteur python que vous avez, voir [ce tutoriel]({{ "/tutoriels/vsc-python" }}#quel-python))

En particulier :

{% attention %}

- afficher un résultat à l'écran avec la commande `print`{.language-} n'est **pas** un test
- faire un assert sans fonction de test n'est **pas** un test
- une fonction de test n'a **pas** de paramètres.

{% endattention %}

Chaque test **doit** commencer par `test_`{.language-} suivi du nom de la fonction à tester. S'il y a plusieurs tests pour une même fonction, on ajoute ce que le test teste :

```python
def test_[nom de la fonction à tester]_[ce que ça teste]():
    # ...
```

{% info %}
Ici, différentier les 2 tests proposés par fonction n'était pas évident. Regrouper les 2 tests en une seule fonction comme je le fais dans le corrigé était légitime.
{% endinfo %}

## Misc

Quelques remarques sur des erreurs ou lourdeurs que j'ai vu chez certains. Essayez d'y faire attention pour vos prochains codes et rendus.

### Nom des fichiers

Il vous faut a priori 2 fichiers :

- un pour le code, que vous pouvez appeler `pendu.py`{.fichier}, ou `code.py`{.fichier}
- un pour tester le code qui s'appelle comme le nom du fichier de code précédé de `test_`{.fichier}. Donc `test_pendu.py`{.fichier} ou `test_code.py`{.fichier} selon le nom de votre fichier de code.

### Description d'une fonction

La description d'une fonction (entre `"""`{.language-}) est inutile. Le code **doit** se suffire à lui-même pour être lisible et compris. Si ce n'est pas le cas, c'est que vous avez mal codé !

La description de chaque fonction n'est utile que si vous faire une bibliothèque (une suite de fonctions qui devront être utilisées par d'autres sans qu'ils aient à connaître leurs codes). Ici, vous faite du code qui sera exécuté ou utilisé par vous et les autres membres de l'équipe de développement (ou le correcteur, ici moi) : la description ou les commentaires **doivent** être inutiles : faites du code lisible.

### Listes

On préférera toujours utiliser `L.append(i)`{.language-} plutôt que `L = L + [i]`{.language-} car `append`{.language-} est une méthode en $\mathcal{O}(1)$ opérations alors `+` crée une nouvelle liste et est donc en $\mathcal{O}(n)$ où $n$ est la taille de la liste `L`{.language-}.

### Comparaison de booléens

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

### Import

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

### Variable différent d'une chaîne de caractère

Ne confondez pas la variable ou le paramètre d'une fonction `x`{.language-} avec une chaîne de caractères contenant le caractère x, notée `'x'`{.language-}.
