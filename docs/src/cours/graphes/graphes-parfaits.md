---
layout: layout/post.njk

title: Graphes parfaits

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

{% lien %}

- [Graphes parfait avec Maria Chudnovsky](https://www.youtube.com/watch?v=C4Zr4cOVm9g)
- [Une revue du problème par Chvatal](https://users.encs.concordia.ca/~chvatal/perfect/spgt.html)
- [un cours détaillé](https://arxiv.org/pdf/1301.5149)

{% endlien %}

- [$\omega(G)$](../structure/#definition-notation-clique-stable-maximum){.interne}
- [$\chi(G)$](../colorabilité/#definition-notation-coloration-minimum){.interne}

> TBD def
>
> TBD différence non bornée : <https://perso.ens-lyon.fr/edouard.bonnet/publi/tree-zykov.pdf> et <https://math.uchicago.edu/~may/VIGRE/VIGRE2008/REUPapers/Zhang.pdf>
> TBD dessins de quelques graphes parfait
>
> NP complet en general mais poly en perfect graphs : <https://www.graphclasses.org/classes/gc_56.html> et <https://en.wikipedia.org/wiki/Perfect_graph#Algorithms>

On en connaît déjà :

- les cliques et les chemins de longueur pair
- graphes biparti (donc les arbres)

Et il y en a plein d'autres :

- [graphes cordées](https://fr.wikipedia.org/wiki/Graphe_cordal) (https://math.stackexchange.com/questions/4045122/why-are-chordal-graphs-always-perfect-graphs), donc aussi [les graphes d'intervalles](https://fr.wikipedia.org/wiki/Graphe_d%27intervalles)
- [graphes de comparabilités](https://fr.wikipedia.org/wiki/Graphe_de_comparabilit%C3%A9)
- ...

> TBD exo : Threshold graphs are perfect : <https://en.wikipedia.org/wiki/Threshold_graph>

Il existe deux types d graphes fondamentaux qui ne sont pas parfait les cycles de longueur impair $C_{2p+1}$ avec $p>1$ - nommés _**odd holes**_ - et leurs complémentaires $\overline{C_{2p+1}}$, nommés _**odd antiholes**_ :

{% exercice %}
Montrez que les graphes $C_{2p+1}$ et $\overline{C_{2p+1}}$ ne sont pas parfaits.
{% endexercice %}
{% details "corrigé" %}
On a vu que $\omega(C_{2p+1}) = 2 < \chi(C_{2p+1}) = 3$.

Pour les $\overline{C_{2p+1}}$, il suffit de remarquer que :

- $\omega(\overline{C_{2p+1}}) = p$ puisque $\\{x_{2i+1} \vert 0\leq i \leq p\\}$ est une clique et tout sous ensemble à $p+1$ sommet contiendra forcément 2 voisins (principe ds tiroirs)
- $\chi(\overline{C_{2p+1}}) = p+1$ car $c(x_i)$ ne peut être au mieux égale qu'à 1 seul de ses voisins ($\chi(\overline{C_{2p+1}}) \geq p+1$) et la coloration $c(x_{1})=0$ et $c(x_{2i}) = c(x_{2i+1}) = i$ pour $1\leq i \leq p$ fonctionne.

{% enddetails %}

> TBD exercice les cycles non cordés de longueur impair (_odd holes_) ne sont pas des graphes parfais, ainsi que leurs complémentaires (_anti odd holes_), en déduire que tout graphe qui possède un cycle impair non cordé ou son complémentaire ne peut-être parfait.

Les graphes parfait lient également les cliques et les stables :

{% note "**Proposition**" %}
Un graphe $G$est parfait si et seulement pour tout sous graphe $H$ de $G$ à $V(H)$ sommets, on a $\omega(H)\alpha(H)> V(H)$

{% endnote %}
{% details "preuve", "open" %}

> TBD thm 3.1 <https://ahmadabdi.com/ltcc/lecture_2.pdf>

{% enddetails %}

> [Weak Perfect Graph Theorem](https://www.youtube.com/watch?v=Koc63QhxPgk)

{% note "**Théorème (Lovàsz, 1972)**" %}
Un graphe est parfait si et seulement si son complémentaire est parfait.
{% endnote %}
{% details "preuve", "open" %}

> TBD

Conséquence directe de la proposition précédente en remarquant que $\omega(G) = \alpha(\overline{G})$.

{% enddetails %}

[Strong Perfect Graph Theorem (179 pages sans un seul dessin)](https://annals.math.princeton.edu/wp-content/uploads/annals-v164-n1-p02.pdf)

Le théorème fort des graphes parfait permet de faire des algorithmes de reconnaissance polynomiaux : <https://algorithms.leeds.ac.uk/wp-content/uploads/sites/117/2017/09/FOCS03final.pdf>

On les retrouves à des endroits inattendus :

> TBD le line graph d'un graphe biparti est parfait.
> TBD graphe auto complémentaire parfait : <https://mathoverflow.net/questions/452045/are-there-many-self-complementary-perfect-graphs>
> TBD problèmes de coloration facile du coup : <https://iuuk.mff.cuni.cz/~rakdver/kgii/lesson20-8.pdf>