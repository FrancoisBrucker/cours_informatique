---
layout: layout/post.njk 
title: Projet exponentiation

eleventyNavigation:
  key: "Projet exponentiation"
  parent: Code

prerequis:
    - "../projet-pourcentages/"
    - "../../algorithme/étude-exponentiation/"
---

<!-- début résumé -->

On vérifie que nos calculs théoriques sont validés expérimentalement.

<!-- end résumé -->

## Mise en place

### Structures

{% faire %}

1. créez un dossier nommé `exponentiation`{.fichier} où vous placerez vos fichiers
2. créez un projet vscode dans ce dossier
3. créez dans ce dossier les 3 fichiers de la trinité du code :
   * `main.py`{.fichier}
   * `exponentiation.py`{.fichier}
   * `test_exponentiation.py`{.fichier}

{% endfaire %}

### Vscode

1. on vérifie que python est ok : le python utilisé par vscode (exécution via le triangle en haut à droite de la fenêtre) et le 
2. on vérifie que le linter est actif (en faisant une faute de style)

{% faire %}
On se force, jusqu'à que cela devienne un automatisme, à écrire du code stylé. C'est à dire sans que le linter ne se fâche.
{% endfaire %}

### Bibliothèques

Nous aurons besoin d'utiliser deux bibliothèques ([matplotlib](https://matplotlib.org/) pour l'affichage des courbes de complexité et [pytest](https://docs.pytest.org/en/6.2.x/) por nos tests). Gérer les bibliothèques python se fait avec l'utilitaire pip que l'on utilise pour interpréteur donné comme ça : `python -m pip`.

{% faire %}
Dans un terminal :

1. vérifiez les bibliothèques déjà installées pour votre interpréteur : `python -m pip list` (remarquez bien qu'ici `list` est un paramètre de `pip` et non de `python`)
2. si besoin installez [matplotlib](https://matplotlib.org/) (`python -m pip install matplotlib`) et [pytest](https://docs.pytest.org/en/6.2.x/) : `python -m pip install pytest`
{% endfaire %}

{% info %}
L'interpréteur python utilisé par vscode n'est pas forcément juste `python`. Retrouvez son nom exact en utilisant [le tutoriel vscode et python]({{ "/tutoriels/vsc-python#quel-python" | url}})
{% endinfo %}

## Le code

### Algorithme naif

{% faire %}

* dans le fichier `exponentiation.py`{.fichier} : implémentez l'algorithme naïf itératif dans une fonction nommée `puissance_naif`{.language-}
* dans le fichier `test_exponentiation.py`{.fichier} : implémentez les tests de l'algorithme naïf itératif :
  * vérifiez que les cas simples avec nombre et/ou exposant à 1 fonctionnent
  * vérifiez qu'un cas général est ok (comme $2^4$ par exemple)
  * vérifiez que les cas particuliers avec l'exposant et/ou nombre valant 1 fonctionnent

Vérifier que vos tests se lancent bien avec l'erlenmeyer et dans le terminal.

{% endfaire %}

Pour les tests, on utilisera les règles suivantes :

{% note %}

Organisation des tests :

* un fichier de test par fichier de code. Chaque fichier de test sea nommé : `test_[nom du fichier de code].py`{.fichier} où *[nom du fichier de code]* sera le nom du fichier (ne mettez pas les *[]*)
* chaque test sera nommé en 3 parties : `test_[nom de la fonction_testée]_[ce que l'on teste]`{.language-} où `[nom de la fonction_testée]`{.language-} est le nom de la fonction testée (ne mettez pas les `[]`) et `[ce que l'on teste]`{.language-} une description succincte (en 1 ou 2 mots max) de ce que l'on teste.
* un unique `assert`{.language-} par fonction de test : on ne doit tester qu'**une seule chose** par test

{% endnote %}

### Algorithme rapide

{% faire %}

* dans le fichier `exponentiation.py`{.fichier} : implémentez l'algorithme rapide dans une fonction nommée `puissance_rapide`{.language-}
* dans le fichier `test_exponentiation.py`{.fichier} : implémentez les tests de l'algorithme rapide en faisant les mêmes tests que pour l'algorithme naïf. :

Vérifier que vos tests se lancent bien avec l'erlenmeyer et dans le terminal.

{% endfaire %}

{% attention %}
Ne supprimez pas les tests de l'algorithme naïf en créant ceux pour l'algorithme rapide ! Vos deux fonctions **DOIVENT** être testées.

Si l'on modifie notre algorithme naif plus tard il faudra toujours qu'il soit testé.
{% endattention %}

## Complexité temporelle

La seule façon de mesurer expérimentalement la complexité d'un algorithme est de mesurer la [complexité en temps](../../algorithme/complexité-max-min#temps-exécution) de celui-ci pour une entrée réalisant la complexité maximale.

Ce n'est cependant pas si simple de mesurer ce temps précisément parce que :

* nous ne sommes pas seul sur la machine, tous les programmes actifs s'exécutent souvent en même temps en se [partageant du temps de processeur](https://fr.wikipedia.org/wiki/Temps_partag%C3%A9) : il est donc difficile de mesurer précisément le temps uniquement pris pour notre algorithme par le processeur.
* python fait des choses sans nous le dire, comme vérifier de temps en temps que les objets ont tous des noms et les supprimer s'ils n'en ont plus (on appelle ça un [ramasse miette](https://fr.wikipedia.org/wiki/Ramasse-miettes_(informatique))) : python lui-même exécute des instructions qui ne sont pas dans notre algorithme.

Mais pour ce qui nous importe, on va dire que c'est pas grave parce que ces *temps parasites* :

* on peut uniquement mesurer le temps pris par le programme python
* les opérations régulières de python sont négligeables lorsque la taille des entrées deviennent grandes
* ils peuvent être vues comme des constantes dans le calcul de notre complexité : il ne participent donc pas à l'allure générale de la courbe de complexité.

Le protocole de calcul sera alors le suivant :

{% note "mesurer le temps d'exécution :" %}

1. on note le nombre de secondes $t_1$ utilisées par le programme python juste avant d'exécuter l'algorithme
2. on exécute l'algorithme
3. on note le temps $t_2$ utilisé par le programme juste après exécution l'algorithme

La complexité temporelle sera alors : $\Delta = t_2 - t_1$.
{% endnote %}

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

Le code précédent utilise une fonction du module [`time`{.language-}](https://docs.python.org/fr/3/library/time.html) : [`perf_counter`{.language-}](https://docs.python.org/3/library/time.html#time.perf_counter) qui mesure le temps utilisé par le programme python en secondes, indépendamment des autres programmes tournant sur votre ordinateur (youtube, instagram, etc). On utilise une fonction longue à calculer (ici $1000^{1000^2}$, vous pouvez essayer $2000^{2000^2}$ ou $500^{500^2}$ pour voir les différences de temps)

{% faire %}

1. Exécutez plusieurs fois le code précédent pour voir que l'on passe bien environ 1 seconde à calculer $1000^{1000^2}$.
2. Faites pour dix essais :
   * le temps maximum de calcul
   * le minimum maximum de calcul
   * le temps moyen de calcul

Conclusion ?
{% endfaire %}

### Expérimentations

#### Un temps d'exécution

{% faire %}

Créer un programme principal (dans le fichier `main.py`{.fichier}) qui demande à l'utilisateur un exposant $y$. Ce programme donne ensuite le temps mis pour exécuter $3^y$ avec l'algorithme naïf et avec l'algorithme rapide.

{% endfaire %}

#### Temps max

{% faire %}

Créer un programme principal (dans le fichier `main_temps.py`{.fichier}) qui demande à l'utilisateur un temps en secondes $s$. Ce programme donne ensuite l'entier $y=2^k$ qui est la première puissance de 2 dont le temps mis pour exécuter $3^y$ avec l'algorithme naïf est supérieur à $s$, puis affiche le temps d'exécution du calcul de $3^y$ avec l'algorithme naïf et avec l'algorithme rapide.

{% endfaire %}
{% details "solution" %}

```python
y = 1

t1 = time.perf_counter()
puissance_naif(3, y)
t2 = time.perf_counter()

delta = t2 - t1

while delta < temps:
    y *= 2

    t1 = time.perf_counter()
    puissance_naif(3, y)
    t2 = time.perf_counter()

    delta = t2 - t1

```

{% enddetails %}

#### <span id="mesure-temps"></span> Liste de temps

{% faire %}
Trouver $2^K$ la première puissance de 2 tel que le temps mis pour exécuter l’exponentiation naïve de $3^y$ dure plus de 1 seconde.
{% endfaire %}

{% faire %}
Créez un fichier `temps_exponentiation.py`{.fichier} dans lequel vous créerez trois listes :

* la liste `exposant`{.language-} valant $[1, 2, 2^2, \dots, 2^K]$ (avec $K$ calculé précédemment)
* la liste `temps_naif`{.language-} dont la valeur à l'indice $i$ correspond au temps mis pour calculer `puissance_naif(3, exposant[i])`{.language-}
* la liste `temps_rapide`{.language-} dont la valeur à l'indice $i$ correspond au temps mis pour calculer `puissance_rapide(3, exposant[i])`{.language-}
{% endfaire %}

{% faire %}
Vérifiez que le rapport `temps_naif[i] / temps_rapide[i]`{.language-} tend vers l'infini lorsque $y$ augmente.

{% endfaire %}

## Graphique de la complexité temporelle

On veut maintenant voir l'évolution de la complexité selon la taille de l'exposant. On va pour cela représenter graphiquement cette évolution en utilisant [matplotlib](https://matplotlib.org/).

### temps naïf

{% faire %}
Ajoutez le code suivant au code du fichier `temps_exponentiation.py`{.fichier} pour afficher le temps mis pour afficher le temps mis pour calculer `puissance_naif(3, exposant[i])`{.language-} en fonction de `exposant[i]`{.language-}.

Est-ce conforme à ce qui était attendu ?
{% endfaire %}

```python

fig, ax = plt.subplots(figsize=(20, 5))

ax.set_title("complexités temporelles")
ax.set_xlabel('y')
ax.set_ylabel('temps')

ax.plot(exposant, temps_naif, 'o-')

plt.show()
```

### Temps exponentiel

{% faire %}
Adaptez le code précédent pour afficher le temps mis pour afficher le temps mis pour calculer `puissance_rapide(3, exposant[i])`{.language-} en fonction de `exposant[i]`{.language-}.

Est-ce conforme à ce qui était attendu ?
{% endfaire %}

### Combinaison des deux

{% faire %}
Superposez en un seul graphique les deux courbes (on pourra faire deux plot l'un à la suite des autres).
{% endfaire %}

Le temps mis par l'exponentiation rapide est très inférieur à celui effectué par l'algorithme d'exponentiation naif.

{% faire %}
Utilisez le code de [ce lien](https://matplotlib.org/stable/gallery/spines/multiple_yaxis_with_spines.html#multiple-yaxis-with-spines) pour utiliser `ax.twinx`{.language-} qui permet de partager l'axe des abscisse en ayant deux axes des ordonnées et permettre de voir les 2 courbes,chacune ayant son axe des ordonnées.

Vous pourrez également changer la couleur d'un des dessins en remplaçant le paramètre `'o-'`{.language-} d'un des 2 plot par `'ro-'`{.language-} pour dessiner en rouge (red).

{% endfaire %}

Terminons cette introduction à matplotlib et remarquant que comme l'on multiplie par 2 car abscisse, il pourrait être utile d'utiliser une échelle logarithmique pour l'axe des abscisses.

{% faire %}
Ajoutez la ligne `plt.xscale('log')`{.language-} à votre graphique pour obtenir une échelle logarithmique. Vos points se retrouveront espacés du même espace.

{% endfaire %}
