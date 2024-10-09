---
layout: layout/post.njk

title: Environnement et configuration

eleventyNavigation:
    order: 1

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

La gestion des variables d'environnement dépend du shell utilisé. On suppose ici que vous utilisez le shell par défaut sous Linux/Ubuntu : [bash](https://www.gnu.org/software/bash/). Ces variables servent à deux choses essentiellement :

- personnaliser son shell (par exemple la langue, les chemins vers les exécutables, ...)
- stocker des paramètres pour plus tard (l'ancien dossier courant par exemple)

L'ensemble de ces variables d'environnement sont disponibles avec la commande `env` ou `export` sans paramètre.

{% lien %}
[env et export](https://www.youtube.com/watch?v=1z6EUUl11qI&list=PLQqbP89HgbbY23Ab_vXGfLXHygquD7cAs&index=2)
{% endlien %}

### Création d'une variable d'environnement

Une variable d'environnement n'est rien d'autre qu'une variable d'un type spécial. Leur intérêt principal est d'être transmise aux shell enfant.

Testons ça dans un terminal :

1. création d'une variable simple : `x="coucou"`
2. création d'un shell enfant : `bash`
3. on vérifie que `x` n'est pas une variable de ce shell : `echo ${x}`
4. on sort du shell enfant : `exit`

On Va maintenant promouvoir `x` en variables d'environnement :

```
export x
```

On peut refaire les manipulation précédente et voir que `x` est bien définie pour le shell enfant.

Sous bash on peut supprimer x de la liste des variables d'environnements par `export -n x`.

## Utilisation des variables d'environnements

### Variables classiques

> TBD y en a t il d'autres ?

- `$PATH`
- `$PWD` `$OLDPATH` (`cd -`)
- `$HOME`

{% exercice %}
La commande `cd` change la variable `$PWD` du shell courant. Ce qui fait que `cd` ne peut-être un fichier exécutable.

Pourquoi ?
{% endexercice %}
{% details "solution" %}
Un fichier exécutable est crée dans un sous shell. Il ne peut donc modifier les variables de son shell parent.
{% enddetails %}

### Modification locale de l'environnement

On peut modifier l'environnement d'exécution d'une commande. Par exemple, pour avoir le manuel de man en anglais  :

```
LANG=C man man
```

On modifie la variable pour le process qui exécutera la commande : comme c'est un process enfant, la variable du shell parent nest pas modifiée.
