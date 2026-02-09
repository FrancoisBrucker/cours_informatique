---
layout: layout/post.njk

title: "sujet Test 2 : programmation"
authors:
  - François Brucker
---

## Barème

Outre les questions, j'ai noté le fait que je puisse :

- lancer le projet en tapant `python main.py` et qu'il s'exécute sans planter. 
- exécuter les tests en tapant `python -m pytest` et que les tests s'exécutent. Des tests peuvent échouer (le correcteur voit sur quoi vous travailliez, c'est ok) mais votre code doit s'exécuter sans erreur de python. 

{% attention2 "**À retenir**" %}
Vous devez toujours vous assurer d'avoir un projet fonctionnel, même si vous n'avez pas fini le test. Si vous  êtes entrain d'écrire une fonction et qu'elle n'est pas terminée ne l'incluez pas dans le programme principal. Il est en revanche tout à fait autorisé de laisser des tests qui échouent lorsque l'on est entrain de coder une fonction du moment que les tests s'exécutent.
{% endattention2 %}

### Ventilation des points

La note du test est sur 7 points répartis comme suit :

- 2pt pour la question 1 (1 point pour le code ; 1 point pour les tests)
- 2pt pour la question 2 (1 point pour le code ; 1 point pour les tests)
- 2pt pour la question 3 (1 point pour le code ; 1 point pour les tests)
- 1pt pour du code fonctionnel `python main.py` et `python -m pytest` doivent s'exécuter sans problème

La note sur $20$ finale est obtenue en multipliant la note sur 7 par $3$

{% note "**Objectif du test**" %}

En 15 minutes :

- **un élève moyen** fait la 1 première question parfaitement, possède du code fonctionnel et à entamé la seconde question ce qui garantit le 10
- **un bon élève** fait les 2 premières questions parfaitement et possède du code fonctionnel ce qui vaut 15.
- **un très bon élève** fait plus que les 2 premières questions parfaitement.

{% endnote %}

### Ventilation des notes

|note/20  | < 10 | [10, 14]  | ]14, 16]  | ]16, 18] | ]18, 20] | >20 |
|---------|------|---------|-------------|----------|----------|-----|
|nombre   |   8  |    8    |     9       |  10      |    3     | 4   |
|rang min |  42  |    34   |    26       |10        |     5    | 1   | 

- moyenne : 14/20 (4.67/7)
- écart-type : 5.15/20 (1.72/7)
- médiane : 15/20 (5/7)


Je suis globalement (**très**) satisfait de votre travail, vous avez travaillé et intégré le cours : c'est bien ([pourvu que ça dure](https://www.youtube.com/watch?v=Gjqe-n1rh0g) mais aussi [pourvu xa dure !](https://www.youtube.com/watch?v=vyk2MZoLST4&list=OLAK5uy_ntRz4sFNPNVhiGTyVR4VsePZzmGG7OPFM&index=8)).


## Erreurs fréquemment rencontrées

### Rendus

- Si vous compressez votre projet, faites en sorte que le correcteur puisse facilement le décompresser. Donc :
  - Utilisez une extension. `test2.zip`{.fichier} se décompresse tout seul alors que mon système d'exploitation ne reconnaît pas `test2`{.fichier} (sans extension) comme un fichier valide : je suis obligé d'ajouter l'extension pour que mon explorateur de fichier le décompresse.
  - Utilisez un logiciel de compression que tout le monde a par défaut. Donc pas de fichier rar. Uniquement du zip
- Le dossier `__pycache__`{.fichier} est généré par python à chaque exécution, il ne fait donc pas parti du code du projet. Supprimez le avant de rendre le projet et/ou avant de le compresser le dossier du projet.

### Fonction et tests

Les tests font parti du projet et sont une partie importante de la notation. Il est préférable pour avoir une bonne note (et votre Karma !) d'aller moins loin mais de faire des fonction de test de vos fonctions.

Pour que les imports se passent bien, **il ne faut pas ** :

- exécuter de fonctions dans le fichier `fonctions.py`{.fichier}. Il ne doit contenir que des déclarations de fonctions qui seront exécutés dans votre programme principal via des import. 
- exécuter les fonctions de test dans le fichier de test. Les fonctions de tests seront exécutées par pytest.

### Suite de Dyck

Vous êtes nombreux à être tombé dans le (tout petit) piège de la question 3.1. Il faut sortir si une somme partielle est négative pas uniquement à la fin. Je vous avais aidé dans le sujet en vous donnant un test qui permettait de le vérifier (`assert not bon_parenthésage([1, -1, -1, 1])`{.language-} qui correspond à la chaîne `"())("` qui n'est pas un bon parenthésage).


## Corrigé

Je joins les 3 fichiers de code que j'ai écris.

### `main.py`{.language-}

```python
from fonctions import parenthèses, suite, bon_parenthésage

s = input("Entrez une chaîne de caractères : ")
s_restriction = parenthèses(s)
print("La chaîne contient la suite de parenthèses :", s_restriction)

suite_1 = suite(s_restriction)
print("La suite associée est : , ", suite_1)

if bon_parenthésage(suite_1):
    print("La suite correspond à un bon parenthésage")
else:
    print("La suite ne correspond pas à un bon parenthésage")

```

### `fonctions.py`{.language-}

```python
def parenthèses(chaîne):
    parenthèses = ""

    for c in chaîne:
        if c in "()":
            parenthèses += c
    return parenthèses


def suite(chaîne_de_parenthèses):
    suite = []

    for c in chaîne_de_parenthèses:
        if c == "(":
            suite.append(1)
        elif c == ")":
            suite.append(-1)
    return suite


def bon_parenthésage(suite_de_0_1):
    somme = 0

    for c in suite_de_0_1:
        somme += c

        if somme < 0:
            return False

    return True

```

### `test_fonctions.py`{.language-}


```python
from fonctions import parenthèses, suite, bon_parenthésage

def test_parenthèses():
    assert "()" == parenthèses("(1+2)-3")
    assert "" == parenthèses("coucou !")
    assert "())" == parenthèses("coucou (toi) :)")

def test_suite():
    assert [1, -1] == suite("()")
    assert [] == suite("")
    assert [1, -1, -1] == suite("())")    

def test_bon_parenthésage():
    assert bon_parenthésage([1, -1])
    assert bon_parenthésage([])
    assert not bon_parenthésage([1, -1, -1, 1])

```
