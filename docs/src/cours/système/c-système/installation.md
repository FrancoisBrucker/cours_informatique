---
layout: layout/post.njk

title: Installation llvm

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---


## Linux/Ubuntu

Fonctionne pour une installation native ou sous wsl.

Copiez coller les paquet à installer de la partie default package de la page : <https://apt.llvm.org/>. N'oubliez pas le `sudo` :

```
sudo apt-get install clang-format clang-tidy clang-tools clang clangd libc++-dev libc++1 libc++abi-dev libc++abi1 libclang-dev libclang1 liblldb-dev libllvm-ocaml-dev libomp-dev libomp5 lld lldb llvm-dev llvm-runtime llvm python3-clang
```

Cela devrait installer tout les paquets nécessaires.

## Macos

1. installer [xcode](https://apps.apple.com/us/app/xcode/id497799835?mt=12)
2. installez les *developper tools* en tapant la commande `xcode-select --install` dans un terminal
3. si vous avez un mac avec une puce arm, il vous faudra peut-être installer Rosetta. Dans un terminal tapez la commande `softwareupdate --install-rosetta`

## Windows 11 Visual Studio

Compilation sous windows.

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
