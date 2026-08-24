---
layout: layout/post.njk

title: Coder des projets

eleventyNavigation:
    prerequis:
        - "/cours/système/interagir-avec-système/"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

La première partie nous a appris les concepts fondamentaux d'un langage de programmation à objet et nous a permis d'écrire et d'exécuter un (petit) programme python. Cette partie nous permettra de passer à l'échelle en créant des programmes sur plusieurs fichiers et à traiter des données.

{% attention %}
Nous allons passer pas mal de temps à créer des fichiers, des dossiers et à utiliser le terminal. **Assurez-vous donc d'avoir lu et compris** les prérequis.
{% endattention %}


Cette partie est consacrée aux moyens et méthodes pour écrire des applications :

- dont la durée de vie va dépasser le cadre d'un TD
- dont la portée et le nombre de fonctionnalité peut être importante

On y verra également que :

- le code en lui même n'est pas important, c'est la fonctionnalité qu'il implémente qui l'est
- on va passer plus de temps à lire du code qu'à l'écrire, il est donc nécessaire d'avoir du code lisible

Enfin :

{% attention2 "**À retenir**" %}
C'est en codant qu'on devient codeur. Vous allez passer votre temps à vous tromper ou ne pas comprendre. Ce processus est normal. **MAIS** si vous ne comprenez pas quelque chose  : arrêtez vous et comprenez. 

Ne recommencez pas à coder avant d'avoir compris sinon les incompréhensions vont s'accumuler et vous perdrez au final plus de temps.
{% endattention2 %}


## <span id="installation-développement"></span> Outils de développement

{% aller %}
[Installer les Outils de développement](./outils/){.interne}
{% endaller %}

## Écrire du code

{% aller %}
[Écrire du code](./écrire-code/){.interne}
{% endaller %}

## <span id="développer"></span>Gestion des données

{% aller %}
[Gestion des données](gestion-données){.interne}
{% endaller %}

