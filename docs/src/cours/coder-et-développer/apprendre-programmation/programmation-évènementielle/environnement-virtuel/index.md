---
layout: layout/post.njk 
title: "Environnement virtuel pour pytglet"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"


---

{% faire %}

Environnement virtuel :

1. créez-vous un environnement virtuel dans un nouveau dossier
2. ajoutez les modules `pyglet` et `pytest` à cet environnement en utilisant `pip` basé sur l'interpréteur de votre environnement virtuel
3. Vérifiez que tout fonctionne en :
   1. mettez une image dans le dossier du projet,
   2. créez un fichier `main.py`{.fichier} ou vous placerez le code ([issu de la documentation](https://pyglet.readthedocs.io/en/latest/programming_guide/quickstart.html#image-viewer)):
    ```python 
      import pyglet

      window = pyglet.window.Window()
      image = pyglet.resource.image('kitten.jpg')

      @window.event
      def on_draw():
          window.clear()
          image.blit(0, 0)

      pyglet.app.run()
      ```
      En remplaçant le nom `'kitten.jpg'`{.language-} par le nom de votre image.

4. Vérifiez que le code fonctionne et affiche votre image à l'écran.
5. Créez les fichiers :
  - `requirements.txt`{.fichier} qui explicite les dépendances
  - `readme.md`{.fichier} qui explicite comment exécuter le programme et le lien vers le cours.

{% endfaire %}