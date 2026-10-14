---
layout: layout/post.njk

title: Nombres aléatoires

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

<!-- 
> TBD : intro
>
> - <https://www.youtube.com/watch?v=HlnHuEEM5ts>{.externe}
> - <https://www.youtube.com/watch?v=J5b4lrCCXRI>{.externe}
> - <https://www.youtube.com/watch?v=4R5xnTAvBgc>{.externe}
>  -->

{% lien "**Bibliographie**" %}

- "random number generators : principles and practices de David Johnston"

{% endlien %}

{% lien %}

- [une intro](https://www.youtube.com/watch?v=qt4fYKhFhFs){.externe}
- [La playlist sur tout ce que vous avez toujours voulu savoir sur les générateurs de nombres aléatoire sans oser le demander](https://www.youtube.com/watch?v=tZse1YyiHdg&list=PLZNqNoh4u1gzKMYgrrgcKK5ozNQ7f_OMP){.externe}
{% endlien %}

La solution la plus simple est de faire $n$ pile ou face pour créer un nombre aléatoire à $n$ bits. Cette solution n'est pas réaliste mais il faut utiliser un processus physique quelque-part car tout algorithme est déterministe. Il est également exclu d'utiliser des humains pour générer des suites aléatoire car l'humain n'est pas fait pour reconnaître l'aléatoire : on cherchera à avoir des suite équilibrées de 0 et de 1 ce qui n'est pas du tout aléatoire :

{% lien %}
<https://www.youtube.com/watch?v=tP-Ipsat90c>{.externe}
{% endlien %}

## TRNG

Il existe des moyens de générer des nombres aléatoire, on appelle ces générateur **_TRNG_** : pour True Random Generator.

> TBD avec des dés plusieurs bits avec 1 lancé : <https://stackoverflow.com/questions/20804899/how-to-generate-an-un-biased-random-number-within-an-arbitrary-range-using-the-f/20818831#20818831>{.externe}
> TBD présenter niquist
> TBD quantique, etc.
> TBD ring oscillatro : <https://www.youtube.com/watch?v=fwU8s1BMNlA>{.externe} <https://www-verimag.imag.fr/~async/CCIS/talk_12/Lubicz_talk.pdf>{.externe} et <https://pqshield.com/wp-content/uploads/2022/02/2021-1363.pdf>{.externe}
## Entropie

Cependant créer un nombre aléatoire est un processus coûteux en temps et en énergie. On utilisera alors souvent des processus approchés pour extraire de l'aléatoire : générer $n$ bits presque aléatoires à partir de $m < n$ bits vraiment aléatoires.

> TBD à revoir et à présenter :
>
> 1. <https://www.youtube.com/watch?v=YvH53vJM69E&list=PLkvhuSoxwjI_JL7GYcJHK7-EK55t0KYGO&index=38>{.externe}
> 2. des preuves : <https://people.seas.harvard.edu/~salil/pseudorandomness/extractors.pdf>{.externe}

## Implémentation

Implémentations :

{% lien %}
<https://www.random.org/>{.externe}
{% endlien %}

Et ces méthodes sont implémentées directement [sur le processeur](https://www.intel.com/content/www/us/en/docs/intrinsics-guide/index.html#ig_expand=5627&cats=Random){.externe} ou via le [système d'exploitation](https://en.wikipedia.org/wiki//dev/random){.externe} :

```shell
xxd < /dev/random
```

Ou de façon plus "lisible" :

```shell
echo "hasard : "$(base64 </dev/random 2>/dev/null| head -c 100)
```

[Sous windows](https://learn.microsoft.com/fr-fr/powershell/module/microsoft.powershell.utility/get-random?view=powershell-7.5){.externe} (attention pas cryptographique) :

```shell
powershell -command "[Convert]::ToBase64String((1..64|%{[byte](Get-Random -Max 256)}))"
```
