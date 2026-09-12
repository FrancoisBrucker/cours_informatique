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

- [erno](https://www.youtube.com/watch?v=IZiUT-ipnj0)
- [perror](https://bulkgpt.ai/blog/what-is-perror-in-c-a-guide-to-error-handling-in-c-programming).

{% endlien %}

> TBD exemple

## Fuite de mémoire

- <https://valgrind.org/> (pas encore sur puce M)
- <https://www.youtube.com/watch?v=bhhDRm926qA>

## Tests

- <https://www.youtube.com/watch?v=JarMkGWTF8Y>

> TBD

## Debugger

Le debugger de llvm s'appelle [lldb](https://lldb.llvm.org/).

- [ce que peut faire un debugger](https://werat.dev/blog/what-a-good-debugger-can-do/)
- [tutoriel lldb](https://www.youtube.com/watch?v=2GV0K9Y2MKA>)
- [plugin vscode lldb](https://marketplace.visualstudio.com/items?itemName=vadimcn.vscode-lldb)
- [lldb pour le reverse engineering](https://rderik.com/blog/using-lldb-for-reverse-engineering/)
