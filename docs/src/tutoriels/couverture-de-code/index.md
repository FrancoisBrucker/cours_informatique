---
layout: layout/post.njk

title: "Couverture de code"
tags: ['tutoriel', 'python']
authors:
    - François Brucker

eleventyNavigation:
  key: "Couverture de code"
  parent: Tutoriels
---

<!-- début résumé -->

Couverture de code.

<!-- end résumé -->

Lorsque l'on développe un projet informatique, faire des tests est obligatoire : chaque fonction codée doit être testée.

Les tests nous permette d'avoir confiance dans la qualité du code. Mais il est parfois compliqué d'être sur que nos tests vérifient bien tous les cas possibles (passent bien par tous les blocs `si/alors/sinon`{.language-} du code par exemple).

Un outil pour vérifier cela est la [couverture de code](https://fr.wikipedia.org/wiki/Couverture_de_code). On exécute les tests et on regarde, fichier par fichier quelles sont les lignes qui ont été vues pour ces tests.

{% faire %}

Installez l'outils de couverture de code en suivant le [tutoriel d'installation de *code coverage*]({{ "/tutoriels/vsc-python-modules-supplémentaires/code-coverage" | url }}).

{% endfaire %}

{% note %}
Dans vos futurs projets, faites en sorte d'avoir toujours 100% de couverture de code.
{% endnote %}

## Fichiers exemple

Pour les besoin de cet exemple, prenons [les 2 fichiers]({{ '/cours/algorithme-code-théorie/code/programmation-objet/classes-et-objets' | url}}#code-final) du cours sur les classes et les objets.

## Utilisation directe

Le fonctionnement de la couverture de code est le suivant :

1. on exécute un fichier dans le terminal via le module coverage : `python -m coverage run main.py`
2. le rapport est visible avec la commande  `python -m coverage report`

Dns mon cas, dans un terminal, je commence par exécuter le programme via le module coverage :

```
» python -m coverage run main.py                       
6 Compteur(pas=3, valeur=6)
1 Compteur(pas=1, valeur=1)
False
```

Puis je visualise le rapport :

```
» python -m coverage report                              
Name                                                                 Stmts   Miss  Cover
----------------------------------------------------------------------------------------
/usr/local/lib/python3.9/site-packages/_distutils_hack/__init__.py      92     88     4%
compteur.py                                                             14      2    88%
main.py                                                                  9      0   100%
----------------------------------------------------------------------------------------
TOTAL                                                                  115     90    22%
```

On voit plusieurs choses :

* le module coverage utilise un fichier qui n'est pas dans notre projet : `/usr/local/lib/python3.9/site-packages/_distutils_hack/__init__.py`{.fichier}
* toutes les lignes du fichier `main.py`{.fichier} sont lues
* seules 88% des lignes du fichier `compteur.py`{.fichier} sont lues

Commençons par supprimer les fichier qui ne font pas parti de notre projet en utilisant le paramètre `--omit` qui permet de supprimer un fichier du rapport :

```
python -m coverage report --omit="**/_distutils_hack/**"
Name          Stmts   Miss  Cover
---------------------------------
compteur.py      14      2    88%
main.py           9      0   100%
---------------------------------
TOTAL            23      2    91%
```

{% info  %}
On a supprimé tous les fichiers dont le chemin contient `/_distutils_hack/`{.fichier} (on a mis les jokers `**` avant et après)
{% endinfo  %}

On peut maintenant voir les lignes qui ne sont pas exécutées dans `compteur.py` en utilisant le paramètre `--show-missing` :

```
» python -m coverage report --omit="**/_distutils_hack/**" --show-missing
Name          Stmts   Miss  Cover   Missing
-------------------------------------------
compteur.py      14      2    88%   13, 16
main.py           9      0   100%
-------------------------------------------
TOTAL            23      2    91%

```

Les lignes 13 et 16 ne sont pas exécutées. Elles correspondent aux corps des fonctions `__gt__`{.language-} et `__eq__`{.language-}.

{% faire %}

Vérifiez que vous avez la même chose pour votre projet.

{% endfaire %}

## Utilisation via `pytest`

L'exécution directe de coverage nous permet de voir s'il y a des fonction codées non utilisées. Il est souvent bien plus intéressant de voir quelles lignes du programme ne sont pas utilisées dans les tests.

Pour voir ce fonctionnement, commençons par ajouter un fichier de test à notre projet.

Fichier `test_compteur.py`{.fichier} :

```python
from compteur import Compteur


def test_lt():
    Compteur(valeur=3) < Compteur(valeur=4)

```

Exécutons les tests en même temps que coverage avec le l'extension `pytest-cov` que nous venons d'installer :

1. on exécute les tests dans le terminal en ajoutant l'extension coverage  `python -m pytest --cov=.`
2. le résultat est donné dans le terminal.

J'obtiens :

```
» python -m pytest --cov=.                                                                                        1 ↵
===================================== test session starts =====================================
platform darwin -- Python 3.9.13, pytest-6.2.5, py-1.10.0, pluggy-1.0.0
rootdir: /Users/fbrucker/Documents/sous_git/cours_informatique/docs/src/tutoriels/couverture-de-code/code
plugins: dash-1.19.0, cov-4.0.0
collected 1 item                                                                                                                                                             

test_compteur.py .                                                                          [100%]

---------- coverage: platform darwin, python 3.9.13-final-0 ----------
Name               Stmts   Miss  Cover
--------------------------------------
compteur.py           14      4    69%
main.py                9      9     0%
test_compteur.py       3      0   100%
--------------------------------------
TOTAL                 26     14    50%

====================================== 1 passed in 0.04s ======================================
```

{% faire %}

Vérifiez que vous avez la même chose pour votre projet.

{% endfaire %}

On voit que l'exécution des tests a eu besoin d'utiliser 100% du fichier `test_compteur.py`{.fichier} (ce qui est normal) mais seulement 69% du fichier `compteur.py`{.fichier}. Le fichier `main.py`{.fichier} n'a quant à lui pas été utilisé du tout (aucune des 9 lignes non vides n'a été vue), ce qui est normal.

Cinq lignes de `compteur.py` n'ont pas été vues. Pour savoir exactement les quelles, la commande `python -m pytest --cov=. --cov-report term-missing` donne :

```
» python -m pytest --cov=.  --cov-report term-missing                                                           130 ↵

===================================== test session starts =====================================
platform darwin -- Python 3.9.13, pytest-6.2.5, py-1.10.0, pluggy-1.0.0
rootdir: /Users/fbrucker/Documents/sous_git/cours_informatique/docs/src/tutoriels/couverture-de-code/code
plugins: dash-1.19.0, cov-4.0.0
collected 1 item                                                                                                                                                             

test_compteur.py .                                                                       [100%]

---------- coverage: platform darwin, python 3.9.13-final-0 ----------
Name               Stmts   Miss  Cover   Missing
------------------------------------------------
compteur.py           14      4    71%   7, 13, 16, 19
main.py                9      9     0%   1-12
test_compteur.py       3      0   100%
------------------------------------------------
TOTAL                 26     13    50%


====================================== 1 passed in 0.05s ======================================
```

{% faire %}
Analysez le résultat précédents. Quelles sont les lignes non *vues* par les tests ?
{% endfaire %}
{% details "corrigé" %}
C'est le des fonctions qui n'est pas exécuté. Lors de l'import de Compteur, python lis le fichier, en particulier les définitions de fonctions (qui sont donc lues) mais il ne les exécutent pas.
{% enddetails %}
