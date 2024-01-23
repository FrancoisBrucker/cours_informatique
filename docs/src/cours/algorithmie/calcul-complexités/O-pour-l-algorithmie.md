---
layout: layout/post.njk

title: Les $\mathcal{O}()$ pour le calcul de complexité

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

> TBD refaire l'intro + exemples
> TBD dire que c'est knuth qui a popularisé l'utilisation de ces calculs.

## Conséquences algorithmiques

Ceci est plutôt intéressant en algorithmie car l'on ne connaît pas toujours exactement le nombre d'opérations élémentaires utilisées, mais on peut les majorer de façon assez précise. On utilisera ainsi les $\mathcal{O}$ pour mesurer par rapport à la taille $N$ de l'entrée de l'algorithme :

- le nombre d'opérations élémentaires effectuées par l'algorithme avant de s'arrêter
- le temps mis par l'algorithme pour s'exécuter
- la taille de la mémoire utilisée pour par l'algorithme

La [première règle](../comparaisons-asymptotiques/#OA1){.interne} montre qu'un nombre constant est toujours en $\mathcal{O}(1)$. Pour un algorithme, il est souvent compliqué de savoir exactement de combien d'[opérations basiques](../pseudo-code#instruction-basique){.interne} est constituée une opération ou le temps exact qu'elle va prendre (pour un ordinateur, cela dépend du type de processeur. Par exemple, l'addition avec un x68 est faite [avec des registres](https://ensiwiki.ensimag.fr/index.php?title=Constructions_de_base_en_assembleur_x86), elle nécessite ainsi 2 opérations du processeur). On pourra cependant toujours montrer qu'il y en a un nombre constant (ou borné) :

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

Enfin, comme en algorithmie on manipulera souvent des polynômes, montrez que l'on peut, avec [les règles arithmétiques des $\mathcal{O}$](../comparaisons-asymptotiques/#arithmétique) que :

{% exercice %}

On a :
$$\sum_{i=0}^na_i x^i = \mathcal{O}(x^n) \mbox{ si } a_n \neq 0$$
{% endexercice %}
{% details "corrigé" %}
> TBD
{% enddetails %}

## Usage

- on cherche le O le plus proche possible
- si lpo veut montrer que ca croit plus vite qu'autre chose Omega
- 
- si on veut montrer des complexité min on se place avec des theta


En première approche utilisez des O car c'est plus simple et permet quelques largesse lorsque le compte exacte des instructions est compliqué à trouver.

On utilisera les theta lorsque l'on voudra montrer que l'on ne peut pas mieux faire.

O, oméga et théta, quand faire quoi

## TBD 


Si le majorant n'est pas trop éloigné de la mesure originale, cela nous donne une **idée générale** de la valeur de la mesure lorsque $N$ devient grand.


Les fonctions en $\mathcal{O}(f(N))$ sont les fonctions qui sont dominées par $f(N)$ asymptotiquement. Cela regroupe en grande nombre de fonctions vraiment petites par rapport à $f(N)$ : par exemple la fonction $\ln_2(n)$ est en $\mathcal{O}(2^n)$
