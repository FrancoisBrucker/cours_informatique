---
layout: layout/post.njk 
title: "Projet : héritage"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---


Mise en œuvre du mécanisme d'héritage.

## Comptes bancaires

Vous allez construire une hiérarchie de produits bancaires.


{% faire %}
Commencez par lire tout l'énoncé et créez la représentation UML des différentes classes.
{% endfaire %}

### Compte (générique)

{% faire %}
Créez et testez une classe `Compte`{.language-} qui servira de classe mère. Cette classe doit :

- posséder un titulaire (on suppose que c'est une chaine de caractères) et être crée sans argent de déposé.
- permettre de retirer et de déposer de l'argent (on suppose que l'on peut être à découvert).

{% endfaire %}

### Compte courant


{% faire %}
Créez et testez une classe `CompteCourant`{.language-}. Cette classe doit :

- être un `Compte`{.language-}
- avoir un découvert autorisé fixé à la création

{% endfaire %}

Vous implémenterez également la user story suivante :

1. je possède un compte courant avec un découvert autorisé de 1000 euros
2. je dépose 100 euros puis je consulte mon solde
3. je retire 700 euros puis je consulte mon solde
3. je retire 600 euros puis je consulte mon solde

### Compte épargne

{% faire %}
Créez et testez une classe `CompteEpargne`{.language-}. Cette classe doit :

