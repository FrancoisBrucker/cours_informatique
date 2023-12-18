---
layout: layout/post.njk 
title: "Mise en œuvre d'un projet informatique"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"

---

<!-- début résumé -->

Définir et conduire un projet informatique. On y montrera les outils nécessaire à tout projet : un linter et une bibliothèque de tests.

<!-- end résumé -->

Un projet informatique a un début, lorsque l'on crée le dossier qui va le contenir, mais il n'a que rarement de fin : il y a toujours des fonctionnalités à ajouter et des bugs à corriger. Enfin, et c'est le plus important, un code est fait pour être utilisé.

De ces deux constatations, on en déduit trois règles fondamentales d'un code utile. Il faut qu'il soit :

* juste pour des utilisateurs puissent s'en servir
* facilement modifiable pour que l'ajout et la correction de fonctionnalités soient aisés
* lisible pour soi et pour les autres membres de l'équipe de développement

Le langage d'application n'a que peu d'intérêt en soit. On choisit celui qui est le plus adapté à notre but. Ici, on utilisera le python mais tout ce qu'on verra est transposable pour tout autre langage sérieux. L'éditeur de texte que l'on utilisera sera vscode. Il en existe d'autres très bien aussi et tout ce qu'on verra avec vscode (les raccourcis claviers, et aides au développement) sont transposables à d'autres éditeurs en lisant la doc.

{% note %}
Écrire du code nécessite de nombreuses automatisations et aides pour que ce ne soit pas pénible, ne vous privez pas d'outils parce que vous n'avez pas envie d'apprendre de nouvelles choses et que *ça suffit bien pour ce que je veux faire*. Vous allez au final perdre plus de temps que l'apprentissage initial (ce qui est tarte).
{% endnote %}

## Un projet

On va créer un projet pour comprendre comment tout ça fonctionne.

Nous allons préparer le projet dans lequel nous allons coder. Ceci se fait avec vscode en ouvrant un dossier. Ce dossier sera le départ de votre projet et s'appelle *workspace*.

{% faire %}

1. Commencez par créer le dossier `hello-dev`{.fichier} dans un explorateur de fichier
2. dans vscode, choisissez : "*fichier > ouvrir le dossier...*" puis naviguez jusqu'à votre dossier `hello-dev`{.fichier}. On vous demande si vous faites confiances aux auteurs, puisque c'est vous dites oui.

{% endfaire %}

{% info %}
Lorsque l'on code et que l'on ne veut pas de problèmes en développement, les noms de fichiers et de dossier doivent êtres **sans espaces et sans accents**.
{% endinfo %}

{% note "Un projet informatique est contenu **dans un dossier**"  %}

Ce n'et pas juste un ensemble de fichiers.

Dans vscode, il faudra toujours choisir d'ouvrir un dossier lorsque l'on travaille sur un projet.
{% endnote %}

### Fichier python

On va créer notre premier fichier python :

{% faire %}

1. allez dans *menu Fichier > Nouveau Fichier*
2. et sauvez le de suite : *menu Fichier > Enregistrer* avec le nom `main.py`{.fichier}.

{% endfaire %}

