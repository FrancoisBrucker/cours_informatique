---
layout: layout/post.njk

title: Golang

eleventyNavigation:
  prerequis:
    - "/cours/coder-et-développer/programmation-objet/"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

> TBD à rendre propre.

{% lien %}
[Le langage Go](https://go.dev/)
{% endlien %}

On suppose que vous connaissez le python et la programmation objet. Pour l'instant juste des notes de lectures.

1. <https://go.dev/doc/>
2. installation :
   1. Macos : <https://formulae.brew.sh/formula/go>
   2. Windows : <https://winstall.app/apps/GoLang.Go>
   3. Linux :
      1. `sudo apt-get update && sudo apt-get -y install golang-go`
      2. <https://go.dev/wiki/Ubuntu>
   4. par défaut : <https://go.dev/doc/install>
3. vscode :
   1. plugin de go : <https://marketplace.visualstudio.com/items?itemName=golang.Go>
   2. changer des paramètres sinon c'est trop énervant. Aller dans [la palette de commande](https://code.visualstudio.com/api/references/contribution-points#contributes.commands) (affichage > palette de commande) puis tapez `preferences: Open User Settings (JSON)`. Ajoutez les paramètres suivant pour go :

     ```
     "gopls": {
       "ui.semanticTokens": true 
     },
     "[go]": {
         "editor.formatOnSave": true,
         "editor.codeActionsOnSave": {
             "source.organizeImports": false
     }
     ```

4. Faire le tuto : <https://go.dev/doc/tutorial/getting-started>. Il vous apprendra à :
   - écrire du code
   - faire un module
   - importer un module
5. Faire le go tour <https://go.dev/tour/>. Base du langage
6. Faire un cours de go venant de python. Pourquoi ne pas utiliser les videos suivantes comme base :
   - <https://www.alexedwards.net/blog/when-is-it-ok-to-panic-in-go>
   - <https://www.youtube.com/watch?v=e8zL5PD8164&t=160s>
   - <https://www.youtube.com/watch?v=WVjc_wl17FA&list=PLNsqkiNPwf2dS-6VirsO1FJNhu2XbjbkT&index=1>
   - <https://www.youtube.com/watch?v=P7dCWOjRwJA&list=PL10piHcP2kVJOxO18iPHsq8IqTArbvFe0>
7. <https://go.dev/doc/effective_go>
8. <https://gobyexample.com/>
9.  Dépendances :
   - <https://go.dev/doc/modules/managing-source>
   - <https://go.dev/doc/modules/layout>
   - <https://go.dev/doc/modules/managing-dependencies>
10. Modules standards : <https://pkg.go.dev/std>
11. tests :
    - <https://speedscale.com/blog/golang-testing-frameworks-for-every-type-of-test/>
    - <https://github.com/stretchr/testify>
    - <https://www.youtube.com/watch?v=A1eR7TxeGcE&list=PLNsqkiNPwf2c2kf01I_Fh_GdT0MywkD-0&index=1>
12. TDD avec go : <https://quii.gitbook.io/learn-go-with-tests>
    1. prendre la version anglaise. La française est truffée de fautes et la traduction est souvent bancale
    2. le début est facile. La fin est trop dure et spécifique
    3. il faudrait reprendre le début avec les ajouts de la lib de test (coverage, exemple, etc) dans un tuto.
13. specs. Très utiles. Ca vaut vraiment le coup de les lire :
    - modules : <https://go.dev/ref/mod>
    - langage : <https://go.dev/ref/spec>

- Basé sur des manipulations de structures de données. Fait pour être simple à lire.
Pas d'héritage (comme tout les nouveaux langages), mais les <https://gobyexample.com/struct-embedding> permettent d'en garder le bénéfice sans les problèmes.<https://www.youtube.com/watch?v=6Vt0xvaDs4I>
- interface = pointeur. Comme en python. Est-ce copié ?

> TBD go + webassembly ? <https://go.dev/wiki/WebAssembly>, <https://go.dev/blog/wasmexport> et <https://golangbot.com/webassembly-using-go/>
> TBD socket : <https://www.kelche.co/blog/go/socket-programming/>
## Test

{% lien %}
<https://pkg.go.dev/testing>
{% endlien %}

- `go test .`
- `go test . -v`

### Exemples

{% lien %}
<https://go.dev/blog/examples>
{% endlien %}

### Benchmark

{% lien %}
<https://pkg.go.dev/testing#hdr-Benchmarks>
{% endlien %}

```shell
go test ./graph -bench=./graph
```

### Coverage

{% lien %}
<https://go.dev/blog/cover>
{% endlien %}

```shell
> go test ./graph -cover
❯ go test ./diss -cover -coverprofile=coverage.out
❯ go tool cover  -html=coverage.out
```

<https://www.youtube.com/watch?v=3ilxk24hzyA>

### Fuzztest

> TBD

### Testify

{% lien %}
<https://github.com/stretchr/testify>
{% endlien %}
