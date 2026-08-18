---
layout: layout/post.njk

title: Exécuter des modules python

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Pour exécuter un module python on peut utiliser l'option `-m` de l'interpréteur python.

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

{% note %}
Cette technique est très utilisée pour permettre d'effectuer des commandes directement avec le terminal (comme `pip`{.language-}) ou pour montrer l'usage que l'on peut faire du module (comme `random`{.language-})
{% endnote %}

Mais pourquoi ces lignes ne s'affichent-elles pas lorsque l'on importe le module random ?

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
