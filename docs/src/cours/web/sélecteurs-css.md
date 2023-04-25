---
layout: layout/post.njk
title: Sélecteurs css

authors:
    - "François Brucker"


eleventyNavigation:
  key: "Sélecteurs css"
  parent: "Web"
---

<!-- début résumé -->

Qu'est ce qu'un sélecteurs css, comment

<!-- fin résumé -->

{% lien "**Documentation**" %}

<https://developer.mozilla.org/fr/docs/Web/CSS/CSS_Selectors>

{% endlien %}

Un sélecteur css peut-être beaucoup de choses. Il permet de sélectionner une ou plusieurs balises html pour lesquelles le style sera appliqué.

### Une combinaison de sélecteur

On peut lier des sélecteurs en utilisant la `,`{.language-}. Par exemple :

```css

p, h1 {
  color: red;
}

```

S'applique aux balises `<p></p>`{.language-} et `<h1></h1>`{.language-}.

{% attention %}

Il ne faut pas oublier la `,`. Le sélecteur `p h1 { ...}` signifie tout à fait autre chose.

{% endattention %}

Le sélecteur `*`{.language-} correspond à tout. Il n'est pas recommandé de l'utiliser tout seul, mais en utilisant une spécialisation par exemple.

### Sélection par attribut

{% lien "**Documentation**" %}

<https://developer.mozilla.org/fr/docs/Web/CSS/Attribute_selectors>

{% endlien %}

On peut sélection une balise selon les attributs qu'elle possède. Par exemple toutes les balises ayant un attribut style :

```css
*[style] {
  color: red;
}

```

### Une spécialisation

* `A B`{.language-} : les balises correspondant au sélecteurs `B`{.language-} descendantes de balises `A`{.language-}.
* `A > B`{.language-} : les balises correspondant au sélecteurs `B`{.language-} enfants directs de balises `A`{.language-}.
* `A ~ B`{.language-} : les balises correspondant au sélecteurs `B`{.language-} voisins de balises `A`{.language-} (ayant même parent).
* `A + B`{.language-} : les balises correspondant au sélecteurs `B`{.language-} voisins direct de balises `A`{.language-} (ayant même parent).

### Une pseudo classe

{% lien "**Documentation**" %}

[les pseudo-classes standards](https://developer.mozilla.org/fr/docs/Web/CSS/Pseudo-classes#liste_des_pseudo-classes_standards)

{% endlien %}

Le pseudo-classes permettent de sélection une balise dans un état particulier.

Utiles pour des liens :

* `a:visited`{.language-} : est le sélecteur des liens visités.
* `a:hover`{.language-} : lorsque la souris passe dessus
* `a:active`{.language-} : lorsque l’on clique dessus

Pour que les liens non encore visités et les liens visités aient le même rendu, on pourra écrire :

```css
a, a:visited {
  color: red;
}
```

Mais c'est utile pour plein de choses. Changer de couleur lorsque l'on passe sur une balise :

```css

p:hover {
  color: red;
}
```

### Un pseudo élément

{% lien "**Documentation**" %}

[les pseudo-éléments](https://developer.mozilla.org/fr/docs/Web/CSS/Pseudo-elements#liste_des_pseudo-%C3%A9l%C3%A9ments)

{% endlien %}

Permet de sélectionner une partie d'une balise. A ne pas confondre avec une pseudo-classe qui sélectionne la balise en entier.

Par exemple :

```css

p::first-letter {
  font-size: 2em;
}
```

Ou encore, le pseudo-élément suivant qui dépend de la taille de l'écran :

```css
p::first-line {
  color: red;
}
```

Enfin, on utilise souvent les pseudo-éléments `::before` et `::after` pour ajouter des éléments avant et après une balise :

```css
p::before {
  content: ">>>>>";
  font-size: 2em
}
p::after {
  content: "<<<<";
  font-size: .5em
}

```

### class et id

On en reparlera dans la partie sur les [balises anonymes](../balises-anonymes#sélecteur-css){.interne}, nous ne ferons que les mentionner ici pour la référence. Il existe deux sélecteurs css très utilisés :

* le [sélecteur de classes](https://developer.mozilla.org/fr/docs/Web/CSS/Class_selectors)
* le [sélecteur d'identifiant](https://developer.mozilla.org/fr/docs/Web/CSS/ID_selectors)
