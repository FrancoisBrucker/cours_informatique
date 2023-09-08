---
layout: layout/post.njk

title: CPU

eleventyNavigation:
    order: 1

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---


## Exécution parallèle de process

### hyper-threading

Un core peut passer beaucoup de temps à attendre des données du cache. L'[hyper-threading](https://en.wikipedia.org/wiki/Hyper-threading) permet de mettre cette attente à profit pour exécuter le code d'un autre thread.

Ceci est possible puisque les threads se partagent tout sauf les registres.

Chaque core peut ainsi exécuter deux thread *quasiment* en parallèle.

> TBD : comment ça marche.
> TBD rappelle process et thread


#### Multi-process

La page se remplit petit à petit par l'OS. Lorsque le process tente d'accéder à une page qui n'existe pas, une exception est levée : [exception page-fault](https://wiki.osdev.org/Exceptions#Page_Fault).

L'OS tente de la résoudre soit :

- en faisant la correspondance avec la mémoire réelle
- en recherchant un bloc mis de côté par manque de place. C'est le [mécanisme de swap](https://fr.wikipedia.org/wiki/Espace_d%27%C3%A9change)
- en interdisant l'accès

### cache

le cache L3 est commun et tout ce qui est dans le cache est forcément en l1 ou l2

### Cache et cores

> TBD à faire bien.

> soucis que si plusieurs core écrivent sur des données identique. Doit quasi pas arriver si process différents
L3 inclusive : donc permet de vérifier que tout est ok.

Les différents caches L1 et L2 sont privé à chaque core. Tant que la mémoire n'est pas modifiée ces caches sont indépendants, mais lorsqu'une donnée contenue dans plusieurs caches est modifiée, il faut [maintenir la cohérence entre tous les caches](https://en.wikipedia.org/wiki/Cache_coherence).

![cores](cores.png)

> TBD cohérence uniquement en L3. Qui est sur le ring. Puis descente invalidation. en L2 et L1 dans le core.

> TBD : attention, plus de snooping. on remonte juste l'invalidation.

Les cores sont liées entre eux par le ring qui permet de faire transiter des informations :

- depuis la mémoire via le bus
- entre chaque core pour maintenir la cohérence de chaque cache

Maintenir la cohérence entre les caches de chaque core nécessite deux actions pour chaque cache :

- il faut qu'il surveille les demandes de lecture/écriture des autres cache. Ceci s'appelle le [bus snooping](https://en.wikipedia.org/wiki/Bus_snooping).
- il faut qu'il s'adapte aux données présentes dans les autres caches :
  - lorsqu'il demande une donnée modifiée dans un autre cache :
    1. il demande au cache ayant la donnée modifiée de l'écrire en mémoire
    2. une fois la donnée écrite, on charge la donnée depuis la mémoire
  - lorsqu'il écrit une donnée présente dans plusieurs cache, il demande aux autres caches d'invalider la ligne contenant cette donnée s'ils la possède (demander aux autres cache de modifier leurs valeurs causerait trop d'écritures inutiles, il n'est en effet pas sur qu'ils auraient encore eu besoin de cette ligne)

Notez que l'on ne modifie la valeur en mémoire que si plusieurs caches ont la ligne. Si seulement un cache à la donnée et qu'il la modifie, elle n'est pas envoyée en mémoire.

La mise en œuvre de cette technique peut être faite de façon plus optimisée en utilisant le protocole [MOESI](https://en.wikipedia.org/wiki/MOESI_protocol) qui ne force pas la réécriture en mémoire à chaque demande de donnée modifiée (le cache ayant la donnée modifiée la passe au cache demandeur). Sa mise en œuvre est cependant plus complexe car il faut des moyens de se partager des données entre caches.

{% info %}
Il en existe une [foule d'autres protocoles](https://en.wikipedia.org/wiki/Cache_coherency_protocols_(examples)#MESI_protocol)
{% endinfo %}

### Context Switching

> TBD changer :
>
> - si thread juste registre.
> - si processus :
>      - proc : la lookup table et les registres.
>      - OS : changer aussi la page table (un pointeur à changer)
>
> Pas besoin de changer le cache puisque VIPT
> exécution context : un process/thread

Ceci doit se faire vite pour simuler le parallèlisme.


Le processeur n'a pas de mémoire. Son état est déterminé par :

- la valeur de ses registres
- la table des addresses de la MMU

> TBD facile de changer de contexte. On vide le cache, puis on remet la table et les valeurs des registres.

