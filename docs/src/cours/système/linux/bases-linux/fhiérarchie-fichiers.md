---
layout: layout/post.njk

title: Hiérarchies des fichiers

eleventyNavigation:
    order: 1

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

<https://man.archlinux.org/man/file-hierarchy.7>

```
cd /
ls -la
```

- config `/etc`
- exécutables `/usr/bin`
- bibliothèque `/usr/lib`
- maison :
  - ses fichiers
  - les fichiers de configuration de ses applications
- root `/root` et `etc/shadow`
- `/opt` remplace petit à petit `/usr/local`. op test un fourre tout avec un dossier par app. usr/local est hiérarchisé /bin. lib, etc. C'est un système local
