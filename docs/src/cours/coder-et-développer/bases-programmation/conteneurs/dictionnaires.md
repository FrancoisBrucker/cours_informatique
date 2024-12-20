---
layout: layout/post.njk
title: Dictionnaires

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Les dictionnaires sont des structures de données très utiles si on sait les utiliser.

Un dictionnaire, aussi appelé [tableau associatif](https://fr.wikipedia.org/wiki/Tableau_associatif) associe une clé à une valeur. On peut voir les listes comme un tableau associatif où les clés sont des entiers allant de 0 à la longueur de la liste moins 1.

Mais cela peut être bien plus général que ça :

- les clés peuvent être de mots et les valeur un nombre. Cela permet par exemple de compter le nombre de fois où un chaque mot d'un texte apparaît.
- associer un nom (valeur) à un numéro de téléphone (clé) sans avoir besoin d'une liste allant de 0 à numéro max de téléphone.

{% info %}
Un ensemble peut être codé en utilisant la structure de dictionnaire en considérant que les valeurs sont toutes les mêmes. On ne considère que les clés qui représentent les éléments de l'ensemble.
{% endinfo %}

{% lien %}

- <https://realpython.com/python-dicts/>
- [`dict`{.language-}](https://docs.python.org/fr/3/tutorial/datastructures.html#dictionaries)

{% endlien %}

On peut créer des dictionnaires de multiples manières. Les 3 façons ci-dessous créent le même dictionnaire :

- directe : `{"un": 1, "deux": 2}`{.language-}
- via un itérable de couples `[clé, valeur]`{.language-} : `dict([["un", 1], ["deux", 2]])`{.language-}
- via une list compréhension : `{clé: valeur for clé, valeur in [["un", 1], ["deux", 2]]}`{.language-}

Les clés ne doivent pas changer une fois créées, sinon la serrure fabriquée dans le dictionnaire ne fonctionne plus. On ne doit donc utiliser que des objets **non modifiable** pour créer des clés d'un dictionnaire python. Les valeurs en revanche peuvent être modifiables. Par exemple `{"l": [1, 2]}`{.language-} est une définition correcte d'un dictionnaire, alors que `{[1, 2]: "liste"}`{.language-} ne l'est pas.

## Obtention, modification, ajout et suppression d'un élément

Identique à une liste, mais on utilise les clés plutôt que les indices :

avec `d = {"un":1, "deux":2}`{.language-} :

- `d["un"]`{.language-} retourne 1
- `d["trois"]`{.language-} retourne une erreur : la clé "trois" n'existe pas.
- Ajout d'un élément : `d["trois"] = 3`{.language-}
- Suppression d'un élément : `del d["deux"]`{.language-}

## Itération

supposons que l'on ait le dictionnaire :

```python
d = {
    "a": 1,
    "b": 2,
}
```

Le code suivant :

```python
for x in d:
    print(x)
```

Affichera les clés du dictionnaires. On affichera donc :

- peut être `'a'`{.language-} puis `'b'`{.language-}
- peut être `'b'`{.language-} puis `'a'`{.language-}

{% attention %}

L'ordre d'itération des clés n'est **PAS** connu à l'avance : il peut changer d'une ordinateur à l'autre, et même d'une exécution à l'autre. Un dictionnaire contient des éléments stockés sans ordre particulier.

{% endattention %}

On peut aussi itérer sur les clés en utilisant la méthode `keys`{.language-} :

```python
for x in d.keys():
    print(x) # affichera les clés
```

On peut aussi itérer sur les valeurs en utilisant la méthode `values`{.language-} :

```python
for x in d.values():
    print(x) # affichera les valeurs
```

Ou encore itérer sur les couples (clé, valeur) avec la méthode `items`{.language-} :

```python
for x in d.items():
    print(x) # affichera les couples (clé, valeur)

```

## Présence

L'opérateur `in`{.language-} appliquée à un dictionnaire vérifie si une clé est dans le dictionnaire, elle ne s'occupe pas des valeurs :

```python
>>> d = {"réponse": 42, "utile": "serviette"}
>>> "utile" in d
True
>>> 42 in d
False
```

On peut aussi utiliser les résultats des méthodes `.keys()`{.language-} et `.values()`{.language-} avec l'opérateur `in`{.language-}

```python
>>> d = {"réponse": 42, "utile": "serviette"}
>>> 42 in d.values()
True
>>> "utile" in d.keys()
True
```

### Exercice fondamental

L'exercice ci-après, en plus d'avoir une importance algorithmique certaine, vous permet de trouver la réponse à un problème de trois façons différentes

{% exercice "Exercice final" %}
On possède une liste $P$ d'entiers correspondant à des prix ($P[i]$ correspond au prix de la marchandise $i$, allant de 0 à `len(p) - 1`{.language-}) et un crédit $C$.

On peut pouvoir donner deux indices $i$ et $j$ tels que $p[i] + p[j] = C$.

Vous allez répondre à cette question de trois façons différentes :

1. utilisez deux boucles imbriquées allant de $0$ à $n-1$ permettent de balayer tous les couples $(i, j)$ avec $0 \leq i, j < n$
2. Commencez par trier la liste $P$ (vous pourrez utiliser la [méthode `sort`{.language-} des listes](https://docs.python.org/fr/3/howto/sorting.html#sorting-basics)) puis utilisez une unique boucle `while`{.language-} pour résoudre le problème. Cette boucle doit commencer avec `i=0`{.language-} et `j=len(P)-1`{.language-} et, à chaque étape, soit augmente `i`{.language-} soit diminue `j`{.language-}.
3. Créez un dictionnaire $d$ dont les clés $c$ sont les prix $P[i]$ ($0 \leq i < \text{len}(P)$) et les valeurs des indices $i$ ($0 \leq i < \text{len}(P)$) tels que `P[d[c]] = c`{.language-}. Utilisez $d$ pour résoudre le problème

{% endexercice %}
{% details "solution" %}

On fait une recherche exhaustive de tous les couples $(i, j)$ :

```python
for i in range(len(P)):
    for j in range(len(P)):
        if P[i] + P[j] == C:
            print(i, j)

```

Pour la deuxième solution, une fois le tableau trié il suffit de remarquer que :

- si $P[i] + P[j] > C$ alors $P[i'] + P[j'] > C$ pour tous $i' \leq i$ et $j' \geq j$
- si $P[i] + P[j] < C$ alors $P[i'] + P[j'] < C$ pour tous $i' \geq i$ et $j' \leq j$

```python
P.sort()

i = 0
j = len(P)-1
while (i != j) and (P[i] + P[j] != C):
    if P[i] + p[j] < C:
        i += 1
    else:
        j -= 1

if i != j:
  print(i, j)
```

La troisième solution est très élégante et est très rapide en moyenne :

```python
d = dict()

for i in range(len(P)):
  d[P[i]] = i

for k in d:
    if C - k in d:
        print(d[C-k], d[k])
```

Cet exercice est étudié de façon théorique dans la partie algorithmie. Les trois complexités sont de valeurs différentes. Si l'on veut une solution efficace en pratique on utilisera la troisième méthode (qui est linéaire en moyenne) et si on cherche une solution de complexité la plus faible on utilisera la seconde méthode (de complexité égale à celle du tri).
{% enddetails %}
