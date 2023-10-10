---
layout: layout/post.njk

title: DM

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

1. dico
  - utiliser liste pour déco avec modulo
  - nb random pour vérifier la taille des listes selon taille de dico
2. avec nb fixe d'élément :
   - en utilisant une fat (struct {int val, size_t next, bool vide}[])
   - faire une fonction de défragmentation ( il faut ajouter un size_t prev à la struct pour faire ça bien)
3. liste circulaire. Uniquement ajout
4. liste circulaire avec suppression et flag "a existé" en plus du flag "vide"

- liste doublement chaînées
- exam ? [algorithm X](https://en.wikipedia.org/wiki/Knuth%27s_Algorithm_X)
- [listes chaînées intrusives](https://www.data-structures-in-practice.com/intrusive-linked-lists/)

{% lien %}
[Type opaque pour une liste chaînée](https://x0r.fr/blog/30).
{% endlien %}

## Qui est en Base

### Base16

{% faire %}
<https://en.wikipedia.org/wiki/Base64>
{% endfaire %}

décalage à droite et gauche de 4 bit pour faire la chaîne.

base16. Avec un décalage de 4bit puis reconstruction

### Base64

1. décalage de bit
2. conversion de 3 byte.
3. association pour reconstruire la fin
4. déconversion pour reconstruire le stream.
  
{% faire %}

- <https://en.wikipedia.org/wiki/Base64>
- <https://stackoverflow.com/questions/342409/how-do-i-base64-encode-decode-in-c>

{% endfaire %}


## Lecture et buffer

<http://sekrit.de/webdocs/c/beginners-guide-away-from-scanf.html>

- scanf : attention buffer overflow
- avec strcmp pour stopper (si vide)
- scanf avec espaces
- scanf limité en taille
- while et getchar avec char32 pour être sur d'avoir un caractère utf8
- tableau de str (char**)
