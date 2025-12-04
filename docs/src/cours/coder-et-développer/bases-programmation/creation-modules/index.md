---
layout: layout/post.njk

title: Modules python

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

[On l'a vu](../principes/modules/){.interne}, le code suivant importe un module :

```python
import random
```

En réalité, python cherche un fichier qui s'appelle `random.py`{.fichier} et l'exécute. La variables crées sont placés dans l'espace de nommage du module.

On peut tout à fait utiliser ce principe, et on va le faire souvent par la suite, pour créer ses propres modules.

{% lien %}
[Documentation python sur les modules](https://docs.python.org/fr/3/tutorial/modules.html)
{% endlien %}

L'endroit où l'interpréteur cherche les modules locaux dépend de l'endroit où il est exécuté. Nous rentrerons dans ces détails plus tard, mais pour l'instant on considère que vous avez suivi [les consignes du tutoriel vscode et python](../éditeur-vscode/python/) :

{% info %}

1. vous avez créé un projet avec vscode
2. que tous les fichiers que vous créez sont dans le dossier du projet
3. que vous exécutez le code en utilisant le triangle vert

Ces consignes précédentes assurent que **vous exécutez votre code python à partir du dossier contenant votre projet**.

{% endinfo %}

Préparons nos fichiers pour comprendre comment tout ça fonctionne :

{% faire %}

Créez un nouveau projet avec vscode dans le dossier `projet_module`{.fichier}. Dans ce projet, créez les deux fichiers `mon_module.py`{.fichier} et `mon_programme.py`{.fichier} tels que :

Fichier `mon_programme.py`{.fichier} :

```python/
import mon_module

print(mon_module.MA_CONSTANTE)
```

Fichier `mon_module.py`{.fichier} :

```python/
MA_CONSTANTE = 42
va_variable = None
```

{% endfaire %}

## Mécanisme d'importation de modules

{% faire %}
Exécutez le fichier `mon_programme.py`{.fichier}.
{% endfaire %}

Vous devriez voir s'afficher `42` dans le terminal de vscode. Examinons comment tout ça se passe. Lorsque l'interpréteur python exécute la première ligne du fichier :

```python/
import mon_module
```

Process d'import :

{% note %}

L'interpréteur procède en deux temps pour exécuter la ligne d'import :

```python
import mon_module
```

1. il cherche dans le dossier d'exécution s'il existe un fichier nommé `mon_module.py`{.fichier}. Si ce fichier n'existe pas il passe à l'étape 2, sinon il passe à l'étape 4.
2. il cherche dans ses dossiers à lui s'il existe un fichier nommé `mon_module.py`{.fichier}. Si ce fichier n'existe pas il passe à l'étape 3.
3. il produit une erreur d'importation : `ModuleNotFoundError: No module named 'mon_module'`{.language-}
4. il exécute le fichier `mon_module.py`{.fichier} dans un nouvel espace de nommage créé pour lui.

{% endnote %}

À la fin de la première instruction on est dans la situation suivante :

![import](import-1.png)

Le nom `mon_module`{.language-} correspond à un objet de type module, contenant un espace de nommage. On peut accéder aux noms de son espace avec la notation pointée :

```python
mon_module.MA_CONSTANTE
```

On cherche le nom `MA_CONSTANTE`{.language-} dans l'espace de nom associé à l'objet de nom `mon_module`{.language-}.

{% exercice %}
Créez un projet vscode et créez le fichier `main.py`{.fichier} suivant que vous exécuterez :

```python/
import math

print(math.pi)
```

Explicitez comment s'est exécuté le programme.
{% endexercice %}
{% details "corrigé" %}
Exactement comme pour le fichier `mon_programme.py`{.fichier}, sauf que l'interpréteur est passé à l'étape 2 et a trouvé un fichier nommé `math.py`{.fichier} dans ses propres fichiers qu'il a exécuté.
{% enddetails %}
{% exercice %}
Ajoutez au projet un fichier `math.py`{.fichier} vide et exécutez à nouveau le fichier `main.py`{.fichier}. Que doit-il se passer ?
{% endexercice %}
{% details "corrigé" %}
L'interpréteur trouve le fichier `math.py`{.fichier} dans le projet et l'a exécuté. Comme ce fichier ne contient pas de variable `pi`{.language-}, le programme plante avec le message d'erreur :

```python
AttributeError: module 'math' has no attribute 'pi'
```

{% enddetails %}

Vous pouvez vous convaincre que le fichier est bien exécuté en ajoutant la ligne suivant dans le fichier `mon_module.py`{.fichier} :

```python
print("coucou de l'import")
```

En exécutant le fichier `mon_programme.py`{.fichier}, vous devriez voir s'afficher `"coucou de l'import"` dans le terminal. C'est pour cette raison que :

{% note %}
Les fichiers utilisés comme modules ne doivent contenir que des déclarations de fonctions ou des variables. Ils ne doivent comporter aucun affichage ni interactions avec l'utilisateur (via des `input`{.language-} par exemple) pour ne pas gêner le processus d'import.
{% endnote %}
