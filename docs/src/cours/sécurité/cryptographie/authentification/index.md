---
layout: layout/post.njk

title: Authentification


eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Les problèmes de confidentialité et d'intégrité ne sont d'intérêt que si on parle à la bonne personne.

Il n'y a du point de vue d'Alice et Bib en effet aucune différence entre :

```
Alice <-------------------------> Bob
  k                                k
```

et :

```
Alice <-------->Mallory<--------> Bob
  k              k  k'             k' 
```

Mallory interceptant tous les messages entre Alice et Bob, en particulier l'échange de clés initial.

Il faut trouver un moyen d'authentifier avec certitude le correspondant.

Un moyen de parvenir à cela est la [cryptographie asymétrique](https://fr.wikipedia.org/wiki/Cryptographie_asym%C3%A9trique) :

{% note "**Définition**" %}
La cryptographie asymétrique est un chiffre $(E, D)$ qui permet, avec un couple $(k, k')$ de clés d'avoir les deux conditions d'intégrité suivante, de façon sécurisée :

- $D(k', E(k, m)) = m$
- $D(k, E(k', m)) = m$

Enfin, la connaissance d'une des deux clés n'entraîne aucune information sur la seconde.
{% endnote %}

Les fonction $E$ et $D$ étant connues, on a coutume d'uniquement s'échanger les clés. Chaque personne garde une clé pour elle, cette clé est appelée *clé privée*, et distribue l'autre, la *clé publique*, à tout le monde.

La clé privé est personnelle et permet :

- de signer des message en chiffrant avec sa clé privé
- de recevoir des messages privés chiffrés avec sa clé publique

La clé publique est ...publique et permet à une autre personne :

- de vérifier une signature déchiffrant avec sa clé publique de la personne signataire
- d'envoyer des messages privés chiffrés avec la clé publique de la personne destinataire.

## <span id="signature"></span> Signature électronique avec clé publique/clé privée

{% lien %}
[Certificat Électronique](https://fr.wikipedia.org/wiki/Certificat_%C3%A9lectronique)
{% endlien %}

La cryptographie asymétrique permet alors d'avoir un couple $(S, V)$ de signature / vérification en utilisant le couple $(k, k')$ de clé privée / publique :

- $S(m) = E(k, h(m))$ : On signe un hash du message avec sa clé privée
- $V(m, c) = (h(m) = D(k', m))$ : on vérifie que le hash du message correspond à la signature

Les rôles des clés sont connus :

- la clé **privée** permettant de **signer**
- la clé **publique**, connue de tous, permet de **vérifier** la signature

{% info %}
Comme fonction de hash on utilise souvent [sha](https://fr.wikipedia.org/wiki/Secure_Hash_Algorithm), préférez la version 2 à la version 1 qui n'est plus sécurisée pour des applications cryptographies.
{% endinfo %}

Par exemple :

Alice veut envoyer un message $m$ à Bob et prouver qu'elle est bien l'autrice de celui-ci :

1. elle signe son message s = E(k, h(m))$
2. elle envoie à Bob le message $m$ et sa signature $s$

À la réception du message, Bob utilise la clé publique $k'$ d'Alice pour vérifier l'authenticité de $m$ : $h(m) = D(k', s)$

## <span id="authentification"></span> Authentification avec clé publique/clé privée

### Présentation de la clé publique

Pour garantir son identité, Alice envoie un message à Bob couplé à sa signature : $(\text{bonjour}, c)$, avec $c = E(k_\text{Alice-priv}, \text{bonjour})$. Bob peut alors vérifier l'identité d'Alice avec sa clé publique : $\text{bonjour} = D(k_\text{Alice-pub}, c)$.

Attention cependant au **message d'authentification envoyé**. C'est lui qui garanti l'authenticité de la personne. Le message d'authentification doit avoir un format déterminé et vérifiable (comme $(\text{bonjour}, S_{\text{Alice}}(\text{bonjour}))$ par exemple).

Ceci est cruciale si la vérification est automatique et non supervisée par un humain qui peut vérifier le message.

En effet, si le format du message d'authentification n'est pas vérifié, Mallory peut envoyer n'importe quoi comme message d'authentification, comme par exemple : $(V_{\text{Alice}}(\text{ha ha ha}), \text{ha ha ha})$ qui fonctionne puisque $V_{\text{Alice}}(\text{ha ha ha})$ est bien égale à $V_{\text{Alice}}(\text{ha ha ha})$.

### Tiers de confiance

Si on ne connaît pas la clé publique de la personne qui nous a envoyé un message, on peut utiliser l'annuaire d'un tiers de confiance dont on connaît la clé publique. Ce tiers de confiance signe la clé publique de la personne recherchée pour assurer de sa véracité.

- Tiers de confiance : certificat (pour le https, boot sécurisé)
- Keyring : ensemble de clés publique de confiance (pour l'installation de packages de mainteneur connu par exemple)

<https://wiki.archlinux.org/title/Pacman/Package_signing>

- keyring ubuntu : <https://www.malekal.com/comment-ajouter-des-cles-de-signature-a-apt-sur-debian-ubuntu-mint/>
- exemple vscode : <https://code.visualstudio.com/docs/setup/linux>

## Chiffrement des documents

Bien que la cryptographie asymétrique soit majoritairement utilisée pour l'authentification on peut aussi l'utiliser pour chiffrer des messages ayant un destinataire unique.

On peut en effet chiffrer un message avec la clé publique $k'$ d'une personne, $E(k', m) =c$. Seule la personne concernée pourra déchiffrer le message avec sa clé privée $k$ : $D(k, c) = m$.

Le chiffrement asymétrique étant beaucoup plus lent que le chiffrement symétrique, cette méthode est utilisée couramment pour chiffrer la clé symétrique ayant servi à chiffrer un long message et non le message tout entier.

## Exemples

### Chiffrement asymétrique RSA

RAS est le protocole très largement utilisé de cryptographie asymétrique. Il est basé sur le problème de la factorisation entière. Il permet chiffrer et de signer très efficacement des documents car sa fonction de chiffrement et de déchiffrement est la même.

- $E(k_\text{pub}, E(k_\text{priv}, m)) = m$
- $E(k_\text{priv}, E(k_\text{pub}, m)) = m$

{% aller %}
[Méthode de chiffrement RSA](./RSA){.interne}
{% endaller %}

### Chiffrement ElGamal

{% aller %}
[Méthode de chiffrement ElGamal](./ElGamal){.interne}
{% endaller %}

### Signature DSA

La méthode DSA de signature utilise le problème du logarithme discret comme fonctionnement, ce qui la rend compatible avec l'utilisation de courbes elliptiques :

{% aller %}
[Méthode de signature DSA](./DSA){.interne}
{% endaller %}

{% info %}
DSA est une variante de la méthode de signature ElGamal, qu'il ne faut pas confondre avec la méthode de chiffrement ElGamal.
{% endinfo %}
