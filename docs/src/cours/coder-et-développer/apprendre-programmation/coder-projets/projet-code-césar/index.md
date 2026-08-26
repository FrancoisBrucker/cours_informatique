---
layout: layout/post.njk
title: "Un projet avec des tests"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Vous aller coder ici une méthode de chiffrement/déchiffrement de texte : [le code de césar](https://fr.wikipedia.org/wiki/Chiffrement_par_d%C3%A9calage).

## Le projet

Du point de vue de python un projet est un dossier qui va contenir les différents fichiers python. Appelons le `chiffre_cesar`{.fichier}.

{% attention2 "**À retenir**" %}
Dans la mesure du possible, le nom des dossiers et des fichiers d'un projet informatiques :
- ne doivent contenir que des lettres **non accentuées**
- ne doivent contenir **pas** contenir d'espaces. On sépare les mots par des _underscore_ `_`
{% endattention2 %}

## Le programme principal

Le programme principal est le fichier que l'on va exécuter, on a coutume de l'appeler `main.py`{.fichier}

{% attention2 "**À retenir**" %}
Un projet informatique va contenir de nombreux fichiers, mais un seul sera le programme principal, celui que l'on exécutera avec la commande `python main.py`.
{% endattention2 %}

Dans notre cas, notre programme est : 

fichier `main.py`{.fichier} :

```python
import texte
from chiffre import césar_chiffre, césar_déchiffre

entrée = input("Tapez une chaîne de caractères en français : ")
texte = texte.conversion(entrée)


clé = input("Tapez une lettre de l'alphabet (clé de chiffrement) : ")
chiffre = césar_chiffre(texte, clé)
déchiffre = césar_déchiffre(chiffre, clé)

print("Texte initial   :", texte)
print("Texte chiffré   :", chiffre)
print("Texte déchiffré :", déchiffre)

```

On voit que ce fichier demande des choses à un utilisateur et utilise deux importations (`texte`{.language-} et `chiffre`{.language-}) qui correspondent à nos fichiers de fonctions.

Pour exécuter le fichier, on utilise le terminal dans le dossier du projet. Ci-après une exécution possible :

```shell
$> python main.py
Tapez une chaîne de caractères en français : Éléonore m'adore !           
Tapez une lettre de l'alphabet (clé de chiffrement) : F
Texte initial   : ELEONORE M'ADORE !
Texte chiffré   : JQJTSTWJ R'FITWJ !
Texte déchiffré : ELEONORE M'ADORE !

```

## Fichiers de fonctions

Là c'est à vous de travailler. On va séparer les fonctions du projet en 2 fichiers :

- un ficher consacré à la mise en forme d'une chaine de caractères
- un ficher consacré au chiffrement/déchiffrement d'un texte écrit en majuscule non accentuées


Prenez l'habitude de tester intensivement vos fonctions avec le terminal. C'est facile à faire en utilisant des raccourci clavier :

{% faire %}

1. ouvrez un terminal dans vscode avec son raccourci clavier (il est visible dans le menu _affichage > terminal_ ou via le les préférences raccourci en tapant "afficher terminal".).
2. exécutez la commande `python -m pytest`. Une fois que vous l'aurez exécuté si vous tapez la flèche du haut dans un terminal vous allez reprendre la dernière commande tapée
3. fermer le terminal pour revenir à votre fenètre de code en utilisant le même raccourci qu'en 1.

{% endfaire %}
{% info %}
La manipulation précédente va très vite ! 
1. le raccourci clavier pour afficher le terminal
2. la flèche du haut dans le terminal
3. le raccourci clavier pour afficher le terminal
{% endinfo %}


### Fonctions chiffre

{% faire %}
Créez un fichier `chiffre.py`{.fichier} et son pendant `test_chiffre.py`{.fichier} qui chiffre et déchiffre un texte écrit en majuscule non accentuée. Il doit contenir 2 fonctions :

- `césar_chiffre(texte_clair, cle)`{.language-} avec :
  - `texte_clair`{.language-} une chaine de caractère en majuscule
  - `clé`{.language-} un caractère en majuscule
  - la fonction doit retourner le chiffre de César de `texte`{.language-} selon la `clé`{.language-}
- `césar_déchiffre(texte_chiffré, cle)`{.language-} avec :
  - `texte_chiffré`{.language-} une chaine de caractère en majuscule
  - `clé`{.language-} un caractère en majuscule
  - la fonction doit retourner le déchiffrement de César de `texte`{.language-} selon la `clé`{.language-}

{% endfaire %}
{% info %}
Vous pourrez utiliser jucicieusement (rappelez vous des différentes [méthodes des chaines de caractère](../../concepts/chaines-caractères/#méthodes){.interne}) la chaine `ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"`{.language-} dans vos fonctions 
{% endinfo %}

### Fonctions texte

Le fichier  `texte.py`{.fichier} ne va contenir qu'une seule fonction, qui va transformer toute chaine de caractère en une chaine en majucule non accentuée. Par exemple :

```python
import unicodedata


def conversion(texte_avec_accent):
    liste_glyphes_unicode = list(unicodedata.normalize("NFKD", texte_avec_accent))

    liste_caractères = []
    for c in liste_glyphes_unicode:
        if not unicodedata.combining(c):
            liste_caractères.append(c)
    
    chaîne_sans_accent = "".join(liste_caractères)
    texte_en_majuscule = chaîne_sans_accent.upper()

    return texte_en_majuscule

```

{% faire %}
Créez un fichier `texte.py`{.fichier} contenant la fonction ci-dessus. Créez le fichier `test_conversion.py`{.fichier} testant que cette fonction fait bien ce qu'elle est sensée faire.
{% endfaire %}



{% attention2 "**À retenir**" %}
Prenez l'habitude de tester vos fichier en utilisant le terminal.
{% endattention2 %}


Ce que l'on teste est dépendant de chaque développeur : si les tests passent il doit être convaincu que son code est fonctionnel.

{% attention2 "**À retenir**" %}
C'est au développeur des fonctions de créer des tests pour elles de tel sorte que s'ils passent il soit persuadé que son code est sans bug (si un bug est découvert plus tard, il suffit de rajouter un test qui le montre puis corriger le code).
{% endattention2 %}

## Corrigé

Les différents fichiers sont disponible [ici](https://github.com/FrancoisBrucker/cours_informatique/tree/main/docs/src/cours/coder-et-d%C3%A9velopper/apprendre-programmation/coder-projets/projet-code-c%C3%A9sar/chffre-cesar)