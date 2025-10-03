---
layout: layout/post.njk

title: Caractérisation des graphes planaires

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

{% lien %}
[Théorème de Kuratowski](https://fr.wikipedia.org/wiki/Graphe_planaire#Caract%C3%A9risation_de_Kuratowski_et_de_Wagner)
{% endlien %}

## Preuve d'un théorème de Jordan simplifié

> TBD suffisant pour les graphes où les sommets sont dénombrables.
> TBD si courbe alors polygone alors droites

## Caractérisation

La caractérisation des graphes planaire de Kuratowski se fait par "_mineur exclu_". C'est à dire caractériser les graphes qui vont nous empêcher de réussir un dessin planaire

{% note "**Définition**" %}
Soit $G$ un graphe. Un graphe $H$ est un mineur de $G$ s'il peut être obtenu par un nombre quelconque des opérations suivantes :

- suppression d'un sommet sans voisin
- suppression d'une arête
- contraction d'un arête: on fusionne l'arête en un nouveau sommet $z$ dont les voisins sont les voisins des anciens sommets formant l'arête
{% endnote %}
{% lien %}
[mineurs de graphes](https://fr.wikipedia.org/wiki/Mineur_(th%C3%A9orie_des_graphes))
{% endlien %}

En deux mots, les mineurs sont les graphes cachés dans un graphe plus gros :

![mineur exemple](./mineur-exemple.png)

### Planarité des Mineurs

{% note "**Proposition**" %}
Si est $G$ un graphe planaire alors tous ses mineurs le sont aussi.
{% endnote %}
{% details "preuve", "open" %}
Les trois opérations pour créer un mineur d'un graphe fonctionnent aussi sur son dessin :

- la suppression d'un sommet ou d'une arête ok
- la contraction d'un arête se fait en concaténant les courbes des arêtes supprimées, comme sur le dessin ci dessous.

![contraction](./contraciton-dessin.png)
{% enddetails  %}

On a donc déjà la proposition suivante :

{% note "**Proposition**" %}
Si $G$ est planaire, il ne peut avoir ni $K_5$ ni $K_{3,3}$ comme mineur
{% endnote %}
{% details "preuve", "open" %}
Clair puisque l'on a montré que ni $K_5$ ni $K_{3,3}$ ne peuvent être planaire.
{% enddetails  %}

### Réciproque

La réciproque est également vraie et c'est cette partie qui va être plus difficile à démontrer.

- [cycle et 2-connectivité](../../chemins-cycles-connexite/#2-connexité-cycle){.interne}
- relation d'équivalence entre arêtes donne les composantes 2-connexes e R f si e = f ou s'il existe un cycle élémentaire contenant e et f
- [composantes 2-connexes](https://en.wikipedia.org/wiki/Biconnected_component)

Séparation par arêtes (déconnecte le graphe) ou par point d'articulation (via algorithme DFS et retour).

{% note "**Proposition**" %}
Si $G$ est planaire si et seulement si ses composantes 2-connexes le sont
{% endnote %}
{% details "preuve", "open" %}
Les composantes 2-connexes sont liées uniquement par un sommet d'articulation ou une arêtes.

![composantes 2 connexes](./composantes-2-connexes.png)

Le graphe dont les sommet sont les composantes 2-connexe et une arête si connexion est un arbre (sinon il existe un cycle et du coup plus gros)

{% enddetails  %}

> TBD caractérisation par mineur exclus gros théorème de Seymour.

> <https://fr.wikipedia.org/wiki/Th%C3%A9or%C3%A8me_de_Robertson-Seymour>
> 

- définitions et propriétés + Kuratowsky : <https://perso.ens-lyon.fr/eric.thierry/Graphes2009/theophile-trunck.pdf> ou <https://perso.ens-lyon.fr/eric.thierry/Graphes2007/vincent-nivoliers.pdf> On a besoin de :
  - coloriabilité via le problème de la galerie d'art :
    - <https://fr.wikipedia.org/wiki/Probl%C3%A8me_de_la_galerie_d%27art>
    - exercices : <https://static.idm314.org/resources/activities/idm-art-gallery-fr.pdf>
    - TIPE : <https://cpge-paradise.com/TIPE/Baudoin_Solal/PPT_Baudoin_Solal.pdf>
    - théorème de Jordan : <https://minerve.ens-rennes.fr/images/Le_Th%C3%A9or%C3%A8me_de_Jordan_S.Quayle_V.Le_Gruiec..pdf>
  - k-connectivité
- preuve Kuratowski juste avec 2-connexité: <https://www.math.cmu.edu/~mradclif/teaching/228F16/Kuratowski.pdf>
- planaire et embedding : <https://www.youtube.com/watch?v=MNgKx4A1pXM&list=PLriUvS7IljvkGesFRuYjqRz4lKgodJgh2&index=13>

  - topologie et courbe fermée Jordan  : <https://pagesperso.g-scop.grenoble-inp.fr/~lazarusf/Enseignement/graphesPlans.pdf>
  - exercices : <http://www.gymomath.ch/javmath/polycopie/th_graphe5.pdf>
  - preuve simple ? <https://www.sciencedirect.com/science/article/pii/0012365X80901454>

## Caractérisation par mineur exclus

> TBD <https://fr.wikipedia.org/wiki/Th%C3%A9or%C3%A8me_de_Robertson-Seymour>
