---
layout: layout/post.njk

title: Tris spéciaux

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

{% lien %}
[Corrigé](./corrigé){.interne}
{% endlien %}

Les tris spéciaux ont des complexités inférieures à $\mathcal{O}(n\log(n))$, ce qui n'est bien sur possible que si l'on se place dans des cas particuliers d'entrées.

## <span id="tri-paquets"></span>Tri par paquets (bucket sort)

On veut trier les $n$ objets d'un tableau $\mathcal{E}$ par rapport à leur valeur via **une injection** $f: \mathcal{E} \to [0, m[$ allant de $\mathcal{E}$ dans l'ensemble des entiers de 0 à $m-1$.

**_Le tri par paquets_** consiste à créer un tableau de taille $m$ et de ranger chaque élément $o$ de $\mathcal{E}$ dans ce tableau à l'indice $f(o)$. Il suffit ensuite de rendre la restriction de ce tableau aux éléments contenant les éléments de $\mathcal{E}$.

{% faire %}
Écrire le pseudocode de cet algorithme. On supposera que l'on cherche à trier $n$ entiers.
{% endfaire %}
{% faire %}
Quelle est la complexité en temps et en mémoire de cet algorithme ?
{% endfaire %}
{% faire %}
Utilisez cet algorithme pour trier :

1. $n$ entiers deux à deux différents.
2. comment modifier cet algorithme si les entiers peuvent être égaux ?
3. complexité de cet algorithme ?
{% endfaire %}
{% faire %}
Quand utiliseriez vous cet algorithme pour trier $n$ objets ?
{% endfaire %}

## <span id="tri-base"></span>Tri par base

Ce tri s'applique uniquement aux entiers positifs. Notre entrée est une liste $T$  de listes de mêmes tailles composées de 0 et de 1 représentant des entiers écrit en base 2 (comme pour le [compteur binaire](../compteur-binaire)). Par exemple : $T = [[1, 0, 0, 1], [1, 1, 1, 0], [0, 0, 0, 1]]$ qui correspond aux nombres $[9, 14, 1]$.

Le principe de ce tri est très simple :

- On considère d'abord le bit de poids le plus faible (_ie._ le plus à droite). On crée alors deux tableaux L0 et L1 initialement vides et on va itérativement considérer chaque élément de la liste à trier :
  - les entiers dont le bit de poids le plus faible est 0 sont ajoutés à la fin de L0
  - les entiers dont le bit de poids le plus faible est 1 sont ajoutés à la fin de L1
- On concatène les deux sous-listes T = L0 + L1
- On recommence sur le bit à gauche de celui qu'on vient de traiter.
- ...

Les parcours des liste T se font, toujours, de la gauche vers la droite.

Pour notre exemple :

1. après premiere boucle : $[[1,1,1,0], [1, 0, 0, 1], [0, 0, 0, 1]]$
2. après deuxième boucle : $[[1, 0, 0, 1], [0, 0, 0, 1], [1,1,1,0]]$
3. après troisième boucle :$[[1, 0, 0, 1], [0, 0, 0, 1], [1,1,1,0]]$
4. après quatrième boucle : $[[0, 0, 0, 1], [1, 0, 0, 1], , [1,1,1,0]]$

Questions :

{% faire %}
Donnez le pseudo-code, la preuve et la complexité de cet algorithme.
{% endfaire %}
