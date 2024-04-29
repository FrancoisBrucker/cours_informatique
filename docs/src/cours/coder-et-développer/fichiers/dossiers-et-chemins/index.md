---
layout: layout/post.njk 
title: "Dossiers et chemins"

eleventyNavigation:
    order: 3

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Comment trouver efficacement un fichier dans le système de fichier de l'ordinateur.

Par défaut python va chercher les fichiers à ouvrir dans le dossier du fichier python en train d'être exécuté. On peut facilement chercher un fichier dans un dossier spécifique en python.

Commencez par intégrer la règle d'or :

{% note %}
On ne présuppose jamais de l'endroit où un fichier est stocké sur un ordinateur.
{% endnote %}

Supposons  que vous ayez un fichier python dans le dossier `/Users/fbrucker/Documents/mon_projet/main.py`{.fichier} et que ce programme python utilise le fichier `/Users/fbrucker/Documents/mon_projet/donnees.txt`{.fichier}.

Si votre programme `main.py`{.fichier} utilise le fichier `donnees.txt`{.fichier} de cette façon :

```python
donnees = open("/Users/fbrucker/Documents/mon_projet/donnees.txt").read()
```

Il ne pourra fonctionner **que** sur votre ordinateur ! En effet, si vous copiez le dossier *"mon_projet"*  et tout son contenu  de l'ordinateur A à l'ordinateur B, il est très peu probable qu'il soit placé au même endroit sur le disque dur.

Une première solution est d'utiliser un chemin relatif :

```python
donnees = open("donnees.txt").read()
```

On voit que le chemin utilisé est *relatif* car il ne commence pas par un `/`{.fichier}. On cherche le fichier `donnees.txt`{.fichier} par rapport au dossier courant du terminal qui a exécuté le fichier python. De là, si vous êtes dans le dossier *"mon_projet"* lorsque vous tapez la commande `python main.py` votre programme marchera sur tous les ordinateurs.

Si cette technique fonctionne souvent, elle n'est cependant pas optimale car vous ne pouvez pas garantir que votre programme sera **toujours** exécuté depuis le dossier `mon_projet/`{.fichier}. S'il est par exemple exécuté depuis le parent de `mon_projet/`{.fichier} : `python mon_projet/main.py` ; votre code ne fonctionnera plus puisque le dossier par défaut ne sera plus le bon...

La solution qui fonctionne tout le temps est de déterminer à l'exécution l'emplacement du fichier*"main.py"*. Ceci se fait grâce à la variable spéciale : `__file__`{.language-}.

{% faire %}
Copiez le code suivant dans un fichier et exécutez le pour voir le fonctionnement de la variable `__file__`{.language-} :

```python
print(__file__)
```

{% endfaire %}

On n'a fait que la moitié du chemin, puisque l'on a l'emplacement du fichier, mais pas le dossier. Ceci peut se faire en utilisant le module [`os.path` de python](https://docs.python.org/fr/3/library/os.path.html) :

{% faire %}
Copiez le code suivant dans un fichier et exécutez le pour voir comment récupérer le dossier à partir de `__file__`{.language-} :

```python
import os

print(__file__) # le chemin absolu jusqu'au fichier
print(os.path.dirname(__file__))  # le dossier
print(os.path.basename(__file__)) # le nom du fichier                                     
```

{% endfaire %}

Cette méthode permet d'obtenir un chemin absolu de référence pour garantir l'accès aux fichiers de données sur toutes les machines où votre projet sera copié.

Un fois un dossier de référence trouvé, on pourra l'utiliser pour accéder à nos données. Mais **jamais** à la main :

{% note %}
Lorsque l'on manipule des fichiers ou que l'on combine des dossiers on utilise **toujours** une bibliothèque dédiée pour cela, on ne manipule **jamais** les noms de fichiers et de dossiers en utilisant des méthodes de chaînes de caractères
{% endnote %}

