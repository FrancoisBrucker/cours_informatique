---
layout: layout/post.njk 
title: "Projet : Voyageur de commerce glouton"

eleventyNavigation:
  key: "Projet : Voyageur de commerce glouton"
  parent: Code

prerequis:
    - "../../algorithme/algorithmes-gloutons/"
    - "../format-données-csv/"
    - "../format-données-json/"
---

<!-- début résumé -->

Analyse et codage d'un algorithme glouton pour résoudre le problème du voyageur de commerce.

<!-- end résumé -->

Le [problème du voyageur de commerce](https://fr.wikipedia.org/wiki/Probl%C3%A8me_du_voyageur_de_commerce) peut s'énoncer comme suit :

{% note "**Problème du voyageur de commerce**" %}
Étant donné un ensemble de villes reliées entre elles par des routes, trouver l'itinéraire le plus court passant par chaque ville une et une seule fois.

On suppose dans la suite de cet exercice que l'on connaît la distance $d(u, v)$ pour n'importe quel couple de villes $u$ et $v$.
{% endnote %}

{% faire %}
Écrivez ce problème sous la forme d'un problème d'optimisation.
{% endfaire %}
{% details "Solution :" %}

Pour un ensemble de villes $V$, on cherche un cycle $v_1 v_2\dots v_1$ passant par toutes les villes 1 fois minimisant la quantité $\sum_{i=1}^nd(v_i, v_{i+1}) + d(v_n, v_1)$.
{% enddetails %}

## <span id="données"></span> Données

{% faire "**Préparation du projet**" %}
Créez un dossier `projet-gloutons`{.fichier} et téléversez-y les deux fichiers de données dont nous aurons besoin (il vous sera peut-être nécessaire de cliquer-droit puis de choisir téléchargement) :

[gps-pays-autres.csv](./projet/gps-pays-autres.csv) (qui est une modification de <https://developers.google.com/public-data/docs/canonical/countries_csv>)

Créez un projet vscode avec ce dossier.
{% endfaire %}

Le fichier `gps-pays-autres.csv`{.fichier} continent les coordonnées gps des 196 pays du monde réparties en parties connexes (les DOM et les TOM français constituent des entités séparées par exemple).

{% faire %}
Le code suivant permet de créer un dictionnaire à partir du fichier csv :

```python
import csv

pays = {}
with open("gps-pays-autres.csv", newline="") as fichier_csv:
    for row in csv.reader(fichier_csv, quotechar='"', quoting=csv.QUOTE_NONNUMERIC):
        pays[row[3]] = (row[2], row[1])
```

Quel sont les clés et valeurs de ce dictionnaire ?
{% endfaire %}
{% details "solution" %}
Les clés sont les noms et les valeurs un couple `(longitude, latitude)`{.language-}
{% enddetails %}

Affichons la carte. Pour cela vous devrez avoir la bibliothèque [matplotlib]({{ '/tutoriels/matplotlib' | url}}) d'installée. La fonction suivante le fait, dans la mesure où `pays`{.language-} est de la forme précédente :

```python
import matplotlib.pyplot as plt

def draw(pays, size=20):
    

    x = []
    y = []
    label = []
    for (nom, (long, lat)) in pays.items():
        x.append(long)
        y.append(lat)

        label.append(nom)

    height = max(y) - min(y)
    width = max(x) - min(x)

    _, ax = plt.subplots(figsize=(size, size * height / width))

    ax.set_title("Les pays")

    ax.scatter(x, y)
    for i in range(len(x)):
        ax.text(x[i], y[i], label[i])

    plt.show()
```

{% faire %}
Afficher la carte de tous les pays, puis restreignez-vous aux pays européen ((-10 < longitude < 40) et (35 ≤ latitude < 70))

{% endfaire %}

## Nombre de solutions

{% exercice %}
Combien de solutions possibles possède un problème du voyageur de commerce à $n$ villes ?
{% endexercice %}
{% details "Solution :" %}
Pour un départ fixé, une permutation des $n - 1$ villes restante produit une solution. Comme la permutation opposée revient à parcourir le cycle dans l'autre sens, il y a $\frac{(n-1)!}{2}$ solutions possibles.
{% enddetails %}

{% faire %}
Et combien ça fait avec nos données ?
{% endfaire %}

## Algorithme glouton

Le nombre de solution astronomique nous empêche de toutes les essayer. De plus, on peut montrer (nous ne le ferons pas ici) qu'il est illusoire de trouver une solution exacte (du moins pendant une séance de code) car le problème du voyageur de commerce est NP-difficile.

Couramment, l'algorithme glouton utilisé pour approximer ce problème est :

1. choisir une ville de départ qui constitue le départ du chemin
2. tant que toutes les villes n'ont pas été ajoutée au chemin : on ajoute la ville la plus proche du dernier élément du chemin.

{% exercice %}
Montrer que cet algorithme n'est pas toujours optimal.
{% endexercice %}
{% details "Solution" %}

En utilisant la distance euclidienne, l'algorithme glouton ne trouvera jamais la bonne solution pour les 6 points de la figure suivante :

![glouton pas optimal](glouton-pas-optimal.png)

{% enddetails %}

{% exercice %}
En utilisant le dictionnaire `pays`{.language-} [définit précédemment](./#données), créez un fonction `d(p1, p2)`{.language-} qui rend la distance euclidienne au carré entre les pays `p1`{.language-} et `p2`{.language-}.

Quelle est l a distance minimale, moyenne et maximale entre deux pays ?
{% endexercice %}
{% details "solution :" %}
En utilisant la distance au carré (plus rapide à calculer), j'obtiens :

* min :  0.013953460656999808
* max :  127150.42156039258
* moyenne :  12358.334742484834

{% enddetails %}
{% faire %}
Codez l'algorithme glouton en prenant un pays de départ aléatoire (utiliser la bibliothèque [random](https://docs.python.org/fr/3/library/random.html))
{% endfaire %}

{% faire %}
Représentez graphiquement le résultat en traçant le chemin sur la carte.
{% endfaire %}
{% faire %}
Idem pour l'Europe
{% endfaire %}

On voit que le résultat n'est pas terrible. Il y a beaucoup d'améliorations locale que l'on peut apporter.

## Optimisation par réitération

Pour améliorer la solution, il faut commencer par coder une fonction objectif qui nous permettra de caractériser une "bonne" solution :

{% faire %}
Coder une fonction `fonction_objectif(chemin)`{.language-} qui à partir d'un chemin $p_1\dots p_n$ calcule la distance du cycle $\sum_{i=1}^{n-1}d(p_i, p_{i+1}) + d(p_n, p_1)$.
{% endfaire %}

La fonction objectif nous permet de réitérer l'algorithme :
{% exercice %}
Lancer l'algo 20 fois et prenez le plus petit. Vérifiez que l'on ne garde bien que les valeurs plus petites.

Combien de fois la fonction objectif s'est-elle améliorée ?
{% endexercice %}
{% details "solution" %}
Chez moi, j'ai eu (toujours avec la distance au carré) :

```text
distance : 122390.22080554374
Iteration : 1 v 122390.22080554374 ≤ 146637.7969272192
Iteration : 2 v 122390.22080554374 ≤ 130003.13332758895
Iteration : 3 v 122390.22080554374 ≤ 184462.02287689561
Iteration : 4 v 122390.22080554374 ≤ 245782.07095032808
Iteration : 5 ^ 122390.22080554374 > 109191.24541426092
Iteration : 6 v 109191.24541426092 ≤ 112152.04119942358
Iteration : 7 v 109191.24541426092 ≤ 111717.00784005513
Iteration : 8 v 109191.24541426092 ≤ 239951.36578693954
Iteration : 9 v 109191.24541426092 ≤ 115575.97089884071
Iteration : 10 v 109191.24541426092 ≤ 181770.37005993415
Iteration : 11 v 109191.24541426092 ≤ 160741.83942046648
Iteration : 12 ^ 109191.24541426092 > 106679.82591169249
Iteration : 13 v 106679.82591169249 ≤ 127800.96668874641
Iteration : 14 v 106679.82591169249 ≤ 242822.36502110917
Iteration : 15 v 106679.82591169249 ≤ 125918.01748259322
Iteration : 16 v 106679.82591169249 ≤ 114826.25834699393
Iteration : 17 v 106679.82591169249 ≤ 227285.14455958785
Iteration : 18 v 106679.82591169249 ≤ 109729.00306187653
Iteration : 19 v 106679.82591169249 ≤ 123173.34741342405
Iteration : 20 v 106679.82591169249 ≤ 124633.17427994366
Nombre d'améliorations : 2
```

{% enddetails %}

On le voit sur la représentation graphique de la solution. On peut bien mieux faire ! L'algorithme glouton nous permet de trouver une solution, mais elle reste améliorable.

## Optimisation par 2-optimisation

L'idée est de faire une passe d'optimisation après l'algorithme glouton.

Ce principe général d'optimisation après a posteriori s'appelle [2-opt](https://fr.wikipedia.org/wiki/2-opt) dabs le cas du voyageur de commerce :

> TBD recroiseremnt faux 

1. Soit un chemin $p_0\dots p_{n-1}$
2. On choisit $ 1 < i < n-1$ et on construit le chemin $p_0 p_i \dots p_{n-1} p_{i-1} \dots p_{1}$
3. si le coût du nouveau chemin est inférieure à l'ancien chemin, on le conserve. Sinon, on le rejette et on conserve le chemin initial.

Par exemple si le chemin est, pour 4 villes françaises, `['Saverne', 'Plan de Cuques', 'Metz', 'Plouzané']`{.language-}, on obtient le cycle suivant :

![cycle 1](./cycle-1.png)

En choisissant `'Metz'`{.language-} (i=2), on obtient le cycle suivant, bien meilleur :

![cycle 2](./cycle-2.png)

Comme on le voit, 2-opt permet de *décroiser* les arêtes $p_0p_{n-1}$ et $p_{i-1}p_i$ chemins partant de l'origine.

{% faire %}
Coder l'algorithme qui à partir d'un chemin et d'un sommet $i$ rend le chemin décroisé s'il est meilleur que le chemin initial.
{% endfaire %}

{% faire %}
Une *passe* de $2$-opt consiste, à partir d'un chemin donné, tester tous les croisements possible à partir de l'origine.

Coder cet algorithme que vous nommerez `passe_deux_opt`{.language-} et testez le sur un chemin en europe.
{% endfaire %}
{% exercice %}
Ceci suffit-il pour décroiser le chemin ?
{% endexercice %}
{% details "Solution" %}
Non, il faut faire varier les début car un croisement peut intervenir entre deux arêtes non dépendantes de l'origine.
{% enddetails  %}

{% faire %}
On appelle *passe globale*, faire une passe de 2-opt pour toutes les origines possibles :

```python
def passe_globale(chemin):
    for debut in range(len(chemin)):
        chemin = passe_deux_opt(chemin[debut:] + chemin[:debut])
    return chemin
```

Codez cet algorithme.

{% endfaire %}
{% exercice %}
Ceci suffit-il pour décroiser le chemin ?
{% endexercice %}
{% details "Solution" %}
Non, car un décroisement d'arête peut créer d'autres croisement.
{% enddetails  %}

{% faire %}
Recommencer les passes globales jusqu'à ce qu'il n'y ait plus de croisement.

{% endfaire %}
{% exercice %}
Le processus converge-t-il ?
{% endexercice %}
{% details "Solution" %}
Oui, le processus converge puisque l'on fait strictement décroître la fonction objectif et il y a un nombre fini de possibilités.
{% enddetails  %}

## Recuit simulé

Le problème de ne modifier la solution que lorsque l'on améliore celle-ci est que l'on est souvent bloqué dans des minima locaux :

![minimum local](./recuit-1.png){:style="margin: auto;display: block;"}

Pour trouver la solution en ne faisant que des changements locaux, il faut parfois accepter une solution moins bonne de temps en temps :

![solution moins bonne](./recuit-2.png){:style="margin: auto;display: block;"}

pour trouver le minimum global :

![solution moins bonne](./recuit-3.png){:style="margin: auto;display: block;"}

Il existe plusieurs techniques pour faire cela, la méthode du [recuit simulé](https://fr.wikipedia.org/wiki/Recuit_simul%C3%A9) accepte une solution moins bonne avec une probabilité qui va diminuer avec le nombre d'itérations.

L'algorithme du recuit simulé appliqué au voyageur de commerce est alors (avec `P()` un réel aléatoire entre 0 et 1) :

```text

c = cycle initial
cycle_min = c

pour k allant de 1 à max_essai:
    c' = deux-opt-aléatoire(c)
    si le coût de c' est inférieur au coût de c ou si P() ≤ P_k:
        c = c'
    
    si le coût de c est strictement inférieur au coût de cycle_min:
        cycle_min = c

rendre cycle_min
```

Dans le recuit simulé, la probabilité de choisir une solution moins bonne est égale à :

$$
P_k = e^\frac{-(C'-C)}{T_k}
$$

Où :

* $C'$ et $C$ sont les cout du circuit $c'$ et $c$ respectivement
* $T_k = \lambda T_{k-1}$ avec $\lambda < 1$

{% faire %}
Codez le recuit simulé avec la fonction `deux_opt_aléatoire`{.language-} qui choisit une origine aléatoire puis un indice $i$ aléatoire également.
{% endfaire %}
