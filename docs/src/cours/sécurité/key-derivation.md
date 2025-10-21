---
layout: layout/post.njk

title: Key derivation

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

{% lien %}

- [Définition](https://en.wikipedia.org/wiki/Key_derivation_function)
- [introduction](https://blog.boot.dev/cryptography/key-derivation-functions/)

{% endlien %}

Lors d'un session de transport on a souvent besoin de nombreuses clés, puisqu'il ne faut **jamais** répéter les clés. La _Key derivation_ est un moyen de créer des clés à partir d'un mot de passe et de sel.

Son autre avantage est de permettre de créer des clé de taille donné et de permettre de rendre plus uniforme une distribution de mots de passe (par exemple les mots de passes issus d'un échange de clé par Diffie-Hellman).

## Principe

La façon la plus simple, si on a un PRF sous la main est de :

- posséder une clé primaire appelée $SK$ (_source key_)
- une constante $\text{iv}$, application dépendante pour éviter que plusieurs applications différentes utilisant la même clé primaires de se trouvent avec les mêmes clés

Puis il suffit d'étier le process à chaque fois que l'in veut une clé avec : $F(\text{SK}, \text{iv} || i)$, où $\text{iv}$ un texte désignant le type de mot de passe concernée et $i$ un nombre comptant le nombre de mots de passe que l'application a demandé.

{% lien %}

- [PBKDF2](https://en.wikipedia.org/wiki/PBKDF2)
- <https://www.youtube.com/watch?v=gTaOccTY9bc>

{% endlien %}

Nous allons montrer préciser le principe en explicitant le protocole `PBKDF2` encore très utilisé aujourd'hui. On lui préférera tout de même [argon2](https://en.wikipedia.org/wiki/Argon2), plus complexe, pour de nouvelles applications.

```sh
❯ openssl kdf -keylen 32 -kdfopt digest:SHA256 -kdfopt pass:"password" -kdfopt salt:"" -kdfopt iter:2 PBKDF2
8B:C2:F9:16:7A:81:CD:CF:AD:12:35:CD:90:47:F1:13:62:71:C1:F9:78:FC:FC:B3:5E:22:DB:EA:FA:46:34:F6
```

`DK = PBKDF2(HMAC, Password, Salt, c, n)`

avec `DK = T1 || T2 || ... || Tn`

Les `Ti` sont de la taille de la sortie du hash.

Et sont générés par : `Ti = U1 ⊕ ... ⊕ Uc` avec :

- `U1 = HMAC(Password, salt || i)`
- `Uj = HMAC(Password, U{j-1})`

On vot que l'itération des fonctions de hash permet d'uniformiser le hash.

> TBD "une ligne"

## Argon2

{% lien %}

- [Argon2 specification](https://www.password-hashing.net/argon2-specs.pdf)
- [Argon2 algorithm](https://www.youtube.com/watch?v=Sc3aHMCc4h0)
- [Argon2 vs PBKDF2](https://mojoauth.com/compare-hashing-algorithms/argon2-vs-pbkdf2/)

{% endlien %}

Argon2 est le gagnant d'une compétition visant à trouver le meilleur hash de mot de passes. Le principe est le même que pour `PBKDF2` mais utilise une matrice plutôt qu'une liste. Il cherche à empêcher le compromis temps/mémoire utilisé pour trouve des hash en :

1. utilisant le plus de mémoire possible : pour qu'il soit impossible de remplacer du temps par de la mémoire
2. empêche de remplacer la mémoire par du temps en pénalisant fortement la diminution de mé,oire

> TBD "une matrice"

```shell
❯ openssl kdf -keylen 50 -kdfopt pass:"password" -kdfopt salt:'des grains de sel' -kdfopt iter:3  ARGON2D
A6:0E:10:5D:A0:6A:63:85:8A:1A:63:25:8E:99:F2:7C:C6:00:F3:23:BE:09:F6:91:62:E5:FD:B6:5F:DA:CF:C0
```

```shell
❯ echo -n "password" | argon2 "des grains de sel" -l 50
Type:           Argon2i
Iterations:     3
Memory:         4096 KiB
Parallelism:    1
Hash:           62ac773d564f583c593e6091c72eeb48766fc1d1e314afdce0bc175328e98afbca29a5078035152cdac35d2720d9cc6cb4e3
Encoded:        $argon2i$v=19$m=4096,t=3,p=1$ZGVzIGdyYWlucyBkZSBzZWw$Yqx3PVZPWDxZPmCRxy7rSHZvwdHjFK/c4LwXUyjpivvKKaUHgDUVLNrDXScg2cxstOM
0.014 seconds
Verification ok

```

{% attention %}
Attention, tous les paramètres sont importants. Trouver le même hash avec openssl et argon2 semble impossible.
{% endattention %}

- renforcement de la clé primaire : hash
- clé primaire puis dérivation.

## Usage

{% lien %}

[Usage](https://blog.trailofbits.com/2025/01/28/best-practices-for-key-derivation/)

{% endlien %}

Trois usages courant :

- password hashing
- key stretching
- key derivation
