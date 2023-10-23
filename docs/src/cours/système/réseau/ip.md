---
layout: layout/post.njk

title: Routage IP

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---


{% lien %}
[Internet Protocol (IP)](https://fr.wikipedia.org/wiki/Internet_Protocol)
{% endlien %}

- ipv6 et ipv4
- organisation réseau (subnet) machine broadcast
- une interface par réseau
- routeur vs machine

- structure paquet
- routage : si choix alors le plus court et sinon, random
- 255 hop = discard

- réseaux privé

- ip4 : existence de réseaux privés et nat

> TBD et parler de dns
> paquet ICMP

wireshark on ne voit que la fin

1. ping6 pour ipv6. Est-ce que ça marche entre ordi de l'élèves ?
2. route en ipv6.
