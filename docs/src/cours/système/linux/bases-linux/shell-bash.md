---
layout: layout/post.njk

title: Shell Bash

eleventyNavigation:
    order: 1

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

<https://www.gnu.org/software/bash/manual/html_node/>
- plusieurs sorte de shell
- [histoire du design sh](https://www.youtube.com/watch?v=FI_bZhV7wpI)

-[variables d'environnement](https://www.youtube.com/watch?v=1z6EUUl11qI&list=PLQqbP89HgbbY23Ab_vXGfLXHygquD7cAs&index=2)

- [pas d'espace dans la déclaration de variable en shell](https://utcc.utoronto.ca/~cks/space/blog/unix/BourneShellObscureErrorRoots)


Taper des commandes = script. Comme python. Il faut trouver un moyen de faifre des bout de commandes san les executer a=à la fin d'une ligne. Python fait des blocs. shell fait autrement. De plus, tout est orienté commandes sans pratiquement aucune surcouche du shell (on le veraa avec les if/then/else qui fonctionnent bien différemment du reste des langages de programmation)

> TBD path : which, type whereis
>

> TBD if then else est fait comme ça

> TBD bouger dans /, ls puis revenir au dossier précédent. POur cela lire la doc google, et le man dans bash. On peut aller plus vite en cherchant "cd" et n pour la prochaine. on peut encore aller plus vite en cherchant "   cd" car c'est une commande
> Ceci permet de parler des variables.
> 

- contrôle de flux différents selon le shell : for/while
- tout ligne à ligne. if commandes
- fichiers de contrôle : .profile, .bashrc
- alias (`ls -la`, python pour python3) : which et file
- "", '', ``, $(), ${}
- [métacaractères](https://www.bogotobogo.com/Linux/linux_shell_programming_tutorial7_metacharacters_quotes.php) (du shell) 

> TBD autre fichier lorsque l'on parlera de l'environnement. pour aller plus loin (ensuite). Lorsque l'on a parlé des variables. PWD, OLDPWD
> TBD dans les env parler de PWD et poser la question de : <https://stackoverflow.com/questions/41147818/no-man-page-for-the-cd-command>


> TBD if then else est fait avec les retour de commandes. Ce n'est PAS une expression. Exemple avec plusieurs lignes.
> `[` est une commande ! C'est pour a qu'il y a le ; avant le then.

> TBD toute exécution d'un fichier crée un processus fils du shell appelant
-[utiliser des $ en script](https://www.gnu.org/software/bash/manual/html_node/Special-Parameters.html)