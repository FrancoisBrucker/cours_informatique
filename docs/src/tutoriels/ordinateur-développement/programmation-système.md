---
layout: layout/post.njk

title: Système Mac

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

## mac

1. installer [xcode](https://apps.apple.com/us/app/xcode/id497799835?mt=12)
2. installez les *developper tools* en tapant la commande `xcode-select --install` dans un terminal
3. installez [docker desktop](https://www.docker.com/)
4. si vous avez un mac avec une puce arm, il vous faudra peut-être installer Rosetta. Dans un terminal tapez la commande `softwareupdate --install-rosetta`

## Tutos linux

* windows powershell : <https://docs.microsoft.com/fr-fr/powershell/scripting/overview?view=powershell-7.1>
* l'application terminal sous mac : <https://support.apple.com/fr-fr/guide/terminal/welcome/mac>


## Windows 11 et wsl


1. vscode installation. `Terminal > Nouveau terminal` et vérifier que c'est bien un powershell
2. ssh
   1. <https://davidaugustat.com/windows/windows-11-setup-ssh>
   2. old w10 : https://learn.microsoft.com/fr-fr/windows-server/administration/openssh/openssh_keymanagement
3. git : <https://git-scm.com/download/win> :
   * installation 64 bit
   * choisissez [notepad++](https://notepad-plus-plus.org/) comme éditeur par défaut (installez le au préalable si nécessaire)
   * "default behaviour of git pull" : rebase
4. wsl install.
   5. 
   7. ssh sous wsl. Il faut juste configurer l'agent pour qu'il se lance au démarrage. À la fin de .profile, ajoutez : [ajout ssh-agent](https://gist.github.com/gabetax/3756756)
5. [docker](https://learn.microsoft.com/fr-fr/windows/wsl/tutorials/wsl-containers)
6. Installation d'une machine virtuelle
   1. téléchargez la dernière version de [virtual box](https://www.virtualbox.org/).
   2. Installez le logiciel. N'installez pas le support python, ce n'est pas nécessaire.


### clang/llvm sous wsl

Dans wsl, installation de compilateurs C, avec llvm/clang.

Copiez coller les paquet à installer de la partie default package de la page : <https://apt.llvm.org/>. N'oubliez pas le `sudo` :

```
sudo apt-get install clang-format clang-tidy clang-tools clang clangd libc++-dev libc++1 libc++abi-dev libc++abi1 libclang-dev libclang1 liblldb-dev libllvm-ocaml-dev libomp-dev libomp5 lld lldb llvm-dev llvm-runtime llvm python3-clang
```

Cela devrait installer tout les paquets nécessaires.

### visual studio

compilation sous windows.

* <https://visualstudio.microsoft.com/fr/> et téléchargez la version 2022 community
* lors de l'installation, choisissez `développement desktop en C++` et cochez également `Outils C++ Clang pour windows`

Ceci installera les différents programmes dans le dossier d'installation de visual studio :

`%VCINSTALLDIR%\Tools\Llvm\bin\ and %VCINSTALLDIR%\Tools\Llvm\x64\bin\` (voir [cette documentation](https://learn.microsoft.com/en-us/cpp/build/clang-support-msbuild?view=msvc-170))

Chez moi, `%VCINSTALLDIR%` vaut : `c:\Program Files\Microsoft\Visual Studio\2022\Community\VC`

On peut alors compiler un programme comme ça :

`c:\Program Files\Microsoft Visual Studio\2022\Community\VCTools\Llvm\bin\ and %VCINSTALLDIR%\Tools\Llvm\x64\bin\clang main.c`

Ou ajouter le chemin au PATH : <https://lecrabeinfo.net/modifier-le-path-de-windows-ajouter-un-dossier-au-path.html>

{% attention %}
Ne pas oublier de cliquer OK partout, sinon ce n'est pas sauvegardé.
{% endattention %}
