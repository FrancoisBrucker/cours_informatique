---
layout: layout/post.njk

title: "sujet Test 2 : preuve et complexité"
authors:
  - François Brucker
---

Ce test vous demande de créer des fonctions de recherche de caractères dans une chaîne de caractères.

## Rendu

### Type de rendu

Rendu sur feuille

### Éléments de notation

1. Écriture sous la forme d'un pseudo-code correcte
2. Preuves :
   - de finitude
   - d'exactitude
3. Calcul de complexité

## 1. Présence

On considère la fonction suivante, de signature : `def est_présent(chaine: str, caractère:str) -> bool`{.language-}.

Son code est le suivant :

```python
def est_présent(chaine, caractère):
    return est_présent_rec(chaine, caractère, 0)


def est_présent_rec(chaine, caractère, indice):
    if indice > len(chaine) - 1:
        return False
    elif chaine[indice] == caractère:
        return True
    else:
        return est_présent_rec(chaine, caractère, indice + 1)
```

{% faire %}

- Est-ce un algorithme ?
- Quel problème résout cette fonction ? Et pourquoi (donnez une démonstration par récurrence) ?
- Quelle est sa complexité, et surtout pourquoi ?

{% endfaire %}

## 2. Lettre dupliquée

{% faire %}
Créer la fonction `possède_caractère_dupliqué(chaine: str) -> bool`{.language-} qui rend :

- `True`{.language-} si la chaîne en paramètre, de longueur $n$, contient deux indices $0\leq i < j < n$ tels que $\text{chaine}[i] = \text{chaine}[j]$,
- `False`{.language-} sinon.

{% endfaire %}

On vous demande également de :

{% faire %}

- Justifier l'exactitude de votre fonction
- Donner (en justifiant) la complexité min et max de votre fonction

{% endfaire %}

## 3. Bit dupliqué

On suppose que l'on applique la fonction de la question précédente à des chaines uniquement composées des caractères `"0"`{.language-} et `"1"`{.language-}.

{% faire %}
Quel est la complexité min et max de la fonction dans ce cas là ?
{% endfaire %}
