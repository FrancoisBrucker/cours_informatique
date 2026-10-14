---
layout: layout/post.njk

title: Gestion des erreurs

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---


## Codes d'erreurs

{% lien %}

- [erno](https://www.youtube.com/watch?v=IZiUT-ipnj0){.externe}
- [perror](https://bulkgpt.ai/blog/what-is-perror-in-c-a-guide-to-error-handling-in-c-programming){.externe}.

{% endlien %}

> TBD exemple

## Fuite de mémoire

- <https://valgrind.org/>{.externe} (pas encore sur puce M)
- <https://www.youtube.com/watch?v=bhhDRm926qA>{.externe}

## Tests

- <https://www.youtube.com/watch?v=JarMkGWTF8Y>{.externe}

> TBD

## Debugger

Le debugger de llvm s'appelle [lldb](https://lldb.llvm.org/){.externe}.

- [ce que peut faire un debugger](https://werat.dev/blog/what-a-good-debugger-can-do/){.externe}
- [tutoriel lldb](https://www.youtube.com/watch?v=2GV0K9Y2MKA>){.externe}
- [plugin vscode lldb](https://marketplace.visualstudio.com/items?itemName=vadimcn.vscode-lldb){.externe}
- [lldb pour le reverse engineering](https://rderik.com/blog/using-lldb-for-reverse-engineering/){.externe}
