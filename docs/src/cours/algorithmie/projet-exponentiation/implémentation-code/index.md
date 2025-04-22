---
layout: layout/post.njk
title: Projet exponentiation

eleventyNavigation:
  prerequis:
    - /cours/coder-et-développer/bases-programmation/matplotlib/

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

> TBD refaire en :
>
> - utilisant numpy pour les indices
> - donner le code des fonctions numpy etc.
>

On vérifie expérimentalement que nos calculs théoriques sont validés expérimentalement. On codera et testera nos algorithmes, donc vérifiez que vous avez les prérequis.

## Mise en place

### Structures

{% faire %}

1. créez un dossier nommé `exponentiation`{.fichier} où vous placerez vos fichiers
2. créez un projet vscode dans ce dossier
3. créez dans ce dossier les 3 fichiers de la trinité du code :
   - `main.py`{.fichier}
   - `exponentiation.py`{.fichier}
   - `test_exponentiation.py`{.fichier}

{% endfaire %}

### Vérifications

{% faire %}

- on vérifie que python est OK avec le terminal et avec vscode
- on vérifie que le linter est actif dans vscode
- on vérifie que les tests fonctionnent (en créant un test bidon dans `tests_exponentiation.py`{.fichier} et en vérifiant que `pytest` et vscode le trouvent)

{% endfaire %}

{% faire %}
On se force, jusqu'à que cela devienne un automatisme, à écrire du code stylé. C'est à dire sans que le linter ne se fâche.
{% endfaire %}

## Le code

### Algorithme naif

{% faire %}

