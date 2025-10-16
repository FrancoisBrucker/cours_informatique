---
layout: layout/post.njk

title: Algorithme Chacha20

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---



{% lien %}
<https://loup-vaillant.fr/tutorials/chacha20-design>
{% endlien %}

> TBD pas de mot secret ni de S-box
> le iv est petit pour ne pas donner prise aux attaques qui forgent un iv special
> la constante est la pour permettre des clés valant 0 par exemple.
>
> 
> TBD <https://crypto.stackexchange.com/questions/77628/is-the-chacha20-block-function-reversible-using-known-plaintext>
>
> 
> TBD :
> - <https://www.youtube.com/watch?v=G0O0VHVtNuM>
> - <https://www.youtube.com/watch?v=UeIpq-C-GSA>
> - <https://www.youtube.com/watch?v=Xw9lBsCc_Qk>
> 
> TBD : dire qu'on ne présente que le bloc principal. Ensuite il s'imbrique dans la suite du cours (taille quelconque et intégrité)

{% lien %}

- [Fonctionnement et origine](https://en.wikipedia.org/wiki/Salsa20#ChaCha_variant)
- [RFC](https://datatracker.ietf.org/doc/html/rfc8439)

{% endlien %}

## Fonctionnement

{% lien %}

- [design](https://loup-vaillant.fr/tutorials/chacha20-design)
- [spec et implémentations](https://cr.yp.to/chacha.html)

{% endlien %}

> TBD : à approfondir
> TBD : faire dessin du chiffrement.
> TBD : Faire des exemple d'utilisation.


### Nécessité de la non linéarité

Pour éviter une attaque classique, nommée [cryptanalyse linéaire](https://fr.wikipedia.org/wiki/Cryptanalyse_lin%C3%A9aire), tous les PRP vont avoir à la fois des transformations linéaires $\oplus$, décalage ou circulation de bits ainsi que des choses non linéaire, souvent encapsulé dans des matrices de transformation appelées [S-box](https://fr.wikipedia.org/wiki/S-Box). Il faut bien sûr que ces opérations soient choisies avec soin pour éviter tout biais, la moindre linéarité cachée pouvant être facilement utilisée comme attaque.

{% info %}
Le chiffrement DES, proposé par la NSA, proposait des [S-box](https://fr.wikipedia.org/wiki/S-Box) obscures qui ont toujours laissé des doutes quant à la sincérité de ses non-linéarités.
{% endinfo %}

La cryptanalyse linéaire va chercher des corrélations linéaires entre le message $m$, le chiffre $c$ et la clé $k$, c'est à dire si :

<div>
$$
Pr[(\oplus_{i \in I} m_i) \oplus (\oplus_{j \in J} c_j) = (\oplus_{l \in L} k_l)] \leq 1/2 + \epsilon
$$
</div>

Si $\epsilon$ est non négligeable, on peut en déduire un algorithme qui va exécuter $1/\epsilon$ fois cette relation et trouver avec une grande probabilité cette corrélation, et donc l'information nécessaire à sa cryptanalyse.

> TBD calcul probabilité avec une binomiale $Pr[B(n, p) \geq 1]$.

Chaque méthode de chiffrement intègre ainsi en son sein des transformations non linéaires permettant de casser ce genre d'attaque.