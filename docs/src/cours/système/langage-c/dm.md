---
layout: layout/post.njk

title: DM

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---


- udefined behaviour simple : <https://www.youtube.com/watch?v=VONnWLo7abU>
- gros exemple : <https://www.youtube.com/watch?v=va_UZwTVR5g>
- utiliser une fonction de hash puis dictionnaire circulaire de knuth
- fonctionnement de malloc avec les blocs libres
- pointeur et cast différents type pour voir la différence. TOu est toujours dépendant du type, uie de l'interprétation
- le C se focalise sur l'utilisation, donc la valeur et son type. C'est pourquoi on écrit `int *p` (la valeur est accédée via un pointeur); et pas `int* p` (un pointeur sur un entier)
- [f() vs f(void)](https://www.youtube.com/watch?v=VsRs0H4hXEE)
- [pointeur sur fonction](https://www.youtube.com/watch?v=axngwDJ79GY)
- [diff entre clone, fork, vfork](https://www.baeldung.com/linux/fork-vfork-exec-clone)
- fork/clone : avec strace : <https://www.youtube.com/watch?v=uRYyj8tcDTE&list=PLhy9gU5W1fvUND_5mdpbNVHC1WCIaABbP&index=17>
- complet : [C et segments mémoires utilisées](https://gist.github.com/CMCDragonkai/10ab53654b2aa6ce55c11cfc5b2432a4)
- [préprocesseur](http://jhnet.co.uk/articles/cpp_magic)
- [timer](https://0xax.gitbooks.io/linux-insides/content/Timers/linux-timers-6.html)
- [une histoire d'amour à sens unix](https://www.cise.ufl.edu/~manuel/obfuscate/westley.hint)
- [ascii art](https://www.welcometothejungle.com/fr/articles/btc-poem-code-avalanche-stars)
- [encore des poèmes](https://code-poetry.com/water)
- memory leak detection : <https://github.com/google/sanitizers/wiki/AddressSanitizer> (<https://clang.llvm.org/docs/AddressSanitizer.html>) pour remplacer <https://valgrind.org/> qui ne marche pas sous ARM.

- [algorithm X](https://en.wikipedia.org/wiki/Knuth%27s_Algorithm_X)
- [listes chaînées intrusives](https://www.data-structures-in-practice.com/intrusive-linked-lists/)
