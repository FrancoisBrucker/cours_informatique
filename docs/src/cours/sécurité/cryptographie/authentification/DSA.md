---
layout: layout/post.njk

title: Digital Signature Algorithm

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

{% info %}
DSA est une variante de [la méthode de signature ElGamal](https://en.wikipedia.org/wiki/ElGamal_encryption), qu'il ne faut pas confondre avec la méthode de chiffrement ElGamal.
{% endinfo %}

> TBD [DSA](https://fr.wikipedia.org/wiki/Digital_Signature_Algorithm)
> problème du log discret et pas de la factorisation comme RSA. Rend cette méthode utilisable avec les courbes elliptiques : [ECDSA](https://en.wikipedia.org/wiki/Elliptic_Curve_Digital_Signature_Algorithm)
> TBD <https://www.youtube.com/watch?v=_gmR5sYGUgs>
