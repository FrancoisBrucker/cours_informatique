---
layout: layout/post.njk

title: "Projet : mesurer la complexité d'un code"


eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Un moyen efficace de mesurer la complexité d'un code est de mesurer le temps qu'il met à être exécuté. Pour la mesure soit conforme à la complexité il faut que :

1. les instructions basiques durent un temps similaire,
2. l'on ait un moyen efficace de mesurer le temps
3. le système ne doit exécuter que l'algorithme et n'avoir aucun autre [processus concurrent](https://fr.wikipedia.org/wiki/Programmation_concurrente){.externe} (en temps partagé).
4. les paramètres d'entrées doivent  :
  - réaliser le maximum si on cherche à mesurer la complexité (maximum),
  - réaliser le minimum si on cherche à mesurer la complexité minimum,
  - être aléatoire si on cherche à mesurer la complexité moyenne.

## Projet python

On présuppose que vous avec fait les prérequis du cours d'algorithmie, en particulier que vous savez coder en python et/ou que vous avez suivi [le cours d'introduction à python](/cours/coder-et-développer/apprendre-programmation/), en particulier les parties 1 et 2.

{% prerequis %}
- [Installation d'un ide et de modules python](/cours/coder-et-développer/apprendre-programmation/coder-projets/outils/)
- [Écriture de projets informatique](/cours/coder-et-développer/apprendre-programmation/coder-projets/écrire-code/),
- [créer un projet vscode](/cours/coder-et-développer/apprendre-programmation/coder-projets/écrire-code/projet-informatique/)
{% endprerequis %}

{% faire %}
1. Créez-vous un projet vscode,
2. créez un fichier `main.py`{.language-} dans ce projet pour copier/coller puis exécuter le code ci-après.
{% endfaire %}

Attention, selon [notre convention](/cours/coder-et-développer/apprendre-programmation/concepts/fondements-programmation/écrire-code/#convention-exemples/#convention-exemples), les exemples de code qui commencent par `>>>` ont été exécutés directement dans un interpréteur.

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

On gagne un petit peu. Vous verrez que plus la taille du table augmente, plus on gagnera (et pus il est important de conserver ce mécanisme en temps normal puisqu'il permet de libérer de la mémoire non utilisée...)

## Une fonction de mesure

Comme on va utiliser intensivement cette mesure de calcul, on va en faire une fonction qui sera facile à utiliser. Créez un fichier `mesure_temps.py`{.fichier} et copiez-collez y le code suivant :

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

On pourra l'utiliser dans un fichier `main.py`{.language-} :

```python
import mesure_temps

def recherche(T, x):
    for e in T:
        if e == x:
            return True
    return False

T = list(range(100))


t = mesure_temps.calcul(recherche, (T, 42))

print("l'exécution de la fonction à duré :", t, "ns")

```

{% info %}
On utilise la possibilité qu'offre python d'utiliser une liste comme suite de paramètres d'une fonction avec la notation `*args`{.language-}
{% endinfo %}
{% aller %}
[Comment utiliser la fonctionnalité `*args`{.language-}](https://believemy.com/fr/glossaires/python/args){.externe}
{% endaller %}

Dans un terminal :

```sh
❯ python main.py
l'exécution de la fonction à duré : 416 ns
```

{% retenir %}
Gardez vous un fichier contenant les fonctions nécessaires à la mesure du temps. Cela vous permettra de l'inclure dans tous les projet ultérieurs où nous aurons besoin de mesurer la complexité.
{% endretenir %}

## Paramètres

> TBD recherche
> TBD faire sauvegarde fichier (pdf et png)
>   - recherche (retrouve-t-on les graphiques du cours ?)

> min/max/moyenne (plusieurs essai et moyenne).
