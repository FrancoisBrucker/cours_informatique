---
layout: layout/post.njk

title: DM en réserve

eleventyNavigation:
    order: 1

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---



## Prénoms

## TP

2. En utilisant [ce tutoriel](https://www.cyberciti.biz/tips/shell-scripting-bash-how-to-create-temporary-random-file-name.html), Créez un script qui récupère le tome 1 du comte de Monte-Cristo et le stocke dans un fichier temporaire créé dans `/tmp`


but : "script qui prend un texte d'un fichier ou de stdin et qui selon les options parle en toulousain (putaing cong ! à la fin de chaque ligne ), en alsacien (hopla,  en début de paragraphe (.^)) ou en marseillais (après une virgule peuchère)"

<https://stackoverflow.com/questions/5790742/sed-how-to-get-the-first-2-sentences-of-a-paragraph>

nombre de mots dans un fichier : <https://www.tecmint.com/count-word-occurrences-in-linux-text-file/>

1. récupère de l'internet :
   1. sauve dans un fichier
   2. supprime les lignes avant le début (sed ou tail) `sed -n '/\*\*\*/='`
   3. sauve dans /tmp avec un nom qui n'existe pas <https://www.cyberciti.biz/tips/shell-scripting-bash-how-to-create-temporary-random-file-name.html>
2. prend un fichier en argument et :
   1. compte le nombre de mots et le nombre moyen de mot par ligne (expr ou $(())).
   2. <https://stackoverflow.com/questions/5790742/sed-how-to-get-the-first-2-sentences-of-a-paragraph> Fait un texte alsacien pour chaque début de paragraphe (ligne vide), ajoute "Hopla !"
   3. Fait un texte marseillais après chaque virgule, ajoute "peuchère, "
   4. options : [option parsing](https://stackabuse.com/how-to-parse-command-line-arguments-in-bash/)
3. fait en sorte de soit lire un fichier en argument, soit en stdin

4. naissances <https://www.insee.fr/fr/statistiques/7633685?sommaire=7635552> avec cut, sort et uniq
5. fichier json <https://www.data.gouv.fr/fr/datasets/villes-de-france/>
   1. utiliser jq pour compter le nombre de ville d'un département avec une boucle for. <https://stackoverflow.com/questions/33950596/iterating-through-json-array-in-shell-script> <https://www.digitalocean.com/community/tutorials/how-to-transform-json-data-with-jq>

```
curl https://www.gutenberg.org/cache/epub/1184/pg1184.txt 2>/dev/null | wc
```
1. faire des tests : <https://medium.com/@sankad_19852/shell-scripting-exercises-5eb7220c2252> pour préparer faire une poubelle pour le rm <https://utminers.utep.edu/xzeng/2016fall_cps5401/CPS_5401_Introduction_to_Computational_Science_files/solution_1.pdf>
1. faire un code de sorite si ok ou pas


2. nb de lignes, mots
3. mettre sur un fichier dans tmp (nom pas encore existant)
4. longueur moyenne de chaque mot avec un awk
5. faire automatiquement dans un script ajouter des options (nb mot, longueur moy, fichier à télécharger ou stdin)
6. et suppression du fichier ensuite

### exo préparatoire

1. récupérer et nb de ligne marseille
2. création d'un script avec boucle
3. json : nombre de villes ?

> <https://www.baeldung.com/linux/csv-parsing>
> <https://www.joeldare.com/wiki/using_awk_on_csv_files>

## autres exos

- [tp ensimag](https://matthieu-moy.fr/cours/unix2/seance2/tp-pas-a-pas.pdf) et [cours](https://matthieu-moy.fr/cours/unix2/)