- être un `Compte`{.language-}
- avoir un taux d'intérêt
- avoir une somme plafond que l'on peut posséder
- être toujours positif ou nul (on ne peut être à découvert)
- on doit pouvoir connaître les intérêt selon son solde (c'est le taux fois son solde)

{% endfaire %}

### Livret A

{% faire %}
Créez et testez une classe `LivretA`{.language-}. Cette classe doit :

- être un `CompteEpargne`{.language-}
- avoir un taux d'intérêt de 3% et un plafond de 22950 euros

{% endfaire %}

Vous implémenterez également la user story suivante :

1. je possède un livret A
2. je dépose 1000 euros puis je consulte mon solde
3. je dépose 25000 euros puis je consulte mon solde
4. je calcule mes intérêts
5. je retire 15000 euros puis je consulte mon solde
6. je retire 15000 euros puis je consulte mon solde

### PEL

{% faire %}
Créez et testez une classe `PEL`{.language-}. Cette classe :

- doit être un `CompteEpargne`{.language-}
- doit avoir un taux d'intérêt de 2% et un plafond de 61200 euros
- ne permet pas de faire de retrait

{% endfaire %}

La particularité du PEL est que l'on ne peut plus déposer d'argent dessus après 10 ans. Il faut donc tenir trace de son année de création et de l'année où l'on veut faire des dépôts. Le code de la user story suivante le fait. Faites en sorte que votre code permette de l'exécuter :

```python
p = PEL("Mme Z", année_ouverture=2011)

print("Dépot (2017)", p.dépose(1000, 2017))
print(p.solde)
print("Dépot (2022)", p.dépose(1000, 2022))
print(p.solde)
print("Intérêts", p.calcule_intérêts())
print(p.solde)
print("Retrait", p.retire(700))
print(p.solde)
print("Retrait", p.retire(700))
print(p.solde)
```
## Donjons et dragons

### Personnages

En reprenant [le cours](../héritage#exemple-D&D){.interne} :

{% faire %}

Créez (et testez) les classes personnage, magicien et guerrière.

{% endfaire %}

### Bataille

{% faire %}

Créez un programme qui demande à l'utilisateur :

- les caractéristiques d'une guerrière (points de vie, attaque et score de défense)
- les caractéristiques d'un [gobelin](https://www.aidedd.org/dnd/monstres.php?vf=gobelin) (points de vie, attaque)
- les caractéristiques d'un magicien (points de vie, attaque et attaque magique)

Puis,  faites en sorte que la guerrière et le gobelin se tapent dessus à tour de rôle jusqu'à ce qu'un des deux meure.

Le dernier héros en vie est ensuite tué par le magicien qui le kite en lui jetant des sorts (comme un fourbe), puis le loote pour aller tout revendre au marchand du bourg (mais c'est une autre histoire et d'autres implémentations).

Vous donnerez le nombre de tours nécessaires pour que toute cette histoire se réalise (faire un cas où le gobelin survit et un autre ou la guerrière survit).

{% endfaire %}



## Le dé

Nous allons ici encore une fois réutiliser la classe `Dé`{.language-} entamée lors du [projet objets : dés](../projet-objets-dés){.interne}. Pour être sûr de repartir sur de bonnes bases, utilisez l'implémentation minimale utilisée lors du [projet composition : dés](../projet-composition-dés/#code-Dé){.interne}.

Le but de cette partie est de compter les moyennes de jets de dés.

### User Story

On commence par créer une user story sur la fonctionnalité que l'on veut ajouter :

{% note "**User Story**" %}

- Nom : "Statistiques descriptives"
- Utilisateur : un joueur
- Story : On veut compter les moyennes de jets de dés
- Actions :
  1. effectuer 10 jets de dé
  2. calculer la moyenne de ces jets

{% endnote %}

{% faire %}

Codez la user story en utilisant uniquement la classe `Dé` dans le fichier `story_moyenne.py`{.fichier}.

{% endfaire %}

### Un dé qui compte

Nous voulons créer une version particulière d'un dé : un dé permettant de conserver les statistiques de ses lancers.

Implémentez la classe `StatDé`{.language-} qui hérite de `Dé`{.language-}, et retient le nombre de fois que chaque valeur possible a été obtenue et permet de calculer les statistiques associées.

{% faire %}

Vous devez donc écrire et tester pour la classe `StatDé`{.language-} :

- la méthode `__init__`{.language-} sans oublier d'appeler le constructeur de la classe mère,
- un nouveau mutateur `position`{.language-} qui utilise le mutateur de la classe parent et met à jour les décomptes de lancers du dé
- une méthode `stats`{.language-} qui renvoie les nombres d'apparition de chaque valeur

{% endfaire %}

{% attention %}
La gestion des accesseurs et des mutateurs hérités est *"compliquée"* en Python. Si vous avez utilisé des `@property`{.language-} vues dans le [projet objets : Dés](../projet-objets-dés#property){.interne} pour votre classe `Dé`{.language-}, il faut un peu tricoter pour les utiliser dans la classe `StatDé`{.language-}.

Supposons que c'est l'attribut `valeur`{.language-} auquel vous accédez par `@property`{.language-}. Pour appeler :

- l'accesseur de la classe mère dans une classe fille on peut utiliser : `super().valeur`{.language-}
- le mutateur de la classe mère dans une classe fille peut être accédé via son nom Python qui est : `super(type(self), type(self)).valeur.fset(self, new_position)`{.language-}

C'est un peu compliqué et vient de l'implémentation de `super()`{.language-} en Python.

Vous pouvez consulter les deux liens suivants pour un peu mieux comprendre ce qu'on fait
{% endattention %}
{% lien %}

- [documentation de `super()`{.language-}](https://docs.python.org/3/library/functions.html#super)
- [héritage d'accesseur et mutateur en python](https://gist.github.com/Susensio/979259559e2bebcd0273f1a95d7c1e79)

{% endlien %}

On pourra stocker le nombre d'apparitions de chaque face dans une liste où l'indice + 1 correspond à la face.

{% faire %}
Modifiez la user story pour qu'elle utilise la classe `StatDé`{.language-} à la place de `Dé`{.language-}.
{% endfaire %}

### Programme principal

{% faire %}

Créez un programme qui lance $N=1000$  fois votre dé (par exemple) et rend ses statistiques.

Vous utiliserez ensuite ces statistiques pour faire un [test d'adéquation du $\chi^2$](https://fr.wikipedia.org/wiki/Test_du_%CF%87%C2%B2#Exemple_1_:_d%C3%A9termination_de_l'%C3%A9quilibrage_d'un_d%C3%A9) pour vérifier que votre dés est bien équiprobable.

{% endfaire %}

Un test d'adéquation du $\chi^2$ permet de s'assurer que le résultat d'une expérience est conforme à ce qu'on devrait avoir théoriquement.

Pour cela on calcule le nombre :

$$
\chi^2 = \sum_{i=1}^I\frac{(O_i - T_i)^2}{T_i}
$$

Où :

- $I$ : l'ensemble des possibilités (pour nous $I=6$ puisque la valeur d'un dés va de 1 à 6)
- $O_i$ est le nombre de cas **observés** pour la modalité $i$ (pour nous c'est le nombre de fois où le dé a eu la position $i$)
- $T_i$ est le nombre de cas **théoriques** que l'on devrait avoir (dans notre cas $\frac{N}{6}$ si on a lancé $N$ fois notre dé)

Plus ce nombre est petit, plus l'expérience est conforme à la théorie.

De façon formelle :

- si la théorie est conforme à la réalité, le nombre $\chi^2$  suit une loi du $\chi^2$ à $I-1$ degrés de liberté (ici 5 degrés de liberté)
- la probabilité $P_{\mbox{df}}(X \geq K)=\alpha$ nous donne la chance d'obtenir $K$ ou plus pour une loi du $\chi^2$ à df degrés de libertés.

Pour nous $df = 5$ et si on prend $\alpha = .1$ on trouve : $P_{5}(X \geq 9.236) = .1$ (pour connaître ces valeurs, on utilise des tables comme [celle-ci](https://people.richland.edu/james/lecture/m170/tbl-chi.html)).

Donc si on trouve un $\chi^2$ plus grand ou égal que $9.206$, il y a moins de 10% de chance d'obtenir ce nombre si l'on suit une loi du chi2 à df degrés de liberté : Il y a moins de 10% de chance de se tromper en supposant que notre expérience ne suit pas la théorie. Dans notre cas, cela signifie qu'il y a moins de 10% de chance de supposer que notre dé n'est pas équilibré.

C'est que l'on appelle le [risque de première espèce](https://fr.wikipedia.org/wiki/Test_statistique#Risque_de_premi%C3%A8re_esp%C3%A8ce_et_confiance) lorsque l'on fait des [test statistiques](https://fr.wikipedia.org/wiki/Test_statistique)

{% info %}

Le test du $\chi^2$ est très pratique lorsque l'on veut vérifier que nos hypothèses théoriques sont satisfaites expérimentalement.
{% endinfo %}
