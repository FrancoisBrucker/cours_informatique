---
layout: layout/post.njk

title: Graphes hamiltonien

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---


La propriété se généralise même :

{% note "**Proposition (Ore, 1960)**" %}
Si $G=(V, E)$ avec $\vert V \vert = n \geq 3$ est un graphe tel que $\delta(x) + \delta(y) \geq \vert V \vert$ pour tous sommets non adjacents $x, y \in V$, alors $G$ admet un chemin Hamiltonien.
{% endnote %}
{% details "preuve", "open" %}

On suppose que $G$ n'est pas hamiltonien. Comme le graphe complet est hamiltonien il va exister $G'=(V, E')$ tel que :

- $E \subseteq E'$
- $G'$ n'est pas hamiltonien (_ie._ pas de cycle hamiltonien)
- si on ajoute l'arête $uv$ à $G'$ il devient hamiltonien.

Il existe donc dans $G'$ un chemin hamiltonien $x_0\dots x_{n-1}$ tel que $u=x_0$ et $v=x_{n-1}$. Pour tout $0\leq i<n-1$, on ne peut avoir $x_ix_k \in E'$ et $x_{i+1}x_0 \in E'$ sinon, tout comme la preuve précédente, on peut construire le cycle hamiltonien $x_0\dots x_ix_{n-1}\dots x_{i+1}x_0$.

De là, $\delta(x_0) + \delta(x_{n-1}) < n$ dans $G'$ puisqu'au plus une des deux arêtes $x_ix_k$ ou $x_{i+1}x_0$ est dans $E'$ pour $0\leq i<n-1$.
Or comme $E \subseteq E'$ on aurait également $\delta(x_0) + \delta(x_{n-1}) < n$ dans $G$, ce qui est impossible.

{% enddetails %}

On le voit, lorsque les graphes ont beaucoup d'arêtes ils vont posséder un cycle hamiltonien.



> TBD degrés : euler clair pair / ham et degré. Prop de Chvatal-Erdos.
> pour orienté : Woodall (1972) d^+(x) +d^+(y)≥n
> TBD voir video de distel : <https://www.youtube.com/watch?v=xqdRiZzKhvM&list=PL_qO0UBYKVJ1myNZdh3j27fniqRtHYifm&index=25>

> algorithmes randomisés.
> [hamiltonian ciruits in random graph](https://www.sciencedirect.com/science/article/pii/0012365X76900686?ref=pdf_download&fr=RR-2&rr=a3dea0291f060c79) (posa) et [Fast probabilistic algorithms for hamiltonian circuits and matchings](https://www.sciencedirect.com/science/article/pii/002200007990045X?ref=pdf_download&fr=RR-2&rr=a3dea07c28a50c79)

