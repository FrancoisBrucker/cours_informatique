---
layout: layout/post.njk 
title: "Environnement virtuel pour pytglet"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"


---

> TBD à faire bien.

{% aller %}

1. Environnement virtuel. Vous allez utiliser [le TP de programmation évènementiel](/cours/coder-et-développer/programmation-évènementielle/projet-arkanoid/){.interne} dont le code est là : [`Arkanoid.zip`{.fichier}](./Arkanoid.zip){.fichier}.
   1. dézippez le projet et créez-vous un environnement virtuel dans le dossier projet
   2. ajoutez les modules `pyglet` et `pytest` à cet environnement en utilisant `pip` basé sur l'interpréteur de votre environnement virtuel
   3. vérifiez que les tests passent et que le code fonctionne avec votre environnement
   4. créez les fichiers :
      - `requirements.txt`{.fichier} qui explicite les dépendances
      - `readme.md`{.fichier} qui explicite comment exécuter le programme et le lien vers le cours.
2. Dépôt :
   1. [créez vous un compte github](/cours/gestion-des-sources/dépôt/github-compte/){.interne} 
   2. projet mettez le projet en ligne sur github (ne mettez pas l'environnement virtuel ni le dossier `__pycache__`{.fichier} !)
1. [Gestion des sources avec github](/cours/gestion-des-sources/évolution-code/github-projet/){.interne}
2. [Partager des sources avec github](/cours/gestion-des-sources/partage/github-desktop/){.interne}


{% endaller %}