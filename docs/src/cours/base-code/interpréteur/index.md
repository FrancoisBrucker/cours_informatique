---
layout: layout/post.njk 
title: Interpréteur

eleventyNavigation:
  key: "Interpréteur"
  parent: "Coder en Python"
---

<!-- début résumé -->

L'interpréteur python comme intermédiaire entre le code python et son exécution.

<!-- fin résumé -->

## Intermédiaire

Tout code python est exécuté *via* un interpréteur dont le but est de transformer le code python en code machine.

Ceci se fait **toujours** comme suit :

1. on donne une ligne de code à l'interpréteur
2. l'interpréteur exécute cette ligne (il transforme la ligne en langue machine et la fait exécuter par l'ordinateur)
3. une fois la ligne exécutée, l'interpréteur redonne la main à l'utilisateur
4. retour à l'étape 1.

Tant que l'interpréteur est actif, un mécanisme de stockage permet de conserver des ***objets*** pour une utilisation future via des ***variables***.

{% note %}
L'interpréteur python est **toujours** présent lorsque l'on exécute du code python.
{% endnote %}

IL y a plusieurs façon d'exécuter du code python, celle qui montre le plus explicitement l'interpréteur est l'***exécution en mode console***.

{% faire "Allez sur le site <https://basthon.fr/> et choisissez *menu console > python*" %}

Vous allez vous retrouver sur le site <https://console.basthon.fr/>
{% endfaire %}

Vous devriez avoir quelque chose du genre :

![console python](console-1.png)

Intéressons nous pour l'instant à la partie de droite nommée la ***console*** :

* l'interpréteur python utilisé est 3.8.2
* le ***prompt*** (les `>>>`) indique que l'on peut écrire une ligne de code

Allons-y ! Exécutons notre premier programme :

{% faire %}
A droite du prompt, écrivez le code `print("Bonjour monde !")`{.language-} puis appuyez sur la touche *entrée*.
{% endfaire %}

Vous devriez obtenir quelque chose du type :

![hello world](console-2.png)

{% info %}
Si vous n'obtenez pas ça, vous pouvez toujours recharger la page (*menu afficher > actualiser cette page* avec le navigateur chrome) pur recommencer avec un interpréteur vierge.
{% endinfo %}

Ce qu'il s'est passé :

1. vous avez écrit une ligne de code dans la console
2. en appuyant sur la touche *entrée*, celle-ci a transmis la ligne à l'interpréteur
3. l'interpréteur à exécuté la ligne de code (son résultat est affiché)
4. une fois le code exécuté, la console reprend la main (le prompt a réapparu) et on peut recommencer en 1.

Ne nous arrêtons pas en si bon chemin et écrivons *plusieurs* lignes de code.

{% faire %}
Dans la partie *éditeur de code* de la fenêtre copiez/collez le code suivant :

```python
print("Bonjour :")
print("* François")
print("* Pierre")
print("* Odile")
```

Puis appuyez sur le bouton *Exécutez*.
{% endfaire %}

Vous devriez obtenir quelque chose du type :

![hello world](console-3.png)

Il s'est passé la même chose que précédemment : chaque ligne a été exécuté à la suite par l'interpréteur, la seule différence est que la console a repris la main uniquement lorsque toutes les lignes de code ont été exécutées.

{% note %}
Le processus que l'on a décrit ici est **toujours** le même lorsque l'on écrit du code python, même si parfois l'interpréteur et la console sont cachés à l'utilisateur.
{% endnote %}
