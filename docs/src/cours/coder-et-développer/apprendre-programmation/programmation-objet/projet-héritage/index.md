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

- posséder un titulaire (on suppose que c'est une chaîne de caractères)
- être créée sans argent déposé initialement.
- permettre de déposer de l'argent.
- permettre de retirer de l'argent (on suppose que l'on peut être à découvert).

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
4. je retire 600 euros puis je consulte mon solde

### Compte épargne

{% faire %}
Créez et testez une classe `CompteÉpargne`{.language-}. Cette classe doit :

- être un `Compte`{.language-}
- avoir un taux d'intérêt
- avoir une somme plafond que l'on peut posséder
- être toujours positif ou nul (on ne peut être à découvert)
- on doit pouvoir connaître les intérêt selon son solde (c'est le taux fois son solde)

{% endfaire %}

### Livret A

{% faire %}
Créez et testez une classe `LivretA`{.language-}. Cette classe doit :

- être un `CompteÉpargne`{.language-}
- avoir un taux d'intérêt de 3% et un plafond de 22950 euros

{% endfaire %}

Vous implémenterez également la user story suivante :

1. je possède un livret A
2. je dépose 1000 euros puis je consulte mon solde
3. je dépose 20000 euros puis je consulte mon solde
4. je calcule mes intérêts
5. je retire 15000 euros puis je consulte mon solde
6. je retire 15000 euros puis je consulte mon solde

### PEL

{% faire %}
Créez et testez une classe `PEL`{.language-}. Cette classe :

- doit être un `CompteÉpargne`{.language-}
- doit avoir un taux d'intérêt de 2% et un plafond de 61200 euros
- ne permet pas de faire de retrait

{% endfaire %}

La particularité du PEL est que l'on ne peut plus déposer d'argent dessus après 10 ans. Il faut donc tenir trace de son année de création et de l'année où l'on veut faire des dépôts. Le code de la user story suivante le fait. Faites en sorte que votre code permette de l'exécuter :

```python
p = PEL("Ada Lovelace", année_ouverture=1835)

print("Dépôt (1840)")
p.dépose(1000, 1840)
print(p.solde)

print("Dépot (2022)")
p.dépose(1000, 2022)
print(p.solde)

print("Intérêts", p.calcule_intérêts())
print(p.solde)

print("Retrait")
p.retire(700)
print(p.solde)

print("Retrait")
p.retire(700)
print(p.solde)
```

## Donjons et dragons

En reprenant [le cours](../héritage#exemple-D&D){.interne}

### Personnages

{% faire %}

Créez (et testez) les classes personnage, magicien et guerrière.

{% endfaire %}

### Bataille

{% faire %}

Créez un programme qui demande à l'utilisateur :

- les caractéristiques d'une guerrière (points de vie, attaque et score de défense)
- les caractéristiques d'un [gobelin](https://www.aidedd.org/dnd/monstres.php?vf=gobelin) (points de vie, attaque)
- les caractéristiques d'un magicien (points de vie, attaque et attaque magique)

Puis, faites en sorte que la guerrière et le gobelin se tapent dessus à tour de rôle jusqu'à ce qu'un des deux meure.

Le dernier héros en vie est ensuite tué par le magicien qui le kite en lui jetant des sorts (comme un fourbe), puis le loote pour aller tout revendre au marchand du bourg (mais c'est une autre histoire et d'autres implémentations).

Vous donnerez le nombre de tours nécessaires pour que toute cette histoire se réalise (faire un cas où le gobelin survit et un autre ou la guerrière survit).

{% endfaire %}

