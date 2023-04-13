---
layout: layout/post.njk

title: Exporter du markdown avec pandoc
tags: ['tutoriel', 'markdown']
authors:
    - François Brucker

eleventyNavigation:
  prerequis:
      - ../terminal/
      - ../format-markdown/


eleventyComputed:
    eleventyNavigation:
        key: "{{ page.url }}"
        title: "{{ title }}"
        parent: Tutoriels
---

<!-- début résumé -->

L'utilitaire [pandoc](https://pandoc.org/) et son utilisation pour le format markdown.

<!-- fin résumé -->

Pandoc est un utilitaire de conversion de fichier texte. Il peut virtuellement transformer tout format texte en un autre (voir les [démos](https://pandoc.org/demos.html) pour différentes conversions).

Nous allons ici juste montrer ses capacités pour le markdown.

## Installation

D'après la [doc](https://pandoc.org/installing.html), selon le système d'exploitation :

{% details "sous linux" %}
`sudo apt install pandoc` dans un [terminal](../terminal.md)
{% enddetails %}

{% details "sous mac" %}
Installez [brew](https://brew.sh/) puis `brew install pandoc` dans un [terminal]({../terminal.md)
{% enddetails %}

{% details "sous windows" %}
Téléchargez le [package windows](https://github.com/jgm/pandoc/releases/tag/2.19) et installez le. Il vous faudra sûrement un dezippeur.(comme [7zip](https://www.7-zip.org/))

{% enddetails %}

Selon le format d'export, il vous faudra d'autres logiciels. Je vous conseille d'ores et déjà d'[installer latex](https://www.latex-project.org/get/) pour pouvoir facilement exporter en pdf sans passer par html et un navigateur.

## exemple d'utilisation

Pour exporter du markdown en html, j'utilise la ligne de commande suivante qui m'écrit de jolies équations avec <https://www.mathjax.org/> :

`pandoc --mathjax --standalone --metadata pagetitle="titre page" --metadata charset="UTF-8"  page.md -o page.html`

* premier élément : le nom de la commande, ici `pandoc`.
* cette commande prend en entrée le fichier `page.md` qui est le dernier élément de la ligne
* les autres éléments de la lignes sont des [arguments](https://fr.wikipedia.org/wiki/Commandes_Unix#Le_passage_d'arguments_aux_commandes). Dans le monde des commandes, il y a deux types de paramètres "un `-` suivit d'une lettre" et "deux `--` suivi d'un mot" Ces paramètre peuvent être suivi d'arguments, c'est à dire des mots ne commençant pas par un `-` (`-o page.html`), ou pas (`--mathjax`) Notre commande a 4 paramètres :
  * `-o page.html`. *Un paramètre avec un argument*. Le fichier se sorti s'appellera `page.html`. Il determine le type de sortie (ici de l'html) et sera dans le même dossier que le fichier `page.md`
  * `--mathjax`. *Un paramètre sans argument*. On utilise la [bibliothèque mathjax](https://www.mathjax.org/) pour *compiler* les équations latex
  * `--standalone`. *Un paramètre sans argument*. On crée un fichier html complet (par défaut, `pandoc` ne crée qu'un bout de html qui peut être combiner avec d'autres bout)
  * `--metadata pagetitle="titre page"`. *Un paramètre avec un argument*. En combinaison avec le paramètre `standalone`. Permet de donner un titre à la page html, ici "titre page".
  * `--metadata charset="UTF-8"`. *Un paramètre avec un argument*. Permet de spécifier l'encodage des caractères (voir cours sur les fichiers). Devrait permettre de voir les accents.

{% info %}
Si vous avez à compiler plein de fois votre page, n'oubliez pas qu'utiliser la *flèche du haut* dans un terminal rappelle la dernière commande utilisée. Donc même une commande avec plein de paramètres est facile à réutiliser. Il suffit d'appuyer sur la flèche du haut.
{% endinfo %}

Lorsque je fais mes tests en html, après chaque re-compilation je recharge la page avec *"F5"* ou *"ctrl+R"* dans le navigateur. Le process est **très rapide**.
