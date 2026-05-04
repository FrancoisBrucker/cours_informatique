---
layout: layout/post.njk

title: Création d'un compte et usage basique de Github

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---


## <span id="compte-github"></span> Compte github

- On crée ici votre compte github _pro_, ne mettez pas de bêtises
- Utilisez une adresse mail pérenne (genre votre adresse pro gmail ou votre adresse ecm)

Allez dans la modification du profil :

- en haut à droite de la fenêtre puis _"Your profile"_
- ou `https://github.com/<votre login>` en remplaçant `<votre login>` par votre login.

Il faut que ces données soient exact. Ceci va vous permettre de valoriser votre travail lorsque vous travaillez à plusieurs sur un projet et permettre de vous contacter s'il y a des questions sur le code que vous avez ajouté. Mettez donc au moins :

- un vrai nom ou un pseudo qui vous représente,
- une vrai photo, un logo ou un dessin qui vous représente (rechargez la page pour avoir la nouvelle photo)

{% attention2 "**À retenir**" %}

Vous êtes responsable du code que vous ajoutez au projet : il **faut** pouvoir identifier toute modification/ajout de code.
{% endattention2 %}

## Projet 

> TBD un projet

1. nouveau projet
2. upload
3. download zip
4. versions :
   1. mettre un tag : une release
   2. mettre une nouvelle version avec upload (est-ce que ça marche ?)
   3. faire une branche
   4. voir les évolutions

Ayez un `readme.md`{.fichier} comme page d'accueil

> TBD attention à ne pas mettre dans le projet :
>
> - les fichiers de vscode
> - l'environnement virtuel
> - les fichiers qui ne sont pas des sources (test, pyc, etc)