On va voir deux façons de faire en python, l'une classique avec le module [os.path](https://docs.python.org/fr/3/library/os.path.html), l'autre plus moderne qui utilise le module [pathlib](https://docs.python.org/fr/3/library/pathlib.html).

## Module `os.path`{.language-}

On suppose que la variable `__file__`{.language-} corresponde au chemin `/Users/fbrucker/Documents/mon_projet/main.py`{.fichier} sur le disque dur. On suppose aussi que le module `os`{.language-} a été importé.

* rendre le dossier où est `__file__`{.language-} avec [dirname](https://docs.python.org/fr/3/library/os.path.html#os.path.dirname) : `dossier = os.path.dirname(__file__)`{.language-}.
* rendre le nom du fichier pointé par `__file__`{.language-} avec [basename](https://docs.python.org/fr/3/library/os.path.html#os.path.basename) : `nom_fichier = os.path.basename(__file__)`{.language-}
* concaténer deux chemins avec [join](https://docs.python.org/fr/3/library/os.path.html#os.path.join) : `os.path.join("/Users/fbrucker", "Documents/mon_projet")`{.language-} rendra : `/Users/fbrucker/Documents/mon_projet`{.fichier}
* rendre le dossier parent : `os.path.join(dossier, "..")`{.language-}.
* rendre le chemin absolu à partir d'un chemin relatif : `os.path.abspath(".")`{.language-}

## Module `pathlib`{.language-}

Le module [pathlib](https://docs.python.org/fr/3/library/pathlib.html) permet d'avoir une approche objet de la manipulation des fichiers.

{% lien %}
[Ce tutoriel](https://jefftriplett.com/2017/pathlib-is-wonderful/) est parfait pour vous montrer comment l'utiliser.

{% endlien %}

## <span id="fichiers-distants"></span>Fichiers distants

{% lien %}
[Module requests](https://requests.readthedocs.io/en/latest/)
{% endlien %}

Les fichiers stockés sur internet peuvent aussi être récupérés en python *via* leur [url](https://fr.wikipedia.org/wiki/Uniform_Resource_Locator). On utilise la bibliothèque [requests](https://requests-fr.readthedocs.io/en/latest/) (`python -m pip install requests`).

Par exemple, le site <https://www.gutenberg.org> possède de nombreux livres au format utf-8 à télécharger. Par exemple <https://www.gutenberg.org/ebooks/14155> :

```python
import requests

page = requests.get("https://www.gutenberg.org/ebooks/14155.txt.utf-8")
```

Le code précédent à téléchargé le fichier contenu dans l'url <https://www.gutenberg.org/ebooks/14155.txt.utf-8> dans la variable page.

Cette variable est un objet qui contient de [nombreux attributs](https://requests.readthedocs.io/en/latest/api/#requests.Response).

Le [texte](https://requests.readthedocs.io/en/latest/api/#requests.Response.text) qui a été téléchargé, au format Unicode :

```python
page.text
```

Un fichier téléchargé par internet l'a été octet par octet. Le type par défaut est donc le `bytes`{.language-} et le contenu brut est disponible avec l'attribut [content](https://requests.readthedocs.io/en/latest/api/#requests.Response.content) :

```python
type(page.content)
```

La bibliothèque fait une conversion pour rendre l'attribut text au format Unicode.

{% attention %}
La fonction `requests.get`{.language-} va chercher le fichier sur internet. Donc utilisez cette fonction avec parcimonie car les accès réseau sont toujours lents par rapport aux fichiers sur le disque dur en local.
{% endattention %}

L'idéal esr de télécharger le fichier une fois, de le sauver sur votre disque dur puis d'utiliser ensuite tout le temps le fichier sauvegardé. Le code suivant regarde si un fichier donné existe (fonction [`os.path.exists`{.language-}](https://docs.python.org/fr/3/library/os.path.html#os.path.exists)), et sinon il le télécharge :

```python
import os.path

import requests

if not os.path.exists("mon_fichier.py"):
    page = requests.get("https://www.gutenberg.org/ebooks/14155.txt.utf-8")
    f = open("mon_fichier.py", "w", encoding="utf-8")
    f.write(page.text)
    f.close()
```
