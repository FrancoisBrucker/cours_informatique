---
layout: layout/post.njk

title: Exécution Conditionnelle de blocs

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---


{% lien "**Documentation**" %}
<https://docs.python.org/fr/3/reference/compound_stmts.html#the-if-statement>
{% endlien %}

Permet d'exécuter un bloc si une condition logique est vraie :

```python
if <condition logique>:
    instruction 1
    instruction 2
    ...
    instruction n
elif <condition logique>:
    instruction 1
    instruction 2
    ...
    instruction n
else:
    instruction 1
    instruction 2
    ...
    instruction n
```

Notez qu'il peut y avoir autant de bloc `elif`{.language-} que l'on veut (même 0) et qu'il n'est pas nécessaire d'avoir de `else`{.language-}.

{% exercice %}
Demandez à l'utilisateur de rentrer un entier au clavier (en utilisant la [fonction `input`{.language-}](../fonctions-méthodes#input){.interne}) et de répondre "C'est entre 2 et 8" si le nombre rentré est entre 2 et 8 et de répondre "ce n'est pas entre 2 et 8" sinon.
{% endexercice %}
{% details "solution" %}

```python

entier = int(input("Un entier entre 2 et 8 : "))
if 2 >= entier and entier <= 8:
    print("C'est entre 2 et 8")
else:
    print("ce n'est pas entre 2 et 8")
```

{% enddetails %}
