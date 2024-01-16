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

Le ***débogueur*** (***debugger***) est un moyen d'exécuter le code ligne à ligne et de pouvoir visualiser et modifier l'état interne de l'interpréteur. Ceci permet de très rapidement corriger un programme.

{% faire %}
Créez un dossier que vous nommerez `debugger`{.fichier} et ouvrez le en tant que projet dans vscode.
{% endfaire %}

L'idée est de remplacer les divers `print`{.language-} utilisés pour visualiser un problème par une exécution contrôlée du code et de pouvoir stopper son exécution à des endroit prédéterminés appelés breakpoint.

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

### Exécution du debugger

On peut exécuter le programme via le debugger de plusieurs façons :

- `menu exécuter > démarrer le débogage`
- choisir le menu exécuter (`menu affichage > exécuter`) puis cliquer sur exécuter et déboguer.

{% note %}
À la première utilisation, il vous sera demandé de choisir une configuration de débogage , choisissez : `Fichier python Déboguer le fichier Python actuellement actif`

{% endnote %}
{% info %}
Vous pouvez refaire votre choix en allant dans le `menu Exécuter` puis en choisissant soit `Ouvrir les configurations` soit `Afficher les configurations`.
{% endinfo %}

![fenêtre de débogage](./fenêtre_débogage.png)

{% faire %}

1. Allez dans le menu exécuter : `menu affichage > exécuter`
2. cliquez sur le bouton bleu `Exécuter et déboguer`

{% endfaire %}
{% info %}
Si vous n'avez pas de bouton bleu c'est peut-être que vous avez ajouté des configurations de débogage à l'insu de votre plein gré. POur les supprimer, supprimez le dossier `.vscode`{.fichier} qui a du apparaître dans votre projet (clique droit dessus puis choisissez supprimer).
{% endinfo %}

Une fois le programme lancé il a du s'exécuter et afficher dans le terminal :

```text
0
1
2
3
4
égalité !
5
6
7
8
9
c'est fini.
```

Il ne s'est rien passé de plus que si vous aviez exécuté votre programme python normalement.

C'est normal par il faut demander explicitement au débogueur de s'arrêter un créant un [***point d'arrêt***](https://fr.wikipedia.org/wiki/Point_d'arr%C3%AAt_(informatique)) (***breakpoint***).

### Création d'un breakpoint

Pour créer [un point d'arrêt (breakpoint)](https://code.visualstudio.com/docs/editor/debugging#_breakpoints) :

- `menu exécuter > activer/desactiver le point d'arrêt`
- cliquer sur la gouttière du fichier, à gauche des numéros de lignes (vous savez que vous êtes au on endroit lorsque un disque rouge foncé apparaît)
- appuyer sur la touche `<F9>`

Une fois le breakpoint placé, un point rouge doit apparaître dans la gouttière du fichier :

![breakpoint placement](./breakpoint-placement.png)

{% faire %}

{% endfaire %}

> TBD reéxécution 

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

## Autres trucs

> TBD : points d'arrêt conditionnels
