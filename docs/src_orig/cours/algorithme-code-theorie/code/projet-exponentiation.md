---
layout: page
title:  "projet / exponentiation "
category: cours
tags: informatique cours 
author: "François Brucker"
---

> [Algorithme, code et théorie]({% link cours/algorithme-code-theorie/index.md %}) / [code]({% link cours/algorithme-code-theorie/code/index.md %}) / [projet : exponentiation]({% link cours/algorithme-code-theorie/code/projet-exponentiation.md %})
>
> **prérequis :**
>
>* [projet : pourcentages]({% link cours/algorithme-code-theorie/code/projet-pourcentages.md %})
>* [étude : l'exponentiation]({% link cours/algorithme-code-theorie/algorithme/etude-exponentiation.md %})
{.chemin}

Ce projet suit l'[étude de l'exponentiation]({% link cours/algorithme-code-theorie/algorithme/etude-exponentiation.md %}). Vous allez vérifier expérimentalement que la complexité de l'[algorithme naïf]({% link cours/algorithme-code-theorie/algorithme/etude-exponentiation.md %}#algo-naif) est en $\mathcal{O}(\mbox{exposant})$ et celle de l'[exponentiation indienne]({% link cours/algorithme-code-theorie/algorithme/etude-exponentiation.md %}#algo-rapide) en $\mathcal{O}(\ln(\mbox{exposant}))$.

## mise en place

### structures

> 1. créez un dossier nommé *"exponentiation"* où vous placerez vos fichiers
> 2. créez un projet vcode dans ce dossier
> 3. créez dans ce dossier les 3 fichiers de la trinité du code :
>    * *"main.py"*
>    * *"exponentiation.py"*
>    * *"test_exponentiation.py"*
>
{.a-faire}

### vscode

1. on vérifie que python est ok : le python utilisé par vscode (exécution via le triangle en haut à droite de la fenêtre) et le terminal doivent être le même :
     * le python utilisé par vscode est marqué dans la [barre de statut](https://code.visualstudio.com/docs/getstarted/userinterface)
     * par défaut, c'est le paramètre `python.defaultInterpreterPath`
     * dans un terminal, la commande `which python3` (mac/unix)/`get-command python.exe` (windows) vous indique quel interpréteur python est utilisé lorsque vous tapez `python`.
2. on vérifie que le linter est actif (en faisant une faute de style)

> On se force, jusqu'à que cela devienne un automatisme, à écrire du code stylé. C'est à dire sans que le linter ne se fâche.
{.a-faire}

### bibliothèques

Nous aurons besoin d'utiliser deux bibliothèques ([matplotlib](https://matplotlib.org/) pour l'affichage des courbes de complexité et [pytest](https://docs.pytest.org/en/6.2.x/) por nos tests). Gérer les bibliothèques python se fait avec l'utilitaire pip que l'on utilise pour interpréteur donné comme ça : `python -m pip`.

> Dans un terminal :
>
> 1. vérifiez les bibliothèques déjà installées pour votre interpréteur : `python -m pip list` (remarquez bien qu'ici `list` est un paramètre de `pip` et non de `python`)
> 2. si besoin installez [matplotlib](https://matplotlib.org/) (`python -m pip install matplotlib`) et [pytest](https://docs.pytest.org/en/6.2.x/) : `python -m pip install pytest`
{.a-faire}

## le code

### algorithme naif

> * dans le fichier *"exponentiation.py"* : implémentez l'algorithme naïf dans une fonction nommée `puissance_naif`
> * dans le fichier *"test_exponentiation.py"* : implémentez les tests de l'algorithme naïf :
>   * vérifiez que les cas simples avec nombre et/ou exposant à 1 fonctionnent
>   * vérifiez qu'un cas général est ok (comme $2^4$ par exemple)
>   * vérifiez que les cas particuliers avec l'exposant et/ou nombre valant 0 fonctionnent
>
> Vérifier que vos tests se lancent bien avec l'erlenmeyer et dans le terminal.
>
{.a-faire}

Pour les tests, on utilisera les règles suivantes :

> Organisation des tests :
>
> * un fichier de test par fichier de code. Chaque fichier de test sea nommé : *"test_[nom du fichier de code].py"* où *[nom du fichier de code]* sera le nom du fichier (ne mettez pas les *[]*)
> * chaque test sera nommé en 3 parties : `test_[nom de la fonction_testée]_[ce que l'on teste]` où `[nom de la fonction_testée]` est le nom de la fonction testée (ne mettez pas les *[]*) et `[ce que l'on teste]` une description succincte (en 1 ou 2 mots max) de ce que l'on teste.
> * un unique `assert` par fonction de test : on ne doit tester qu'**une seule chose** par test
>
{.note}

### algorithme rapide

> * dans le fichier *"exponentiation.py"* : implémentez l'algorithme rapide dans une fonction nommée `puissance_rapide`
> * dans le fichier *"test_exponentiation.py"* : implémentez les tests de l'algorithme rapide en faisant les mêmes tests que pour l'algorithme naïf. :
>
> Vérifier que vos tests se lancent bien avec l'erlenmeyer et dans le terminal.
>
{.a-faire}

> Ne supprimez pas les tests de l'algorithme naïf en créant ceux pour l'algorithme rapide ! Vos deux fonctions DOIVENT être testées.
{.attention}

## complexité temporelle

La seule façon de mesurer expérimentalement la complexité d'un algorithme est de mesurer la [complexité en temps]({% link cours/algorithme-code-theorie/algorithme/complexite-max-min.md %}#temps-dexécution) de celui-ci pour une entrée réalisant la complexité maximale.

Ce n'est cependant pas si simple de mesurer ce temps précisément parce que :

* nous ne sommes pas seul sur la machine, tous les programmes actifs s'exécutent souvent en même temps en se [partageant du temps de processeur](https://fr.wikipedia.org/wiki/Temps_partag%C3%A9) : il est donc difficile de mesurer précisément le temps uniquement pris pour notre algorithme par le processeur.
* python fait des choses sans nous le dire, comme vérifier de temps en temps que les objets ont tous des noms et les supprimer s'ils n'en ont plus (on appelle ça un [ramasse miette](https://fr.wikipedia.org/wiki/Ramasse-miettes_(informatique))) : python lui-même exécute des instructions qui ne sont pas dans notre algorithme.

Mais pour ce qui nous importe, on va dire que c'est pas grave parce que ces *temps parasites* :

* sont négligeables lorsque la taille des entrées deviennent grandes
* ils peuvent être vues comme des constantes dans le calcul de notre complexité : il ne participent donc pas à l'allure générale de la courbe de complexité.

Le protocole de calcul sera alors le suivant :

1. on note l'heure $t_1$ juste avant d'exécuter l'algorithme
2. on exécute l'algorithme
3. on note l'heure $t_2$ juste après exécution l'algorithme

La complexité temporelle sera alors : $\Delta = t_2 - t_1$.

### comment faire

On va utiliser les fonctions simple du module [time](https://docs.python.org/fr/3/library/time.html). Faisons une petite fonction de test pour voir comment on peut utiliser la mesure du temps dans notre programme.

> Créez un fichier *"temp_mesure.py"* (*temp* pour *temporaire*) et mettez y le code suivant :
{.a-faire}

```python
import time

t1 = time.time()
time.sleep(1)
t2 = time.time()

delta = t2 - t1

print(delta)
```

Le code précédent utilise deux fonction du module [time](https://docs.python.org/fr/3/library/time.html) :

* [time.time()](https://docs.python.org/fr/3/library/time.html#time.time) qui rend le nombre de seconde depuis l'[origine des temps informatique](https://fr.wikipedia.org/wiki/Heure_Unix), c'est à dire le 1er janvier 1970
* [`time.sleep(1)`](https://docs.python.org/fr/3/library/time.html#time.sleep) qui ne fait rien pendant un nombre de secondes données en entrée.

> Exécutez plusieurs fois le code précédent pour voir que l'on passe bien environ 1 seconde à ne rien faire.
{.a-faire}

### expérimentations

> Créer un programme principal (dans le fichier *"main.py"*) qui demande à l'utilisateur un exposant $y$. Ce programme donne ensuite le temps mis pour exécuter $3^y$ avec l'algorithme naïf et avec l'algorithme rapide.
{.a-faire}

## graphique de la complexité temporelle

On veut maintenant voir l'évolution de la complexité selon la taille de l'exposant. On va pour cela représenter graphiquement cette évolution en utilisant [matplotlib](https://matplotlib.org/).

### comment faire {#graphique-comment}

[matplotlib](https://matplotlib.org/) peut être une bibliothèque difficile à utiliser. Pour que tout se passe au mieux, on va toujours utiliser la même procédure :

1. on crée les données à représenter
2. créer le graphique avec matplotlib : `fig, ax = plt.subplots(figsize=(20, 5))`
3. ajouter des choses au dessin : plusieurs commandes ajoutant des choses au dessin, c'est à dire `ax`
4. représenter la figure (commande `plt.show()`) ou la sauver dans un fichier

> Créez un fichier *"temp_matplotlib.py"*  et mettez y le code suivant :
{.a-faire}

```python
import matplotlib.pyplot as plt

# 1. création des données
x = []
y = []
for i in range(1000):
    x.append(i)
    y.append(i ** 2)

# 2. créer le dessin (ici ax)
fig, ax = plt.subplots(figsize=(20, 5))

# 2.1 limite des axes
ax.set_xlim(0, 1000)
ax.set_ylim(0, 1000000)

# 2.2 les légendes
ax.set_title("la courbe y=x^2")
ax.set_xlabel('x')
ax.set_ylabel('x^2')

# 3. ajouter des choses au dessin

ax.plot(x, y)

# 4. représenter le graphique
plt.show()

```

> Pour sauver votre graphique au format pdf, vous pouvez remplacez la partie 4 par la ligne : `plt.savefig("graphique.pdf", format="pdf", bbox_inches='tight')`.

### expérimentations {#graphique-test}

> Créez un fichier *"main_graphique.py"* et représentez sur le même graphique (il suffit de mettre deux instructions `ax.plot`) le temps mis par les deux algorithmes pour effectuer l'exponentiation de $ 3^y$  où $y$ varie de $0$ à $100000$ par pas de $1000$.
{.a-faire}

Attention aux constantes de votre code :

> Mantra : pas de [magic numbers](https://en.wikipedia.org/wiki/Magic_number_(programming)#Unnamed_numerical_constants) dans le code.
>
> On remplace les nombres pas des constantes que l'on identifie dans le code par un nom (en majuscules) signifiant.
{.note}
