---
layout: layout/post.njk

title: Les $\mathcal{O}()$ pour le calcul de complexité

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

> TBD dire que c'est knuth qui a popularisé l'utiliation de ces calculs.

### Conséquences algorithmiques

Ceci est plutôt intéressant en algorithmie car l'on ne connaît pas toujours exactement le nombre d'opérations élémentaires utilisées, mais on peut les majorer de façon assez précise. On utilisera ainsi les $\mathcal{O}$ pour mesurer par rapport à la taille $N$ de l'entrée de l'algorithme :

* le nombre d'opérations élémentaires effectuées par l'algorithme avant de s'arrêter
* le temps mis par l'algorithme pour s'exécuter
* la taille de la mémoire utilisée pour par l'algorithme


La [première règle](./#OA1){.interne} montre qu'un nombre constant est toujours en $\mathcal{O}(1)$. Pour un algorithme, il est souvent compliqué de savoir exactement de combien d'[opérations basiques](../pseudo-code#instruction-basique){.interne} est constituée une opération ou le temps exact qu'elle va prendre (pour un ordinateur, cela dépend du type de processeur. Par exemple, l'addition avec un x68 est faite [avec des registres](https://ensiwiki.ensimag.fr/index.php?title=Constructions_de_base_en_assembleur_x86), elle nécessite ainsi 2 opérations du processeur). On pourra cependant toujours montrer qu'il y en a un nombre constant (ou borné) :

{% note %}
La complexité d'une opération basique nécessite $\mathcal{O}(1)$ opérations.
{% endnote %}

De là :

{% note %}
Un nombre constant d'opérations basiques nécessite $\mathcal{O}(1)$ opérations.
{% endnote %}

Les règles précédentes permettent plus généralement de montrer :

{% note %}
$\mathcal{O}(A \cdot f(N)) \Leftrightarrow A \cdot \mathcal{O}(f(N)) \Leftrightarrow \mathcal{O}(f(N))$, avec $A$ une constante strictement positive et $f(N)$ une fonction strictement positive pour $N > N_0$
{% endnote %}

Ceci est pratique, car cela permet de ne pas compter toutes les opérations basiques précisément. Ainsi, en reprenant l'exemple de la partie [complexité des pseudo-code](../pseudo-code#complexité){.interne} :

```text#
x = 30
if ((x > 12) AND (x < 36)):
    z = x * "coucou"
```

1. on affecte un objet à x : 1 instruction, donc $\mathcal{O}(1)$ opérations.
2. un test avec 2 comparaisons et un `AND`{.language-} pour deux variables : 6 instructions, donc $\mathcal{O}(6) = \mathcal{O}(1)$ opérations.
3. on affecte le résultat d'une opération élémentaire : 3 instructions, donc $\mathcal{O}(3) = \mathcal{O}(1)$ opérations.

Un nombre total d'instructions de $3 \cdot \mathcal{O}(1) = \mathcal{O}(1)$ opérations.

En revanche, faites attention, cela ne marche que pour les constantes !

{% attention %}
Si le nombre d'opérations élémentaires est variable on a : $n \cdot \mathcal{O}(1) = \mathcal{O}(n)$. **On ne peut pas simplifier les éléments variables**.
{% endattention %}

Enfin, comme en algorithmie on manipulera souvent des polynômes, on peut montrer facilement avec les règles précédentes que :

{% note %}
$$\sum_{i=0}^na_i x^i = \mathcal{O}(x^n) \mbox{ si } a_n \neq 0$$
{% endnote %}



> TBD : O et borne la plus fine possible

## Si on veut être plus précis

Omega et theta car un algo linéaire est en O exponentiel. Cela ne donne qu'une borne max.

> TBD outil pour la mesurer : $\mathcal{O}$ (parler de $\Omega$) et ajouter $\Theta$. Limite lorsque entree grossi. Si petit on s'en fiche ca va vite.


## TBD 

> TBD outil pour la mesurer : $\mathcal{O}$ (parler de $\Omega$) et ajouter $\Theta$. Limite lorsque entree grossi. Si petit on s'en fiche ca va vite.
>
> C'est un peut chiant de faire comme ça et c'est pas très utile de faire tous ces détails :
> 
> 1. pas se faire suer avec tous les détails. Par exemple, comment fonctionne la boucle for ? Juste une affectation on bien c'est une somme si on l'écrit avec un tant que ?
> 2. ce qui nous intéresse c'est les grosses valeurs, lorsque c'est petit ça va vite et on s'en fiche.
> 3. la tendance de la complexité est cruciale : faire schéma des complexités.
> solution = $\mathcal{O}$, oméga et théta.
>
> enfin 
De plus 
> allure similaire, même si on va plus vite/plus lentement.