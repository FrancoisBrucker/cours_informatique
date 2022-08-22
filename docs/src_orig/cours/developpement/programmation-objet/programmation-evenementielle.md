---
layout: page
title:  "Programmation évènementielle"
category: cours
authors: 
  - François Brucker
  - Célia Châtel
---

On utilise la programmation évènementielle pour créer des interfaces graphiques.

## bibliothèque utilisée

On utilise [appjar](http://appjar.info) une bibliothèque graphique permettant d'apprendre les interfaces graphiques. On la déconseille fortement pour des applications pro, mais pour apprendre, elle est très bien.

> Pour toute son utilisation, regardez la documentation, elle est très bien faite !

### installation

Il y a 2 moyens d'[installer appjar](http://appjar.info/Install/) :

* soit en l'installant avec pip : `pip install appjar` (ou pip3 si votre interpréteur python s'appelle `python3`), c'est la méthode recommandée.
* soit en [téléchargeant le module](https://github.com/RWBA/appJar/blob/appJar/releases/appJar.zip?raw=true) puis en décompressant le dossier dans votre projet (vous aurez un dossier nommé *"appJar"* dans votre projet). Si vous êtes sous windows et que vous n'avez pas de logiciel pour dézipper des dossiers, vous pouvez télécharger et installer le logiciel [7zip](https://www.7-zip.org/download.html) (prenez la version 64bit)

> Si vous avez installé python avec anaconda, comme recommandé, tout devrait bien se passer. Sinon, il se peut qu'il vous faille installer un python avec tk.
{.attention}

### un exemple

Créez un nouveau projet et copier le code suivant dans un fichier nommé *"ui.py"*

```python
from appJar import gui

model = {"valeur": 0}


def press_plus1():
    model["valeur"] += 1
    app.setLabel("valeur", str(model["valeur"]))


def press_moins1():
    model["valeur"] -= 1
    app.setLabel("valeur", str(model["valeur"]))


app = gui()
app.setSize(300, 100)

app.addButton("-1", press_moins1, 0, 0)
app.addLabel("valeur", str(model["valeur"]), 0, 1)
app.addButton("+1", press_plus1, 0, 2)

app.go()
print("c'est fini.")
```

Lorsque vous exécutez ce code vous devriez voir une fenêtre s'ouvrir qui ressemble à ça :

![Une ui]({{ "/assets/cours/developpement/programmation-objet/ui_ui.png" | relative_url }}){:style="margin: auto;display: block}

Lorsque vous cliquez sur le bouton *"-1"* le nombre du milieu décroit, lorsque vous cliquez sur le bouton *"+1"* le nombre du milieu croit.

Examinons le code ensemble :

#### import

```python
from appJar import gui
```

On importe la bibliothèque `appJar`, et en particulier la fenêtre : `gui`.

```python
model = {
    "valeur": 0
}
```

On utilise un [dictionnaire](https://python.doctor/page-apprendre-dictionnaire-python) pour garder nos données. C'est très pratique et s'utilise comme une liste où l'on accède aux données non plus avec leur position mais avec une "clé". Pour nous, ces clés seront toujours des chaines de caractères.

Dans le code, on crée une clé nommé `"valeur"`. On accède à la donnée en tapant : `model["valeur"]`.

##### déclaration des fonctions évènements

```python
def press_plus1():
    model["valeur"] += 1
    app.setLabel("valeur", str(model["valeur"]))


def press_moins1():
    model["valeur"] -= 1
    app.setLabel("valeur", str(model["valeur"]))
```

Le 2 fonctions seront exécutées lorsque l'on cliquera sur les boutons : elles seront les réaction aux évènements de clique sur les boutons.

##### la fenêtre

```python
app = gui()
app.setSize(300, 100)
```

On crée la fenêtre avec la fonction `gui` de `appJar` et on lui donne la taille de 300 pixels de large et 100 pixels de haut.

##### les widgets de la fenêtre

Un *widget*  est un élément de la fenêtre. On en ajoute 3 ici :

```python
app.addButton("-1", press_moins1, 0, 0)
app.addLabel("valeur", str(model["valeur"]), 0, 1)
app.addButton("+1", press_plus1, 0, 2)
```

On ajoute à la fenêtre ;:

* un bouton nommé *-1* (c'est aussi son identifiant) à la position 1ère ligne, 1ère colonne (c'est les `0, 0` de la fin) et lorsque l'on cliquera dessus, on exécutera la fonction `press_moins1`.
* un label nommé "valeur" (c'est aussi son identifiant) une chaine de caractère) à la position 1ère ligne, 2ème colonne (c'est les `0, 1` de la fin) et avec comme label `model["valeur"]` transformé en chaine de caractère.
* un bouton nommé *+1* (c'est aussi son identifiant) à la position 1ère ligne, 3ère colonne (c'est les `0, 2` de la fin) et lorsque l'on cliquera dessus, on exécutera la fonction `press_plus1`.

> notez que l'on exécute pas les fonction ici, on ne fait que passer leurs noms (donc **sans** les parenthèses)

##### on ouvre la fenêtre

```python
app.go()
```

On ouvre la fenêtre.

##### fin du programme

```python
print("c'est fini.")
```

Cette ligne ne sera affichée que lorsque l'on fermera la fenêtre. Il est donc inutile d'écrire du code après la ligne `app.go()`, puisqu'il ne sera pas exécuté avant la fermeture de la fenêtre.

### premières modifications

#### couleur du label

Faites en sorte que la couleur du label soit :

* bleu si le nombre est strictement positif
* noire si le nombre vaut 0
* rouge si le nombre est strictement négatif

Pour cela, il faut **modifier** le label. Avec `appJar` on crée une seule fois le label (avec une méthode qui commence par `add`), puis on le modifie avec une méthode qui commence par `set` et dans le 1er paramètre est l'identifiant du label (ici c'est "valeur").

Ici la méthode est `setLabelFg` et s'utilise comme `setLabelBg` décrit dans la [documentation](http://appjar.info/outputWidgets/#label)

#### reset

Ajoutez un bouton qui remet le nombre à zéro. Vous mettrez ce bouton sue la 2ème ligne, en 2ème colonne.

## lancer de dés

Vous allez lancer des dés avec appJar

### un dé

Reprenez le code du dé de la [séance d'exercices sur l'héritage]({% link cours/developpement/programmation-objet/héritage-exercices.md %}#code-dice)

### l'interface

Utilisez le code du dé pour réaliser l'interface suivante :

![Lancé de dé]({{ "/assets/cours/developpement/programmation-objet/ui-de.png" | relative_url }}){:style="margin: auto;display: block}

> L'interface précédente est une *idée* ce que ce ça doit faire, votre fenêtre peut-être différente. En revanche, les fonctionnalités demandées doivent être là.

### changer le dé

Utilisez la documentation sur les [caractères spéciaux](http://appjar.info/specialCharacters/) pour remplacer les valeurs des dés par une image de dé.

Ce sont les caractères unicode allant de "\u2680" à "\u2685"

Vous pourrez aussi changer la taile de la font. par exemple : `app.getLabelWidget("test").config(font="Time 40")` change la taille de la font à 40 du label d'identifiant `test`.

### Lancer 3 dés

Reprenez le code précédents et faites en sorte de pouvoir lancer 3 dés simultanément.

La fenêtre pourra ressembler à ça :

![Lancé de dé]({{ "/assets/cours/developpement/programmation-objet/ui-de-2.png" | relative_url }}){:style="margin: auto;display: block}

### somme

Ajoutez un label qui donne la somme des 3 dés. Cela pourra ressembler à ça :

![Lancé de 3 dés]({{ "/assets/cours/developpement/programmation-objet/ui-de-3.png" | relative_url }}){:style="margin: auto;display: block}

Vous pourrez utiliser des [frame](http://appjar.info/pythonWidgetGrouping/#frame) pour grouper vos éléments.

### Lancer des dés choisis

Ajoutez des *checkbox pour ne lancer que les dés cochés.

La fenêtre pourra ressembler à ça :

![Lancé de dé choisis]({{ "/assets/cours/developpement/programmation-objet/ui-de-4.png" | relative_url }}){:style="margin: auto;display: block}

Vous pourrez utilisez des [checkbox](http://appjar.info/inputWidgets/#checkbox) pour cela.

> Si vous voulez que les checkboxes n'aient pas de texte, juste la coche, il faudra leur donner des noms différents et le même label vide à chacune. Vous devrez alors utiliser des `NamedCheckBox`
