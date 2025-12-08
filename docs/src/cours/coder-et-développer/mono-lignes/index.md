---
layout: layout/post.njk

title: "Mono-lignes"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Les mono-lignes sont 100 petit exercices que l'on doit à Aristide Grange. Ils permettent de se creuser un peu la tête pour écrire de façon condensé du code python.

{% aller %}
[100 mono-lignes d'Aristide Grange](monolignes-questions.pdf){.interne}
{% endaller %}
{% attention %}
Dans l'énoncé soit :

- remplacez `m27`{.language-} par `m23`{.language-}, le 23ème nombre de Mersenne ($2^{11213}-1$)
- soit augmentez la taille des chaînes de caractères en tapant les commandes suivante dans votre interpréteur :

    ```python
    import sys
    sys.set_int_max_str_digits(15000)
    ```

{% endattention %}
{% info %}
On en a déjà vu quelques-une pendant ce cours, à vous de les retrouver.
{% endinfo %}

Dans la vraie vie pn préférera toujours du code explicite et facile à lire plutôt que du code compact, mais cela reste un très bon exercice pour comprendre comment fonctionne un langage informatique en général et python en particulier.

{% details "indices" %}

Les fonctions suivantes vous seront utiles :

- [`divmod`{.language-}](https://docs.python.org/fr/3.14/library/functions.html#divmod)
- [`input`{.language-}](https://docs.python.org/fr/3.14/library/functions.html#input)
- [`chr`{.language-}](https://docs.python.org/fr/3.14/library/functions.html#chr) et [`ord`{.language-}](https://docs.python.org/fr/3.14/library/functions.html#ord)
- [`sum`{.language-}](https://docs.python.org/fr/3.14/library/functions.html#sum)

Les méthodes des :

- [listes](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists)
- [chaînes de caractères](https://docs.python.org/fr/3.14/library/string.html#module-string)

Savoir [lire et écrire des fichiers texte](https://docs.python.org/fr/3.14/tutorial/inputoutput.html#reading-and-writing-files).

{% enddetails %}
