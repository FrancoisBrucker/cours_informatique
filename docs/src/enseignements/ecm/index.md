---
layout: layout/post.njk

title: Enseignement à l'ECM
tags: ["enseignement", "ecm"]

eleventyNavigation:

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Liste des cours d'informatique que j'effectue au sein de l'École Centrale Méditerranée.

## Mes cours actuels

1. S5 training (Semaine d'Ouverture Scientifique, SOS) : [JEMNEP](1A/jemnep/){.interne} (bases de la programmation en python)
2. S6 training (SOS) : architecture des ordinateurs et système d'exploitation. Initiation à la programmation en C et en assembleur (et Rust si on a le temps)
3. S7 :
   <!-- - training (SOS) : langages fonctionnels. Applications avec Haskell -->
   - MIE : programmation objet en python, tests et gestion des sources
4. S9 :
   - T1 : méthodes de développement : programmation par les tests ; aux sources de git
   - T2 : bases des systèmes Unix/Linux et utilisation d'un serveur distant
   - T3 : algorithmie avancée : hasard, algorithmes cryptographiques et protocoles internets

## Comment apprendre l'informatique dans une école "généraliste"

1. **Choisir** toutes les options/cours où on peut en faire :
   1. Suivez les socles fondamentaux d'algorithmie ou de système. Acquérir ces connaissances seul est ardu.
   2. Avec les bases théoriques en poche, vous pourrez apprendre les technos/languages du moment par vous-même avec des projets perso ou ceux de la formation pour lesquels la mise en œuvre est libre.
2. **Partir en S8 à l'étranger** pour suivre un cursus d'informatique dans une université étrangère. Vous allez acquérir les fondamentaux qui vous manquent encore.
3. **Venir** en Do_It en 3A :)

Une fois que vous commencerez à progresser, **faites attention à** :

- [L'effet Dunning-Kruger](https://fr.wikipedia.org/wiki/Effet_Dunning-Kruger) qui fait qu'on se croit meilleurs que ce qu'on est. Vous n'êtes presque sûrement que borgne dans une école d'aveugles (au moins en informatique)
- L'illusion de croire que tout peut s'apprendre avec un tuto. Sans prof pour des sujets pour lesquels vous n'avez aucune compétence/connaissances, vous irez moins loin; en plus longtemps et sans être sûr d'y être
- Vous reposer sur du code assisté (voir généré) par IA sans avoir les connaissances algorithmiques, système ou de développement associées pour le comprendre lui et ses implications sur le reste du système. Bien que ce soit un outil puissant, utilisé sans conscience il produira du code certainement non maintenable et dont vous ne serez pas sûr qu'il fonctionne.
