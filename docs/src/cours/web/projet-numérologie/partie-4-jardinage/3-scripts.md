---
layout: layout/post.njk

title: "Projet numérologie : partie 4 / scripts"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

<!-- début résumé -->

On explicite les divers scripts de notre serveur

<!-- fin résumé -->

Ajout des scripts permettant l'installation et l'exécution du serveur.

## Scripts utiles

L'usage veut que l'on lance le serveur en exécutant la commande : `npm start`. Ceci se fait en ajoutant un script `"start"` au fichier `numérologie/package.json`{.fichier} :

```json
...

"scripts": {
    "init": "node db-init.js",
    "test": "echo \"Error: no test specified\" && exit 1",
    "start": "node index.js"
},

...
```

On exécute alors le serveur avec la commande `npm start` qui est classique et est un raccourci pour `npm run start`.

On a pas encore de script de tests, mais ça va venir. C'est le boulot de la partie suivante.

## Instructions

On modifie aussi le README.md pour ne pas prendre à dépourvu un utilisateur voulant utiliser notre programme.

```markdown
# Numérologie

Voyez la vie en base 10 en associant un chiffre à votre prénom.

## Initialisation

Une fois cloné le projet on :

1. installe les dépendances : `npm install`
2. initialise la base de donnée `npm run init`

## Lancement du serveur

`npm start`
```

## Plus tard

Lorsque l'on aura plus qu'une commande à utiliser pour installer le serveur (des dépendances front et back par exemple), on créera un dossier script où l'on placera nos scripts shell unix (et windows si nécessaire) pour gérer tout ça.

Il est indispensable que tout se fasse le plus simplement possible pour un utilisateur voulant utiliser ou mettre à jour son serveur. Si la mise à jour du serveur est aisée, il sera facile de le mettre en production et on aura plus peur de modifier le code.

{% note %}
La modification du code et la mise en production d'un serveur doit être un **non évènement**.
{% endnote %}
