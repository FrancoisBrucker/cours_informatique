---
layout: layout/post.njk

title: Conteneurs

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

En plus des 6 types de bases, python met à notre disposition plusieurs objets qui peuvent _contenir_ d'autres objets.

Un conteneur est un objet itérable et possède l'opérateur `in`{.language-} (comme on l'a déjà vu avec les [chaînes de caractères](../../principes/opérations#chaines-in){.interne}). On pourra ainsi toujours utiliser `x in C`{.language-} pour savoir si l'objet `x`{.language-} est dans le conteneur `C`{.language-}.

Parmi ces conteneurs, la **_liste_** est certainement la plus utilisée.

## Listes

{% aller %}
[Listes](listes){.interne}
{% endaller %}

## Ensembles et dictionnaires

Les deux autres conteneurs à connaître sont les **_ensembles_** et les **_dictionnaires_**. Ces deux structures sont très utiles lorsque l'on manipule des données mais sont plus complexes à manipuler que des listes. Prenez le temps d'apprendre à utiliser leurs nombreux avantages :

{% aller %}
[Ensembles et dictionnaires](ensembles-dictionnaires){.interne}
{% endaller %}

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

## Cas particulier des chaines de caractères

Une chaine de caractère peut être vue comme un conteneur non mutable. On peut donc accéder à un caractère particulier comme une liste :

```python

>>> "abcdefghijklmnopqrstuvwxyz"[2]
'c'
```

Ou même utiliser des [slices de liste](./listes/#slices){.interne} :

```python
>>> "abcdefghijklmnopqrstuvwxyz"[2:15:4]
'cgko'
```

En reprenant le 27ème [nombre de Mersenne](https://fr.wikipedia.org/wiki/Nombre_de_Mersenne_premier) sous sa forme chaine de caractère, `m27 = str(2 ** 44497 - 1)`{.language-}, résolvez les exercices suivants :

{% exercice %}
Quels sont les 10 premiers chiffres de `m27`{.language-} ?
{% endexercice %}
{% details "solution" %}

`str(m27)[:10]`{.language-}

{% enddetails %}

{% exercice %}
Quels sont les 10 derniers chiffres de `m27`{.language-} ?
{% endexercice %}
{% details "solution" %}

`str(m27)[-10:]`{.language-}

{% enddetails %}

{% exercice %}
Est-ce que  `m27`{.language-} est un [palindrome](https://fr.wikipedia.org/wiki/Palindrome) ?
{% endexercice %}
{% details "solution" %}

`str(m27) == str(m27)[::-1]`{.language-} (`s[::-1]`{.language-} renverse la chaîne)

{% enddetails %}

En revanche, il est interdit de modifier une chaine de caractère :

```python
>>> x = "chaine"
>>> x[0] = "C"
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment

```

Enfin on ne le répètera jamais assez, python vient avec tout un tas de méthodes utilitaires permettant de résoudre nombre d'opérations courantes. Utilisez la documentation sur les [méthodes de chaînes](https://docs.python.org/3/library/stdtypes.html#string-methods) en python pour résoudre les exercices suivants :

{% exercice %}
Index de la première occurrence de `1234` dans m27. Et de la deuxième ?
{% endexercice %}
{% details "solution" %}

- `str(m27).find('1234')`{.language-}
- `str(m27).find('1234', 19260 + 1)`{.language-} : la première occurrence est à l'indice 19260, on cherche donc après.
- on peut faire en une ligne : `str(m27).find('1234', str(m27).find('1234') + 1)`{.language-}

{% enddetails %}

