---
layout: layout/post.njk

title: Bonnes pratiques
authors: 
  - Corentin Lange
  - François Brucker

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

La gestion des sources est un outil formidable pour travailler au quotidien. Cependant, beaucoup de connaissance et un peu de pratique sont nécessaires pour que son utilisation soit fluide. Si vous ne faites pas l'effort de comprendre ce que vous faite ou (surtout) de chercher dans la documentation les commandes pour réaliser ce que vous avez envie de faire, utiliser un système de gestion des sources va vous sembler lourd et fastidieux (et vous ne l'utiliserez plus) ou magique (et vous allez faire plein d'erreurs qui peuvent coûter très cher en temps de développement).

Pour que tout se passe au mieux lorsque vous utilisez un système de gestion des sources, il est important de suivre quelques règles qui vous permettront de facilement :

- connaître le contenu d'un commit
- contacter la personne ayant fait un commit
- naviguer dans l'historique du projet

Sans les trois conditions ci-dessus, utiliser un SCM n'est pas vraiment utile et vous fera perdre plus de temps qu'en gagner.

## Identité

Pour que le processus de gestion des sources soit efficace il est nécessaire que tout commit soit bien :

- identifié : l'auteur du commit doit pouvoir être retrouvé
- documenté : le message accompagnant le commit doit être descriptif.

### Profil

Ayez votre profil à jour :

- nom et prénom ou pseudo identifiable
- adresse mail à jour

Il vous est facile d'avoir une identité par défaut (liée à votre compte) et une identité par projet (dans la configuration du projet). Ceci permet de différentier les projet pro des projets perso sans avoir à faire de grandes manipulations.

### Message de commits

Utilisez un éditeur de texte que vous maîtrisez pour éditer le message de commit. Par défaut c'est [vi](https://fr.wikipedia.org/wiki/Vi), éditeur historique et présent sur toute machine unix qui est utilisé, mais qui n'est pas forcément votre éditeur de prédilection.

Un message de commit contient forcément **1 ligne** décrivant le commit (on verra dans la partie suivante des méthodes pour les écrire). Puis, si nécessaire, une description plus long (souvent inutile).

<!-- TBD 

à étoffer (faire un exemple) en utilisant les liens précédent 

-->
### .gitignore

{% lien %}

- [fichier .gitignore avec github](https://docs.github.com/fr/get-started/git-basics/ignoring-files)
- [tuto en français](https://www.youtube.com/watch?v=gkzBzBomYyI)

{% endlien %}

## Actions courantes

### Travailler en local

- commitez souvent pour pouvoir revenir en arrière si nécessaire
- créez des branches temporaires locale pour vos expérimentations et n'hésitez pas à revenir en arrière
- utilisez un [fichier `.gitignore`](https://docs.github.com/en/get-started/git-basics/ignoring-files) pour contrôler les fichier à suivre. Tout fichier doit être soit suivi soit ignoré : ne tolérez pas d'exception sinon vous allez vous perdre et (forcément) faire des erreurs.

### Récupérer l'état de l'origine

Utilisez la commande `fetch` pour voir l'état de l'origine pour les branches que vous suivez. Cela vous montrera l'avancé de vos collègues et les votre et vous dira quand faire un commit sur le serveur.

### Récupérer les commits de l'origine

Lorsque vous récupérez des données de l'origine faites le avec un `rebase` pour qu'ils se placent avant vos commit linéairement. Ne créez pas de fusions de branches inutiles.

{% info %}
On peut le faire puisque vos modifications sont encore locales.
{% endinfo %}

N'ayez pas peur de gérer les conflits. Une fois qu'on a l'habitude cela se fait aisément.

### Envoyer ses modification à l'origine

- Mettez vos fichiers sur l'origine régulièrement (une fois une fonctionnalité terminée par exemple) avec un `push`. Cela permet de montrer vos avancées aux collègue et n'induira pas de mise en commun fastidieuses.
- Ne modifiez **jamais** l'état de l'origine : ne faites que des ajouts. S'il faut revenir en arrière utilisez un `revert` qui ajoute un nouveau commit.

## Nommer ses commits

{% lien "**Documentation**"  %}
<https://www.conventionalcommits.org/en/v1.0.0/>
{% endlien %}

La forme du nom de ses commits est aussi important, même si on est l'unique développeur de son projet. Une liste de commits mal nommés peut vite devenir illisible et occasionner des pertes de fluidité pour la relecture.

Message de commit :

- titre du message : \<type\> [scope (optionnel)]: \<description\>
  - type :
    - **feature** : Ajout d’une nouvelle fonctionnalité
    - **test** : Ajout de tests
    - **bugfix** : Correction d’un bug
    - **hotfix** : Correction d’un bug critique
    - **chore** : Nettoyage du code
    - **experiment** : Expérimentation de fonctionnalités
    - ...
  - scope : Optionnel. l'endroit dans le code où les modification on été faites
    - **api** : changement dans l'api
    - **lang** : ajout d'une traduction dans une nouvelle langue
    - **style** : changement dans le css
    - ...
  - description : en une courte phrase d'une ligne.

- corps du message : à n'utiliser que si nsi vous avez besoin d'ajouter beaucoup de description à votre commit. Cela doit être rare

{% lien "**Documentation**"  %}
<https://gitmoji.dev/>
{% endlien %}

Pour aller encore plus loin on peut voir apparaître désormais des émojis dans les commits pour améliorer la relecture.

Il est conseillé de le mettre soit avant votre scope soit directement le remplacer avec.

Exemple de commits:

- Sans scope:
  - :bug: correction of bad codes
  - :zap: accelerated program launch on windows

- Avec scope:
  - :hammer: refact: refactored sql db
  - :rotating_light: fix: compiler problems

{% lien %}
Le tableau [ici](https://gist.github.com/parmentf/035de27d6ed1dce0b36a) vous aide à trouver l'émoji associé au commit que vous souhaitez.
{% endlien %}

Vous pouvez vous même rédiger votre tableau dans votre **CONTRIBUTING** ! (On en parle plus bas)

## Branches partagées

Il existe de nombreuses méthodes pour organiser les branches d'un projet. Chacune ayant ses pour et ses contre. Si vous arrivez dans un projet déjà existant adaptez-vous mais si vous créez un nouveau projet, voici quelques façon de faire qui vous ferons gagner du temps. Il y a deux grandes familles :

- les méthodes avec de nombreuses branches bien spécifiées
- les méthodes sans branches

Chacune à ses pour et ses contre et viennent avec leurs propre contraintes. A vous de voir celle que vous préférez avec votre projet.

### Feature branching

La première idée est de consacrer une branche par feature à développer. Une fois cette branche terminée elle s'intègre à la branche principale par un merge. Cette méthode, appelé **_feature branching_** peut générer de nombreuses branches si l'équipe de développement est importante. C'est pourquoi, certaines adaptations ont vu le jour comme [Git flow](https://leanpub.com/git-flow/read) (si vous utilisez cette méthode, il existe [un plugin git](https://danielkummer.github.io/git-flow-cheatsheet/index.fr_FR.html)) ou encore [Github flow](https://githubflow.github.io/) (qui préconise de n'avoir qu'une unique branche de développement pour une synchronisation plus claire entre les développeurs) pour préciser et nommer les différentes branches d'un projet.

{% lien %}
[Présentation concise des deux méthodes](https://www.youtube.com/watch?v=hG_P6IRAjNQ) (2min08 et 4min38)
{% endlien %}

UN projet sous le git workflow va se représenter de cette façon :

![Git_flow_4](git_flow_4.png)

Chaque branche va avoir sa sémantique propre qui permet de savoir immédiatement ce que'elle fait :

- `main`. Cette branche contient le code de production (celui actuellement utilisé sur votre produit/système fonctionnel).
Tout le code de développement(branch develop) est fusionné dans master au fur et à mesure que les features,etc... ont été dûment testées et validées.
- `develop`. Cette branche contient le code de pré-production. Lorsque les fonctionnalités sont terminées, elles sont fusionnées dans la branche de développement pour de futurs tests avant validation pour "partir en prod".
- `feature/<nom feature>`. Les branches feature sont utilisées pour développer de nouvelles fonctionnalités pour les prochaines versions. Elles peuvent être dérivées de develop et doivent être fusionnées avec develop(jamais main directement !). On ajoute après le / le nom de la feature ajoutée.
- `hotfix/<nom hotfix>`. Les branches hotfix sont nécessaires pour agir immédiatement sur un statut non désiré de master. Peut se ramifier à partir de master et doit fusionner dans master et develop.
- `release/<nom release>`. Les branches de version prennent en charge la préparation d'une nouvelle version de production. Elles permettent de corriger de nombreux bogues mineurs et de préparer les méta-données pour une version. Peut se ramifier à partir de develop et doit fusionner avec master et develop.

Le principal soucis, outre son formalisme stricte, est la multiplicité des des branches qui fait qu'on peut facilement s'y perdre.

### Continuous Integration

La continuous integration prend le contre-pied des méthodes précédentes et préconise de minimiser le nombre et la durée des branches au stricte maximum tout en commitant souvent sur la branche principale. Le but ultime de cette méthode est d'avoir le workflow suivant :

![CI](./git_flow_1.png)

Cette méthode, très prisée actuellement, fonctionne. Le lien suivant décrit l'idée :

{% lien %}
[CI workflow](https://www.youtube.com/watch?v=v4Ijkq6Myfc)
{% endlien %}

On a cependant rien sans rien. Le workflow CI s'appuie sur de nombreux tests automatisés pour vérifier que tout se passe bien et est construite pour que tout puisse aller vite en production...et être corrigé rapidement si nécessaire.

{% attention %}
La production est le dernier endroit ou votre code est testé, certes, mais ça ne doit pas être le seul
{% endattention %}

> TBD à étoffer

## Gestion du projet

### Documentation

Il est important de bien documenter son repository sur GitHub afin d'aider à la compréhension de ce dernier : que ce soit pour un projet fermé si de nouveaux développeurs arrivent dans l'équipe, ou bien dans une dynamique open-source pour toute personne souhaitant participer au projet.

Les fichiers Markdown(.md) sont donc vos meilleurs amis pour aider à la compréhension du projet.

#### Readme

{% lien "**Documentation**" %}
<https://www.makeareadme.com/>
{% endlien %}

C'est le fichier `README.md`{.fichier} visible directement sur votre repo quand on arrive dessus, il est à placer dans le fichier racine de votre projet. Il contient les informations qui sont généralement nécessaires pour comprendre le sujet du projet. Il est écrit en **markdown**(.md), comme tout ce site d'ailleurs, qui est un langage de balisage léger.

On y retrouve en général :

- le nom du projet
- son installation
- son utilisation
- des visuels

Vous pouvez vous inspirer du [readme d'Atom](https://github.com/atom/atom#readme)

#### <span id="contributing"></span> Contributing

Il est d'usage aussi de réaliser un fichier markdown `CONTRIBUTING.md`{.fichier} afin d'expliquer à toutes personnes participant au code/projet comment :

- bien faire leur commits dans ce projet
- ce qui est autorisé ou non
- un "template" pour les issues
- un "template" pour les pull requests

Vous pouvez vous inspirer du **CONTRIBUTING** de [Atom](https://github.com/atom/atom/blob/master/CONTRIBUTING.md), ainsi que celui de [GodotEngine](https://github.com/godotengine/godot/blob/master/CONTRIBUTING.md) (Moteur de jeux open-source).

Ces derniers sont très explicites et aident vraiment à obtenir des commits, pull requests de qualités étant une grande aide à toute personne souhaitant participer.

[Atom_contributing](https://github.com/atom/atom/blob/master/CONTRIBUTING.md)
[Godot_contributing](https://github.com/godotengine/godot/blob/master/CONTRIBUTING.md)

### Versioning - sémantique des versions

{% lien "**Documentation**" %}
<https://semver.org/lang/fr/>
{% endlien %}

Pour les versions de votre projet il existe une sémantique précise.
On peut résumer cette sémantique à l'aide de ce graphe ci-dessous.

```shell
<major>.<minor>.<patch>-<label>
```

Par exemple :

```text
1.0.0-beta1
```

On retrouve dans la version de son projet :

- le numéro de version **MAJEUR** : Quand les changements apportés ne sont pas rétrocompatibles, vulgairement de gros changements
- le numéro de version **MINEUR** : Quand les ajouts sont rétrocompatibles
- le numéro de version de **CORRECTIF/PATCH** : Pas d'ajouts de fonctionnalités mais uniquement des corrections.
- un **LABEL** facultatif: Pour apporter des précisions sur le type de version
  (ex: beta/alpha/stable)

## Participer à un projet

Si vous contribuez à un projet avec plusieurs développeurs, ou si vous trouvez et corrigez un problème d'un projet qui n'est pas le votre, une façon courtoise de demander l'ajout d'intégration de vos travaux est d'effectuer une **_pull request_**.

Une pull request est une proposition de commit qui pourra être accepté, amendé ou parfois rejeté par l'équipe de développement. Cette méthode permet aussi de facilement travailler avec une équipe de niveau hétérogène où les commits des développeurs les moins expérimentés sont inspecté par les lead développeurs avant acceptation.

### <span id="pull-request"></span>Pull Request (PR)

Voici un exemple de pull request :

![Versioning](pull_request.png)

Comme vous pouvez le voir sur cette capture, sur une pull_request vous avez la possibilité d'assigner :

- Des **relecteurs** : devant donner leur aval pour accepter le merge
- Des **labels**: afin de trier les différentes pull request (ex : hotfix, feature,...)
- Définir si la pull request s'inscrit dans un projet ou/et à des milestones (un outil de gestion de projet présent sur github)
- Lier des **issues** qui seront automatiquement fermées au moment du merge de la pull request dans la branch master du projet

Cet outil permet ainsi d'"empaqueter" des commits au sein d'un ajout d'une plus grande quantité de modifications dans le projet.

### Issues

De la même manière que les Pull Requests, il est possible de créer des issues (ou problèmes) afin de mettre l'accent sur :

- l'ajout d'une fonctionnalité
- une dis-fonctionnalité

Une bonne issue doit être bien rédiger afin d'aider la personne qui va s'en occuper :

- si ajout d'une fonctionnalité :
  - bien décrire la fonctionnalité voulue
  - son fonctionnement
  - des visuels.
- si dis-fonctionnalité :
  - visuels,
  - comment l'erreur s'est produite ?
  - sur quelle machine ?
  - avec quelle version ?
  - si reproductible, expliquer comment la reproduire
  - indiquer des pistes si vous en avez
