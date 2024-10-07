---
layout: layout/post.njk

title: Exercices

eleventyNavigation:
    order: 1

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

## Fichiers

1. Quel est le chemin de votre dossier maison
2. Quels sont les fichiers présents ?
3. Quel est la différence entre :
   - `ls`
   - `ls -l`
   - `ls -a`
   - `ls -la`
4. Créez un dossier `temporaire`{.fichier} dans votre dossier maison. Quels sont les droits de ce fichier ?
5. Affichez la liste des fichiers par date de dernière modification/création (c'est une option de `ls`). Le dossier `temporaire`{.fichier} devrait être en premier.
6. Modifier la date de modification du dossier modifié le dernier (grace à la commande `touch`) et vérifier qu'il est maintenant en premier dans la liste
7. Que fait `touch fichier` si `fichier`{.fichier} n'existe pas ?
8. Affichez les 3 éléments plus récemment modifiés, puis les 5 moins récemment modifié (vous pouvez utiliser les commandes `head` et `tail`)
9. Copiez le fichier `/etc/passwd` dans le dossier `${HOME}/temporaire`{.fichier} créé précédemment et appelez le mot-de-passe, le tout en une seule commande
10. Supprimez le dossier `${HOME}/temporaire`{.fichier} en une seule commande `rm`
11. Créez un dossier `private` dans maison et modifiez ses droits pour qu'il ne soit accessible que de vous même. Faites cette modification en utilisant la notation symbolique.
12. À quoi correspondent ces droits en notation [octale](https://docs.oracle.com/cd/E19504-01/802-5750/6i9g464pv/index.html) ?
13. Créez un fichier nommé `hello.txt` dans votre dossier maison contenant le texte "bonjour" avec un éditeur de texte (nano par exemple)
14. Ajoutez " monde !" à la fin du fichier `hello.txt` avec une commande commande echo
15. Déplacez le fichier `hello.txt` dans le dossier `private`
16. Créez un lien symbolique dans votre maison vers le fichier `hello.txt` de votre dossier private.
17. Modifiez le contenu du fichier symbolique pour son contenu soit sur une seule ligne (vous pourrez vous aider de la commande `tr` et de [ce tutoriel](https://www.baeldung.com/linux/join-multiple-lines))
18. Afficher, avec la commande `cat`, le contenu du fichier dans `private/hello.txt`
19. Que se passe-t-il pour le lien si vous supprimez ou renommez le fichier original ?
20. Créez avec `nano` un fichier nommé `brise marine.txt`{,.fichier} et mettez-y le [poème de Mallarmé](https://www.poetica.fr/poeme-109/stephane-mallarme-brise-marine/)
21. Affichez ce fichier avec la commande `cat` en [escapant](https://www.shellscript.sh/escape.html) le métacaractère espace
22. renommez, avec la commande `mv` le fichier `brise marine.txt`{.fichier} en `brise_marine.txt`{.fichier}

## find

[find](https://shapeshed.com/unix-find/)
trouver les fichiers qui ont été modifié il y a moins de 7 jours (find . -mtime +30 -print)

Déterminez quel est le dossier contenant le plus de méga de votre système.(du -h | sort -h | tail)

## Process

1. Lister tous les process de tous les utilisateurs (avec la commande `ps` et ses options)
2. Les compter (avec la commande `wc`)
3. Comptez uniquement les process de root puis les vôtres (avec l'aide de la commande `grep`)
4. À l\aide de deux terminaux :
   1. ouvrir un `nano` dans lun,
   2. à l'aide de son PID, tuer le process `nano` dans l'autre terminal.

## Que fait ça ?

Vu dans un fichier de configuration d'un nouvel utilisateur :

```shell
password=$(cat /dev/urandom | tr -dc 'a-zA-Z0-9' | fold -w 8 | head -n 1)
```

> TBD en ajouter d'autres
