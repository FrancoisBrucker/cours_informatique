---
layout: page
title:  "Installation d'un nouveau système"
category: tutorial
tags: combat w10
author: "François Brucker"
---



## python

Avoir un interpréteur python est très pratique pour faire de petits programmes et/ou de la data science. Pour le dev proprement dit, python sera installé sur la wsl, voir installé pour chaque projet, mais pour des besoins plus ponctuel on va installer anaconda sur la système windows. 

### anaconda

Anaconda est une distribution python oriente data science. Commençons par l'[installer](https://www.anaconda.com/products/individual) :

  - on utilisera la version windows 64bits utilisant `python3`,
  - installez la pour tous les utilisateurs
  - laissez coché la case qui lie l'interpréteur python d'anaconda au système.

Anaconda est maintenant installé sur votre disque dur dans le dossier : `c:\ProgramData\Anaconda3` et vous trouverez un dossier *Anaconda3* dans le menu démarrer

#### jupyter

Depuis le *menu démarrer > Anaconda3* vous pouvez lancer le programme `Anaconda navigator`` qui vous permettra d'exécuter jupyter sur votre navigateur.

#### installer de nouveau packages dans anacoda

Vous pouvez le faire via anaconda navigator, mais le plus simple est encore d'installer directement.

Cliquer sur /menu démarrer > Anaconda3 > Aanconda powershell prompt/. Une fenêtre poershell se lance aliée avec l'interpréteur python d'anaconda.

Vous pouvez ainsi taper directement la commande pip pour installer des modules python :
- tapez /python/ dans cette fenêtre et vous exécuterez l'interpréteur pyhton d'anaconda (/exit()/ puis entrée ou control+D pour sortir de l'interpréteur)
- La commande /pip list/ va lister tous les modules que vous avez installé par exemple.
 
### pycharm

Installez [pycharm professionnel](https://www.jetbrains.com/fr-fr/pycharm/download/). En tant qu'étudiant vous pouvez obtenir une licence gratuite du logiciel. Faites le pour pouvoir utiliser les fonctionnalités avancées de pycharm, comme l'utilisation d'un python de wsl.

Une fois l'installation terminée créer un nouveau projet en utilisant l'interpréteur d'anaconda. Pour cela, une fois avoir choisi de faire un nouveau projet :

  1. choisissez /existing interpreter/ puis cliquez sur les /.../
  2. cliquez sur /Conda Environment/ puis sur les /.../ pour trouver l'interpréteur.
     Si vous avez installé anaconda pour tous les utilisateur, il doit se trouver dans `c:\ProgramData\Anaconda3\Scripts\python.exe`
  3. Avant de cliquer sur *Ok*, n'oubliez pas de cocher la case *Make available to all projects* pour ne pas avoir a rechercher l'interpréteur à chaque fois.
  4. Votre interpréteur est crée, vous pouvez maintenant cliquer sur *Create* pour générer votre projet.

Créer un fichier `hello_world.py` :

~~~ python
print("hello world!")
~~~

Puis exécutez le pour vérifier que tout fonctionne.

>**odds and ends** :
>
>  - Il est possible que le triangle vert de l'exécution ne soit pas disponible. C'est le cas lorsque pycharm *"travaille"* : la ligne de status, tout en bas de la fenêtre, indique en bleue *process running...* (vous pouvez cliquer dessus pour voir ce que pycharm est entrain de faire). Une fois qu'il a fini de travailler, vous pourrez exécuter votre code.
>  - j'ai récemment eu des soucis avec pycharm qui ne voulait pas se relancer après l'avoir fermé. C'est parce que le programme pycharm ne s'était pas bien arrêté. Donc `ctrl+alt+supr > gestionnaire des taches > processus en arrière plan` et cherchez pycharm. Fermez le et on peut réouvrir le programme.
  

### un python dans wsl et son utilisation dans pycharm

Pour utiliser python sur la wsl, on peut l'installer avec `brew` :

~~~ sh
brew install python3
~~~

Ce qui est chouette avec pycharm, c'est qu'il peut utiliser un interpréteur python distant. Faisons en sorte que le pycharm sous windows utilise l'[interpréteur python de la wsl](https://www.jetbrains.com/help/pycharm/using-wsl-as-a-remote-interpreter.html) :

  - dans un shell wsl tapez `which python3` pour connaître l'emplacement de l'interpréteur python3 (c'est celui de brew que l'on vient d'installer)
  - Ouvrez un projet pycharm existant (le hello world de l'installation d'anacoda par exemple) et allez dans les *file > settings > project interpreter*. Cliquez sur l'engrenage à droite du nom de votre interpreteur :
      1. choisissez wsl (à gauche, c'est le manchot)
      2. choisissez existing environnment puis cliquez sur les *...*
      3. retrouvez le chemin de l'interpréteur de wsl. Le chemin commence forcément par `\\wsl\Debian\`

Une fois que pycharm aura fini d'analyser le nouvel interpréteur, vous pourrez exécuter le fichier.

Vous pouvez même [configurer le terminal](https://www.jetbrains.com/help/pycharm/using-wsl-as-a-remote-interpreter.html#wsl-terminal) pour que ce soit celui du wsl et pas celui de votre windows.

>**odds and ends** :
>
>  - en créant un nouveau projet, ça ne marche pas. Il faut modifier un projet existant. Je ne sais pas pourquoi.

## docker
## virtualbox

## sdkman

# autres
- scoop
- git bash ?


