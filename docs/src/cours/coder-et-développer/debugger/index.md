---
layout: layout/post.njk

title: Déboguer son code

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

{% lien %}

- <https://www.youtube.com/watch?v=7qZBwhSlfOo>
- <https://www.youtube.com/watch?v=KEdq7gC_RTA&list=PLQzZ4krxwT9Yay3kz8ly4wXiYJHzMtsWi>

{% endlien %}

Le ***débogueur*** (debugger***) est un moyen d'exécuter le code ligne à ligne et de pouvoir visualiser et modifier l'état interne de l'interpréteur. Ceci permet de très rapidement corriger un programme.

{% faire %}
Créez un projet vscode que vous nommerez `deboguage`{.fichier}.
{% endfaire %}


## Breakpoint et exécution pas à pas


{% faire %}
Créez un fichier `boucle.py`{.fichier} où vous copiez/collerez le code ci-après
{% endfaire %}

```python
x = 4
for i in range(10):
    print(i)
    if x == i:
        print("égalité !")

print("c'est fini.")


```

Pour créer [un point d'arrêt (breakpoint)](https://code.visualstudio.com/docs/editor/debugging#_breakpoints) :

- `exécuter > activer/desactiver le point d'arrêt`
- cliquer sur la gouttière 
- appuyer sur la touche `<F9>`



> TBD
>
> - montrer l'exécution de l'interpréteur, une ligne à près l'autre, puis exécution des fonctions.
> - montrer les variables
> - utiliser les watch à la place des prints
> - modifier l'appel
> - breakpoint conditionnel (nombre de passages dans une boucle, valeur d'une variable, etc)

## Fonctions et step into

```python
def test_égalité(i, x):
    print(i)
    if x == i:
        print("égalité !")


x = 4
for i in range(10):
    print(i)
    test_égalité(i, x)

print("c'est fini.")

```

> TBD
>
> - step_into ne marche qu'avec nos fonctions, pas ceux de python (on ne connaît pas le code de print par exemple.)

## Pile d'apels

```python
def factorielle(n):
    if n <= 1:
        return n
    else:
        return n * factorielle(n - 1)


print(factorielle(10))

```

> TBD
>
> - montrer les appels successifs aux fonctions : stacks
> - faire une fonction récursive pour montrer les appels.

## Exercice

```python
def élague(x, crible):
    y = 2 * x
    while y < len(crible):
        crible[y] = False
        y += x


def nouveau_max_premier(ancien_max, crible):
    nouveau_max = ancien_max
    while not crible[nouveau_max]:
        nouveau_max -= 1

    return nouveau_max


def nouveau_min_premier(ancien_min, crible):
    nouveau_min = ancien_min
    while not crible[nouveau_min]:
        nouveau_min += 1

    return nouveau_min


n = 1000


crible = [True] * (n + 1)
crible[0] = False
crible[1] = False

x = 2
max_premier = len(crible) - 1

while x ** 2 < max_premier:
    élague(x, crible)
    max_premier = nouveau_max_premier(max_premier, crible)

    if x < max_premier:
        x = nouveau_min_premier(x + 1, crible)


premiers = [i for i in range(len(crible)) if crible[i]]

print("Les nombres premiers plus petits que", n, "sont :")
print(premiers)

```

> TBD : tout refaire faire.
>
> - montrer les variables et en modifier une
> - montrer l'exécution de l'interpréteur, une ligne à près l'autre, puis exécution des fonctions.
> - utiliser les watch à la place des prints
> - step_into ne marche qu'avec nos fonctions, pas ceux de python (on ne connaît pas le code de print par exemple.)
