---
layout: layout/post.njk

title: AEAD

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

> TBD AEAD Authenticated Encryption Associated Data

On s'autorise l'ajout de données externes (les données associées) qui n'ont pas besoin (ou dont on a pas envie que) qu'elles soient chiffrées, comme les headers du protocole, mais dont on veut garantir l'intégrité.

De façon pratique cela revient à associer au MAC le message crypté et les données associées.

Le message envoyée est alors de la forme :

<div>
$$
E(k, m) || S(k', AD || F(k, m))
$$
</div>

La clé utilisée pour la signature doit être différente de la clé utilisée pour signer. Ces deux clés sont souvent des clés dérivées.

{% lien %}
[AEAD](https://www.youtube.com/watch?v=Q4EmXJTwcdo)
{% endlien %}

## Chacha20-poly1309

Le MAC associé au chiffrement chacha20 est poly1305.

{% lien %}
[chacha20-poly1305](https://en.wikipedia.org/wiki/ChaCha20-Poly1305)
{% endlien %}

On hash une concaténation de toutes les données :

- données associées
- longueur des données associées
- message chiffré
- longueur du message chiffré

Un padding est ajouté à la chaîne pour que leurs emplacements soient facile à coder.

## AES-GCM

Le MAC associé au chiffrement AES est Galois counter mode (GCM).

{% lien %}
[AES GCM](https://www.youtube.com/watch?v=g_eY7JXOc8U)

{% endlien %}

Le [Galois counter mode](https://en.wikipedia.org/wiki/Galois/Counter_Mode) fait ses opérations dans un corps :

{% lien %}
[GCM](https://www.youtube.com/watch?v=R2SodepLWLg)
[galois counter mode spécification](https://csrc.nist.rip/groups/ST/toolkit/BCM/documents/proposedmodes/gcm/gcm-spec.pdf)

{% endlien %}
