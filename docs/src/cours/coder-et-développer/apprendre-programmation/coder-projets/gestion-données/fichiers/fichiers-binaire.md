---
layout: layout/post.njk 
title: "Fichier binaire"

eleventyNavigation:
    order: 2

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Les fichiers binaires sont une succession de byte. Ils sont la plupart du temps structurés selon un format particulier.

On peut voir un fichier texte comme un fichier binaire particulier. C'est d'ailleurs comme ça que python traite les fichiers texte non utf-8.

La plupart dfs choses vues avec un fichier texte s'applique avec un fichier binaire sauf qu'on lit/écrit byte à byte. Pour tenter d'afficher un fichier binaire python utilise :

- le format ASCII sur 7bit si le byte correspond à un cqractère imprimable
- un nombre hexadécimal sous la forme `\xUU' (avec UU allant de 00 à FF) sinon.

Pour ouvrir un fichier binaire sous python, on utilise le caractère `'b'` suivi de ce que l'on veut faire avec.

L'exemple suivant ouvre l'image `IMG_0192.jpeg`{.fichier} en lecture sous la forme d'un fichier binaire, puis place le contenu de celui-ci dans la variable `img`{.language-}

```python
>>> f = open("IMG_0192.jpeg", "rb")
>>> img = f.read()
>>> img[:100]
b'\xff\xd8\xff\xe0\x00\x14JFIF\x00\x01\x01\x01\x01,\x01,\x00\x00AMPF\xff\xe1\nbExif\x00\x00MM\x00*\x00\x00\x00\x08\x00\x0e\x01\x0f\x00\x02\x00\x00\x00\x06\x00\x00\x00\xb6\x01\x10\x00\x02\x00\x00\x00\x0f\x00\x00\x00\xbc\x01\x12\x00\x03\x00\x00\x00\x01\x00\x01\x00\x00\x01\x1a\x00\x05\x00\x00\x00\x01\x00\x00\x00\xcc\x01\x1b\x00\x05\x00\x00\x00\x01'
```

En regardant le type de `img`{.language-} (avec la commande `type(x)`{.language-}) :

```text
>>> type(img)
&lt;class 'bytes'>
```

On se rend compte que ce n'est pas une chaîne de caractères, mais un `bytes` (une suite d'octets). Affichons ses 100 premiers bytes :

```python
>>> img[:100]
b'\xff\xd8\xff\xe0\x00\x14JFIF\x00\x01\x01\x01\x01,\x01,\x00\x00AMPF\xff\xe1\nbExif\x00\x00MM\x00*\x00\x00\x00\x08\x00\x0e\x01\x0f\x00\x02\x00\x00\x00\x06\x00\x00\x00\xb6\x01\x10\x00\x02\x00\x00\x00\x0f\x00\x00\x00\xbc\x01\x12\x00\x03\x00\x00\x00\x01\x00\x01\x00\x00\x01\x1a\x00\x05\x00\x00\x00\x01\x00\x00\x00\xcc\x01\x1b\x00\x05\x00\x00\x00\x01'
```

Quand python affiche des suites d'octets, il essaie de les écrire en ASCII et pour tous les caractères qu'il ne comprend pas (ici les accents car ils sont codés sur 2 octets en utf-8), il écrit juste le nombre sous format hexadécimal `\xff` par exemple. De plus, il fait commencer l'affichage par un `b`  pour bien montrer que ce n'est **PAS** une chaîne de caractère.

Ces premiers caractères sont significatifs des fichiers jpeg, comme l'atteste : [la liste de signatures de fichiers](https://en.wikipedia.org/wiki/List_of_file_signatures). Attention, cette liste n'est qu'une convention préférez utiliser des extensions de fichiers plutôt que de vous fier à ces signatures de façon aveugle.

Lorsque l'on manipule des fichiers binaires avec python, il est bien sur recommandé de ne pas les manipuler directement. Utilisez des bibliothèques faites pour cela. Pour les images, on recommande souvent d'utiliser [pillow](https://pillow.readthedocs.io/en/stable/) :

```python
>>> from PIL import Image
>>> img = Image.open("IMG_0192.jpeg")
>>> img.show()
```
