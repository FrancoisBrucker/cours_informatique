---
layout: layout/post.njk

title: Codes symétriques

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---



{% note "définition" %}
Un code est dit ***symétrique*** ou ***à clé secrète*** lorsque la clé de déchiffrement est identique ou s'il est *facile* de la déterminer à partir de la clé de chiffrement.
{% endnote %}

Dans le cas de code symétrique, il est indispensable de garder la clé de chiffrement secrète sans quoi Eve pourra aisément décoder le message

Le principal intérêt des codes à clés secrètes est leur simplicité. Il sont très rapide à coder et décoder des messages.

De plus, les seuls codes prouvés inviolables sont des codes à clés secrètes.

> sensible à l'analyse en fréquence pour la cryptanalyse <https://fr.wikipedia.org/wiki/Analyse_fr%C3%A9quentielle>

### Masque jetable

taille max ou Vigenère plus petit. Mais attention à l'analyse en fréquence (ex césar)

> Vernam, ou encore masque jetable <https://fr.wikipedia.org/wiki/Masque_jetable> inviolable
> mais clé trop longue, impossible à mettre ne oeuvre ne pratique, on découpe le message en bout de taille = longueur de la clé.
> clé = 1 = césar
> clé = k = vigenere <https://fr.wikipedia.org/wiki/Chiffre_de_Vigen%C3%A8re>

> Ex césar et découpe par caractère
> dire que ca simplifie le code mais affaiblie sa sécurité :
>  * césar que 26 possibilité
>  * si cesar avec un décalage différent pour chaque case, le message est inviolable (on peut potentiellement retrouver tous les textes français ! C'est la [bibliothèque de Babel](https://fr.wikipedia.org/wiki/La_Biblioth%C3%A8que_de_Babel))
>

### XOR

<https://en.wikipedia.org/wiki/XOR_cipher>

> TBD lien ci-dessus tout dedans sur Vernam et block
