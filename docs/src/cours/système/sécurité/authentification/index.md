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

ENfin, la connaissance d'une des deux clés n'entraîne aucune information sur la seconde.
{% endnote %}

La cryptographie asymétrique permet alors d'avoir un couple $(S, V)$ de signature / vérification :

- $S(m) = E(k, m)$
- $V(m, c) = (m == D(k', m))$

Où la fonction de signature est privée mais la fonction de vérification publique.

L'authentification se faisant alors de la sorte :

- Seule Alice connaît sa signature $S_{\text{Alice}}$, mais sa fonction de vérification $V_{\text{Alice}}$ est connue de tout le monde (dont Bob)
- Tout message $m$ envoyé par Alice est accompagné de sa signature $S_{\text{Alice}}(m)$
- Bob peut vérifier que le message provient bien d'Alice grace à la fonction de vérification d'Alice qui est publique.

{% info %}
La cryptographie asymétrique est utilisée en pratique uniquement pour l'authentification avant une communication avec un chiffrement symétrique et non pour la transmission de données. Ceci pour essentiellement deux raisons :

1. elle est moins rapide algorithmiquement que la cryptographie symétrique
2. on garde son couple de clés publique/privée bien plus longtemps qu'une clé symétrique qui est à usage unique.
{% endinfo %}

## RSA

RAS est le protocole très largement utilisé de cryptographie asymétrique. Le couple de clés $(k, k')$ est appelé clé privé et clé publique. Le chiffrement et le déchiffrement se font avec la même fonction $E$ et on a les équations d'intégrités :

- $E(k_\text{pub}, E(k_\text{priv}, m)) = m$
- $E(k_\text{priv}, E(k_\text{pub}, m)) = m$

On a donc coutume d'uniquement s'échanger les clés publiques et non la fonction de vérification.

La clé privé est personnelle et permet :

- d'authentifier des message en chiffrant avec sa clé privé
- de recevoir des messages privés chiffrés avec sa clé publique

{% aller %}
[Méthode de chiffrement RSA](./RSA){.interne}
{% endaller %}

## DSA

La méthode DSA de signature utilise le problème du logarithme discret comme fonctionnement, ce qui la rend compatible avec l'utilisation de courbes elliptiques :

{% aller %}
[Méthode de signature DSA](./RSA){.interne}
{% endaller %}

## <span id="authentification"></span> Authentification avec clé publique/clé privée

### Présentation de la clé publique

Pour garantir son identité, Alice envoie un message à Bob couplé à sa signature : $(\text{bonjour}, c)$, avec $c = E(k_\text{Alice-priv}, \text{bonjour})$. Bob peut alors vérifier l'identité d'Alice avec sa clé publique : $\text{bonjour} == E(k_\text{Alice-pub}, c)$.

Attention cependant au **message d'authentification envoyé**. C'est lui qui garantie de l'authenticité de la personne. Le message d'authentification doit avoir un format déterminé et vérifiable, comme $(\text{bonjour}, S_{\text{Alice}}(\text{bonjour}))$. Sans quoi,
Mallory peut envoyer comme message d'authentification : $(V_{\text{Alice}}(\text{ha ha ha}), \text{ha ha ha})$.

Ceci est cruciale si la vérification est automatique et non supervisée par un humain qui peut vérifier le message.

### Tiers de confiance

Si on ne connaît pas la clé publique de la personne qui nous a envoyé un message, on peut utiliser l'annuaire d'un tiers de confiance dont on connaît la clé publique. Ce tiers de confiance signe la clé publique de la personne recherchée pour assurer de sa véracité.

- Tiers de confiance : certificat (pour le https, boot sécurisé)
- Keyring : ensemble de clés publique de confiance (pour l'installation de packages de mainteneur connu par exemple)

<https://wiki.archlinux.org/title/Pacman/Package_signing>

- keyring ubuntu : <https://www.malekal.com/comment-ajouter-des-cles-de-signature-a-apt-sur-debian-ubuntu-mint/>
- exemple vscode : <https://code.visualstudio.com/docs/setup/linux>

## <span id="signature"></span> Signature électronique avec clé publique/clé privée

{% lien %}
[Certificat Électronique](https://fr.wikipedia.org/wiki/Certificat_%C3%A9lectronique)
{% endlien %}

{% info %}
Il existe d'autres façon de signer des documents, comme la
[Signature Elgamal](https://en.wikipedia.org/wiki/ElGamal_signature_scheme)
{% endinfo %}

- document à certifier
- condensat (ou [somme de contrôle/checksum](https://fr.wikipedia.org/wiki/Somme_de_contr%C3%B4le)) est un hash du contenu du document.

Le document à certifier peut être un fichier ou des informations.

{% info %}
Comme fonction de hash on utilise souvent [sha](https://fr.wikipedia.org/wiki/Secure_Hash_Algorithm), préférez la version 2 à la version 1 qui n'est plus sécurisée pour des applications cryptographies.
{% endinfo %}

Le hash est un moyen efficace de savoir si un document a été modifié car deux documents différents auront un condensat différent (la probabilité que deux document différents aient le même condensat est infinitésimale).

En soit, le condensat permet de vérifier l'intégrité d'un fichier si on peut assurer qu'il a bien été émis par le créateur du fichier. Pour cela, le condensat est crypté avec la clé privée du créateur du fichier. Le condensat crypté est appelé ***signature***

Vérifier l'intégrité d'un fichier se fait alors en trois étapes :

1. on calcule le condensat du fichier
2. on décrypte la signature avec la clé public du créateur du fichier
3. on compare les les deux condensats :
   - si les condensats sont identiques le fichier est dans l'état donné par le créateur
   - si les condensats sont différents le fichier a été modifié
