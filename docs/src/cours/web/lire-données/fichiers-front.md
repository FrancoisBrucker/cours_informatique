---
layout: layout/post.njk

title: Lire des fichiers avec le navigateur

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Pour qu'un code javascript puisse charger un fichier, il faut que l'utilisateur choisisse le fichier à charger via la balise [`<input>`{.language-}](https://developer.mozilla.org/fr/docs/Web/HTML/Element/input).

Par exemple :

```html
<!doctype html>
<html lang="fr">
<head>
    <meta charset="utf-8">
    <title>Chargement d'un fichier texte</title>
</head>
<body>
    <div>
        <h1>Choisissez un fichier texte</h1>
        <input type="file" id="fichier-input" />
    </div>
    <p id="texte"></p>
    <script>
        const elem = document.getElementById("fichier-input");    

        elem.addEventListener("change", () => {
            const file =  elem.files[0];
            file.text().then(data => {
                const texte = document.getElementById("texte");
                texte.innerText = data;
                console.log(data)
            })
            
        });
    </script>
</body>
</html>
```

Vous pouvez voir le résultat [ici](../code-fichiers-front/fichier).

Lorsque l'utilisateur choisit un fichier de son disque dur, il génère l'évènement change qui est intercepté. Le fichier choisit contient plusieurs méthodes, dont `text()`{.language-} qui est une promesse de lecture du fichier au format texte.

Si le fichier contient des données json par exemple, elles peuvent alors être désérialisées en objets javascript utilisable.

Il est possible de charger d'autres types de fichiers, comme une image par exemple. On ne prend pas directement le contenu de l'image (on verra ça lorsque l'on traitera de la commande fetch), mais son url pour l'afficher dans le fichier html :

```html
<!doctype html>
<html lang="fr">
<head>
    <meta charset="utf-8">
    <title>Chargement d'un fichier texte</title>
</head>
<body>
    <div>
      <h1>Choisissez un fichier image</h1>
        <input type="file" id="fichier-input" />
    </div>
    <img id="image" src="">

    <script>
        const elem = document.getElementById("fichier-input");    

        elem.addEventListener("change", () => {
            const file =  elem.files[0];

            const image = document.getElementById("image");    
            image.src = URL.createObjectURL(file);
            
        });
    </script>
</body>
</html>
```

Vous pouvez voir le résultat [ici](../code-fichiers-front/image).

{% lien %}
[Autres usages](https://developer.mozilla.org/fr/docs/Web/API/File_API/Using_files_from_web_applications)
{% endlien %}
