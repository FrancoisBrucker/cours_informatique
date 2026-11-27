---
layout: layout/post.njk

title: Aléatoire

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

> TBD on a mis des choses dans </cours/algor>

> TBD <https://en.wikipedia.org/wiki/Entropy_(information_theory)>
> TBD entropy : <https://www.youtube.com/watch?v=QjD3nvJLmbA>
> TBD <https://sortingsearching.com/2023/11/25/random.html>
> TBD loi aléatoire, genre Poisson : <https://www.youtube.com/shorts/Ofg_S9Lk20E>


D. Knuth cite dans le volume 2 de [Art of computer programming](https://www.amazon.fr/Art-Computer-Programming-Seminumerical-Combinatorial/dp/0137935102/) près d'une dizaine d'application où l'on a besoin de nombres aléatoires (simulation, échantillonnages, jeu, ...). Cependant, à part l'usage de [générateurs aléatoires physiques](https://fr.wikipedia.org/wiki/G%C3%A9n%C3%A9rateur_de_nombres_al%C3%A9atoires_mat%C3%A9riel) ou encore l'utilisation de [tables](https://fr.wikipedia.org/wiki/Table_de_nombres_al%C3%A9atoires), l'aléatoire semble cependant hors de portée d'un ordinateur, par essence déterministe.

{% lien %}
<https://www.random.org/>
{% endlien %}

Si un algorithme ne ne peut "créer" de nombres aléatoires, le relancer avec les mêmes paramètres redonnera exactement les mêmes résultats, on peut cependant des nombres ayant *l'air* d'être aléatoire. Ces nombres sont alors appelés ***nombres pseudo-aléatoires***.

Il nous faut cependant avant tout définir précisément ce qu'aléatoire veut dire avant de montrer deux méthodes permettant d'en générer.


Ca existe :

- [les nombres pseudo-aléatoire de python](https://docs.python.org/fr/3.14/library/random.html). Fonctionnent avec une seed.
- le modulo $x_{n+1} = a \cdot x_n + b \pmod p$ avec $p$ un nombre premier.

Ou encore les décimales de pi à partir de la $k$ème
voir des méthodes plus sophistiquée comme [les lsfr](../../sécurité/cryptographie/confidentialité/nombres-pseudo-aléatoires-cryptographiques/Rapport_de_Stage_Laura_Michelutti.pdf).


Ces générateur (python, ou encore le modulo avec un entier premier) sont parfait pour prédire le monde physique, les sorties sont bien uniformes et indétectables de l'aléatoire, mais pour les applications crypto on veut en plus non-prédictible.

Du coup $\pi$ marche pas non plus trop (<https://mathoverflow.net/questions/26942/is-pi-a-good-random-number-generator> et <https://www2.lbl.gov/Science-Articles/Archive/pi-random.html>).

Et les lsfr il faut travailler.

{% lien %}
[Différences entre les différents générateur pseudo-aléatoires](https://fr.eitca.org/cybersecurity/eitc-is-ccf-classical-cryptography-fundamentals/stream-ciphers/stream-ciphers-random-numbers-and-the-one-time-pad/examination-review-stream-ciphers-random-numbers-and-the-one-time-pad/what-are-the-key-differences-between-true-random-number-generators-trngs-pseudorandom-number-generators-prngs-and-cryptographically-secure-pseudorandom-number-generators-csprngs/)
{% endlien %}



<!-- > TBD TP
>
> - lsfr avec python etc.
> - les décimales de pi :
>   - <https://www.youtube.com/watch?v=FDXf1XxCXAk>
>   - sont aléatoires si tu ne sais pas que c'est elles.
>   - prendre les bits de la représentation binaire des décimales de pi et leur faire passer des tests d'aléatoire. 
> -->
> 
## Aléatoire

{% note "**Définition**" %}
Une séquence $(x_i)_{i\geq 0}$ d'entiers positifs inférieur strictement à $m$ est ***aléatoire*** si elle est constituée de nombres ***indépendants*** suivant une ***loi de distribution***.

- ***indépendance*** des données : $Pr[x_i = a, x_j = b] = Pr[x_i = a] \cdot Pr[x_j = b]$
- une ***loi de distribution*** pour un ensemble finie est l'ensemble des probabilités : $0\leq Pr[x_i = k] = p_k \leq 1$. On a de plus $0\leq k < m$ telle que $\sum_k p_k = 1$.

{% endnote %}

Lorsque l'on parle d'aléatoire sans préciser la loi de distribution, on sous-entend qu'elle est ***uniforme***, c'est à dire que tout évènement a la même probabilité de se produire :

{% note "**Définition**" %}
Une distribution de $m$ évènements $e_k$ est ***uniforme*** si $Pr[x = e_k] = \frac{1}{m}$ pour tout $0\leq k < m$.
{% endnote %}

Savoir si une suite finie donnée est aléatoire est problématique, puisque chaque suite à une probabilité, même faible, d'exister. Une suite binaire de 1 million de 0 a autant de chance d'arriver qu'une suite alternant les 0 et les 1.

{% info %}
C'est pourquoi les être humains ne sont pas bon pour générer des suites aléatoires. En demandant à des humains de générer des suites aléatoires, la suite constante sera sous-représentée.
{% endinfo %}

Déterminer si une suite est aléatoire ne peut se faire que via des tests statistiques qui vont assurer de telle ou telle propriété :

- alternance de 0 et de 1,
- probabilité uniforme,
- ...

### Test statistique

Un [test statistique](https://fr.wikipedia.org/wiki/Test_statistique) permet de déterminer avec une probabilité donnée si une hypothèse est vérifiée ou non.

Nous allons ici nous restreindre aux tests sur les suites finies d'entiers $(x_i)_{0 \leq i < n}$, on peut bien sur mathématiquement les définir de façon plus générale.

{% note "**Définition**" %}
Un ***test statistique*** $T(X)$ sur une suite finie $X = (x_i)_{0 \leq i < n}$ peut prendre deux valeurs, vrai ou faux. On définit :

- la ***probabilité d'acceptation*** comme probabilité que $T(X)$ soit vrai
- la ***probabilité de rejet*** comme probabilité que $T(X)$ soit faux

Un test est créé à partir d'une ***hypothèse $H_0$*** (qui dépend du test) que doit vérifier $X$ pour que le test soit vrai. À un test est alors associé deux risques :

- le ***risque de première espèce*** qui est la probabilité que $T(X)$ soit faux alors alors $X$ satisfait $H_0$ (un paramètre du test).
- le ***risque de seconde espèce*** qui est la probabilité que $T(X)$ soit vrai alors alors $X$ ne satisfait pas $H_0$ (habituellement plus compliqué à déterminer).

On paramètre le test selon un risque de première espèce que l'on considère acceptable acceptable, souvent 5%.
{% endnote %}

O utilise alors un test comme suit :

1. on choisit une hypothèse $H_0$ et un risque de première espace acceptable (usuellement 5%), c'est à dire le risque acceptable que l'on se donne de rejeter l'hypothèse alors qu'elle est vraie.
2. on choisit un test qui nous permettra de savoir si $H_0$ doit être acceptée ou rejetée
3. on effectue le test
4. on regarde le risque de première espèce associé au test. Si ce risque est :
   - supérieure au risque acceptable, on ne rejette pas le test car le risque de rejeter le test alors que l'hypothèse est vérifiée est supérieure au risque acceptable
   - inférieure au risque acceptable, on rejette le test car le risque de rejeter le test alors que l'hypothèse est vérifiée est inférieure au risque acceptable

L'outil principal utilisé pour vérifier l'adéquation d'une siute de nombres fini à une loi est le test du $\chi^2$ (lettre grecque chi, qui se dit "ki").

#### Test du chi2

{% lien %}
[test du chi2](https://fr.wikipedia.org/wiki/Test_du_%CF%87%C2%B2)
{% endlien %}

Si l'on possède une loi de distribution discrète sur $m$ éléments $e_i$ ($0\leq i < m$), telle que $Pr(x=e_i) = p_i$ et une suite finie $X=(x_i)_{0 \leq i < N}$, le $\chi^2$ est un réel valant :

<div>
$$
\chi^2 = \sum_{0 \leq i < m} \frac{(E_i - O_i)^2}{E_i}
$$
</div>

où :

- $E_i = N\cdot p_i$ et est le nombre théorique d'observations qui devrait valoir $e_i$ pour $N$ observations (valeurs espérées si $X$ suit la distribution)
- $O_i = \vert \{x_j = e_i \ \vert\   0\leq j < N \} \vert$ est le nombre d'élément observé valant $e_i$

Si la suite finie $X$ suit la loi de distribution, chaque élément de la somme du $\chi^2$ sera petit et donc le $\chi^2$ lui-même sera petit. Si $X$ satisfait la distribution, on peut même calculer la probabilité que $Pr[\chi^2 \geq V] \leq \alpha$.

On a alors le test statistique suivant :

- hypothèse $H_0$ : la suite finie $X$ satisfait la loi de distribution
- le risque de première espèce est la probabilité d'obtenir une valeur supérieure au $\chi^2$ calculé.

> TBD règles de validité.

#### Chi2 en python

On installe la bibliothèque [scipy](https://scipy.org/) :

```shell
python -m pip install scipy
```

Et vérifions que la fonction randint de python soit bien uniforme.

Commençons par tirer 1000 nombre entre 0 (inclus) et 10 (exclus) :

```python
import random
X = [random.randint(0, 9) for i in range(1000)]

print(X)  # [9, 6, 3, 2, 2, 6, 0, 3, 6, 3, 0, 8, 6, 1, 6, 7, 3, 8, 7, 4, 0, 7, 6, 1, 4, 9, 1, 8, 7, 6, 3, 9, 2, 2, 9, 0, 0, 3, 9, 9, 7, 2, 4, 6, 8, 9, 3, 3, 8, 0, 8, 4, 0, 8, 1, 1, 2, 6, 3, 0, 4, 8, 4, 6, 2, 0, 1, 4, 6, 5, 1, 9, 6, 2, 5, 0, 6, 4, 0, 5, 0, 8, 7, 9, 7, 5, 9, 2, 1, 5, 3, 9, 7, 8, 7, 3, 1, 3, 6, 0, 3, 7, 5, 1, 8, 9, 1, 3, 3, 9, 3, 9, 4, 9, 0, 3, 9, 6, 5, 6, 2, 7, 4, 9, 6, 7, 2, 6, 4, 1, 5, 7, 6, 9, 4, 2, 9, 3, 2, 1, 3, 2, 9, 9, 8, 3, 0, 7, 8, 2, 7, 4, 6, 5, 3, 8, 8, 0, 4, 7, 4, 6, 3, 2, 5, 5, 2, 8, 8, 4, 9, 8, 6, 8, 1, 4, 2, 9, 2, 0, 4, 7, 3, 6, 2, 6, 1, 1, 1, 8, 6, 6, 0, 8, 6, 2, 8, 2, 8, 0, 4, 4, 8, 6, 1, 7, 0, 9, 1, 0, 0, 4, 2, 5, 9, 4, 3, 6, 8, 9, 8, 5, 3, 5, 6, 0, 0, 6, 2, 3, 8, 1, 2, 0, 0, 8, 9, 9, 2, 2, 3, 5, 2, 2, 8, 9, 1, 5, 0, 5, 4, 2, 0, 1, 0, 5, 8, 1, 4, 3, 6, 9, 0, 6, 4, 0, 6, 7, 1, 4, 0, 1, 6, 8, 7, 9, 2, 5, 7, 1, 9, 0, 1, 0, 8, 9, 7, 9, 8, 3, 7, 7, 1, 8, 0, 0, 4, 0, 1, 0, 9, 5, 1, 8, 3, 4, 1, 7, 2, 8, 1, 2, 0, 2, 7, 9, 8, 1, 8, 5, 2, 9, 6, 1, 3, 4, 4, 6, 4, 6, 3, 6, 6, 6, 4, 4, 5, 6, 7, 5, 1, 0, 8, 2, 6, 9, 3, 8, 6, 1, 6, 5, 9, 1, 8, 5, 8, 9, 0, 7, 8, 6, 0, 7, 7, 7, 7, 0, 2, 8, 1, 8, 2, 4, 5, 7, 8, 9, 1, 7, 0, 3, 4, 4, 0, 6, 9, 8, 6, 2, 1, 2, 0, 3, 8, 3, 8, 5, 8, 4, 4, 5, 0, 0, 0, 7, 7, 7, 3, 2, 3, 0, 2, 3, 3, 7, 8, 6, 6, 2, 7, 3, 6, 9, 9, 8, 6, 8, 0, 0, 0, 0, 3, 5, 5, 3, 5, 8, 8, 7, 6, 3, 4, 6, 2, 2, 3, 8, 9, 2, 7, 8, 5, 7, 1, 5, 7, 6, 4, 6, 6, 9, 7, 1, 5, 5, 6, 9, 4, 9, 0, 0, 2, 4, 8, 0, 6, 4, 5, 1, 6, 9, 2, 1, 2, 6, 0, 8, 7, 6, 4, 7, 3, 9, 1, 1, 7, 4, 8, 8, 1, 1, 6, 0, 2, 3, 5, 0, 5, 1, 3, 4, 1, 3, 8, 6, 0, 1, 9, 5, 3, 8, 3, 4, 7, 1, 4, 1, 9, 7, 1, 7, 9, 4, 6, 5, 1, 3, 9, 1, 7, 8, 1, 9, 3, 1, 6, 8, 9, 9, 5, 3, 2, 6, 3, 3, 1, 0, 6, 1, 2, 6, 8, 4, 4, 7, 3, 6, 3, 1, 7, 3, 7, 4, 6, 6, 0, 7, 1, 6, 2, 8, 0, 3, 6, 3, 4, 8, 0, 7, 1, 7, 0, 3, 7, 8, 7, 3, 4, 8, 9, 8, 0, 2, 5, 5, 3, 4, 4, 8, 0, 2, 9, 7, 7, 1, 5, 1, 0, 4, 0, 0, 6, 6, 1, 7, 9, 7, 0, 0, 7, 7, 5, 4, 7, 1, 9, 2, 8, 6, 7, 3, 2, 5, 8, 0, 6, 1, 8, 0, 5, 5, 8, 6, 7, 8, 6, 9, 8, 0, 5, 3, 8, 8, 9, 2, 4, 8, 8, 2, 4, 9, 0, 3, 1, 4, 0, 0, 0, 9, 3, 1, 8, 8, 6, 1, 2, 9, 2, 0, 4, 3, 5, 3, 3, 8, 2, 6, 1, 5, 2, 1, 8, 1, 8, 9, 5, 2, 4, 4, 1, 9, 8, 3, 6, 2, 3, 3, 8, 6, 8, 4, 9, 6, 2, 2, 7, 8, 9, 0, 5, 8, 4, 6, 0, 0, 0, 2, 0, 6, 8, 0, 7, 2, 7, 4, 7, 8, 4, 1, 1, 3, 5, 6, 1, 1, 2, 1, 2, 7, 4, 9, 0, 4, 1, 2, 1, 2, 1, 1, 8, 9, 3, 1, 6, 5, 5, 0, 9, 8, 3, 1, 3, 5, 7, 5, 2, 3, 7, 3, 5, 7, 3, 6, 3, 6, 0, 0, 2, 6, 6, 1, 0, 6, 6, 5, 4, 9, 7, 3, 2, 4, 9, 1, 2, 5, 1, 9, 8, 2, 2, 9, 3, 3, 7, 3, 9, 1, 7, 8, 8, 3, 5, 7, 8, 0, 5, 5, 7, 8, 8, 6, 3, 2, 8, 2, 6, 5, 2, 2, 7, 7, 0, 3, 8, 7, 1, 9, 0, 4, 2, 2, 2, 3, 5, 5, 4, 4, 8, 1, 1, 6, 1, 6, 6, 0, 6, 9, 9, 0, 1, 3, 6, 5, 9, 1, 7, 9, 8, 6, 8, 9, 7, 2, 0, 6, 6, 2, 0, 2, 7, 3, 9, 6, 5, 6, 2, 9, 3, 1, 2, 7, 2, 0, 7, 2, 0, 5, 9, 6, 8, 8, 0, 9, 7, 2, 3, 3, 4, 7, 2, 7, 0, 7, 0, 3, 5, 4, 2, 4, 7, 3, 8, 9, 1, 3, 3, 0, 2, 7, 4, 9, 2, 5, 9, 8, 6, 5, 1, 5, 0, 9, 4, 1, 5, 2, 8, 9, 8, 4, 6, 5, 9, 1, 0, 1, 2, 1, 2, 0, 5, 9, 0, 8, 3, 7, 0, 4, 8, 9, 3, 7, 4, 4, 0, 2, 4, 2, 4, 4]

```

Si la loi est uniforme on devrait obtenir $1000 / 10 = 100$ éléments valant $k$ ($0\leq k < 10$) :

```python
E = [100] * 10  
print(E)  # [100, 100, 100, 100, 100, 100, 100, 100, 100, 100]
```

En on obtient :

```python
O = [0] * 10
for x in X:
  O[x] += 1
print(O)  # [111, 103, 103, 101, 87, 77, 110, 97, 115, 96]
```

Il nous reste à calculer le risque de première espèce du test du $\chi^2$  en utilisant [`scipy.stats.chisquare`{.language-}](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.chisquare.html#scipy-stats-chisquare). On veut un risque inférieure à 5% de rejeter l'uniformité alors qu'elle est vraie :

```python
print(scipy.stats.chisquare(O, E))  # Power_divergenceResult(statistic=11.88, pvalue=0.22015919911793527)
```

Ce qui donne (pour mon cas, lorsque vous ferez l'exercice vous même vous devriez trouver quelque chose d'un peu différent) :

- $\chi^2 = 11.88$
- $Pr[\chi^2 \geq 11.88] = .22$

Notre risque de première espèce est de 22%, on ne rejette donc pas notre hypothèse : la méthode `random.randint`{.language-} génère des nombres selon une distribution uniforme.

{% faire %}
Refaite cette exercice et vérifiez que cela fonctionne aussi pour votre python.
{% endfaire %}

Terminons cette partie avec un petit exercice où, normalement, vous devriez rejeter l'hypothèse :

{% exercice %}
En utilisant la fonction [`random.random()`{.language-}](https://docs.python.org/fr/3/library/random.html#random.random) générez 1000 entiers valant :

- 0 avec une probabilité .6
- 1 avec une probabilité .4

Vérifiez que ces milles lancés ne peuvent satisfaire une loi uniforme.
{% endexercice %}
{% details "solution" %}

```python
X = [1 if (random.random() >= .6) else 0 for i in range(1000)]
print(X)  # [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1]

O = [0] * 2
for x in X:
  O[x] += 1

print(O)  # [608, 392]

print(scipy.stats.chisquare(O), [500, 500])  # Power_divergenceResult(statistic=46.656, pvalue=8.460753211639738e-12)
```

Le risque de première espèce vaut $8 \cdot 10^{-12}$, on rejette l'hypothèse d'uniformité.

{% enddetails %}

## TRNG

{% aller %}

[_Truly Random Number Generator_](nombres-aléatoires)

{% endaller %}

## PRNG

{% aller %}

[_Pseudo Random Number Generator_](nombres-pseudo-aléatoires)

{% endaller %}
