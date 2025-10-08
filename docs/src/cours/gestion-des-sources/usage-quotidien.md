---
layout: layout/post.njk

title: Gérer ses sources au quotidien

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Pour que tout se passe au mieux lorsque vous utilisez un système de gestion des sources, il est important de suivre quelques règles qui vous permettront de facilement :

- connaître le contenu d'un commit
- contacter la personne ayant fait un commit
- naviguer dans l'historique du projet

Sans les trois conditions ci-dessus, utiliser un SCM n'est pas vraiment utile et vous fera perdre plus de temps qu'en gagner.

## Identité

Pour que le processus de gestion des sources soit efficace il est nécessaire que tout commit soit bien :

- identifié : l'auteur du commit doit pouvoir être retrouvé
- documenté : le message accompagnant le commit doit être descriptif.

### Profil

Ayez votre profil à jour :

- nom et prénom ou pseudo identifiable
- adresse mail à jour

Il vous est facile d'avoir une identité par défaut (liée à votre compte) et une identité par projet (dans la configuration du projet). Ceci permet de différentier les projet pro des projets perso sans avoir à faire de grandes manipulations.

### Message de commits

Utilisez un éditeur de texte que vous maîtrisez pour éditer le message de commit. Par défaut c'est [vi](https://fr.wikipedia.org/wiki/Vi), éditeur historique et présent sur toute machine unix qui est utilisé, mais qui n'est pas forcément votre éditeur de prédilection.

Un message de commit contient forcément **1 ligne** décrivant le commit (on verra dans la partie suivante des méthodes pour les écrire). Puis, si nécessaire, une description plus long (souvent inutile).


<!-- TBD 

à étoffer (faire un exemple) en utilisant les liens précédent 

-->
### .gitignore

{% lien %}

- [fichier .gitignore avec github](https://docs.github.com/fr/get-started/git-basics/ignoring-files)
- [tuto en français](https://www.youtube.com/watch?v=gkzBzBomYyI)

{% endlien %}
