---
layout: layout/post.njk

title: Hash cryptographiques

eleventyNavigation:
  prerequis:
    - "/cours/algorithmie/structure-dictionnaire/fonctions-hash/"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

{% lien %}

- [Hash cryptographique](https://fr.wikipedia.org/wiki/Fonction_de_hachage_cryptographique)
- [Hash propriétés et autres](https://membres-ljk.imag.fr/Bruno.Grenet/IntroCrypto/4.HashFunctions.pdf)

{% endlien %}

Une fonction de hash cryptographique doit être conçue pour éviter les collisions, c'est à dire qu'en connaissant $a$ il est très difficile de trouver $b \neq a$ tel que $f(b) = f(a)$

{% note "**Définition**" %}
Une fonction $H: \\{0, 1\\}^\star \rightarrow \\{0, 1\\}^n$ est une fonction de **_hash cryptographique_** si elle est résistante aux collisions.

Tout algorithme efficace ne peut rendre un couple $(x, x')$ tel que $H(x) = H(x')$ qu'avec un avantage négligeable.
{% endnote %}

On peut relâcher la condition de résistance à la collision en :

{% note "**Définition**" %}
Une fonction $H: \\{0, 1\\}^\star \rightarrow \\{0, 1\\}^n$ est **_résistant à la pré-image_** si étant donné $y$, tout algorithme efficace ne peut trouver $x$ tel que $H(x) = y$ qu'avec un avantage négligeable.
{% endnote %}

Ou encore :

{% note "**Définition**" %}
Une fonction $H: \\{0, 1\\}^\star \rightarrow \\{0, 1\\}^n$ est **_résistant à la seconde pré-image_** si étant donné $x$, tout algorithme efficace ne peut trouver $x'$ tel que $H(x) = H(x')$ qu'avec un avantage négligeable.
{% endnote %}

La résistance à la seconde pré-image condition étant plus restrictive que la résistance à la pré-image.

## Usage

### Intégrité non sécurisée

On accole le hash au message envoyé : $m || H(m)$

Le message est bien transmis si le hash du message arrivé correspond au hash concaténé. On peut alors associer un couple $(S, V)$ **_signe et vérifie_** :

- $S(m) = H(m)$
- $V(m, h) = (H(m) == h)$

{% attention %}
Rien n'empêche un attaquant de modifier et $m$ et son hash. Cette technique est uniquement preuve de transmission correct d'un message dans un canal pouvant être bruité, mais pas susceptible d'être attaqué.
{% endattention %}

### Stockage sécurisé

{% lien %}
[stocker ses mots de passes](https://patouche.github.io/2015/03/21/stocker-des-mots-de-passe/)
{% endlien %}

Les mots de passe d'un système son normalement stockés sous la forme d'un hash, auquel on ajoute un _sel_ aléatoire. Voyons pourquoi.

#### Ne pas faire

1. Stockage en clair dans un fichier : pas sécurisé du tout
2. Stockage en clair dans un fichier accessible par un seul utilisateur : si vol de l'ordinateur pas sécurisé
3. Mot de passe chiffré : le mot de passe est potentiellement connu de plusieurs autres personnes, dont l'administrateur.

#### Utilisation d'un hash

A priori **personne** à part l'utilisateur n'à à connaître son mot de passe. On peut arriver à ceci en utilisant une fonction de hash :

1. on stocke dans la base le hash d'un mot de passe
2. si le hash du mot de passe tapé correspond au hash de la base, c'est bon

Si le hash est cryptographique la probabilité de collision est négligeable : il est statistiquement impossible de tomber par hasard sur un mot ayant le même hash.

{% attention %}
Si le mot de passe est simple la probabilité de tomber sur vote mot de passe sera plus grande que la probabilité de collision. Utiliser une table de hachage ne dispense pas d'avoir un mot de passe _sécurisé_.

{% endattention %}

Deux types d'attaques génériques fonctionne bien pour des mot de passes non sécurisés (_ie._ pas assez long ou sur par assez de caractères différents). L'attaque [Brute force si faible nombre de possibilités](https://fr.wikipedia.org/wiki/Attaque_par_force_brute#Complexit%C3%A9_th%C3%A9orique_de_l'attaque) fonctionne assez bien car :

- si uniquement des caractères minuscules $2^{128} = 26^x$ donne $x = 28$ ce qui est trop long
- si uniquement des caractères minuscules et majuscule $2^{128} = 26^x$ donne $x = 23$ ce qui est trop long aussi, mais ok pour des [passphrase](https://fr.wikipedia.org/wiki/Phrase_secr%C3%A8te).
- si tout le clvier, l'ordre de 100 possibilité ce qui fait pour un mot de passe de 8 caractères $2^{54}$. D'où la nécessité de limiter le nombre d'essais.
- si base 64, il faut $128/7 \simeq 18$ pour obtenir pour obtenir jun mot de passe sécurisé brute force.

On peut accélérer le processus en utilisant un dictionnaire des mots de passes les plus utilisés (des mots ou des combinaisons de mots français) et en les choisissant en priorité. Et on les choisis par ordre aléatoires.

#### Salage du hash

Enfin, stocker les et pas les mots de passes en clair hash n'aide pas vraiment :

- on peut utiliser des tables de hash déjà faites
- si la base de mots de passes est grande on va retrouver plusieurs fois le même hash.

Pour ne garder aucune trace statistique dans le fichier stocké [on utilise un sel](https://fr.wikipedia.org/wiki/Salage_(cryptographie)). On obtient le couple signature, vérification :

- $S(m) = SALT || H(SALT || m)$
- $V(m, t) = H(t[:p] || m) = t[p:]$ où $p$ est la longueur du sel

{% lien %}
[argon2](https://www.youtube.com/watch?v=Sc3aHMCc4h0)
{% endlien %}

### Clés

La non collision permet de rechercher les hash plutôt que les valeurs exactes dans une liste stockant toutes les données. C'est la technique utilisée par Git pour gérer les ajouts, suppressions et modifications de code dans un projet.

{% info %}
Git utilise par défaut la fonction de hash [SHA-1](https://fr.wikipedia.org/wiki/SHA-1).
{% endinfo %}

## Construction

Il existe de nombreux hash. Testez les différences pour voir :

{% lien %}
[exemples de hash](https://emn178.github.io/online-tools/sha1.html)
{% endlien %}

Nous allons voir deux constructions. La première utilisée actuellement, la seconde qui vient.

### Construction courante

> TBD comme pour le chiffrement. Un bloc
> puis on lie de façon sécurisée.

#### construction par Davies–Meyer

{% lien %}
[Construction Davies–Meyer](https://fr.wikipedia.org/wiki/Construction_de_Davies-Meyer)
{% endlien %}

On utilise la construction Davies–Meyer qui permet de transformer [une permutation pseudo-aléatoire sécurisée](../../confidentialité/nombres-pseudo-aléatoires-cryptographiques/#PRP){.interne} $P : \\{0, 1\\}^s \times \\{0, 1\\}^t \rightarrow \\{0, 1\\}^t$ ($P(k, x)$ est une permutation aléatoire de $x$) en hash à taille fixe.

```
       iv   
        |   
      --|-- 
 k---|> P  |
      ----- 
        |
     P(k,iv)   
```

On fait rentrer le message là où normalement arrive la clé. Et un utilisant une constante $\text{IV}$ (initial value) à la place de la où habituellement se place un message.

<div>
$$
H(m) = P(m, \text{IV}) \oplus \text{IV}
$$
</div>

Ce qui donne schéma :

```
       iv 
        |  
        |------⊕------ H(m)  
     ---|--    |
m---|>  P  |   |
     ------    |
        |      |
        --------
```

{% note "**Théorème**" %}

Si le bloc est une PRP, alors la résistance à la collision est maximale.
{% endnote %}
{% details "preuve", "open" %}

Comme la permutation de $P(k, \cdot)$ est répartie uniformément selon $k$, la probabilité que deux messages différents aient le même hash $P(m, \text{iv}) \oplus \text{iv} = P(m', \text{iv}) \oplus \text{iv}$ est la même qu'avoir deux fonctions différentes $f$ et $f'$ de $\mathcal{F}(\\{0, 1\\}^t, \\{0, 1\\}^t)$ telle que $f(\text{iv}) = f'(\text{iv})$. Cela revient à la probabilité de choisir deux fois le même élément de $\\{0, 1\\}^t$, c'est à dire $1/2^t$.

Réciproquement, si l'on connaît $P(m, \text{iv}) \oplus \text{iv}$, trouver $m' \neq m$ tel que $P(m, \text{iv}) \oplus \text{iv} = P(m', \text{iv}) \oplus \text{iv}$ revient à trouver au hasard une fonction $f$ de $\mathcal{F}(\\{0, 1\\}^t, \\{0, 1\\}^t)$ telle que $f(\text{iv}) = P(m, \text{iv})$ cette probabilité est aussi de $1/2^t$.

{% enddetails %}

La preuve nécessite un PRP, mais comme on est pas sur que cela existe, les algorithmes mettant en oeuvre ce principe doivent être conçus pour très bien mélanger les bits tout en étant non prédictif (il faut le faire de façon "_compliquée_").

Les algorithmes SHA-1 et SHA-2 sont basés sur ce principes. Les permutation sécurisées utilisées sont appelées [shacal-1 et shacal-2](https://fr.wikipedia.org/wiki/Shacal). Mais on pourrait tout aussi bien utiliser chacha20 pour cela ! Ou son grand frère salsa20 originellement construit pour ça.

#### Extension par Merkel Damgard

{% lien %}

[Merkel Damgard preuve](https://www.youtube.com/watch?v=s7arHByjSOw)

{% endlien %}

On utilise la construction de [Construction de Merkel Damgard](https://fr.wikipedia.org/wiki/Construction_de_Merkle-Damg%C3%A5rd) pour étendre la portée du hash à taille fixe à des messages dont la taille est un multiple de $t$. POur cela, on commence par ajouter [un padding](https://fr.wikipedia.org/wiki/Remplissage_(cryptographie)) à la fin qui consiste en :

<div>
$$
m \;\|\; 1 \;\|\; 0\dots 0 \;\|\; \text{taille du message}
$$
</div>

Ensuite, on itère la construction précédente :

```
       iv        H(m1)                   H(m2)                   H(mi)                  H(m)  
        |------⊕----------------|------⊕------- ... ----|------⊕------- .... ---|------⊕--------
        |      |                |      |                |      |                |      |        
     ---|--    |             ---|--    |             ---|--    |             ---|--    |        
m1--|>  P  |   |        m2--|>  P  |   |        mi--|>  P  |   |        ml--|>  P  |   |        
     ------    |             ------    |             ------    |             ------    |        
        |      |                |      |                |      |                |      |        
        --------                --------                --------                --------        
```

Le message final doit bien faire une taille multiple de la taille du hash à taille fixe. Si le message est déjà de la bonne taille on ajoute tout de même un bloc ne contenant que le padding et la taille.

{% note "**Théorème**" %}
Si un bloc est résistant à la collision, la construction entière l'est.
{% endnote %}
{% details "preuve", "open" %}
Supposons qu'il y ait une collision :

On a alors $H_n = H'_{n'}$ ce qui implique :

<div>
$$
P(H_{m-1}, m_n \ ||\  \text{pad}) = P(H'_{m'-1}, m'_{n'} \ ||\  \text{pad}')
$$
</div>

De là si :

<div>
$$
m_n \ ||\  \text{pad} \neq m'_{n'} \ ||\  \text{pad}
$$
</div>

On a découvert une collision interne ce qui est improbable. Donc :

<div>
$$
m_n \ ||\  \text{pad} = m'_{n'} \ ||\  \text{pad}'
$$
</div>

Alors :

1. $\text{pad} = \text{pad}'$ ce qui implique que les deux messages ont la même taille
2. $m_n = m'_n$ : les messages ont la même fin

On conclut la preuve en remarquant que si $H_{m-1}$ est différent de ${H'}_{m-1}$ on a une collision ce qui est improbable. Les deux sont alors égaux et poursuit par récurrence.

{% enddetails %}

Les fonctions de hash très utilisés que sont les SHA-1 et SHA-2 sont basées sur ce principe. En revanche, SHA-3, le petit nouveau, est basé sur un autre principe que nous allons rapidement aborder maintenant.

{% lien %}
[L'algorithme sha2](https://www.youtube.com/watch?v=orIgy2MjqrA)
{% endlien %}

### Construction en éponge

{% info %}
Les [sponge function](https://en.wikipedia.org/wiki/Sponge_function)
{% endinfo %}

> TBD :
>
> - [fonctionnement de SHA-3](https://www.youtube.com/watch?v=fzlflyw7X2I)
> - [sha 3 sponge function](https://www.youtube.com/watch?v=bTOJ9An9wpE)
> - [sponge function thm](https://keccak.team/files/SpongeFunctions.pdf)
> - <https://summerschool-croatia.cs.ru.nl/2017/slides/introduction%20to%20permutation-based%20cryptography.pdf>

## Attaque

{% lien %}

- [Attaque des fonctions de hash](https://people.cs.uchicago.edu/~davidcash/284-autumn-21/12-hash.pdf)
- [sha 1 collision](https://www.youtube.com/watch?v=Zl1TZJGfvPo)

{% endlien %}

### Attaque des anniversaires

L'attaque générique des anniversaires est l'attaque brute force associée aux fonctions de hash cryptographique.

Grace au [paradoxe des anniversaires](/cours/algorithmie/structure-dictionnaire/fonctions-hash/#paradoxe-anniversaires){.interne}, on sait qu'il suffit de $2^{n/2}$ mots de $\\{0, 1\\}^n$ pour avoir une probabilité supérieure à 1/2 d'avoir deux éléments $x$ et $x'$ tels que $H(x) = H(x')$.

Il n'est pas nécessaire de stocker tous les mots en mémoire, on peut montrer qu'il suffit de :

{% note "**Algorithme attaque par point fixe**" %}

1. prendre $x_1 = y_1$ un mot aléatoire de $\\{0, 1\\}^n$
2. créer itérativement $x_i = H(x_{i−1})$ et $y_i = H(H(y_{i−1}))$ jusqu'à ce que $x_m = y_m$
3. on a alors $H(x_{m−1}) = H(H(y_{m−1}))$ si $x_{m-1} \neq H(y_{m−1})$ (ce qui est très probable)

Il faut, comme l'attaque brute force du dictionnaire de l'ordre de $\mathcal{O}(2^{n/2})$ opération avant de trouver une collision

{% endnote %}
{% details "preuve", "open" %}

C'est l'[algorithme du lièvre et de la tortue](https://fr.wikipedia.org/wiki/Algorithme_du_li%C3%A8vre_et_de_la_tortue).

L'ensemble d'arrivée de $H$ étant fini, il va exister, pour tout $x$, un entier $p$ tels que $H^p(x) = H^q(x)$ avec $q > p$.

On pose :

- $\lambda = p$
- $\mu = q-p$

Soit $x$ le plus petit entier tel que $\lambda +x$ soit un multiple de $\mu$. On a $0 \leq x \leq \mu$ puisque la division euclidienne de $\lambda$ par $\mu$ donne $\lambda = q\cdot \mu +r$ et donc $x=\mu-r$

On a alors : $2(\lambda +x) = \lambda +x + k\cdot \mu$ et donc $H^{2(\lambda +x)}(x) = H^{\lambda +x}(x)$.

> TBD aussi en analysant si lapin en arrière de k de la tortue sur le cycle : à l'étape d'après k-1 en arrière.

{% enddetails %}

Notez que si l'attaque des anniversaires ne donne pas de garanties sur les deux mots que l'on trouve, il est très facile de modifier 2 documents différents de façon aléatoire un très grand nombre de fois, ce qui va garantir de tomber sur une collision tout en ayant deux texte se ressemblant.

{% info %}
La technique précédente permet de présenter deux textes différents de même hash en :

1. écrivant deux textes différents
2. modifier aléatoirement les deux textes en ajoutant des espaces, des retours chariots ou backspace. Bref plein de choses qui ne se voient pas une fois.
3. au bout de $2^{n/2}$ modifications, on a deux deux texte de même hash où le contenu _visible_ est celui des deux textes initiaux.

Il suffit ensuite de faire signer la version $A$ du texte puis de présenter la version $B$, prétendument signée.

Il faut toujours modifier un peu un document que l'on signe, histoire que l'attaquant doive tout refaire.
{% endinfo %}

### Brute force par Rainbow tables

On peut même préparer un dictionnaire de ots hachés pour aller plus vite voir utiliser des <https://en.wikipedia.org/wiki/Rainbow_table> (voir aussi <https://rsheasby.medium.com/rainbow-tables-probably-arent-what-you-think-30f8a61ba6a5>) qui est encore une version du compromis temps/mémoire déjà vu pour le baby step/giant step.

> TBD expliquer et faire exemple Donner complexité en temps et en mémoire

### Length extension attack

Pour des construction Merkel-Damgard on peut continuer la procédure et étendre le hash. Tout se passe comme si on avait un message plus grand. Si le protocole en face n'est pas propre ce la peut mener à des catastrophes :

```

...

destinataire : François
versement : 100 euros
```

Si on ajoute la ligne :

```

....

destinataire : François
versement : 100 euros
versement : 1000000 euros
```

On peut continuer le hash sans connaître le message initial.

### Differential Analysis

{% lien %}

[differential analysis](https://en.wikipedia.org/wiki/Differential_cryptanalysis)

{% endlien %}

> TBD

<!-- TBD

> :
> - <https://antoine.delignat-lavaud.fr/doc/slides_md5.pdf>
> <https://www.youtube.com/watch?v=GQX8W8zKf2Q>
> - <https://crypto.stackexchange.com/questions/98092/what-is-a-differential-attack-on-a-hash-function-how-would-one-attack-a-sha-alg>

-->
