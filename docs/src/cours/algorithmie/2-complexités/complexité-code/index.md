---
layout: layout/post.njk

title: "Projet : mesurer la complexité d'un code"

eleventyNavigation:
  prerequis: 
    - "/cours/système/ordinateur-programmes-OS/"


eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Un moyen efficace de mesurer la complexité d'un code est de mesurer le temps qu'il met à être exécuté. Pour la mesure soit conforme à la complexité il faut que :

1. les instructions basiques durent un temps similaire,
2. l'on ait un moyen efficace de mesurer le temps
3. le système ne doit exécuter que l'algorithme et n'avoir aucun autre [processus concurrent](https://fr.wikipedia.org/wiki/Programmation_concurrente){.externe} (en temps partagé) (voir prérequis système)
4. les paramètres d'entrées doivent  :
  - réaliser le maximum si on cherche à mesurer la complexité (maximum),
  - réaliser le minimum si on cherche à mesurer la complexité minimum,
  - être aléatoire et uniforme si on cherche à mesurer la complexité moyenne.

## Code python

On présuppose que vous avec fait les prérequis du cours d'algorithmie, en particulier que vous savez coder en python et/ou que vous avez suivi [le cours d'introduction à python](/cours/coder-et-développer/apprendre-programmation/). Selon [notre convention](/cours/coder-et-développer/apprendre-programmation/concepts/fondements-programmation/écrire-code/#convention-exemples/#convention-exemples), les exemples de code qui commencent par `>>>` ont été exécutés directement dans un interpréteur.

On utilisera deux modules très utiles :

- <https://matplotlib.org/>
- <https://numpy.org/>

{% info %}
On vous fera installer tout ça dans un projet juste après. Essayez ici de comprendre la logique ce code.
{% endinfo %}

## Comment mesurer la complexité

Reprenons les 4 conditions que l'on vient d'expliciter.

Nous allons utiliser [les mesures de l'algorithme](../complexité-moyenne/#mesure) recherche que l'on a déjà vu :

```python
def recherche(T, x):
    for e in T:
        if e == x:
            return True
    return False
```

### 1. durée d'une instruction basique

Le code source d'un programme ne correspond pas aux instructions qui sont effectivement effectuées sur l'ordinateur. Selon le type de langages le code source est soit :

- soit converties en [bytecode](https://fr.wikipedia.org/wiki/Bytecode){.externe} (comme [le python](https://www.python.org/){.externe} ou [le java](https://www.java.com/fr/){.externe}), qui sont des instructions compréhensibles par un interpréteur qui les exécute sur l'ordinateur
- directement converti en langage machine (comme [le go](https://go.dev/){.externe} ou encore [le rust](https://rust-lang.org/fr/){.externe}), c'est à dire en [instructions processeurs](https://fr.wikipedia.org/wiki/Jeu_d%27instructions){.externe},

Ces deux approches nécessitent une étape de conversion :

- la première est plus rapide à la conversion (souvent faite au moment même de l'exécution pour le python) mais (un peu) plus lente à l'exécution
- la seconde est plus rapide à l'exécution mais plus longue à la conversion 

Enfin, la première approche permet de créer un code portable, seul l'interpréteur doit-être prévu pour le système (windows, lLinux ou mac) et le type de processeur utilisé (x86 ou arm essentiellement).

#### Instruction python

Pour voir le bytecode python, on peut utiliser [le module `dis`{.language-}](https://docs.python.org/fr/3.15/library/dis.html){.externe} :

```python
import dis

def recherche(T, x):
    for e in T:
        if e == x:
            return True
    return False

print(dis.dis(recherche))
```

Qui va afficher le bytecode associé à la fonction `recherche`{.language-} :

```text
  3           RESUME                   0

  4           LOAD_FAST                0 (T)
              GET_ITER                 0
      L1:     FOR_ITER                13 (to L3)
              STORE_FAST               2 (e)

  5           LOAD_FAST_BORROW_LOAD_FAST_BORROW 33 (e, x)
              COMPARE_OP              88 (bool(==))
              POP_JUMP_IF_TRUE         3 (to L2)
              NOT_TAKEN
              JUMP_BACKWARD           11 (to L1)

  6   L2:     POP_TOP
              POP_TOP
              LOAD_COMMON_CONSTANT     9 (True)
              RETURN_VALUE

  4   L3:     END_FOR
              POP_ITER

  7           LOAD_COMMON_CONSTANT    10 (False)
              RETURN_VALUE
```

Les instructions élémentaires de python ne sont donc pas celles du pseudo-code. De plus, le byte-code correspond à des algorithmes, par exemple l'addition :

```python
>>> import dis
>>> dis.dis("a+b")
  0           RESUME                   0

  1           LOAD_NAME                0 (a)
              LOAD_NAME                1 (b)
              BINARY_OP                0 (+)
              RETURN_VALUE

```

Qui utilise l'instruction de bytecode `BINARY_OP` est un algorithme qui va prendre un temps proportionnel aux nombres de chiffres de ses paramètres. Pour le vérifier on peut utiliser [le module `timeit`{.language-}](https://docs.python.org/fr/3.15/library/timeit.html){.externe} qui va mesurer le temps mis pour exécuter du code python `number`{.language-} fois :

```python
>>> import timeit

>>> timeit.timeit("a + b", setup="a, b = 1, 1", number=10**5)
0.0007226660382002592
>>> timeit.timeit("a + b", setup="a, b = 10**100000, 10**100000", number=10**5)
1.1451560839777812
```


On ne peut donc pas mesurer le temps mis pour chaque instruction du byte-code et sommer le tout car leurs durées dépend de leurs paramètres. Ce qui n'est pas le cas des instructions du processeur.


#### Instructions processeur

Une instruction du processeur va durer un certains nombre de cycle processeur (1 cycle correspond à la vitesse du processeur) fixe pour chaque instruction. Le problème est que chaque type de processeur va avoir son propre jeu d'instructions. Les processeurs x86 (en gros les PC) sont ainsi des [processeur CISC](https://fr.wikipedia.org/wiki/Processeur_%C3%A0_jeu_d%27instructions_%C3%A9tendu){.externe} qui possèdent des instructions complexes et les processeur ARM (portables, tablettes et mac) sont à contrario des [processeurs RISC](https://fr.wikipedia.org/wiki/Processeur_%C3%A0_jeu_d%27instructions_r%C3%A9duit){.externe} avec peu d'instructions.

Enfin, si les instructions ARM sont faites pour toutes durer 1 cycle, les instructions x86 vont varier grandement, de 1 cycle pour test booléen, quelques dizaine de cycle pour une division de deux nombres codés sur 64 bit à plusieurs millions de cycle pour [l'instruction `WBINVD`](https://www.felixcloutier.com/x86/wbinvd){.externe}. 

#### En pratique

En pratique ceci importe peu puisque :

1. on veut de toute façon avoir le code le plus rapide possible,
2. ces variations ne vont influer sur les constantes additives et multiplicatives du code, pas sur l'allure générale de la courbe

Enfin, d'un point de vue algorithmique, l'ordre de grandeur en $\mathcal{O}$ sera conservé quelque soit l'ordinateur sur lequel le code sera exécuté.

{% retenir %}
Même si les instructions processeurs sont très différentes du pseudo-code et que leur durée d'exécution n'est pas homogène, mesurer le temps permet d'avoir l'allure générale de la courbe de complexité.
{% endretenir %}

Trouver un bon algorithme peut faire gagner un ordre de grandeur optimiser le code ne va faire gagner qu'un facteur au mieux multiplicatif. On ne cherchera à optimiser le code processeur qu'après avoir choisi le bon algorithme et, surtout, on ne le fera jamais directement : on laissera le compilateur faire.

### 2. mesure du temps

On possède de deux outils pour mesurer le temps :

- une horloge : <https://docs.python.org/fr/3.15/library/datetime.html>
- un chronomètre : <https://docs.python.org/fr/3.15/library/time.html#time.perf_counter_ns>

Le premier va rendre une date (ce que l'on cherche est un temps et faire des différences de date est compliqué), dépendante du [fuseau horaire](https://fr.wikipedia.org/wiki/Fuseau_horaire){.externe} et  finalement moins précise (à la microseconde prêt) qu'un chronomètre (à la nanoseconde prêt).

On a déjà vu un exemple de mesure d'un code python avec le module `timeit`{.language-}. Il n'est cependant pas pratique car il faut mettre le code sous la forme d'une chaîne à exécuter ou d'une fonction sans paramètre. Il est plus simple d'utiliser le chronomètre [du module `time`{.language-}](https://docs.python.org/fr/3.15/library/time.html){.externe}.

```python
from time import perf_counter_ns

def recherche(T, x):
    for e in T:
        if e == x:
            return True
    return False

T = list(range(100))
début = perf_counter_ns()
recherche(T, 42)
fin = perf_counter_ns()
t = fin - début

print("l'exécution de la fonction à duré :", t, "ns")
```

Ce qui donne chez moi :

```text
l'exécution de la fonction à duré : 50458 ns
```

L'exécution de la fonction `perf_counter_ns()`{.language-} rend un entier qui augmente de 1 toute les nanosecondes. Si on exécute cette méthode juste avant et juste après l'exécution de la fonction `recherche`{.language-} sa différence nous donne le temps d'exécution en nano-secondes.

### 3. Isoler l'algorithme du système

#### Isoler des autres programmes

Si vous relancez le code précédent plusieurs fois, vous constaterez que le temps mis n'est pas une constante :

```python
from time import perf_counter_ns

def recherche(T, x):
    for e in T:
        if e == x:
            return True
    return False

T = list(range(100))

for _ in range(5):
    début = perf_counter_ns()
    recherche(T, 42)
    fin = perf_counter_ns()
    t = fin - début

    print("l'exécution de la fonction à duré :", t, "ns")
```

Par exemple :

```text
l'exécution de la fonction à duré : 24500 ns
l'exécution de la fonction à duré : 3333 ns
l'exécution de la fonction à duré : 1875 ns
l'exécution de la fonction à duré : 2166 ns
l'exécution de la fonction à duré : 2125 ns
```

La première instruction a duré presque 10 fois plus de temps que les 4 suivante. Ceci est du au fait que notre programme python ne tourne pas tout seul sur l'ordinateur, de nombreux autres programme fonctionnent en concurrence, c'est à dire que chacun va tourner une fraction du temps puis passer la main à un autre programme. Cela va si vite qu'on ne se rend pas compte qu'il n'y a qu'un seul programme qui tourne sur 1 processeur.

Notre chronomètre ne mesure donc pas le temps qu'à mis uniquement notre programme pour tourner mais également l'ensemble des programme du système qui tournaient en même temps. Comme tout ces temps sont ajoutés, on peut relancer le programme plusieurs fois et prendre le minimum.

{% retenir %}
Pour minimiser les variations dues aux exécutions d'autres programmes concurrent, on mesure l'exécution plusieurs fois (typiquement 10 fois, mais on peut diminuer ce temps si l'exécution est longue de notre mesure est longue) et on prend le minimum.
{% endretenir %}

Le code devient :

```python
from time import perf_counter_ns

def recherche(T, x):
    for e in T:
        if e == x:
            return True
    return False

T = list(range(100))

t = None
for _ in range(10):
  début = perf_counter_ns()
  recherche(T, 42)
  fin = perf_counter_ns()
  delta = fin - début
  if (t is None) or (delta < t):
    t = delta

print("l'exécution de la fonction à duré :", t, "ns")
```

Et il donne chez moi :

```text
l'exécution de la fonction à duré : 500 ns
```

{% info %}
Notez qu'on a initialisé le temps à `None`{.language-} pour toujours prendre la première mesure qui donnera une valeur entière à `t`{.language-}

{% endinfo %}

#### Isoler de python

Maintenant que notre programme est isolé du reste du système une dernière amélioration serait de l'isoler de python lui-même. En effet, python fait épisodiquement un état des lieux des différentes variables pour supprimer celles qui ne sont plus utilisées. Ce mécanisme s'apple [le ramasse-miettes](https://fr.wikipedia.org/wiki/Ramasse-miettes_(informatique)){.externe} et est un mécanisme fondamental qui permet de minimiser la mémoire utilisées. En règle générale il ne faut pas l'enlever mais dans notre cas cela peut être utile de voir uniquement la complexité de la fonction. Pour cela on utilise [le module `gc`{.language-}](https://docs.python.org/fr/3.15/library/gc.html) qui ous permet de controller ce mécanisme.

Le code devient maintenant :


```python
from time import perf_counter_ns
import gc

def recherche(T, x):
    for e in T:
        if e == x:
            return True
    return False

T = list(range(100))

gc_actif = gc.isenabled()
if gc_actif:
    gc.disable()

t = None
for _ in range(10):
  début = perf_counter_ns()
  recherche(T, 42)
  fin = perf_counter_ns()
  delta = fin - début
  if (t is None) or (delta < t):
    t = delta

if gc_actif:
    gc.enable()

print("l'exécution de la fonction à duré :", t, "ns")
```
{% info %}
Notez que l'on ne réactive le ramasse-miette que s'il était actif avant notre manipulation (on stocke l'état courant dans la variable `gc_actif`{.language-}).
{% endinfo %}

Qui donne chez moi :

```text
l'exécution de la fonction à duré : 459 ns
```

On gagne un petit peu. Vous verrez que plus la taille du table augmente, plus on gagnera (et plus il est important de conserver ce mécanisme en temps normal puisqu'il permet de libérer de la mémoire non utilisée...)

## Une fonction de mesure

Comme on va utiliser intensivement cette mesure de calcul, on va en faire une fonction qui sera facile à utiliser :

<span id="calcul"></span>

```python
from time import perf_counter_ns
import gc

def calcul(f, f_params, rep=10):
    
    gc_actif = gc.isenabled()
    if gc_actif:
        gc.disable()

    t = None
    for _ in range(rep):
        début = perf_counter_ns()
        f(*f_params)
        fin = perf_counter_ns()

        delta = fin - début
        if (t is None) or (delta < t):
          t = delta

    if gc_actif:
        gc.enable()
    
    return t
```

{% info %}
On utilise la possibilité qu'offre python d'utiliser une liste comme suite de paramètres d'une fonction avec [la notation `*args`{.language-}](https://believemy.com/fr/glossaires/python/args){.externe}.
{% endinfo %}

On pourra l'utiliser ainsi :

```python

T = list(range(100))
t = calcul(recherche, (T, 42))
print("l'exécution de la fonction à duré :", t, "ns")

```

Ce qui donne chez moi :

```text
l'exécution de la fonction à duré : 416 ns
```

{% retenir %}
Gardez vous un fichier contenant les fonctions nécessaires à la mesure du temps. Cela vous permettra de l'inclure dans tous les projet ultérieurs où nous aurons besoin de mesurer la complexité.
{% endretenir %}

## Complexité maximum et minimum

Le but est de pouvoir mesurer la complexité maximale, minimale et moyenne d'un algorithme codé. [La complexité dépendant d'un paramètre](../définitions-mesure-O/définitions/#complexité) il faudra le faire varier pour déterminer la courbe de complexité (pour notre exemple de l'algorithme recherche, le paramètre était la longueur du tableau). 

Pour que tout soit homogène, on crée alors deux fonctions dédiées prenant uniquement ce paramètre plutôt que les différents paramètres initiaux de l'algorithme :

```python 
def calcule_max(n):
    T = list(range(n))
    return calcul(recherche, (T, -1))


def calcule_min(n):
    T = list(range(n))
    return calcul(recherche, (T, 0))
```

La complexité max est en effet atteinte pour la recherche d'un élément qui n'est pas dans le tableau (ici -1) et la complexité minimale est atteinte pour la recherche du premier élément du tableau.

{% retenir %}
Pour le calcul des complexités min et max on se crée de fonctions ayant uniquement comme paramètre celui utilisé pour le calcul de la complexité et on adapte les entrées de l'algorithme initial qu calcul recherché.
{% endretenir %}

On cherche à représenter graphiquement la durée par rapport au paramètre. Pour que notre courbe soit représentative :

- il faut qu'il y ait assez de points : on se fixe ce nombre `K`{.language-},
- il faut que le paramètre puisse varier grandement sans que cela ne prenne trop de temps : on se fixe un temps de calcul `T_MAX`{.language-} maximum.

Pour trouver rapidement le nombre `N_max`{.language-} correspondant à `T_MAX`{.language-}, on utilise l'algorithme suivant, qui double $n$ à chaque itération et s'arrête au premier $n$ dont la mesure prend plus que le temps maximum alloué :

```python
def calcul_n_max(f_calcul_temps_complexité, n_min, T_MAX):
    n_max = n_min
    while f_calcul_temps_complexité(n_max) < T_MAX:
        n_max *= 2

    return n_max
```

Je trouve un `N_max = 16777216`{.language-} avec un temps max de 0.1s et le code suivant :

```python
N_min = 1

T_max = 10 ** 8  # 0.1s
N_max = calcul_n_max(calcule_max, N_min, T_max)
print("Pour un dixième de seconde N_max =", N_max)

```

On ne peut pas se permettre de mesurer le temps pris pour tous les tableaux de taille 1 à N_max = 16777216, cela prendrait trop de temps et serait inutile. On utilise [la fonction `linspace`{.language-}](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html){.externe} du module numpy qui rend un découpage d'un intervalle donné. Si on veut un découpage en `K`{.language-} points d'un intervalle allant de `N_min`{.language-} à `N_max`{.language-}, en gardant le fait que ce sont des entiers :

```python
import numpy as np

K = 10
Ns = [int(x) for x in np.linspace(N_min, N_max, K)]

```

{% retenir %}
Fixez-vous une taille min et max de paramètre et donnez-vous un nombre d'expérimentation $K$ pour déterminer les $K$ différentes mesures de temps à faire. 

Déterminez les tailles min et max de paramètre **une** fois, ne refaite pas le calcul à chaque lancement.
{% endretenir %}

On peut enfin calculer les temps min et max :

```python
for n in Ns:
    print("taille", n)
    print("     max :", calcule_max(n))
    print("     min :", calcule_min(n))

```

Ce qui donne chez moi :

```text
taille 1
     max : 83
     min : 42
taille 14913081
     max : 131349625
     min : 42
taille 29826162
     max : 262013875
     min : 83
taille 44739243
     max : 394027000
     min : 83
taille 59652324
     max : 526060458
     min : 83
taille 74565404
     max : 655763916
     min : 42
taille 89478485
     max : 795593000
     min : 41
taille 104391566
     max : 930963834
     min : 83
taille 119304647
     max : 1064934541
     min : 83
taille 134217728
     max : 1199735750
     min : 83
```

{% info %}
Les derniers calculs peuvent prendre du temps puisque l'on fait 10 fois un calcul qui va prendre de l'ordre de .1s. Si vous voulez accélérer le process :

- soit diminuez le nombre maximum d'éléments dans le tableau,
- soit diminuez le nombre de répétition (passer de 10 à 5 par exemple),
- soit les deux.

{% endinfo %}

## Complexité en moyenne

Pour calculer la complexité en moyenne, il faut chercher un entier quelconque du tableau ou pas. On peut par exemple utiliser le code suivant, utilisant la fonction `randrange`{.language-} [du module random](https://docs.python.org/fr/3/library/random.html){.externe} :

```python
import random

def calcule_moyenne(n, rep=10):
    T = list(range(n))
    return calcul(recherche, (T, random.randrange(-1, n)))
```

Mais ceci n'est pas suffisant car il peut y avoir de grandes variations selon l'élément à rechercher. Ci-après le temps pris pour un tableau de 100000 éléments, on va de 2208ns à prêt de 500000ns :

```text
409500.0
488959.0
146625.0
93791.0
225209.0
422500.0
22125.0
317041.0
227875.0
2208.0
```

La solution est de moyenner le résultat (par défaut 10 essais) :

```python
def calcule_moyenne(n, rep=10):
    T = list(range(n))
    t = calcul(recherche, (T, random.randrange(-1, n)))
    for _ in range(rep-1):
        t += calcul(recherche, (T, random.randrange(-1, n)))
    return t / rep

```

On peut alors ajouter la moyenne à notre calcul :

```python
for n in Ns:
    print("taille", n)
    print("     max :", calcule_max(n))
    print("     moy :", calcule_moyenne(n))
    print("     min :", calcule_min(n))

```

Chez moi j'obtiens :

```text
taille 1
     max : 83
     moyenne : 58.1
     min : 41
taille 14913081
     max : 129418084
     moyenne : 62261433.3
     min : 42
taille 29826162
     max : 259101583
     moyenne : 114150833.3
     min : 42
taille 44739243
     max : 388659917
     moyenne : 163993899.7
     min : 42
taille 59652324
     max : 516515208
     moyenne : 210178308.4
     min : 42
taille 74565404
     max : 645720458
     moyenne : 307273212.3
     min : 41
taille 89478485
     max : 785189500
     moyenne : 503277858.3
     min : 42
taille 104391566
     max : 915702833
     moyenne : 420030974.9
     min : 42
taille 119304647
     max : 1045916584
     moyenne : 506352900.1
     min : 42
taille 134217728
     max : 1185341667
     moyenne : 497359804.2
     min : 41
```


{% info %}
Les derniers calculs peuvent prendre du temps puisque l'on fait 10x un calcul qui va prendre de l'ordre de 10 x .1s. Si vous voulez accélérer le process :

- soit diminuez le nombre maximum d'éléments dans le tableau,
- soit diminuez le nombre de répétition (passer de 10 à 5 par exemple),
- soit diminuez le nombre d'essais pour la moyenne (passer de 10 à 5 par exemple),
- soit deux des trois,
- soit les trois.
{% endinfo %}

## Représentation graphique

Enfin, on peut représenter graphiquement les résultats. Pour cala, il faut commencer pas stocker les résultat de nos mesures et pas juste les afficher :


```python
c_min = []
c_moy = []
c_max = []
for n in Ns:
    print("taille", n)
    c_max.append(calcule_max(n))
    print("     max :", c_max[-1])
    c_moy.append(calcule_moyenne(n))
    print("     moy :", c_moy[-1])
    c_min.append(calcule_min(n))
    print("     min :", c_min[-1])

```

Et on utilise la fonction de dessin suivante qui affiche les 3 courbes de complexité :

```python
import matplotlib.pyplot as plt

def affiche_complexité(N, c_min, c_moy, c_max):
    _, ax = plt.subplots(figsize=(20, 5))

    ax.set_title("complexités temporelles")
    ax.set_xlabel("taille du tableau")
    ax.set_ylabel("temps de calcul en ns")

    p1, = ax.plot(N, c_min, 'o-', label="min")
    p2, = ax.plot(N, c_moy, 'o-', label="moyenne")
    p3, = ax.plot(N, c_max, 'o-', label="max")


    ax.legend(handles=(p1, p2, p3))

    plt.show()
```


## Fichiers finaux

On a séparé notre code en 3 fichiers :

- `algorithmes.py`{.language-} qui contient le code à mesurer et `test_algorithmes.py`{.language-} qui contient les lests,
- `mesure_temps.py`{.language-} qui contient les fonctions utiles pour les mesures,
- `main.py`{.language-} qui est le programme principal.

### `algorithmes.py`{.language-}

```python
import random

from mesure_temps import calcul

def recherche(T, x):
    for e in T:
        if e == x:
            return True
    return False


def calcule_max(n):
    T = list(range(n))
    return calcul(recherche, (T, -1), rep=5)


def calcule_min(n):
    T = list(range(n))
    return calcul(recherche, (T, 0))


def calcule_moyenne(n, rep=10):
    T = list(range(n))
    t = calcul(recherche, (T, random.randrange(-1, n)), rep=5)
    for _ in range(rep-1):
        t += calcul(recherche, (T, random.randrange(-1, n)), rep=5)
    return t / rep
```

### `mesure_temps.py`{.language-}

```python
from time import perf_counter_ns
import gc

import matplotlib.pyplot as plt


def calcul(f, f_params, rep=10):
    
    gc_actif = gc.isenabled()
    if gc_actif:
        gc.disable()

    t = None
    for _ in range(rep):
        début = perf_counter_ns()
        f(*f_params)
        fin = perf_counter_ns()

        delta = fin - début
        if (t is None) or (delta < t):
          t = delta

    if gc_actif:
        gc.enable()
    
    return t

def calcul_n_max(f_calcul_temps_complexité, n_min, T_MAX):
    n_max = n_min
    while f_calcul_temps_complexité(n_max) < T_MAX:
        n_max *= 2

    return n_max

def affiche_complexité(N, c_min, c_moy, c_max):
    _, ax = plt.subplots(figsize=(20, 5))

    ax.set_title("complexités temporelles")
    ax.set_xlabel("taille du tableau")
    ax.set_ylabel("temps de calcul en ns")

    p1, = ax.plot(N, c_min, 'o-', label="min")
    p2, = ax.plot(N, c_moy, 'o-', label="moyenne")
    p3, = ax.plot(N, c_max, 'o-', label="max")


    ax.legend(handles=(p1, p2, p3))

    plt.show()
```

### `main.py`{.language-}

Avec une réduction du nombre de répétitions et un temps max de 1 centième de seconde :

```python
import numpy as np

from mesure_temps import calcul_n_max, affiche_complexité
from algorithmes import calcule_max, calcule_min, calcule_moyenne

N_min = 1

T_max = 10**7  # 0.01s
N_max = calcul_n_max(calcule_max, N_min, T_max)
print("Pour", T_max / 10**9, "seconde, N_max =", N_max)

K = 6
Ns = [int(n) for n in np.linspace(N_min, N_max, K)]
print(Ns)

c_min = []
c_moy = []
c_max = []
for n in Ns:
    print("taille", n)
    c_max.append(calcule_max(n))
    print("     max :", c_max[-1])
    c_moy.append(calcule_moyenne(n))
    print("     moy :", c_moy[-1])
    c_min.append(calcule_min(n))
    print("     min :", c_min[-1])

affiche_complexité(Ns, c_min, c_moy, c_max)
```
