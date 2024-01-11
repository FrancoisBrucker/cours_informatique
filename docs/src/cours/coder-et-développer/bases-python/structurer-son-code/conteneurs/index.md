---
layout: layout/post.njk

title: Conteneurs

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

En plus des 6 types de bases, python met à notre disposition plusieurs objets qui peuvent *contenir* d'autres objets.

Un conteneur est un objet itérable et possède l'opérateur `in`{.language-} (comme on l'a déjà vu avec les [chaînes de caractères](../../principes/opérations#chaines-in){.interne}). On pourra ainsi toujours utiliser `x in C`{.language-} pour savoir si l'objet `x`{.language-} est dans le conteneur `C`{.language-}.

Parmi ces conteneurs, la ***liste*** est certainement la plus utilisée :

{% aller %}
[Listes](listes){.interne}
{% endaller %}

Les deux autres conteneurs à connaître sont les ***ensembles*** et les ***dictionnaires***. Ces deux structures sont très utiles lorsque l'on manipule des données mais sont plus complexes à manipuler que des listes. Prenez le temps d'apprendre à utiliser leurs nombreux avantages :

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
