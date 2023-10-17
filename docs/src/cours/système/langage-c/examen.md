---
layout: layout/post.njk

title: Examen

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Vérifiez que vous avez acquis les connaissances nécessaires en C.

## Compilation

{% exercice %}
Explicitez les différentes phases de la compilation d'un programme **C**.
{% endexercice %}
{% exercice %}
Quelle est l'utilité des fichiers d'entêtes (les fichiers `.h`{.fichier}) dans le processus de compilation ?
{% endexercice %}
{% exercice %}
Supposons que l'on crée une bibliothèque de fonctions sous la forme de deux fichiers `bib.h`{.fichier} et `bib.c`{.fichier}.

Explicitez comment faire pour :

- utiliser cette bibliothèque dans un fichier `main.c`{.fichier}.
- mettre à disposition de l'utilisateur de cette bibliothèque la fonction `'a'`{.language-} définie dans `bib.c`{.fichier}.
- cacher à l'utilisateur final l'existence de la fonction `'b'`{.language-}, elle aussi définie dans le fichier `bib.c`{.fichier}.

{% endexercice %}

## Pointeurs

Exercices de manipulation de pointeurs.

### Simple

```c
int i = 42;
int *p = &i;
```

{% exercice %}
Explicitez les deux lignes de code précédentes.
{% endexercice %}

{% exercice %}
Quelle sont les différences entre et que valent les trois notations suivantes :

- `p`{.language-}
- `*p`{.language-}
- `&p`{.language-}

{% endexercice %}

### Allocation dynamique

```c
int *t = malloc(10 * sizeof(int));
```

{% exercice %}
Explicitez la ligne de code précédente.
{% endexercice %}
{% exercice %}
Quelle sont les différences entre et que valent les trois notations suivantes, en supposant que `i`{.language-} soit un entier :

- `t + i`{.language-}
- `*(t + i)`{.language-}
- `&(t + i)`{.language-}
- `*t + i`{.language-}
- `&t + i`{.language-}

{% endexercice %}

### Rendre un pointeur

On vous demande de créer pour un utilisateur final une fonction nommée `donne_tableau`{.language-} qui rend un tableau composé d'entiers.

La taille du tableau n'est pas connue *a priori* et peut changer d'un appel à l'autre (le tableau peut être modifié par d'autres utilisateurs sur le réseau par exemple) mais vous avez à votre disposition deux fonctions auxiliaires, inconnues de l'utilisateur final :

1. `int donne_taille();`{.language-} qui renvoie la taille du tableau,
2. `int donne_valeur(size_t i);`{.language-} qui donne l'élément d'index `i`{.language-} du tableau.

