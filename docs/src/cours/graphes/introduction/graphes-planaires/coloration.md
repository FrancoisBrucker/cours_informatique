---
layout: layout/post.njk

title: Coloration de graphes planaires

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---


## Propriétés

> TBD si sommets de degré ≤ 4 alors on peut restreindre
> TBD si pas 4-coloriable min alors il est triangulé.
> TBD si carré
> TBD chaine de Kempe déjà utilisé en coloration.

## 6-colorable

> TBD 6 par notre algo de coloration

> TBD algo direct
> 
## 5-colorable

> TBD 5 couleur : démonstration de Kempe.

> TBD algo linéaire : <https://www.enseignement.polytechnique.fr/profs/informatique/Francois.Morain/INF431/X06/5col.pdf>

> TBD algo direct puis il faut faire les transformations des chaines de Kempe

Attention : ne fonctionne pas pour 4 couleur à cause de 
> TBD Une démo (fausse) du théorème des 4 couleurs par Kempe : <https://www.youtube.com/watch?v=adZZv4eEPs8>

## Théorème des 4 couleurs

> thm des 4 couleurs qui est le 1er théorème assisté par ordinateur (pas une IA, c'est la preuve qui est un algorithme)

>
> TBD théorème des 4 couleurs :
>
> - <https://www.lix.polytechnique.fr/~werner/PI-4C/sujet4C.html> <https://www.lix.polytechnique.fr/~werner/PI-4C/four.pdf>
> - 4 couleurs : <https://inria.hal.science/hal-04034866/document>

> algorithmes polynomiaux pour le trouver, mais dur à implémenter. La preuve originelle donne un algo en O(n^4) avec l'étude de 1478  et configuration. Amélioré par Rob-Sey en O(n^2) 633 et en 2026 en O(n log(n)) <https://arxiv.org/abs/2603.24880>
> Principe par réduction :
>

Fonctionne en évitant les configuration impossible de Kempe :

1. Recherche d'une configuration réductible : Grâce à la formule d'Euler, on sait que tout graphe planaire contient au moins un sommet de degré inférieur ou égal à 5. Plus largement, le graphe contient obligatoirement au moins une configuration appartenant à un ensemble inévitable de configurations réductibles (ex: [633 configurations](https://thomas.math.gatech.edu/OLDFTP/fcdir/unavoidable.pdf) pour l'algorithme de Robertson et al.).
2. Réduction : On isole cette configuration, puis on "simplifie" ou retire temporairement ces sommets du graphe $G$ pour obtenir un graphe plus petit $G'$.
3. Appel récursif : On applique l'algorithme sur le graphe réduit $G'$.
4. Extension de la coloration : Une fois que $G'$ est coloré avec 4 couleurs, on réintègre la configuration initiale. Par définition d'une configuration "réductible", il est toujours possible d'ajuster les couleurs des sommets voisins — parfois en inversant les couleurs le long de chemins spécifiques appelés chaînes de Kempe — afin de libérer une couleur valide pour les sommets réinsérés.


{% lien %}
<https://thomas.math.gatech.edu/FC/fourcolor.html>
description de l'algorithmie ici : <https://thomas.math.gatech.edu/PAP/npfc.pdf>
le papier complet : <https://thomas.math.gatech.edu/PAP/fc.pdf>
{% endlien %}

## Colorable est NP-complet

> TBD pareil que colorier les faces.
 
> TBD 3 colorable planaire np-complet : <https://www.cs.cmu.edu/afs/cs/academic/class/15451-s04/www/Lectures/chapter23.pdf> ds 2026


## Algorithmes de coloration

> - 6 coloration avec l'algo de coloration
> - 5 coloration linéaire 
> - 4 coloration d'un graphe planaire 3 colorable (Kawarabayashi et Ozeki 2009) <https://tgt.ynu.ac.jp/ozeki/2009KO2.pdf>. Soit il sort une 4 coloration, soit il dit que le graphe n'est pas 3 colorable. Pourquoi n'est-ce pas en contradiction avec le fait que le problème est NP-complet ?

> TBD  algorithme en O(n^2) dans N. Robertson, D. P. Sanders, P. Seymour, R. Thomas, « The four-colour theorem », J. Combin. Theory Ser. B 70 (1997), 2–44.
> Mais compliqué à mettre en oeuvre...
> 

## Applications 

### Dans des problèmes

3 colorable et problème de la galerie d'art : <https://fr.wikipedia.org/wiki/Probl%C3%A8me_de_la_galerie_d%27art>

### Coloration de cartes de géographie

coloration de cartes de géographie (pourquoi souvent 6 couleurs ?)
 
### Coloration et partage de secrets

> TBD un sujet qui lie tout ce qu'on a fait jusqu'à maintenant.

> <https://fr.wikipedia.org/wiki/Preuve_%C3%A0_divulgation_nulle_de_connaissance>
>
{% lien %}

- [Avi Wigderson parle des zero knowledge proof](https://www.youtube.com/watch?v=5ovdoxnfFVc)
- [le papier](https://www.wisdom.weizmann.ac.il/~oded/X/gmw1j.pdf)

{% endlien %}

> [Curry-Howard correspondance](https://fr.wikipedia.org/wiki/Correspondance_de_Curry-Howard)

### Algorithmes de coloration de listes

> 5 liste colorable.

### Variantes

> TBD pays non connexes
> TBD colonies lunaires

### Dans les démonstrations

> TBD Coloriabilité via le problème de la galerie d'art :
> 
> - <https://fr.wikipedia.org/wiki/Probl%C3%A8me_de_la_galerie_d%27art>
> - exercices : <https://static.idm314.org/resources/activities/idm-art-gallery-fr.pdf>
> - TIPE : <https://cpge-paradise.com/TIPE/Baudoin_Solal/PPT_Baudoin_Solal.pdf>
