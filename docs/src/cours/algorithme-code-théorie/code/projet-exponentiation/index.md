---
layout: layout/post.njk 
title: Projet exponentiation

eleventyNavigation:
  key: "Projet exponentiation"
  parent: Code
---

{% prerequis "**Prérequis** :" %}

* [Projet pourcentage](../projet-pourcentages)
* [Etude : exponentiation](../../algorithme/étude-exponentiation)

{% endprerequis %}

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

1. on vérifie que python est ok : le python utilisé par vscode (exécution via le triangle en haut à droite de la fenêtre) et le terminal doivent être le même :
     * le python utilisé par vscode est marqué dans la [barre de statut](https://code.visualstudio.com/docs/getstarted/userinterface)
     * par défaut, c'est le paramètre `python.defaultInterpreterPath`
     * dans un terminal, la commande `which python3` (mac/unix)/`get-command python.exe` (windows) vous indique quel interpréteur python est utilisé lorsque vous tapez `python`.
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

## Le code

### Algorithme naif

{% faire %}

* dans le fichier `exponentiation.py`{.fichier} : implémentez l'algorithme naïf dans une fonction nommée `puissance_naif`{.language-}
* dans le fichier `test_exponentiation.py`{.fichier} : implémentez les tests de l'algorithme naïf :
  * vérifiez que les cas simples avec nombre et/ou exposant à 1 fonctionnent
  * vérifiez qu'un cas général est ok (comme $2^4$ par exemple)
  * vérifiez que les cas particuliers avec l'exposant et/ou nombre valant 0 fonctionnent

Vérifier que vos tests se lancent bien avec l'erlenmeyer et dans le terminal.

{% endfaire %}

Pour les tests, on utilisera les règles suivantes :

{% note %}

Organisation des tests :

* un fichier de test par fichier de code. Chaque fichier de test sea nommé : `test_[nom du fichier de code].py`{.fichier} où *[nom du fichier de code]* sera le nom du fichier (ne mettez pas les *[]*)
* chaque test sera nommé en 3 parties : `test_[nom de la fonction_testée]_[ce que l'on teste]`.{language-python} où `[nom de la fonction_testée]`.{language-python} est le nom de la fonction testée (ne mettez pas les `[]`) et `[ce que l'on teste]`.{language-python} une description succincte (en 1 ou 2 mots max) de ce que l'on teste.
* un unique `assert`.{language-python} par fonction de test : on ne doit tester qu'**une seule chose** par test

{% endnote %}

### Algorithme rapide

{% faire %}

* dans le fichier *"exponentiation.py"* : implémentez l'algorithme rapide dans une fonction nommée `puissance_rapide`
* dans le fichier *"test_exponentiation.py"* : implémentez les tests de l'algorithme rapide en faisant les mêmes tests que pour l'algorithme naïf. :

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

* sont négligeables lorsque la taille des entrées deviennent grandes
* ils peuvent être vues comme des constantes dans le calcul de notre complexité : il ne participent donc pas à l'allure générale de la courbe de complexité.

Le protocole de calcul sera alors le suivant :

{% note "mesurer le temps d'exécution :" %}

1. on note l'heure $t_1$ juste avant d'exécuter l'algorithme
2. on exécute l'algorithme
3. on note l'heure $t_2$ juste après exécution l'algorithme

La complexité temporelle sera alors : $\Delta = t_2 - t_1$.
{% endnote %}

### Comment faire

On va utiliser les fonctions simple du module [time](https://docs.python.org/fr/3/library/time.html). Faisons une petite fonction de test pour voir comment on peut utiliser la mesure du temps dans notre programme.

{% faire %}
Créez un fichier `temps_mesure.py`{.fichier} et mettez y le code suivant :

```python
import time

Print("Avant l'attente")
t1 = time.time()
time.sleep(1)
t2 = time.time()
Print("Après l'attente")

delta = t2 - t1

print("Temps d'attente :", delta)
```

{% endfaire %}

Le code précédent utilise deux fonction du module [time](https://docs.python.org/fr/3/library/time.html) :

* [`time.time()`{.language-}](https://docs.python.org/fr/3/library/time.html#time.time) qui rend le nombre de seconde depuis l'[origine des temps informatique](https://fr.wikipedia.org/wiki/Heure_Unix), c'est à dire le 1er janvier 1970
* [`time.sleep(1)`{.language-}](https://docs.python.org/fr/3/library/time.html#time.sleep) qui ne fait rien pendant un nombre de secondes données en entrée.

{% exercice %}

1. Exécutez plusieurs fois le code précédent pour voir que l'on passe bien environ 1 seconde à ne rien faire.
2. Changez le temps d'attente à 2s et donnez pour dix essais :
   * le temps maximum d'attente
   * le minimum maximum d'attente
   * le temps moyen d'attente

{% endexercice %}

### Expérimentations

#### Un temps d'exécution

{% exercice %}

Créer un programme principal (dans le fichier `main.py`{.fichier}) qui demande à l'utilisateur un exposant $y$. Ce programme donne ensuite le temps mis pour exécuter $3^y$ avec l'algorithme naïf et avec l'algorithme rapide.

{% endexercice %}

#### Liste de temps

{% faire %}
Créez un fichier `temps_exponentiation.py`{.fichier} mettez dans une liste, pour $x = 2$ et  $y$ allant de $0$ à $100000$ par pas de $1000$, le temps mis pour calculer $x^y$ :

* pour l'algorithme naÏf
* pour l'algorithme rapide

Vérifiez que le rapport entre les deux valeurs tant vers l'infini lorsque $y$ augmente.

{% endfaire %}

## Graphique de la complexité temporelle

On veut maintenant voir l'évolution de la complexité selon la taille de l'exposant. On va pour cela représenter graphiquement cette évolution en utilisant [matplotlib](https://matplotlib.org/).

### Comment faire { #graphique-comment }

#### Matplotlib

{% chemin %}
[Tutoriel matplotlib]({{ "/tutoriels/matplotlib" | url }})
{% endchemin %}

[matplotlib](https://matplotlib.org/) peut être une bibliothèque difficile à utiliser. Pour que tout se passe au mieux, on va toujours utiliser la même procédure :

1. on crée les données à représenter
2. créer le graphique avec matplotlib : `fig, ax = plt.subplots(figsize=(20, 5))`
3. ajouter des choses au dessin : plusieurs commandes ajoutant des choses au dessin, c'est à dire `ax`
4. représenter la figure (commande `plt.show()`) ou la sauver dans un fichier

{% faire %}
Créez un fichier `utilisation_matplotlib.py`{.fichier}  et mettez y le code suivant :

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

Vérifiez le code précédent fonctionne et comprenez comment il fonctionne.

{% endfaire %}

{% info %}
Pour sauver votre graphique au format pdf, vous pouvez remplacez la partie 4 par la ligne : `plt.savefig("graphique.pdf", format="pdf", bbox_inches='tight')`.
{% endinfo %}

#### Nos courbes

{% faire %}
Modifiez le code précédant pour représenter la courbe $y=x$ où $y$ varie de $0$ à $100000$ par pas de $1000$.
{% endfaire %}

{% faire %}
Modifiez le code précédant pour représenter la courbe puis la courbe $y=ln(x)$, où $y$ varie de $0$ à $100000$ par pas de $1000$.
{% endfaire %}

{% faire %}
Mettez les courbes sur un même graphique avec 2 figures.
{% endfaire %}

{% faire %}
Mettez les courbes sur un même graphique avec 1 seule figure (il suffit de mettre deux instructions `ax.plot`{.language-}).
{% endfaire %}

### Expérimentations { #graphique-test }

{% faire %}
Créez un fichier `main_graphique.py`{.fichier} et représentez sur le même graphique le temps mis par les deux algorithmes pour effectuer l'exponentiation de $ 3^y$  où $y$ varie de $0$ à $100000$ par pas de $1000$.
{% endfaire %}

Attention aux constantes de votre code :

{% note "**Coding mantra :** [Pas de magic numbers](https://maximilianocontieri.com/code-smell-02-constants-and-magic-numbers)" %}

On remplace les nombres pas des constantes que l'on identifie dans le code par un nom (en majuscules) signifiant.
{% endnote %}