Vscode à compris que c'était du python, il l'écrit dans la barre de statut (la dernière ligne, en bleu, de la fenêtre vscode, voir [user interface](https://code.visualstudio.com/docs/getstarted/userinterface)).

{% info %}

Si vous n'avez pas suivi le tuto d'installation de vscode et son interaction avec python, il vous demandera peut-être de :

1. choisir un interpréteur : prenez le python de votre distribution
2. choisir un linter : supprimer la fenêtre de warning, on fera ça plus tard.
3. choisir des tests : supprimer la fenêtre de warning, on fera ça plus tard.

{% endinfo %}

### Exécution d'un fichier

{% faire %}

Écrivez dans le fichier `main.py`{.fichier} :

```python
print("bonjour les gens !")

```

{% endfaire %}

En vous rappelant ce que vous avez vu dans [le tutorial python et vscode](/tutoriels/éditeur-vscode/python#exécuter-programme){.interne} :

{% faire %}
Exécutez le code de deux manières différentes :

* avec le terminal
* avec le petit triangle

{% endfaire %}

## <spans id="linter"></span> Du joli code

Vous allez passer beaucoup de temps à lire du code, le votre et celui des autres. Il est important que ce soit facile. Pour cela il faut que le style de code soit cohérent. Python donne des règle de style, c'est ce qu'on appelle la [PEP8](https://www.python.org/dev/peps/pep-0008/).

### Linter

Un linter est un programme permettant de signaler les erreurs de style pour les corriger. Installer un linter vous permet de vous familiariser avec les règles d'un joli code.

Il existe de nombreux linter, nous allons utiliser [flake8](https://flake8.pycqa.org/en/latest/) qui s'intègre bien avec vscode.

#### Installation

{% aller %}
[Installer flake8](/tutoriels/vsc-python-suppléments/flake8){.interne}.
{% endaller %}

#### Utilisation

Vérifions qu'il remarque bien les fautes :

{% faire %}

Modifiez le fichier `main.py`{.fichier} pour écrire :

```python

print ("bonjour les gens !")

```

{% endfaire %}

Une fois le fichier sauvé vous devriez voir que l'espace entre print et la parenthèse est souligné en rouge :

![vsc-linter-souligne](code-vsc-linter.png)

On peut cliquer sur la status-bar pour voir l'erreur ou passer le curseur sur la partie rouge :

{% note "**style** : **NE JAMAIS METTRE D'ESPACE APRÈS UN NOM DE FONCTION**" %}
Parce qu'on ne voit pas immédiatement si c'est une fonction ou un nom de variable.
{% endnote %}

Vous devriez peut-être aussi avoir la parenthèse de fin souligné en jaune. C'est parce que la dernière ligne de votre fichier n'est pas vide. Si ce n'est pas le cas, c'est que vous avez bien que 2 lignes dans votre fichier, la seconde étant vide.

{% note %}
**style** : **la dernière ligne d'un fichier python est vide**
{% endnote %}

{% note %}
Prenez l'habitude d'écrire du code sans aucune erreur de style. Et, surtout, **apprenez pourquoi cette règle existe**. Suivre une règle sans comprendre pourquoi elle existe n'est pas efficace... Parce qu'on ne sait pas s'il faut la suivre ou pas.
{% endnote %}

Tout au long de ce projet et des prochains, il faut faire en sorte qu'il n'y ait jamais d'erreur de style. Soyez donc vigilant au début avant que cela devienne naturel.

### black

Il existe des outils permettant de formatter automatiquement le code, comme l'utilitaire [black](https://github.com/psf/black) par exemple.

{% aller %}
[Installer black](/tutoriels/vsc-python-suppléments/black){.interne}.
{% endaller %}

Une fois black installé, vous pouvez l'utiliser depuis un terminal ou depuis vscode.

## Séparer code et main

{% note "Un projet c'est trois choses d'égale importance :" %}

* le code : les fonctions utilisées
* le main : le programme principal, c'est ce qu'on exécute lorsque veut faire marcher le projet
* les tests : ce qui garantit que le code fonctionne

{% endnote %}

Pour séparer les différentes parties vous allez :

{% faire %}
Créez deux fichiers dans notre projet, l'un nommé `le_code.py`{.fichier} qui contiendra notre code et l'autre nommé `main.py`{.fichier} qui sera notre programme principal
{% endfaire %}

Fichier `le_code.py`{.fichier} :

```python
def bonjour():
    return "Bonjour les gens !"

```

Fichier `main.py`{.fichier} :

```python
from le_code import bonjour

print(bonjour())

```

On a importé le nom `bonjour` défini dans le fichier `le_code.py`{.fichier} grâce à un import. L'autre façon aurait été d'importer juste le fichier code. On aurait alors eu :

```python
import le_code

print(le_code.bonjour())

```

La notation pointée se lit alors : exécute le nom `bonjour` définit dans `le_code.py`{.fichier}.

{% aller %}
[Cours sur les modules python]({{"/cours/utiliser-python/modules" | url }}){.interne} pour plus d'information.
{% endaller %}

{% attention %}
Ne **jamais jamais jamais** utiliser `from le_code import *` qui importe tous les noms définis dans `le_code.py`{.fichier}. On ne sait pas vraiment ce qui a été importé en lisant `le_code.py`{.fichier}. : notre code n'est pas lisible ! Le gain d'écriture de `*` plutôt que `bonjour` sera perdu au centuple plus tard lorsque l'on devra chercher dans tous les fichiers du projet où l'on a bien pu définir `bonjour`...
{% endattention %}

{% note %}
Comme on va passer plus de temps à lire/comprendre du code qu'à l'écrire, il faut **optimiser la lecture et non l'écriture de code**.  On préférera toujours **la lisibilité à la rapidité**.
{% endnote %}

## Tests

Les tests permettent de vérifier que notre code fonctionne. Ils font partie du programme et on peut s'y référer quand on veut. Lorsque l'on modifie le code, on pourra toujours exécuter **tous les tests** pour vérifier que notre programme fonctionne aussi bien qu'avant.

### La commande assert

On utilise en python la commande [assert](https://docs.python.org/fr/3/reference/simple_stmts.html#the-assert-statement). Elle fonctionne ainsi :

```text
assert <expression logique>
```

Si l'expression logique est vraie, le programme continue sans rien dire et si l'expression logique est fausse, le programme s'arrête avec l'erreur : `AssertionError`.

Essayons ça avec la plus simple des expressions logiques : `True`

{% faire %}
Créez un fichier nommé `test_projet.py`{.fichier} qui contiendra le code :

```python
print("avant l'assert")

assert True

print("après l'assert")

```

Exécutez-le.

{% endfaire %}

Lorsque vous exécutez ce fichier, vous devez obtenir le résultat suivant :

```text
avant l'assert
après l'assert
```

La condition logique étant vraie, la commande `assert` n'a rien fait.

Changeons ça en mettant une condition logique fausse :

{% faire %}
Modifiez `test_projet.py`{.fichier} pour qu'il contienne le code :

```python
print("avant l'assert")

assert False

print("après l'assert")

```

Exécutez le fichier `test_projet.py`{.fichier}.

{% endfaire %}

Vous devez obtenir le résultat suivant :

```text
avant l'assert
Traceback (most recent call last):
  File "/Users/fbrucker/Documents/temp/hello-dev/test_projet.py", line 3, in <module>
    assert False
AssertionError
```

La première ligne a bien été exécutée (on voit écrit `avant l'assert`), puis le programme a planté. La condition logique étant fausse, la commande `assert` a levé une exception nommée `AssertionError` qui a stoppé l'exécution du programme. La ligne `print("après l'assert")` n'a pas été exécutée.

D'habitude, nos expressions logiques vérifie qu'un comportement observé (l'exécution d'une fonction) est conforme au comportement théorique (le résultat qu'on aimerait avoir). Pour ne pas se perdre on range ce test dans une fonction dont le nom décrit le test. Par exemple, testons la somme :

{% faire %}
Modifiez `test_projet.py`{.fichier} pour qu'il contienne le code :

```python

def test_somme_neutre():
    tête_a_toto = 0
    assert 0 + 0 == tête_a_toto

def test_somme_1_plus_0():
    assert 0 + 1 == 1


def test_somme_1_plus_2():
    assert 1 + 2 == 3
 
```

Exécutez le fichier `test_projet.py`{.fichier}.

{% endfaire %}

Pour tester la somme, j'ai décidé de faire 3 tests :

* le cas le plus simple où il ne se passe rien (`0 + 0 = 0`{.language-})
* un cas simple (`0 + 1 = 1`{.language-})
* un cas général (`1 + 2 = 3`{.language-})

Lorsque l'on exécute ce code, il ne se passe rien. Est-ce bon signe ?

{% faire %}
Modifiez la fonction `test_somme_neutre`{.language-} du fichier `test_projet.py`{.fichier} pour qu'elle soit égale à  :

```python
# ...

def test_somme_neutre():
    tête_a_toto = 0
    assert 0 + 0 == 42

# ...
```

Exécutez le fichier `test_projet.py`{.fichier}.

{% endfaire %}
{% info %}
On a coutume de mettre des `# ...`{.language-} pour dire que le reste du code du fichier n’est pas changé.

Ce n’est pas la peine de les copier/coller.
{% endinfo %}

Le code s'exécute encore encombre. Bon, là, c'est pas normal car `0 + 0` ne peut être égal à `42`.

La raison est que `test_projet.py`{.fichier} définit des fonctions mais **il ne les exécute jamais**. Les trois fonctions de test sont définies mais jamais utilisées.

On a donc 2 choix :

* exécuter les fonctions dans le fichier après les avoir définies
* utiliser un module que le fait pour nous

Nous allons utiliser la seconde option avec le module [Pytest](https://docs.pytest.org).

### Installation de la bibliothèque de tests

{% aller %}
[Installer la bibliothèque de test avec vsc](/tutoriels/vsc-python-suppléments/pytest){.interne}
{% endaller %}

### Utilisation de la bibliothèque de tests

On y reviendra à de nombreuses reprises :

{% note %}
Les tests sont la pierre angulaire d'une bonne programmation : ils garantissent le fonctionnement de votre code et qu'[il ne peut régresser](https://blog.octo.com/via-negativa-tdd-et-la-conception-de-logiciel/).
{% endnote %}

Les tests sont de petites fonctions dont le but est de *tester* une fonctionnalité du programme (souvent le résultat de l'exécution d'une fonction). Le test consiste en une [assertion](https://fr.wikipedia.org/wiki/Assertion) que l'on veut être vraie si que le code fonctionne. Si l'assertion est fausse c'est qu'il y a un bug.

{% faire %}
Tapez la commande `python -m pytest` dans un terminal.
{% endfaire %}
{% info %}
Il vous faut utiliser le python de vscode, son nom peut donc changer.
{% endinfo %}

Vous devriez obtenir quelque chose du genre :

![vsc-pytest](code-projet-pytest.png)

{% faire %}
Corrigez le test de `test_projet.py`{.fichier} qui rate et re-exécutez le code pour voir les 3 tests réussir.

{% endfaire %}

Que fait pytest :

{% note %}
Pytest exécute toutes les fonctions commençant par `test_` de tous les fichiers commençant par `test_` d’un projet.
{% endnote %}

On peut aussi exécuter les tests directement avec vscode. Pour cela, cliquez sur [le petit erlenmeyer](https://code.visualstudio.com/docs/python/testing#_configure-tests). Vous pourrez ensuite :

1. découvrir les tests du projet
2. exécuter tous les tests
3. n'exécuter qu'un seul test

![vsc-pytest-erlenmeyer](code-projet-pytest-erlenmeyer.png)

### Test du projet

Notre projet contient pour l'instant une fonction qui rend une constante. Tester une constante n'a pas de sens, modifions notre code pour que notre fonction ait plus de sens :

{% faire %}
Modifiez le fichier `le_code.py`{.fichier} pour qu'il contienne le code :

```python
def bonjour(nom):
    return "bonjour " + nom + " !"

```

{% endfaire %}

On peut maintenant remplacer les tests :

{% faire %}
Modifiez le fichier `test_projet.py`{.fichier} pour qu'il contienne le code :

```python
from le_code import bonjour


def test_bonjour():
    assert bonjour("monde") == "bonjour monde !"
```

Exécutez les tests pour vérifier que votre code fonctionne.

{% endfaire %}

Maintenant que les tests passent, on peut modifier le programme principal.

{% faire %}
Modifiez le fichier `main.py`{.fichier} pour qu'il contienne le code :

```python
from le_code import bonjour

print(bonjour("monde"))

```

Exécutez le programme principal.

{% endfaire %}

Félicitations, vous avez fait votre premier projet fonctionnel !

## Les fichiers

Les trois fichiers du projet final sont [disponibles](https://github.com/FrancoisBrucker/cours_informatique/tree/main/docs/src/cours/algorithme-code-théorie/code/projet-hello-dev/hello-dev)
