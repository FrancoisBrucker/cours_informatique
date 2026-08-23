---
layout: layout/post.njk

title: DM

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---


## FIFO

Structure de file pour communication réseau

```
   d     f
   v     v
xxxxxxxxxxxxxxx
```

- d = f : vide
- push : on place en f puis on incrémente f de 1 modulo n
- pop : on récupère en d puis on incrémente d de 1 modulo n
- (f-d) % n == -1 : reste une place = plein

La file va se remplir selon le ratio r = ecriture / lecture.
Si r > 1 elle va grossir tout le temps
 si r<=1 on a une proba de taille, comme une {+1, -1} marche aléatoire.

Vérification expérimentale.

## dico

1. dico
  - utiliser liste pour déco avec modulo
  - nb random pour vérifier la taille des listes selon taille de dico
2. avec nb fixe d'élément :
   - en utilisant une fat (struct {int val, size_t next, bool vide}[])
   - faire une fonction de défragmentation ( il faut ajouter un size_t prev à la struct pour faire ça bien)
3. liste circulaire. Uniquement ajout
4. liste circulaire avec suppression et flag "a existé" en plus du flag "vide"

## liste chainee intrusives

- comme un fat
- [listes chaînées intrusives](https://www.data-structures-in-practice.com/intrusive-linked-lists/)

{% lien %}
[Type opaque pour une liste chaînée](https://x0r.fr/blog/30).
{% endlien %}


## Base64

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
