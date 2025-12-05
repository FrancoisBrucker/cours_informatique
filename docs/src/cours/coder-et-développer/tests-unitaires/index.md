---
layout: layout/post.njk
title: "Tests Unitaires"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Les tests permettent de vérifier que notre code fonctionne. Ils font partie du programme et on peut s'y référer quand on veut. Lorsque l'on modifie le code, on pourra toujours exécuter **tous les tests** pour vérifier que notre programme fonctionne aussi bien qu'avant. Les tests font partie intégrante du projet : ils garantissent que votre programme fonctionne **maintenant**, et pas seulement au moment où vous avez écrit vos tests.

On y reviendra à de nombreuses reprises :

{% attention "**À retenir**" %}
Les tests sont la pierre angulaire d'une bonne programmation : ils garantissent le fonctionnement de votre code et qu'[il ne peut pas régresser](https://blog.octo.com/via-negativa-tdd-et-la-conception-de-logiciel/).
{% endattention %}

Les tests sont de petites fonctions dont le but est de _tester_ une fonctionnalité du programme (souvent le résultat de l'exécution d'une fonction). Le test consiste en [une assertion](https://fr.wikipedia.org/wiki/Assertion) que l'on veut être vraie si que le code fonctionne. Si l'assertion est fausse c'est qu'il y a un bug.

On va créer un projet pour comprendre comment tout ça fonctionne.

Nous allons préparer le projet dans lequel nous allons coder. Ceci se fait avec vscode en ouvrant un dossier. Ce dossier sera le départ de votre projet et s'appelle _workspace_.

{% faire %}

1. Commencez par créer le dossier `hello-test`{.fichier} dans un explorateur de fichier
2. dans vscode, choisissez : "_fichier > ouvrir le dossier..._" puis naviguez jusqu'à votre dossier `hello-test`{.fichier}. On vous demande si vous faites confiances aux auteurs, puisque c'est vous dites oui.
3. créez un fichier `main.py`{.fichier} contenant uniquement la ligne `print("bonjour")`{.language-}

Exécutez le fichier main avec vscode et le terminal pour vérifier que tout fonctionne.
{% endfaire %}

## La commande assert

On utilise en python [la commande assert](https://docs.python.org/fr/3/reference/simple_stmts.html#the-assert-statement) pour vérifier que quelque chose est correct. Elle fonctionne ainsi :

```python
assert <expression logique>
```

Si l'expression logique est vraie, le programme continue sans rien dire et si l'expression logique est fausse, le programme s'arrête avec l'erreur : `AssertionError`{.language-}.

Essayons ça avec la plus simple des expressions logiques : `True`{.language-}.

{% faire %}

1. allez dans _menu Fichier > Nouveau Fichier_
2. et sauvez le de suite : _menu Fichier > Enregistrer_ avec le nom `test_projet.py`{.fichier}
3. écrivez-y le code suivant :

    ```python
    print("avant l'assert")

    assert True

    print("après l'assert")

    ```

4. Exécutez-le.

{% endfaire %}

Lorsque vous exécutez ce fichier, vous devez obtenir le résultat suivant :

```text
avant l'assert
après l'assert
```

La condition logique étant vraie, la commande `assert`{.language-} n'a rien fait.

Changeons ça en mettant une condition logique fausse :

{% faire %}
Modifiez `test_projet.py`{.fichier} pour qu'il contienne le code :

```python
print("avant l'assert")

assert False

print("après l'assert")

```

Exécutez le fichier `test_projet.py`{.fichier}.

{% endfaire %}

Vous devez obtenir le résultat suivant :

```text
avant l'assert
Traceback (most recent call last):
  File "/Users/fbrucker/Documents/temp/hello-dev/test_projet.py", line 3, in <module>
    assert False
AssertionError
```

La première ligne a bien été exécutée (on voit écrit `avant l'assert`), puis le programme a planté. La condition logique étant fausse, la commande `assert`{.language-} a levé une exception nommée `AssertionError`{.language-} qui a stoppé l'exécution du programme. La ligne `print("après l'assert")`{.language-} n'a pas été exécutée.

D'habitude, nos expressions logiques vérifie qu'un comportement observé (l'exécution d'une fonction) est conforme au comportement théorique (le résultat qu'on aimerait avoir). Pour ne pas se perdre on range ce test dans une fonction dont le nom décrit le test. Par exemple, testons la somme :

{% faire %}
Modifiez `test_projet.py`{.fichier} pour qu'il contienne le code :

```python
#  Définitions des tests


def test_somme_neutre():
    tête_a_toto = 0
    assert 0 + 0 == tête_a_toto


def test_somme_1_plus_0():
    assert 0 + 1 == 1


def test_somme_1_plus_2():
    assert 1 + 2 == 3


#  Exécution des tests

test_somme_neutre()
test_somme_1_plus_0()
test_somme_1_plus_2()
```

Exécutez le fichier `test_projet.py`{.fichier}.

{% endfaire %}

Pour tester la somme, j'ai décidé de faire 3 tests :

- le cas le plus simple où il ne se passe rien (`0 + 0 = 0`{.language-})
- un cas simple (`0 + 1 = 1`{.language-})
- un cas général (`1 + 2 = 3`{.language-})

Lorsque l'on exécute ce code, il ne se passe rien : les fonctions se sont exécutées sans erreurs

{% faire %}
Modifiez la fonction `test_somme_neutre`{.language-} du fichier `test_projet.py`{.fichier} pour qu'elle soit égale à :

```python
# ...

def test_somme_neutre():
    tête_a_toto = 0
    assert 0 + 0 == 42

# ...
```

Exécutez le fichier `test_projet.py`{.fichier}.

{% endfaire %}
{% info %}
On a coutume de mettre des `# ...`{.language-} pour dire que le reste du code du fichier n’est pas changé.

Ce n’est pas la peine de les copier/coller.
{% endinfo %}

Le code ne fonctionne plus et stope avec le message :

```shell
❯ python ./test_projet.py
Traceback (most recent call last):
  File "./test_projet.py", line 25, in <module>
    test_somme_neutre()
    ~~~~~~~~~~~~~~~~~^^
  File "./test_projet.py", line 12, in test_somme_neutre
    assert 0 + 0 == 42
           ^^^^^^^^^^^
AssertionError

```

On voit que :

1. l'exécution de la fonction `test_somme_neutre()`{.language-} a causé une erreur
2. l'assertion `assert 0 + 0 == 42`{.language} a provoqué une erreur.

Si l'on corrige notre test (en remettant `assert 0 + 0 == tête_a_toto`{.language-}) et que conserve ce fichier. On pourra l'exécuter régulièrement pour vérifier que la somme fonctionne toujours !

Ce n'est cependant pour l'instant pas très pratique :

1. si tout se passe bien on a pas de retour
2. il faut explicitement exécuter les fonctions de tests (on peut en oublier et rien ne nous l'indiquera)
3. si un test rate, les autres tests ne seront pas exécutés.

Pour pallier ces inconvénients on utilise une bibliothèque de test spécialisée : [Pytest](https://docs.pytest.org).

### Installation de la bibliothèque de tests

{% lien %}
[tests avec vscode](https://code.visualstudio.com/docs/python/testing)
{% endlien %}

### <span id="installation-pytest"></span> Installation

```shell
python -m pip install pytest
```

### <span id="configuration-pytest"></span> Configuration

1. dans les préférences (_menu file/code > Préférences > settings_) tapez `python.testing.pytestEnabled` dans la barre de recherche et cochez la case. Ceci dit à vscode que notre framework de test est pytest (il y en a d'autres possible comme [unittest](https://docs.python.org/fr/3.9/library/unittest.html) ou encore [nosetests](https://nose.readthedocs.io/en/latest/), mais on ne va pas les utiliser. Assurez vous cependant qu'un seul framework de test soit utilisé à la fois. Ca devrait être le cas si vous n'avez pas cliqué un peu partout).
2. on configure les tests de notre projet en tapant la commande (dans la [palette de commande](../vsc-installation-et-prise-en-main#palette-de-commande){.interne}) : _python : Configure tests_ on choisit _pytest_ puis _. (root)_ qui donne le dossier de départ où aller chercher nos tests

### <span id="utilisation-pytest"></span> Utilisation

{% faire %}
Supprimez la partie exécution des fonctions de tests dans le fichier `test_projet.py`{.fichier}, pytest le fera pour nous. Votre fichier doit maintenant uniquement contenir le code suivant :

```python
def test_somme_neutre():
    tête_a_toto = 0
    assert 0 + 0 == tête_a_toto


def test_somme_1_plus_0():
    assert 0 + 1 == 1


def test_somme_1_plus_2():
    assert 1 + 2 == 3
```

{% endfaire %}

Si vous l'exécutez, il ne va rien se passer, même si vous remettez une erreur dans l'assertion :

{% faire %}
Testez le !
{% endfaire %}

Ceci est normal puisque le code ne fait que **définir** des fonctions sans jamais les exécuter. Il faut l'utiliser via la bibliothèque `pytest` que vous venez d'installer. Ceci peut se faire directement avec vscode en ouvrant la fenêtre de tests avec _Menu Affichage testing_ (le petit erlenmeyer de la [barre d'activité](https://code.visualstudio.com/docs/getstarted/userinterface)).

En suite le menu _TESTING_ en haut de cette nouvelle fenêtre vous permet :

- redécouvrir les tests
- exécutez les tests.
- ...

![tests](python-pytest-env.png)

On peut également directement utiliser pytest avec le terminal en tapant `python -m pytest` alors que vous êtes dans le dossier du projet. C'est la façon conseillée de faire car cette méthode fonctionne toujours et est plus informative que l'exécution via vscode.

{% faire %}
Testez l'exécution des tests avec le terminal
{% endfaire %}

{% attention "**À retenir**" %}
pytest exécute toutes les fonctions commençant par `test_`{.fichier} de tous les fichiers commençant par `test_`{.fichier} du projet.
{% endattention %}
{% faire %}
Ajoutez une fonction ne commençant pas par `test_`{.fichier} et exécutez les tests " elle ne sera pas exécutée.
{% endfaire %}

### Utilisation de la bibliothèque de tests

{% faire %}
Tapez la commande `python -m pytest` dans un terminal.
{% endfaire %}

Vous devriez obtenir quelque chose du genre :

![vsc-pytest](code-projet-pytest.png)

{% faire %}
Corrigez le test de `test_projet.py`{.fichier} qui rate et re-exécutez le code pour voir les 3 tests réussir.

{% endfaire %}

Que fait pytest :

{% note %}
Pytest exécute toutes les fonctions commençant par `test_`{.fichier} de tous les fichiers commençant par `test_`{.fichier} d’un projet.
{% endnote %}

On peut aussi exécuter les tests directement avec vscode. Pour cela, cliquez sur [le petit erlenmeyer](https://code.visualstudio.com/docs/python/testing#_configure-tests). Vous pourrez ensuite :

1. découvrir les tests du projet
2. exécuter tous les tests
3. n'exécuter qu'un seul test

![vsc-pytest-erlenmeyer](code-projet-pytest-erlenmeyer.png)

### Test du projet

Faisons de vrais tests maintenant.

{% faire %}
Créez un fichier `le_code.py`{.fichier} et placez-y le code :

```python
def bonjour(nom):
    return "bonjour " + nom + " !"

```

{% endfaire %}

On peut maintenant remplacer les tests :

{% faire %}
Modifiez le fichier `test_projet.py`{.fichier} pour qu'il contienne le code :

```python
from le_code import bonjour


def test_bonjour():
    assert bonjour("monde") == "bonjour monde !"
```

Exécutez les tests pour vérifier que votre code fonctionne.

{% endfaire %}

Maintenant que les tests passent, on peut modifier le programme principal.

{% faire %}
Modifiez le fichier `main.py`{.fichier} pour qu'il contienne le code :

```python
from le_code import bonjour

print(bonjour("monde"))

```

Exécutez le programme principal.

{% endfaire %}

Félicitations, vous avez fait votre premier projet fonctionnel !
