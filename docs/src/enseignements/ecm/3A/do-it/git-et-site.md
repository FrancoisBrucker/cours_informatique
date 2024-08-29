---
layout: layout/post.njk 
templateEngineOverride: njk, md

title: Gestion des source et site do-it
tags: ['enseignement', 'ECM']

eleventyNavigation:
    order: 1
    prerequis:
        - "/cours/coder-et-développer/ordinateur-développement/"
        - "/tutoriels/format-markdown/"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---



Ce cours introductif ne présuppose aucune connaissance informatique spécifique (à part les acquis du tronc commun, c'est à dire vraiment pas grand chose).

Le but de ce cours est que vous puissiez :

- comprendre la problématique de la gestion des sources
- gérer efficacement un projet à plusieurs
- contribuer [au parcours Do_It](https://francoisbrucker.github.io/do-it/)

## Gestion des sources ?

### Pourquoi

1. introduction à la gestion des sources
   1. pourquoi ?
      - Pour ne plus avoir peur d'avancer et de tester ; et pour le travail en groupe
      - <https://www.atlassian.com/fr/git/tutorials/why-git>
   2. pour qui ? Tout le monde ! C'es un cadeau fait par les informaticiens au monde. Ne le salopez pas comme la gestion de projet agile...
   3. histoire :
      - <https://www.atikteam.com/fr/blog/page/Gestion-de-sources-centralisee-vs-decentralisee>
      - <https://blog.tarynmcmillan.com/a-history-of-version-control>
2. Travailler sur un projet
   1. 1 personne :
      1. modification linéaire (temporelle d'un fichier)
      2. si erreur ou avancée non pertinente, il faut pouvoir revenir en arrière.
         1. Garder un backup de tous le projet n'est pas optimal :
            - on peut revenir trop en arrière si on ne sauve pas assez souvent
            - on prend trop de place si on sauve tout trop souvent
            - on ne se souvient plus trop ce qu'on a modifié
            - on ne peut pas tester plusieurs choses différentes en parallèle
         2. solution :
            - ne sauver que ce qui est modifié
            - marquer chaque modification d'un résumé du travail effectué
            - faire de branches
            - > TBD faire des schémas.
         3. On ne peut pas faire ça a la mimine. Il faut un logiciel qui gère tout ça.
            1. gestion des branches
            2. des logs
            3. des fusions (merge et rebase)
   2. plusieurs personnes :
      1. ajout de complexité :
         1. plusieurs versions d'un projets
         2. plusieurs personnes qui travaillent sur le même fichier
         3. travail asynchrone entre les personnes. Une personne va avancer à un endroit pendant qu'une autre travaille sur autre chose
         4. reprendre un projet
      2. mauvaise solution :
         1. ajouter des règles : ce ne sera jamais ok et sclérosera l'ensemble. On fera des règles parce que'elle sont facile à vérifier pas parce qu'elle sont utiles (voir l'administration).
         2. un superviseur général qui doit tout valider avant. Il va y avoir de gros bottleneck et va ralentir tout le process : on ne mets à jour que tous les mois, ...
      3. bonne solution :
         1. environnement distribué
         2. branches

### Comment

On utilise git et github pour montrer comment tout ça fonctionne. On fera ça sur un projet existant : [le projet do-it](https://github.com/FrancoisBrucker/do-it).

1. [création d'un compte github](/cours/gestion-des-sources#compte-github){.interne}
2. Ajout en tant que collaborateur
3. utilisation de l'[application desktop](/cours/gestion-des-sources/projet-github-desktop/){.interne} pour [télécharger le projet](/cours/gestion-des-sources/projet-github-desktop/#récupérer-projet){.interne}.
4. Analyse du projet :
   1. fichiers
   2. compilation
   3. visualisation en local
5. contribuer

## Le site Do_It

### Faire des modifications en local

> TBD : prendre un cobaye et utiliser son ordi pour le montrer à tous.

1. fait son home et vérifie en local que c'est ok.
2. voir les ajouts en local et continuer jusqu'à ce que tout se compile bien.
3. commit

### Envoyer ses modifications sur le serveur

> TBD faire en sorte que ce soit bien un rebase

1. pull
2. push

> TBD simuler un merge

## À faire chez soit

1. suivre le cours desktop pour [faire un nouveau projet](/cours/gestion-des-sources/projet-github-desktop/#nouveau-projet){.interne} ce qui vous apprendra les principales actions de la gestion des sources.
2. ajouter ses pok et mon du temps 1.

{% info %}
[Aide markdown du site Do_It](https://francoisbrucker.github.io/do-it/cs/contribuer-au-site/)
{% endinfo %}

## Pour aller plus loin

Continuez le cours suivant, au moins la partie où l'on crée et gère des projets uniquement avec le site github :

{% aller %}
[Cours Gestion des sources](/cours/gestion-des-sources/){.interne}
{% endaller %}

Et si vous voulez faire de l'informatique, faites la suite du cours et faite toute la gestion de projet git au terminal. Vous aurez plus de contrôle sur ce que vous faites.

> TBD :
>
> - histoire de la gestion des sources à étoffer et à mettre en perspective
> - résumé des différentes actions à effectuer pour que tout se passe bien