Pour vos tests et pour le rendu, vous pourrez implémenter ces deux fonctions par des [*stubs*](https://en.wikipedia.org/wiki/Method_stub) (méthodes minimales pour répondre au problème) comme ceux-ci :

```c
int donne_taille() {
  return 10;
}

int donne_valeur(size_t i) {
  return (int)i;
}

```

Si l'utilisateur final ne connaît ni `donne_taille`{.language-} ni de `donne_valeur`{.language-}, la fonction `donne_tableau`{.language-} doit obligatoirement rendre deux informations :  

- le tableau d'entier
- sa taille

{% exercice %}
Pourquoi ?
{% endexercice %}

On vous demande d'écrire la fonction `donne_tableau`{.language-} selon différentes manières de rendre les deux données nécessaires. Vous accompagnerez chaque implémentation d'un petit programme main illustrant son utilisation.

{% exercice %}
On suppose que l'utilisateur final possède un tableau d'entiers de taille suffisante pour ranger toutes les valeurs du tableau. Donnez la fonction `donne_tableau`{.language-} qui :

- prend en paramètre un tableau de taille suffisante.
- rend le nombre d'élément du tableau.
{% endexercice %}

L'utilisateur final ne possède aucune information sur la taille du tableau à rendre et s'en remet à vous pour tout faire.

{% exercice %}
Donnez la fonction `donne_tableau`{.language-} qui :

- prend en paramètre un pointeur permettant de rendre la taille du tableau.
- rend le tableau en sortie.
{% endexercice %}

{% exercice %}
Donnez la fonction `donne_tableau`{.language-} qui :

- prend en paramètre un pointeur permettant de rendre le tableau.
- rend le nombre d'éléments du tableau en sortie.
{% endexercice %}

{% exercice %}
Donnez la fonction `donne_tableau`{.language-} qui :

- prend en paramètre un pointeur permettant de rendre le tableau.
- prend en paramètre un pointeur permettant de rendre la taille du tableau.
- ne rend aucune sortie.
{% endexercice %}

## Base16

On vous demande d'implémenter l'encodage/décodage en Base16, variante de l'encodage/décodage en base64 :

{% lien %}
<https://en.wikipedia.org/wiki/Base64>
{% endlien %}

L'idée de ce type de codage est de convertir un flux de bytes (comme une image par exemple) en un flux de caractères ASCII. Le format texte étant plus facilement transportable via le web (ou le mail) qu'un flux binaire, ce moyen de transmission est encore très populaire.

On a le schéma suivant :

```
flux binaire entrée      transmission       flux binaire sortie
00011101110101101001 ->      bnngj       ->  00011101110101101
```

L'encodage en base16 associe à un groupe de 4bits successifs une lettre de l'alphabet entre a et p (16 lettres).

Si on utilise la table `char *T = "abcdefghijklmnop"`{.language-}, le flux binaire 00011101110101101001 est encodé de droite à gauche par les caractères :

1. 1001 binaire vaut 9 en décimal : on encode avec 'j' (`T[9]`{.language-})
2. 0110 binaire vaut 6 en décimal : on encode avec 'g' (`T[6]`{.language-})
3. 1101 binaire vaut 13 en décimal : on encode avec 'n' (`T[13]`{.language-})
4. 1101 binaire vaut 13 en décimal : on encode avec 'n' (`T[13]`{.language-})
5. 0001 binaire vaut 1 en décimal : on encode avec 'b' (`T[1]`{.language-})
6. l'encodage final vaut : 'bnngj'

Le décodage de fait avec une fonction associant un entier à chaque lettre du code.

{% exercice %}
Codez la fonction de décodage associée à `T`{.language-}. La fonction doit avoir comme signature :

```c
size_t decode(char c)
```

Et devra rendre l'entier $i$ tel que $T[i] = c$. On suppose que le codage est fixé, vous implémenterez donc cette cette fonction avec une instruction `switch`{.language-}.
{% endexercice %}

Vous allez vous focaliser sur les chaînes de caractères qui sont, en utf-8, des flux de `char`{.language-}. Un `char`{.language-} faisant 8b, chaque char est encodé avec 2 lettres.

En utf-8, certains caractères sont codés sur 7b (les caractères ASCII), donc 1 byte, par exemple 'A' qui vaut l'entier' 65 ; d'autres sur 16b, comme 'é' qui est codé sur le tableau de 2 bytes [195, 169] ; d'autres sur encore plus, comme '好' qui est encodé sur le tableau de 3 bytes [229, 165, 189].

Vous pouvez vous en rendre compte en utilisant la fonction [`strlen`{.language-}](https://koor.fr/C/cstring/strlen.wp) :

{% exercice %}
Codez un programme qui rend le nombre de char de :

- `"A"`{.language-}
- `"é"`{.language-}
- `"好"`{.language-}
{% endexercice %}

Lorsque l'on utilise chaque `char`{.language-} séparément pour un encodage en utf-8, il faut faire un peu attention car même si un `char`{.language-} est codé sur 8 bits, il peut être considéré comme signé ou non. Comme nous avons besoin de considérer qu'un `char`{.language-} est non signé pour rendre compte des caractères encodés sur plusieurs bytes : il nous faut convertir chaque `char`{.language-} en entier non signé avant utilisation.

Dans son standard c23, le **C** définit un type pour cela, `char8_t`{.language-}, mais il n'est pas sûr que vous l'ayez déjà. Pour s'éviter tout soucis, définissez son type dans votre code :

```c
typedef unsigned char char8_t;
```

Et utilisez-le à chaque fois que vous devrez travailler avec un char d'une chaîne utf-8 sous la forme d'un entier (vous convertissant ce `char`{.language-} en `char8_t`{.language-}).

{% exercice %}

Affichez la valeur sous la forme d'entier chaque `char8_t`{.language-} des 3 chaînes de caractères `"A"`{.language-}, `"é"`{.language-} et `"好"`{.language-}.

{% endexercice %}
{% info %}
Pour afficher un `char8_t`{.language-} sous la forme d'un entier avec `printf`{.language-}, il faut utiliser le format `"%u"`{.language-} (pour `unsigned int`{.language-}).
{% endinfo %}

À chaque `char8_t`{.language-} de la chaîne sera associé deux lettres, l'une correspondant aux 4 bits de poids faible (ceux encodant $2^0$ à $2^3$), l'autre aux 4 bits de poids fort (ceux encodant $2^4$ à $2^7$).

Par exemple le `char`{.language-} correspondant à 'A' vaut 65 en `char8_t`{.language-} donc $01000001$ en binaire :

- ses 4 bits de poids faible valent : $0001$
- ses 4 bits de poids fort valent : $0100$

Prendre les 4 bits de poids fort et les 4 bits de poids faible d'un `char8_t`{.language-} peut se faire en utilisant des [comparateurs de bits](https://www.geeksforgeeks.org/bitwise-operators-in-c-cpp/) :

{% exercice %}

En utilisant l'opérateur ET bit à bit `&`{.language-}, rendez l'entier correspondant au 4 bits de poids faible d'un `char8_t`{.language-}. La fonction devra avoir comme signature :

```c
size_t faible(char8_t c);
```

{% endexercice %}
{% info %}

- Comme `char *s = "A"`{.language-} vaut le tableau de `char8_t`{.language-} valant `{ 65, 0}`{.language-} (on n'oublie pas le caractère '\0' de fin de chaîne) et que 65 vaut 01000001 en binaire, `faible((char8_t)s[0])`{.language-} doit rendre 1
- Comme `char *s = "é"`{.language-}  vaut le tableau de `char8_t`{.language-} valant `{195, 169, 0}`{.language-} et que 195 vaut 11000011, `faible((char8_t)s[0])`{.language-} doit rendre 3

{% endinfo %}

{% exercice %}

En utilisant l'opérateur de décalage à droite bit à bit `>>`{.language-}, rendez l'entier correspondant au 4 bits de poids fort d'un char. La fonction devra avoir comme signature :

```c
size_t fort(char8_t c);
```

{% endexercice %}
{% info %}

- Comme `char *s = "A"`{.language-} vaut le tableau de `char8_t`{.language-} valant `{ 65, 0}`{.language-} (on n'oublie pas le caractère '\0' de fin de chaîne) et que 65 vaut 01000001 en binaire, `fort((char8_t)s[0])`{.language-} doit rendre 4
- Comme `char *s = "é"`{.language-}  vaut le tableau de `char8_t`{.language-} valant `{195, 169, 0}`{.language-} et que 195 vaut 11000011 en binaire, `fort((char8_t)s[0])`{.language-} doit rendre 12

{% endinfo %}

On peut maintenant associer à chaque `char`{.language-} une chaîne de caractères composée des deux caractères.

{% exercice %}
Implémentez une fonction qui rend l'encodage en base16 d'un `char8_t`{.language-} sous la forme d'une chaîne de caractères.

```c
void encode_char(char *sortie, char8_t c);
```

On suppose que `sortie`{.language-} est assez grand pour contenir les deux caractères de la conversion plus le caractère '\0' de fin de chaîne, qu'il ne vous faudra pas oublier d'ajouter.
{% endexercice %}

Vous pouvez maintenant écrire la fonction terminale :

{% exercice %}
Implémentez une fonction qui rend l'encodage en base16 d'une chaîne de caractères.

Votre fonction devra avoir la signature suivante :

```c
char *encode_base16(char *s);
```

Et devra rendre une chaîne de caractères.
{% endexercice %}
{% info %}

La fonction doit rendre "mdkj" pour l'entrée valant "é".

{% endinfo %}

Pour terminer, il vous reste à implémenter le décodage. On va procéder en deux temps.

{% exercice %}
Implémentez une fonction qui rend le `char8_t`{.language-} associé à deux codes successifs. Cette fonction doit avoir comme signature :

```c
char8_t decode_char(char *cs);
```

Où `cs`{.language-} est un pointeur vers moins 2 `char`{.language-} successifs.
{% endexercice %}
{% info %}

Si `char *s = "mdkj"`{.language-}, la fonction doit rendre 195 pour l'entrée `s`{.language-} et 169 pour l'entrée `s+2`{.language-}.

{% endinfo %}

La fonction précédente doit vous permettre d'écrire facilement la fonction qui décode :

{% exercice %}
Implémentez une fonction qui rend le décodage en base16 d'une chaîne de caractères.

Votre fonction devra avoir la signature suivante :

```c
char *decode_base16(char *s);
```

Et devra rendre une chaîne de caractères.
{% endexercice %}
{% info %}

La fonction doit rendre "é" pour l'entrée valant "mdkj".

{% endinfo %}

Vérifiez bien que tout fonctionne :

{% exercice %}
Vérifiez que votre codage/décodage fonctionne en :

1. affichant la chaîne "je code et décode parfaitement !"
2. affichant le codage de la chaîne "je code et décode parfaitement !"
3. affichant le décodage du codage de la chaîne "je code et décode parfaitement !"
4. en affichant le résultat de la comparaison des chaînes 1 et 3 en utilisant la fonction [`strcmp`{.language-}](https://fr.wikipedia.org/wiki/Strcmp).

{% endexercice %}
