---
layout: layout/post.njk

title: Exercices

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Vos fonctions ne doivent produire ni erreurs ni warnings en utilisant les options de compilation :

```
-Wall -Wextra -pedantic -std=c23
```

{% info %}
Si `-std=c23` n'est pas une option reconnue, essayez `-std=c2x`.
{% endinfo %}

Déclarez bien vos variables dans une fonction (au pire dans la fonction main), sans quoi elle seront stockées dans la partie data de votre programme et pas la pile.

Chaque série d'exercice va vous apprendre une technique nouvelle de programmation en C. Ils sont pensés pour être de plus en plus spécifique, faites les donc dans l'ordre. Lorsque vous arriverez à tous les faire et que vous les avez compris, vous pourrez considérer que vous avez acquis les bases de programmation en C.

{% info %}
[corrigé des exercices](https://github.com/FrancoisBrucker/cours_informatique/tree/main/docs/src/cours/syst%C3%A8me/langage-c/exercices/corrig%C3%A9).

Ne regardez la solution qu'**après avoir résolu l'exercice**. En C comme partout c'est se casser les dents sur un problème qui vous fait progresser. Pas juste passivement regarder la solution.
{% endinfo %}

## Bases

Création de fonctions simples et compilation avec des bibliothèques annexes.

{% aller %}
[Nombre de chiffres d'un entier](./nb-chiffres){.interne}
{% endaller %}

## <span id="proba"></span> Retour de Pointeurs

On utilise des pointeurs comme retour de fonctions et on termine en créant un makefile.

{% aller %}
[Nombres aléatoires](./nb-aléatoires){.interne}
{% endaller %}

## <span id="liste"></span> Structure de liste

Création d'une structure de donnée complexe grâce aux [`struct`{.language-}](../langage/structures/){.interne}.

{% aller %}
[Listes](./structure-liste){.interne}
{% endaller %}

## <span id="matrice"></span>Structure de matrice

On y apprend comment gérer des pointeurs de pointeurs et la technique du pointeur opaque.

{% aller %}
[Matrices](./matrices){.interne}
{% endaller %}

## Listes doublement chaînées

On y apprend à utiliser des données sans type prédéfinis et des pointeurs sur des fonctions.

{% aller %}
[Listes doublement chaînées](./listes-chaînées){.interne}
{% endaller %}

## Syracuse

On personnalise notre exécutable avec des paramètres.

{% aller %}
[Syracuse](./syracuse){.interne}
{% endaller %}