- dans le fichier `exponentiation.py`{.fichier} : implémentez [l'algorithme naïf itératif](../étude-algorithmique/#algorithme-puissance-naif) dans une fonction nommée `puissance_naif`{.language-} (utilisez des noms explicites).
- dans le fichier `test_exponentiation.py`{.fichier} : implémentez les tests de l'algorithme naïf itératif :
  - vérifiez que les cas simples avec nombre et/ou exposant à 1 fonctionnent
  - vérifiez qu'un cas général est correct (comme $2^3$ par exemple)

Vérifier que vos tests se lancent bien dans le terminal.

{% endfaire %}

Pour les tests, on utilisera les règles suivantes :

{% note %}

Organisation des tests :

- un fichier de test par fichier de code. Chaque fichier de test sea nommé : `test_[nom du fichier de code].py`{.fichier} où _[nom du fichier de code]_ sera le nom du fichier (ne mettez pas les _[]_)
- chaque test sera nommé en 3 parties : `test_[nom de la fonction_testée]_[ce que l'on teste]`{.language-} où `[nom de la fonction_testée]`{.language-} est le nom de la fonction testée (ne mettez pas les `[]`) et `[ce que l'on teste]`{.language-} une description succincte (en 1 ou 2 mots max) de ce que l'on teste.
- un test doit tester **une unique chose**. On peut se permettre d'avoir plusieurs `assert`{.language-} par fonction de test du moment que ce qu'on test peut être qualifié par un nom précis (la partie `[ce que l'on teste]`{.language-} du nom de la fonction de test)

{% endnote %}

Terminons cette partie en utilisant le débogueur :

{% faire %}

Dans le programme principal, calculez l'exponentiation d'un entier par un autre (ces entiers pourront être issus de deux variables ou demandées à l'utilisateur), puis rendez la.

En utilisant le débogueur, vérifiez l'invariant de boucle (pour pourrez utiliser un espion et un log breakpoint).

{% endfaire %}

### Algorithme rapide

{% faire %}

- dans le fichier `exponentiation.py`{.fichier} : implémentez [l'algorithme rapide](../étude-algorithmique/#algorithme-puissance-indienne) dans une fonction nommée `puissance_rapide`{.language-}
- dans le fichier `test_exponentiation.py`{.fichier} : implémentez les tests de l'algorithme rapide en faisant les mêmes tests que pour l'algorithme naïf.

Vérifier que vos tests se lancent bien dans le terminal.

{% endfaire %}

Terminons cette partie en utilisant le débogueur :

{% faire %}

Dans le programme principal, calculez l'exponentiation d'un entier par un autre (ces entiers pourront être issue de variables ou demandés à l'utilisateur), puis rendez la issue du calcul rapide.

En utilisant le débogueur, vérifiez que l'invariant de boucle est vérifié (pour pourrez utiliser un espion et un log breakpoint).

{% endfaire %}

{% attention %}
Ne supprimez pas les tests de l'algorithme naïf en créant ceux pour l'algorithme rapide ! Vos deux fonctions **DOIVENT** être testées.

Si l'on modifie notre algorithme naif plus tard il faudra toujours qu'il soit testé.
{% endattention %}

## Complexité temporelle

La seule façon de mesurer expérimentalement la complexité d'un algorithme est de mesurer la [complexité en temps](../../complexité-calculs/définitions/#complexité-temps){.interne} de celui-ci pour une entrée réalisant la complexité maximale.

Ce n'est cependant pas si simple de mesurer ce temps précisément parce que :

- nous ne sommes pas seul sur la machine, tous les programmes actifs s'exécutent souvent en même temps en se [partageant du temps de processeur](https://fr.wikipedia.org/wiki/Temps_partag%C3%A9) : il est donc difficile de mesurer précisément le temps uniquement pris pour notre algorithme par le processeur.
- python fait des choses sans nous le dire, comme vérifier de temps en temps que les objets ont tous des noms et les supprimer s'ils n'en ont plus (on appelle ça un [ramasse miette](<https://fr.wikipedia.org/wiki/Ramasse-miettes_(informatique)>)) : python lui-même exécute des instructions qui ne sont pas dans notre algorithme.

Mais pour ce qui nous importe, on va dire que c'est pas grave parce que ces _temps parasites_ :

- on peut uniquement mesurer le temps pris par le programme python
- les opérations régulières de python sont négligeables lorsque la taille des entrées deviennent grandes
- ils peuvent être vues comme des constantes dans le calcul de notre complexité : il ne participent donc pas à l'allure générale de la courbe de complexité.

Le protocole de calcul sera alors le suivant :

{% attention "**À retenir**" %}

Pour mesurer le temps d'exécution d'un algorithme :

1. on note le nombre de secondes $t_1$ utilisées par le programme python juste avant d'exécuter l'algorithme
2. on exécute l'algorithme
3. on note le temps $t_2$ utilisé par le programme juste après exécution l'algorithme

La complexité temporelle sera alors : $\Delta = t_2 - t_1$.
{% endattention %}

### Comment faire

On va utiliser les fonctions simple du module [time](https://docs.python.org/fr/3/library/time.html). Faisons une petite fonction de test pour voir comment on peut utiliser la mesure du temps dans notre programme.

{% faire %}
Créez un fichier `temps_mesure.py`{.fichier} et mettez y le code suivant :

```python
import time

print("Avant l'attente")
x = 1000
t1 = time.perf_counter()
x ** x ** 2
t2 = time.perf_counter()
print("Après l'attente")

delta = t2 - t1

print("Temps d'attente :", delta)
```

{% endfaire %}
{% info %}
On utilise à dessein un calcul long $x^{x^2}$ pour que vous voyiez le temps passé à le calculer.
{% endinfo %}

Le code précédent utilise une fonction du module [`time`{.language-}](https://docs.python.org/fr/3/library/time.html) : [`perf_counter`{.language-}](https://docs.python.org/3/library/time.html#time.perf_counter) qui mesure le temps utilisé par le programme python en secondes, indépendamment des autres programmes tournant sur votre ordinateur (Youtube, Instagram, etc). On utilise une fonction longue à calculer (ici $1000^{1000^2}$, vous pouvez essayer $2000^{2000^2}$ ou $500^{500^2}$ pour voir les différences de temps)

{% faire %}

1. Exécutez plusieurs fois le code précédent pour voir que l'on passe bien environ 1 seconde à calculer $1000^{1000^2}$.
2. Faites pour dix essais :
   - le temps maximum de calcul
   - le minimum maximum de calcul
   - le temps moyen de calcul

{% endfaire %}

Voua devriez voir que le temps d'exécution de chaque fonction est similaire mais non identique.

{% info %}
Lorsque l'on calcule des complexités temporelles, on réalise plusieurs mesures pour en rendre la moyenne et ainsi atténuer les fluctuations.
{% endinfo %}

### Expérimentations

#### Un temps d'exécution

{% faire %}

Créer un programme principal (dans le fichier `main.py`{.fichier}) qui demande à l'utilisateur un exposant $n$. Ce programme donne ensuite le temps mis pour exécuter $3^n$ avec l'algorithme naïf et avec l'algorithme rapide.

{% endfaire %}

#### Temps max

{% faire %}

Créer dans un fichier nommé `main_temps.py`{.fichier} un programme permettant de trouver $K$ et $N$ tels que $N = 2^K$ soit la première puissance de 2 pour laquelle le temps mis pour exécuter l’exponentiation naïve de $3^N$ dure plus de 1 seconde.

{% endfaire %}
{% info %}
On trouve que $K$ vaut de l'ordre de 20.
{% endinfo %}
{% details "solution" %}

```python
temps = 1

delta = 0 # valeur par défaut pour rentrer dans la boucle while
K = 0
N = 1

while delta < temps:
    t1 = time.perf_counter()
    puissance_naif(3, N)
    t2 = time.perf_counter()

    delta = t2 - t1
    K += 1
    N *= 2

```

{% enddetails %}

#### <span id="mesure-temps"></span> Liste de temps

On va mesurer le temps pris pour chaque algorithme à des pas de temps discrets correspondants aux calculs de $3^{n}$ pour $n$ allant de $n=2$ à $n=N$ (avec le $N$ calculé dans la partie précédente). Ceci nous permettra d'avoir quelques points de contrôles espacés dans le temps et nécessitant chacun peu de temps de calcul (moins d'une seconde pour chaque mesure).

Commençons par créer les points de contrôles sous la forme d'un tableau d'exposants à calculer :

{% faire %}
Créez (et testez) une fonction `donne_pas(nombre_pas: int, min_valeur: int, max_valeur: int) -> [int]`{.language-} qui rend une liste d'entiers allant de `min_valeur`{.language-} à au plus `max_valeur`{.language-} par pas de `(max_valeur - min_valeur) //  nombre_pas`{.language-}
{% endfaire %}
{% info %}
`donne_pas(4, 2, 23)`{.language-} rendra la liste `[2, 7, 12, 17, 22]`{.language-}. Elle est très facile à créer avec la fonction `range`{.language-}
{% endinfo %}

Puis mesurons le temps pris pour calculer $3^n$, pour 20 points de contrôles entre $1$ et $N$ :

{% faire %}
Ajoutez au programme du fichier `temps_exponentiation.py`{.fichier} trois nouvelles listes :

- la liste `exposant`{.language-} qui est le retour de la fonction `donne_pas(20, 1, N)`{.language-} (avec le $N$ calculé la partie précédente)
- la liste `mesures_temps_naif`{.language-} telle que `mesures_temps_naif[i]`{.language-} corresponde au temps mis pour exécuter la fonction calculer `puissance_naif(3, exposant[i])`{.language-}
- la liste `mesures_temps_rapide`{.language-}corresponde au temps mis pour exécuter la fonction calculer `puissance_rapide(3, exposant[i])`{.language-}
  {% endfaire %}

La complexité de l'algorithme naif doit être linéaire et celui de l'algorithme rapide logarithmique, donc :

{% faire %}
Vérifiez que le rapport `mesures_temps_naif[i] / mesures_temps_rapide[i]`{.language-} augmente lorsque $i$ augmente (il doit tendre vers l'infini).
{% endfaire %}

{% faire %}
Vérifiez que le rapport :

- `mesures_temps_naif[i] / exposant[i]`{.language-} reste à peut prêt constant
- `mesures_temps_rapide[i] / log(exposant[i])`{.language-} reste à peut prêt constant (`log`{.language-} est une fonction du [module `math`{.language-} de python](https://docs.python.org/fr/3/library/math.html))
  {% endfaire %}

## Graphiques

Nous allons dans cette partie représenter graphiquement nos mesures. Nous utiliserons pour cela la bibliothèque [Matplotlib](https://matplotlib.org/).

### <span id="Matplotlib"></span>Bibliothèque Matplotlib

Commencez par l'installer :

{% faire %}
Dans un terminal, tapez la commande suivante pour installer [Matplotlib](https://matplotlib.org/) :

```
python -m pip install matplotlib
```

{% endfaire %}

Utiliser cette bibliothèque ne s'improvise pas. Commencez par lire le tutoriel suivant pour en comprendre les bases :

{% aller %}
Suivez le [tutoriel Matplotlib](/cours/coder-et-développer/bases-programmation/matplotlib/){.interne}. Il est fait pour être utilisé avec un notebook, mais vous devriez pouvoir facilement convertir les exemples pour pouvoir les utiliser dans un fichier python normal.
{% endaller %}

### Temps naïf

{% faire %}
Ajoutez le code suivant au code du fichier `temps_exponentiation.py`{.fichier} pour afficher le temps mis pour afficher le temps mis pour calculer `puissance_naif(3, exposant[i])`{.language-} en fonction de `exposant[i]`{.language-}.

Est-ce conforme à ce qui était attendu ?
{% endfaire %}

```python
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(20, 5))

ax.set_title("complexités temporelles")
ax.set_xlabel("valeur de l'exposant")
ax.set_ylabel("temps de calcul")

ax.plot(exposant, mesures_temps_naif, 'o-')

plt.show()
```

### Temps exponentiel

{% faire %}
Adaptez le code précédent pour afficher les mesures de temps pour l'exponentiation rapide.

Est-ce conforme à ce qui était attendu ?
{% endfaire %}

### Combinaison des deux

{% faire %}
Superposez en un seul graphique les deux courbes (on pourra faire deux plot l'un à la suite des autres).
{% endfaire %}

Le temps mis par l'exponentiation rapide est très inférieur à celui effectué par l'algorithme d'exponentiation naif, on ne le voit pratiquement p[as.

### Deux axes des ordonnées

{% faire %}
Utilisez le code de [ce lien](https://matplotlib.org/stable/gallery/spines/multiple_yaxis_with_spines.html#multiple-yaxis-with-spines) pour utiliser `ax.twinx`{.language-} qui permet de partager l'axe des abscisse en ayant deux axes des ordonnées et permettre de voir les 2 courbes,chacune ayant son axe des ordonnées.

Vous pourrez également changer la couleur d'un des dessins en remplaçant le paramètre `'o-'`{.language-} d'un des 2 plot par `'ro-'`{.language-} pour dessiner en rouge (red).

{% endfaire %}
