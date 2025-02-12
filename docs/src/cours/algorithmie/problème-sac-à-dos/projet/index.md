---
layout: layout/post.njk
title: Projet

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Séance de code pour tester le problème du sac à dos en condition (presque) réelle.


{% faire %}
Créez un projet vscode pour mettre toutes vos programmes.
{% endfaire %}

## Données

{% faire %}
Créez un fichier `données.py`{.fichier} et placez y l'exemple du cours sous la forme d'une constante.
{% endfaire %}

## Algorithmes gloutons

### Sac à dos fractionnel

{% faire %}
Créez un fichier `fractionnel.py`{.fichier} où vous écrirez le code de l'algorithme glouton trouvant le sac à dos fractionnel optimal.

Vous testerez votre code dans le fichier `test_fractionnel.py`{.fichier}
{% endfaire %}
{% info %}
N'oubliez pas qu'il ne faut **jamais** tester directement des réels. On utilise [`approx`{.language-} de pytest](https://docs.pytest.org/en/7.1.x/reference/reference.html#pytest-approx) pour vérifier qu'ils sont à peu prêt égaux.
{% endinfo %}


Une fois que vous êtes assuré du bon fonctionnement de votre algorithme :


{% faire %}
Exécutez l'algorithme glouton fractionnel avec l'`EXEMPLE`{.language-} du fichier `données.py`{.fichier}.
{% endfaire %}

Pour vérifier que le profit est bien celui attendu, créons une fonction :

{% faire %}
Ajoutez au fichier `données.py`{.fichier} une fonction `profit(sac_à_dos, produits)`{.language-} qui rend le profit réalisé pour le sac à dos (donné comme une liste de proportions de chaque produit, telle que renvoyé par les algorithmes) et les produits en entrée (une liste de dictionnaires, telle que dans l'exemple).

Vous testerez cette fonction dans le fichier  `test_données.py`{.fichier}.

{% endfaire %}

Enfin :

{% faire %}
Créez un fichier `main_fractionnel.py`{.fichier} dont l'exécution rende les données, le sac à dos et le profit pour l'exemple. Vous devez avoir quelque chose du genre en sortie :

```text
Données :
{'nom': 'poudre 1', 'kg': 15, 'prix': 135}
{'nom': 'poudre 2', 'kg': 2, 'prix': 30}
{'nom': 'poudre 3', 'kg': 4, 'prix': 32}
{'nom': 'poudre 4', 'kg': 1, 'prix': 6}
{'nom': 'poudre 5', 'kg': 6, 'prix': 18}
{'nom': 'poudre 6', 'kg': 80, 'prix': 800}

Sac à dos fractionnel optimal :
0 poudre 1
1 poudre 2
0 poudre 3
0 poudre 4
0 poudre 5
0.225 poudre 6

Profit : 210.0

```

{% endfaire %}

### Sac à dos glouton

{% faire %}
Créez un fichier `sac_a_dos.py`{.fichier} où vous écrirez le code de l'algorithme glouton trouvant le sac à dos.

Vous testerez votre code dans le fichier `test_sac_a_dos.py`{.fichier}
{% endfaire %}

Pour comparer les résultats par rapport au problème du sac à dos fractionnel :

{% faire %}
Créez un fichier `main_sac_a_dos.py`{.fichier} dont l'exécution rende les données, le sac à dos et le profit pour l'exemple. Vous devez avoir quelque chose du genre en sortie :

```text
Données :
{'nom': 'poudre 1', 'kg': 15, 'prix': 135}
{'nom': 'poudre 2', 'kg': 2, 'prix': 30}
{'nom': 'poudre 3', 'kg': 4, 'prix': 32}
{'nom': 'poudre 4', 'kg': 1, 'prix': 6}
{'nom': 'poudre 5', 'kg': 6, 'prix': 18}
{'nom': 'poudre 6', 'kg': 80, 'prix': 800}

Sac à dos glouton :
1 poudre 1
1 poudre 2
0 poudre 3
1 poudre 4
0 poudre 5
0 poudre 6

Profit : 171
```

{% endfaire %}

### Expérimentation aléatoire

{% faire %}
Dans le fichier `données.py`{.language-} créez une fonction `sac_à_dos(n, prix, K)`{.language-} qui génère aléatoirement un jeu de $n$ données où chaque donnée a un prix inférieure au paramètre `prix`{.language-} et un poids inférieur à `K`{.language-}
{% endfaire %}

Testez un peu vos algorithmes :

{% faire %}
Dans un fichier `aléatoire_glouton.py`{.language-} testez pour plusieurs jeux de donnés les différences entre :

- la valeur de la solution fractionnelle optimale,
- la valeur du glouton
- les différences entre les deux sac à dos
{% endfaire %}

## Programmation dynamique

{% faire %}
Dans un fichier `efficace.py`{.fichier} créez une fonction `programmation_dynamique(produits, masse_totale)` qui utilise la programmation dynamique pour trouver la valeur du sac à dos optimal. 

{% endfaire %}
On peut maintenant comparer les résultats :

{% faire %}
Dans le fichier `main_efficace.py`{.fichier}, vérifiez que l'exemple donne bien la bonne valeur.
{% endfaire %}


{% faire %}
Dans un fichier `aléatoire_valeur.py`{.language-} testez pour plusieurs jeux de donnés les différences entre :

- la valeur de la solution fractionnelle optimale,
- la valeur du glouton
- la valeur de la solution optimale (utilisez des valeurs de $K$ pas trop grande pour que le calcul par programmation dynamique soit possible en temps raisonnable)
{% endfaire %}

## Énumération exhaustive

### Tous les sac à dos

{% faire %}
Dans le fichier `sac_a_dos.py`{.fichier} créez une fonction `énumération(produits, masse_totale)` qui énumère tous les sac à dos possibles et rend le sac à dos maximum.

Vous testerez votre code dans le fichier `test_sac_a_dos.py`{.fichier}
{% endfaire %}

On peut maintenant comparer les résultats :

{% faire %}
Dans le fichier `main_sac_a_dos.py`{.fichier}, vérifiez que l'exemple donne bien le bon résultat.
{% endfaire %}

### Branch and Bound

{% faire %}
Dans le fichier `énumération.py`{.fichier} créez une fonction `branch_and_bound(produits, masse_totale)` qui utilise le _branch and bound_ pour trouver le sac à dos optimal. 
{% endfaire %}

On peut maintenant comparer les résultats :

{% faire %}
Dans le fichier `main_efficace.py`{.fichier}, vérifiez que l'exemple donne bien la même valeure optimale pour le branch and bound et l'énumération.
{% endfaire %}

Améliorons la complexité :

{% faire %}
- Faites en sorte de commencer avec le résultat de l'algorithme glouton plutôt que le sac à dos vide
- Faites le tri des produits une fois pour toute au début de la fonction `branch_and_bound`{.language-} et pas à chaque appel du glouton fractionnel.
{% endfaire %}

### Expérimentation aléatoire

{% faire %}
Dans un fichier `aléatoire_temps.py`{.language-}, mesurez le temps pris par l'algorithme du branch and bound pour résoudre des problèmes avec :

- de plus en plus d'éléments mais un sac de capacité petite
- peux d'éléments mais un gros sac à dos (pour que la solution ne soit pas triviale, assurez vous que les poids des éléments soient grand...)

{% endfaire %}

Vous pouvez bien sur comparer par rapport à l'énumération exhaustive, mais le temps va devir très vite prohibitif.

## Pour aller plus loin

{% faire %}
Implémentez l'algorithme à performance garantie et vérifiez que l'on est bien au pire deux fois moins bon que la solution optimale.
Comparez son résultat à la solution optimale (calculée par branch and bound) et au résultat du glouton.
{% endfaire %}

Vous pouvez aussi trouver le sac à dos optimal en remontant la programmation dynamique :

{% faire %}
Implémentez un algorithme qui, à partir de la matrice rendue par l'algorithme de programmation dynamique, rend le sac à dos optimal associé.

{% endfaire %}
