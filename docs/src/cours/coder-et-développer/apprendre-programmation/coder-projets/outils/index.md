---
layout: layout/post.njk

title: Outils de développement

eleventyNavigation:
    prerequis:
        - "/cours/système/interagir-avec-système/"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Lorsque l'on veut coder plus d'une fonction ou deux, il est nécessaire d'avoir de bons outils. On va ainsi passer d'un éditeur d'apprensissage comme spyder à une suite logicielle nous permettant de contrôler parfaitement ce qui est exécuté (nous allons installer notre propre interpréteur) et nous permettant de gagner du temps de développement en intégrant des outils puissant d'édition de code (on utilise des logiciels d'édition de code professionnel).

Commençons par installer notre propre interpréteur python.

## Installer et utiliser un interpréteur python

Jusqu'à présent on a utilisé des interpréteurs externes pour exécuter notre code. Si l'on cherche à créer ses propres programmes, il est préférable d'avoir un interpréteur sur propre ordinateur. Ceci sera plus rapide et permettra à terme d'être paramétrable à l'envie.

{% aller %}
[Installer un interpréteur python](interpréteur-installation){.interne}
{% endaller %}

## IDE

Une fois l'interpréteur installé, plutôt que de l'utiliser directement, on utilise un éditeur de texte spécialisé dans l'écriture de code : [un IDE](https://fr.wikipedia.org/wiki/Environnement_de_d%C3%A9veloppement). Il existe plusieurs choix possible, mais le plus utilisé actuellement est vscode.

{% aller %}
[Éditeur vscode](éditeur-vscode){.interne}
{% endaller %}

La principale différence entre un éditeur de texte et un notebook est que l'interpréteur est re-exécuté à chaque exécution : il ne garde rien en mémoire de la précédente exécution du code. Ceci permet de faire du code rép´table où toutes les informations sont uniquement contenues dans le fichier que l'on exécute.

## Installer des modules externes

Même si python vient avec de nombreux modules d'installés il arrive toujours un moment où l'on devra installer des modules développés par d'autres personnes :

{% aller %}
[Installer des modules](./modules-externes-python/){.interne}
{% endaller %}
