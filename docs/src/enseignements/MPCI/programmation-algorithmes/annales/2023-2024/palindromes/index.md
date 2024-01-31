---
layout: layout/post.njk

title:  "Projet palindromes"
authors:
    - François Brucker
---

Le but de ce projet est de trouver des palindromes dans un texte.

{% note "**Définition**" %}
Une chaîne de caractères $s$ de longueur $n > 0$ est un ***palindrome*** si : $s[i] = s[n-1-i]$ pour tout $0 \leq i < n$
{% endnote %}

Par exemple `lol`, `elle` ou `snobons` sont des palindromes en Français. De façon plus générale, on appelle ***phrase palindrome***, les chaînes de caractères dont la concaténation de leurs lettres forme un palindrome :

{% note "**Définition**" %}
Soit $s$ une chaîne de caractères écrite en Français. On définit  $s^\star$ la sous-chaîne de $s$ ne contenant que les lettres de $s$ dont on a supprimé les accents et mis en majuscule.

La chaîne $s$ est une ***phrase palindrome*** si $s^\star$ est un palindrome (donc également non vide).

{% endnote %}
{% info %}
Par exemple, la chaîne $s=\text{"Zeus a été à Suez."}$ est une phrase palindrome puisque $s^\star = \text{"ZEUSAETEASUEZ"}$ qui est un palindrome.
{% endinfo %}

Les phrases palindromes donnent bien de plus de liberté et donne des choses comme `élu par cette crapule` , `c'est sec ?` ou encore `À l'étape, épate-la !`.

{% lien %}
[Une liste de palindromes](https://fr.wiktionary.org/wiki/Annexe:Liste_de_palindromes_français)
{% endlien %}

La partie algorithmie se concentrera sur les palindromes et la partie code sur les phrases palindromes.

{% aller "**Questions**" %}

1. [Partie algorithmie](algorithmie){.interne}
2. [Partie code](code){.interne}

{% endaller %}
