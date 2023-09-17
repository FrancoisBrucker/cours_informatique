---
layout: layout/post.njk

title: Bases Linux

eleventyNavigation:
    order: 1

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Bases d'un système Linux.

1. Lire la partie Linux du tutoriel [Ordinateur pour le développement](/tutoriels/ordinateur-développement){.interne}
2. [post installation](post-installation){.interne}
3. [commandes](./commandes){.interne}
5. [droits et utilisateurs](droits-utilisateurs){.interne}
6. [process](process)
7. configuration :
   1. variables d'environnement
   2. shell bash file
      1. .profile, .bashrc, ... : quoi faire quand
      2. exemples de ubuntu : path, alias, etc.

## Bibliographie

- très didactique. Deux séries de vidéos :
  - <https://www.youtube.com/watch?v=EYRWohJeCkk&list=PLQqbP89HgbbbD0WSKRR90R5yjmTpSNNIl>
  - <https://www.youtube.com/watch?v=M5dZHdN-Aac&list=PLQqbP89HgbbY23Ab_vXGfLXHygquD7cAs>
- <https://ubuntu.com/tutorials/command-line-for-beginners#1-overview>
- <https://www.youtube.com/watch?v=sAD4dq_jDTA&list=PLShDm2AZYnK1SdG3dufPdCqk08sOahUBP>
- <https://www.youtube.com/watch?v=QlWKQAh7MKc&list=PLTXMX1FE5Hj6QRdYfuLsTdwCDDISV9TtB>