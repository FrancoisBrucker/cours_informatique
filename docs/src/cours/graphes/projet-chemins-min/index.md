---
layout: layout/post.njk

title: Projet recherche de chemin de poids minimum
authors: 
    - François Brucker

eleventyNavigation:
  key: "Projet recherche de chemin de poids minimum"
  parent: "Graphes"
---

<!-- début résumé -->

Utilisation de l'algorithme de Dijkstra et de $A^\star$.

<!-- fin résumé -->

Le fichier que nous utiliserons ici est : [`villes_10000_habitants.json`{.fichier}](./villes_10000_habitants.json)

{% faire %}
Téléchargez le fichier dans un dossier `projet-chemin-min`{.fichier}.

{% endfaire %}
{% info %}
Il vous faudra peut-être cliquer-droit puis choisir `enregistrer le lien sous...` pour télécharger le fichier et non juste l'afficher dans votre navigateur.
{% endinfo %}

## Chargement du graphe

Si vous ouvrez ces fichier dans un éditeur de texte, on voit que le fichier est totalement lisible. Il est au format [json](https://fr.wikipedia.org/wiki/JavaScript_Object_Notation) et est une liste de dictionnaire de la forme :

```python
{
    "nom": "Marseille",
    "voisins": [
        "Aix-en-Provence",
        "Antibes",
        "Arles",
        "Avignon",
        "Cannes",
        "Grenoble",
        "LaSeyne-sur-Mer",
        "Marseille",
        "Montpellier",
        "Nice",
        "Nimes",
        "Toulon",
        "Valence"
    ],
    "longitude": 5.4,
    "latitude": 43.3
},
```

Vous allez dans une première partie transformer cette liste de villes en un graphe valué
{% faire %}
En utilisant le code suivant, chargez la liste contenue dans le fichier `villes_10000_habitants.json`{.fichier} dans une liste python nommée `villes`{.language-}.

```python
import json

with open("../villes_10000_habitants.json") as entree:
    villes = json.load(entree)

```

{% endfaire %}

## Sauvegarde et relecture des données

Sauver une structure de donnée pour qu'elle soit éditable et réutilisable se fait couramment en utilisant le format [json](https://fr.wikipedia.org/wiki/JavaScript_Object_Notation) qui associe à chaque type d'objet une chaîne de caractère. On sauve alors nos données au format texte qu'il est ensuite facilement éditable avec un éditeur et ré-importable ensuite pour être utilisé.

### Sauvegarde et relecture du Graphe

Le problème ici, c'est que l'on utilise des ensembles qui ne sont **pas** reconnus par json...

Une solution simple pour résoudre ce problème est d'utiliser des listes à la place des ensemble pour la sauvegarde. Commençons par convertir notre graphe en un graphe utilisant des listes :

```python
def voisinage_vers_liste(G):
    return {x: list(G[x]) for x in G}
```

On peut ensuite sauver le graphe en json sur le disque en utilisant la [bibliothèque json de python](https://docs.python.org/fr/3/library/json.html) :

```python
def sauve_graphe(G):

    import json

    with open("graphe.json", "w") as sortie:
        json.dump(voisinage_vers_liste(G), sortie, ensure_ascii=False, indent=4)

```

{% info %}
On a utilisé les paramètres :

* `ensure_ascii=False`{.language-} pour la fonction [`json.dump`](https://docs.python.org/fr/3/library/json.html#json.dump) pour que python écrive bien nos accents.
* `indent=4`{.language-} pour que le fichier sauvé soit agréable à lire.

{% endinfo %}

En exécutant la fonction `sauve_graphe(G)`{.language-} vous devriez avoir un fichier `graphe.json`{.fichier} sur votre disque dur.

On peut ensuite le recharger puis le convertir pour transformer les liste en ensemble :

```python
def voisinage_vers_ensemble(G):
    return {x: set(G[x]) for x in G}


def charge_graphe(nom_fichier):

    import json

    with open(nom_fichier, "r") as entrée:
        G = json.loads(entrée.read())
    
    return voisinage_vers_ensemble(G)
```

### Sauvegarde et relecture de la valuation

Sauvegarder la valuation au format json es un peu plus compliqué car les cls des dictionnaires en json ne peuvent être que des nombres ou des chaines de caractères.

{% faire %}
Créer une fonction qui transforme la valuation (un dictionnaire où les clés sont des couples et les valeurs des réels) en liste de dictionnaires où chaque dictionnaire encode un couple clé: valeur de  la valuation.

Si par exemple notre valuation est :

```python

f = {
    ('A', 'B'): 12,
    ('B', 'A'): 12,
    ('B', 'C'): 4,
    ('C', 'B'): 4,
}
```

On doit la transformer en :

```python

f_json = [
    {"clé": ['A', 'B'], "valeur": 12}, 
    {"clé": ['B', 'A'], "valeur": 12}, 
    {"clé": ['C', 'B'], "valeur": 4}
    {"clé": ['B', 'C'], "valeur": 4}, 
]
```

{% endfaire %}
{% details "solution" %}

```python
def valuation_vers_liste(f):
    return [{"clé": list(clé), "valeur": valeur} for clé, valeur in f.items()]
```

{% enddetails %}

{% faire %}
Faite également la fonction inverse qui retransforme notre liste en une valuation.
{% endfaire %}
{% details "solution" %}

```python
def liste_vers_valuation(f_liste):
    return {tuple(x["clé"]): x["valeur"] for x in f_liste}
```

{% enddetails %}

Enfin :

{% faire %}
Créez les fonction `charge_valuation`{.language-} et `sauve_valuation`{.language-}
{% endfaire %}
{% details "solution" %}

```python
def sauve_valuation(f):

    import json

    with open("valuation.json", "w") as sortie:
        json.dump(valuation_vers_liste(f), sortie, ensure_ascii=False, indent=4)


def charge_valuation(nom_fichier):

    import json

    with open(nom_fichier, "r") as entrée:
        f = json.loads(entrée.read())

    return liste_vers_valuation(f)

```

{% enddetails %}

## Algorithme Dijkstra

chemins + distances

## A étoile et distances

> TBD : on utilise le csv des villes de france


## représentations graphiques

avec networkx



> TBD : graphe
Nous allons utiliser 

> TBD : donner aussi coordonnées pour représenter graphiquement