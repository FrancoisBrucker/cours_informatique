---
layout: layout/post.njk

title: Modules python

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Un module python est en réalité un fichier qui est lu lorsqu'il est importé.

Par exemple, le code suivant cherche un fichier `random.py`{.fichier} qu'il exécute dans son espace de nommage :

```python
import random
```

Il est tout à fait possible, et on va le faire souvent par la suite de créer ses propres modules.

{% lien %}
[Documentation python sur les modules](https://docs.python.org/fr/3/tutorial/modules.html)
{% endlien %}

## Mécanisme d'importation de modules

Lorsque l'interpréteur python exécute une instruction d'import comme :

```python
import mon_module
```

Il procède en deux temps :

1. il cherche dans le dossier courant s'il existe un fichier nommé `mon_module.py`{.fichier}. Si ce fichier n'existe pas il passe à l'étape 2, sinon il passe à l'étape 4.
2. il cherche dans ses dossiers à lui s'il existe un fichier nommé `mon_module.py`{.fichier}. Si ce fichier n'existe pas il passe à l'étape 3.
3. il produit une erreur d'importation : `ModuleNotFoundError: No module named 'mon_module'`{.language-}
4. il exécute le fichier `mon_module.py`{.fichier} dans un nouvel espace de nommage créé pour l'occasion.

Supposons que l'on ait dans le même dossier les fichiers  `programme_principal.py`{.fichier} et `mon_module.py`{.fichier} et tels que :

- `programme_principal.py`{.fichier} vale :

    ```python/
    import mon_module

    print(mon_module.MA_CONSTANTE)
    ```

- `mon_module.py`{.fichier} vale :

    ```python/
    MA_CONSTANTE = 42
    va_variable = None
    ```

À la fin de l'exécution de la ligne 1 du fichier `programme_principal.py`{.fichier}, on a les différents espaces de noms suivant :

![import](import-1.png)

Le nom `mon_module`{.language-} correspond à un objet de type module, contenant un espace de nom. On peut accéder aux noms de son espace avec la notation pointée :

```python
mon_module.MA_CONSTANTE
```

On cherche le nom `MA_CONSTANTE`{.language-} dans l'espace de nom associé à l'objet de nom `mon_module`{.language-}.

Faite l'exercice ci-dessous pour vous convaincre que l'import exécute bien le fichier importé :

{% faire %}
Créez les deux fichiers `mon_module.py`{.fichier} et `programme_principal.py`{.fichier} et copiez/collez y leurs codes.

1. exécutez le fichier `programme_principal.py`{.fichier} pour voir s'afficher `42`{.language-}
2. Ajouter dans le fichier `mon_module.py`{.fichier} une ligne avec l'instruction `print("coucou de l'import")`{.language-} puis exécutez le fichier `programme_principal.py`{.fichier}.

Vous devriez voir s'afficher `"coucou de l'import"` à l'écran, ce qui prouve que chaque ligne du fichier `mon_module.py`{.fichier} est exécuté à l'import.
{% endfaire %}

## Exécution de modules

### Exécution d'un module comme un programme

On peut utiliser l'interpréteur python pour exécuter un module. Par exemple notre fichier `mon_module.py`{.fichier} précédent :

```shell
python mon_module.py
```

Il n'y a pas de différence fondamentale entre un programme et un module en python. C'est juste un programme dont on garde trace de son espace de noms `global`{.language-} après exécution.

### Exécution d'un module python

Pour exécuter un module python, il n'est pas nécessaire de connaître son emplacement, on peut utiliser l'option `-m` de l'interpréteur python.

{% lien %}
[Option `-m` de l'interpréteur Python](https://docs.python.org/fr/3/using/cmdline.html#cmdoption-m)
{% endlien %}

On l'a déjà fait à de multiples reprises en utilisant le module pip :

```shell
python -m pip
```

Le résultat de la commande précédente dans le terminal affichera l'aide de `pip`{.fichier}.

{% faire %}
Exécutez le module `random`{.language-} de python dans le terminal avec la commande : `python -m random`.
{% endfaire %}

Si vous exécutez le module python `random`{.language-}, vous verrez s'afficher tout un tas de choses sur l'écran :

```shell
$ python -m random

0.000 sec, 10000 times random()
avg 0.498948, stddev 0.285393, min 1.74181e-05, max 0.999923

0.003 sec, 10000 times normalvariate(0.0, 1.0)
avg -0.00160272, stddev 1.00174, min -3.42565, max 3.90493

0.003 sec, 10000 times lognormvariate(0.0, 1.0)
avg 1.64736, stddev 2.19193, min 0.0147119, max 65.9514

0.004 sec, 10000 times vonmisesvariate(0.0, 1.0)
avg 3.11325, stddev 2.28549, min 0.000433248, max 6.28223

0.009 sec, 10000 times binomialvariate(15, 0.6)
avg 8.9936, stddev 1.89413, min 2, max 15

[...]
```

Ces lignes montrent le temps mis pour générer des nombres aléatoires selon plusieurs lois de probabilités.

Mais pourquoi ces lignes ne s'affichent-elles pas lorsque l'on importe le module random ?

### Variable `__name__`{.language-}

{% lien %}
[`__name__`{.language-} et `__main__`{.language-} en python](https://docs.python.org/fr/3.12/library/__main__.html)
{% endlien %}

Python distingue les deux types d'exécutions d'un programme via la variable spéciale `__name__`{.language-} :

- elle vaut la chaîne de caractères `"__main__"`{.language-} si le fichier est exécuté directement
- elle vaut le nom du fichier s'il est exécuté via un import

{% faire %}
Créez un fichier nommé `test_exécution.py`{.fichier} et copiez/collez y le code suivant :

```python
print(__name__)
```

Exécutez le fichier précédant directement avec l'interpréteur puis via un import. Vous pourrez créez puis exécuter un fichier contenant uniquement la ligne de code `import test_exécution`{.language-}.
{% endfaire %}

Cette différence dans le nom d'une variable permet de différentier les deux types d'exécution et est parfois utilisé pour séparer le programme principal d'un fichier du reste du code avec :

```python
# code pouvant être importé

if __name__ == "__main__":
    # code du programme principal
```

## Où sont les modules ?

Les dossiers où python va cherchez les modules sont listés dans la variable `sys.path` et dépendent de l'interpréteur utilisé :

{% attention %}
Il faut installer les modules en utilisant `python -m pip` et non directement le programme `pip`, car l'interpréteur pour lequel sera installé le module est ainsi explicite.
{% endattention %}

vous pouvez le voir en exécutant le code :

```python
import sys
for dossier in sys.path:
   print(dossier)
```

Chez moi, sur un mac où python est installé avec [brew](https://brew.sh/) ce programme rend :

```shell
/opt/homebrew/Cellar/python@3.11/3.11.5/Frameworks/Python.framework/Versions/3.11/lib/python311.zip
/opt/homebrew/Cellar/python@3.11/3.11.5/Frameworks/Python.framework/Versions/3.11/lib/python3.11
/opt/homebrew/Cellar/python@3.11/3.11.5/Frameworks/Python.framework/Versions/3.11/lib/python3.11/lib-dynload
/Users/fbrucker/Library/Python/3.11/lib/python/site-packages
/opt/homebrew/lib/python3.11/site-packages
/opt/homebrew/lib/python3.11/site-packages/gpg-1.22.0-py3.11-macosx-13-arm64.egg
/opt/homebrew/opt/python-tk@3.11/libexec
```

Il y a plusieurs dossiers :

- `/opt/homebrew/Cellar/python@3.11/3.11.5/Frameworks/Python.framework/Versions/3.11/lib/python3.11`{.fichier} contient les packages de bibliothèque standard (il contient par exemple un fichier _"random.py"_ qui contient le code du package `random`)
- `/opt/homebrew/Cellar/python@3.11/3.11.5/Frameworks/Python.framework/Versions/3.11/lib/python3.11/lib-dynload`{.fichier} contient les packages python qui ne sont pas écrit en python mais en C
- `/opt/homebrew/lib/python3.11/site-packages`{.fichier} qui contient les packages qui seront installés par pip.

{% attention %}
La gestion des packages peut être compliquée. Normalement, si vous vous y prenez comme indiqué ici et en utilisant votre ordinateur personnel, tout devrait bien se passer. Si cela commence à ne plus aller, vous pouvez essayer d'installer les packages à un autre en endroit en suivant [ce tuto](https://opensource.com/article/19/4/managing-python-packages), ou, comme on le fera plus tard en utilisant un environnement virtuel. Mais, dans le doute, consultez un prof qui s'y connaît.
{% endattention %}
