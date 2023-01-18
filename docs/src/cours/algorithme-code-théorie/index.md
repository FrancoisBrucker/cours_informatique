---
layout: layout/post.njk

title: Algorithme, code et théorie
authors:
    - François Brucker

tags: ['cours', 'algorithmie', 'code', 'théorie']

eleventyNavigation:
  key: "Algorithme, code et théorie"
  parent: Cours

prerequis:
    - "/cours/base-code/"
---

<!-- début résumé -->

Ce cours montrera l'informatique sous trois aspects complémentaires — théorie, code et algorithmes — que tout [honnête informaticien](https://fr.wikipedia.org/wiki/Honn%C3%AAte_homme) devrait connaître. Il s'adresse à des personnes ayant des connaissances minimales en informatiques mais voulant (ou étant obligé d' :-)) approfondir le sujet.

<!-- fin résumé -->

> TBD : refaire l'ordre. Il y a des changements avec le cours objet de l'ec casa.

## Prérequis

Les connaissances et les outils que vous devez avoir pour commencer le cours. Ils sont minimaux :

* vous allez coder. Et beaucoup. Pour cela, il faut que vous ayez un ordinateur configuré pour le faire.
* connaissances système :
  * pouvoir ouvrir un explorateur de fichier
  * installer un programme avec un installeur

{% faire "**indispensable !**" %}
Faites une installation fraîche de votre système en suivant ce tutoriel : [Nouvelle installation de son système]({{ "/tutoriels/installation-système" | url }}).
{% endfaire %}

## Parties

Ce cours est composé de trois grandes parties qui s'enchevêtrent.


<div>
<script>
tree = {{ collections.all | eleventyNavigation | dump | safe }}
</script>  
</div>


<div>
<script>
console.log(tree)
</script>  
</div>


<div>
  <script>
  var graph = {
    nodes: [],
    links: []
  }
  var groups = {
    théorie: 1,
    algorithmie: 2,
    code: 3,
    autre: 4,
  }
  </script>
</div>


### Algorithmie

1. [un algorithme ?](algorithme/définition)
2. [pseudo-code](algorithme/pseudo-code)
3. [preuve d'algorithme](algorithme/preuve-algorithme)
4. [complexité max/min](algorithme/complexité-max-min)
5. [étude de cas : l'exponentiation](algorithme/étude-exponentiation)
6. [étude : mélanger un tableau](algorithme/étude-mélange)
7. [complexité en moyenne](algorithme/complexité-moyenne)
8. [étude : trier un tableau](algorithme/étude-tris)
9. [structure : liste](algorithme/structure-liste)
10. [structure : dictionnaire](algorithme/structure-dictionnaire)
11. [algorithmes gloutons](algorithme/algorithmes-gloutons)
12. [étude : voyageur de commerce](algorithme/etude-voyageur-de-commerce)
13. [structure : chaîne de caractères](algorithme/structure-chaîne-de-caractères)
14. [étude : recherche de sous-chaines](algorithme/etude-recherche-sous-chaines)
15. [étude : alignement de séquences](algorithme/étude-alignement-séquences)

### Théorie

1. [fonctions](théorie/fonctions)
2. [complexité d'un problème](théorie/complexité-problème)
3. [fonctions de hash](théorie/fonctions-hash)
4. [machines de Turing](théorie/machine-turing)
5. [décidabilité](théorie/decidabilite)
6. [calculabilité](théorie/calculabilite)

### Code

1. [coder](code/coder)
2. [projet informatique](code/projet-hello-dev)
3. [projet : pourcentages](code/projet-pourcentages)
4. [projet : exponentiation](code/projet-exponentiation)
5. [projet : tris](code/projet-tris)
6. [mémoire et espace de noms](code/mémoire-espace-noms)
7. [programmation objet](code/programmation-objet/)
   1. [classes et objets](code/programmation-objet/classes-et-objets)
   2. [coder ses objets](code/programmation-objet/coder-ses-objets)
   3. [projet : coder ses objets](code/programmation-objet/projet-code-objets)
   4. [composition et agrégation](code/programmation-objet/composition-agrégation)
   5. [projet : composition et agrégation](code/programmation-objet/projet-composition-agrégation)
   6. [héritage](code/programmation-objet/héritage)
   7. [projet : héritage](code/programmation-objet/projet-héritage)
   8. [projet : TDD](code/programmation-objet/projet-tdd)
   9. [projet : programmation événementielle](code/projet-programmation-évènementielle)
8. [fichiers](code/fichiers)
9. [projet : fichiers](code/projet-fichiers)
10. [projet : alignement de séquences](code/projet-alignement-séquences)

## Structure

<div id="graph">
  <style>
  .links line {
    stroke: #999;
    stroke-opacity: 0.6;
    stroke-width: 1px;
    marker-end: url(#end-arrow);
  }
  .nodes circle {
    stroke: #fff;
    stroke-width: 1.5px;
  }
  text {
    font-family: sans-serif;
  }
  </style>
  <svg id="dessin" style="width:100%;"></svg>
</div>

<script src="https://d3js.org/d3.v7.min.js"></script>

<script>
var svg = d3.select('#dessin');

var width = svg.node().getBoundingClientRect().width,
    height = width

svg.style("height", height)
</script>

<script>

graph.nodes.push({
  id: 'Algorithmie',
  link: "algorithme",
  group: groups.algorithmie,
  root: true,
  fx: 0.1 *width,
fy: 0.1* height,
})

graph.nodes.push({
  id: 'Code',
  link: "code",
  group: groups.code,
  root: true,
  fx: 0.5 *width,
fy: 0.1* height,
})

graph.nodes.push({
  id: 'Théorie',
  link: "théorie",
  group: groups.théorie,
  root: true,
  fx: 0.9 *width,
fy: 0.1* height,
})

graph.nodes.push({
  id: 'algorithme ?',
  link: "algorithme/définition",
  group: groups.algorithmie
})
graph.links.push({
  source: 'Algorithmie',
  target: 'algorithme ?'
})

graph.nodes.push({
  id: 'pseudo-code',
  link: "algorithme/pseudo-code",
  group: groups.algorithmie
})
graph.links.push({
  source: 'algorithme ?',
  target: 'pseudo-code'
})

graph.nodes.push({
  id: 'coder',
  link: "code/coder",
  group: groups.code
})
graph.links.push({
  source: 'Code',
  target: 'coder'
})

graph.links.push({
  source: 'pseudo-code',
  target: 'coder'
})

graph.nodes.push({
  id: 'fonctions',
  link: "théorie/fonctions",
  group: groups.théorie
})

graph.links.push({
  source: 'Théorie',
  target: 'fonctions'
})

graph.links.push({
  source: 'pseudo-code',
  target: 'fonctions'
})

graph.nodes.push({
  id: 'machine de Turing',
  link: "théorie/machine-turing",
  group: groups.théorie
})
graph.links.push({
  source: 'fonctions',
  target: 'machine de Turing'
})

graph.nodes.push({
  id: 'décidabilité',
  link: "théorie/decidabilite",
  group: groups.théorie
})

graph.links.push({
  source: 'fonctions',
  target: 'décidabilité'
})

graph.nodes.push({
  id: 'calculabilité',
  link: "théorie/calculabilite",
  group: groups.théorie
})
graph.links.push({
  source: 'machine de Turing',
  target: 'calculabilité'
})

graph.links.push({
  source: 'décidabilité',
  target: 'calculabilité'
})

graph.nodes.push({
  id: 'projet informatique',
  link: "code/projet-hello-dev",
  group: groups.code
})

graph.links.push({
  source: 'coder',
  target: 'projet informatique'
})

graph.nodes.push({
  id: 'naviguer dans un système de fichiers',
  link: '{{ "/tutoriels/fichiers-navigation" | url }}',
  group: groups.autre
})
graph.nodes.push({
  id: 'vscode & python',
  link: '{{ "/tutoriels/vsc-python" | url }}',
  group: groups.autre
})
graph.links.push({
  source: 'vscode & python',
  target: 'projet informatique'
})
graph.links.push({
  source: 'naviguer dans un système de fichiers',
  target: 'projet informatique'
})

graph.nodes.push({
  id: 'installation vscode',
  link: '{{ "/tutoriels/vsc-installation-et-prise-en-main" | url }}',
  group: groups.autre
})
graph.nodes.push({
  id: 'installation python',
  link: '{{ "/tutoriels/installation-de-python" | url }}',
  group: groups.autre
})
graph.links.push({
  source: 'installation vscode',
  target: 'vscode & python'
})
graph.links.push({
  source: 'installation python',
  target: 'vscode & python'
})

graph.nodes.push({
  id: 'terminal',
  link:'{{ "/tutoriels/terminal" | url }}',
  group: groups.autre
})
graph.nodes.push({
  id: 'utilisation du terminal',
  link: '{{ "/tutoriels/terminal-utilisation" | url }}',
  group: groups.autre
})
graph.links.push({
  source: 'naviguer dans un système de fichiers',
  target: 'terminal'
})
graph.links.push({
  source: 'terminal',
  target: 'utilisation du terminal'
})

graph.nodes.push({
  id: 'projet : pourcentages',
  link: "code/projet-pourcentages",
  group: groups.code
})
graph.links.push({
  source: 'projet informatique',
  target: 'projet : pourcentages'
})
graph.links.push({
  source: 'utilisation du terminal',
  target: 'projet : pourcentages'
})

graph.nodes.push({
  id: 'complexité max/min',
  link: "algorithme/complexité-max-min",
  group: groups.algorithmie
})
graph.links.push({
  source: 'pseudo-code',
  target: 'complexité max/min'
})

graph.nodes.push({
  id: "preuve d'algorithme",
  link: "algorithme/preuve-algorithme",
  group: groups.algorithmie
})
graph.links.push({
  source: 'pseudo-code',
  target: "preuve d'algorithme"
})

graph.nodes.push({
  id: "étude : l'exponentiation",
  link: "algorithme/étude-exponentiation",
  group: groups.algorithmie
})
graph.links.push({
  source: "preuve d'algorithme",
  target: "étude : l'exponentiation"
})

graph.links.push({
  source: 'complexité max/min',
  target: "étude : l'exponentiation"
})

graph.nodes.push({
  id: "projet : exponentiation",
  link: "code/projet-exponentiation",
  group: groups.code
})

graph.links.push({
  source: "étude : l'exponentiation",
  target: "projet : exponentiation"
})

graph.links.push({
  source: 'projet : pourcentages',
  target: "projet : exponentiation"
})

graph.nodes.push({
  id: "complexité en moyenne",
  link: "algorithme/complexité-moyenne",
  group: groups.algorithmie
})

graph.links.push({
  source: 'complexité max/min',
  target: "complexité en moyenne"
})

graph.nodes.push({
  id: "complexité d'un problème",
  link: "algorithme/complexité-problème",
  group: groups.théorie
})

graph.links.push({
  source: "étude : l'exponentiation",
  target: "complexité d'un problème"

})

graph.nodes.push({
  id: "étude : mélanger un tableau",
  link: "algorithme/étude-mélange",
  group: groups.algorithmie
})

graph.links.push({
  source: "étude : l'exponentiation",
  target: "étude : mélanger un tableau"

})

graph.nodes.push({
  id: "étude : trier un tableau",
  link: "algorithme/étude-tris",
  group: groups.algorithmie
})

graph.links.push({
  source: "complexité d'un problème",
  target: "étude : trier un tableau"
})

graph.links.push({
  source: "étude : mélanger un tableau",
  target: "étude : trier un tableau"
})

graph.links.push({
  source: "complexité en moyenne",
  target: "étude : trier un tableau"
})

graph.nodes.push({
  id: "projet : les tris",
  link: "code/projet-tris",
  group: groups.code
})

graph.links.push({
  source: "étude : trier un tableau",
  target: "projet : les tris"
})

graph.links.push({
  source: "projet : exponentiation",
  target: "projet : les tris"
})

graph.nodes.push({
  id: 'mémoire et espace de noms',
  link: "code/mémoire-espace-noms",
  group: groups.code
})
graph.links.push({
  source: 'coder',
  target: 'mémoire et espace de noms'
})

graph.nodes.push({
id: "classes et objets",
  link: "code/programmation-objet/classes-et-objets",
  group: groups.code
})

graph.links.push({
  source: "mémoire et espace de noms",
  target: "classes et objets"
})

graph.nodes.push({
id: "composition et agrégation",
  link: "code/programmation-objet/composition-agrégation",
  group: groups.code
})

graph.links.push({
  source: "mémoire et espace de noms",
  target: "composition et agrégation"
})

graph.nodes.push({
id: "projet : composition et agrégation",
  link: "code/programmation-objet/projet-composition-agrégation",
  group: groups.code
})

graph.links.push({
  source: "composition et agrégation",
  target: "projet : composition et agrégation"
})

graph.nodes.push({
id: "héritage",
  link: "code/programmation-objet/héritage",
  group: groups.code
})

graph.links.push({
  source: "composition et agrégation",
  target: "héritage"
})

graph.nodes.push({
id: "projet : héritage",
  link: "code/programmation-objet/projet-héritage",
  group: groups.code
})

graph.links.push({
  source: "héritage",
  target: "projet : héritage"
})

graph.links.push({
  source: "projet : composition et agrégation",
  target: "projet : héritage"
})

graph.nodes.push({
id: "projet : TDD",
  link: "code/programmation-objet/projet-tdd",
  group: groups.code
})

graph.links.push({
  source: "projet : héritage",
  target: "projet : TDD"
})

graph.nodes.push({
id: "fonctions de hash",
  link: "théorie/fonctions-hash",
  group: groups.théorie
})

graph.links.push({
  source: 'fonctions',
  target: "fonctions de hash"
})

graph.nodes.push({
id: "structure : dictionnaire",
  link: "algorithme/structure-dictionnaire",
  group: groups.algorithmie
})

graph.links.push({
  source: "fonctions de hash",
  target: "structure : dictionnaire"
})

graph.links.push({
  source: "complexité en moyenne",
  target: "structure : dictionnaire"
})

graph.nodes.push({
id: "structure : liste",
  link: "algorithme/structure-liste",
  group: groups.algorithmie
})

graph.links.push({
  source: "complexité en moyenne",
  target: "structure : liste"
})

graph.nodes.push({
id: "structure : chaine de caractères",
  link: "algorithme/structure-chaîne-de-caractères",
  group: groups.algorithmie
})

graph.links.push({
  source: "Algorithmie",
  target: "structure : chaine de caractères"
})

graph.links.push({
  source: "mémoire et espace de noms",
  target: "structure : chaine de caractères"
})

graph.nodes.push({
id: "fichiers",
  link: "code/fichiers",
  group: groups.code
})

graph.links.push({
  source: "Code",
  target: "fichiers"
})

graph.links.push({
  source: "structure : chaine de caractères",
  target: "fichiers"
})

graph.links.push({
  source: "naviguer dans un système de fichiers",
  target: "fichiers"
})

graph.links.push({
  source: "structure : dictionnaire",
  target: "fichiers"
})

graph.nodes.push({
id: "projet : programmation événementielle",
  link: "code/projet-programmation-évènementielle",
  group: groups.code
})

graph.links.push({
  source: "projet : héritage",
  target: "projet : programmation événementielle"
})

graph.nodes.push({
id: "projet : fichiers",
  link: "code/projet-fichiers",
  group: groups.code
})

graph.links.push({
  source: "fichiers",
  target: "projet : fichiers"
})

graph.nodes.push({
id: "algorithmes gloutons",
  link: "algorithme/algorithmes-gloutons",
  group: groups.algorithmie
})

graph.links.push({
  source: "complexité max/min",
  target: "algorithmes gloutons"

})

graph.nodes.push({
id: "étude : voyageur de commerce",
  link: "algorithme/etude-voyageur-de-commerce",
  group: groups.algorithmie
})

graph.links.push({
  source: "algorithmes gloutons",
  target: "étude : voyageur de commerce"
  
})

graph.links.push({
  source: "projet : exponentiation",
  target: "étude : voyageur de commerce"
  
})

graph.nodes.push({
id: "étude : recherche de sous-chaines",
  link: "algorithme/etude-recherche-sous-chaines",
  group: groups.algorithmie
})

graph.links.push({
  source: "structure : chaine de caractères",
  target: "étude : recherche de sous-chaines",
})

graph.links.push({
  source: "complexité en moyenne",
  target: "étude : recherche de sous-chaines",
})

graph.links.push({
  source: "fonctions de hash",
  target: "étude : recherche de sous-chaines",
})

graph.nodes.push({
id: "étude : alignement de séquences",
  link: "algorithme/étude-alignement-séquences",
  group: groups.algorithmie
})

graph.links.push({
  source: "étude : recherche de sous-chaines",
  target: "étude : alignement de séquences",
})

graph.nodes.push({
id: "projet : alignement de séquences",
  link: "code/projet-alignement-séquences",
  group: groups.code
})

graph.links.push({
  source: "étude : alignement de séquences",
  target: "projet : alignement de séquences",
})

graph.links.push({
  source: "projet : fichiers",
  target: "projet : alignement de séquences",
})

graph.links.push({
  source: "héritage",
  target: "projet : alignement de séquences",
})

</script>
<script>
var color = d3.scaleOrdinal(d3.schemeCategory10);

svg.append("rect")
    .attr("width", "100%")
    .attr("height", "100%")
    .attr("fill", "#EEE6FA");

// define arrow markers for graph links
svg.append("svg:defs").append("svg:marker")
  .attr("id", "end-arrow")
  .attr("viewBox", "0 -5 20 10")
  .attr("refX", 25)
  .attr("markerWidth", 20)
  .attr("markerHeight", 20)
  .attr("orient", "auto")
  .append("svg:path")
  .attr("d", "M0,-5L20,0L0,5")
  .attr("fill", "#000");

var simulation = d3.forceSimulation()
    .force("link", d3.forceLink().id(d => { return d.id; }))
    .force("charge", d3.forceManyBody().strength(-100))
    .force("center", d3.forceCenter(width / 2, height / 2));

var link = svg.append("g")
    .attr("class", "links")
    .selectAll("line")
    .data(graph.links)
    .enter().append("line");

  var node = svg.append("g")
    .attr("class", "nodes")
    .selectAll("g")
    .data(graph.nodes)
    .enter().append("g")
    .attr("fx", d => {return d.fx})
    .attr("fy", d => {return d.fy})

  node.append("a")
    .attr("xlink:href", d => { return d.link})
    .append("circle")
    .attr("r", 5)
    .attr("fill", function(d) { return color(d.group); })

  node.append("a")
    .attr("xlink:href", d => { return d.link})
    .append("text")
      .text(function(d) {
        return d.id;
      })
      .attr('x', 6)
      .attr('y', 3)
      .style('fill', d => { if (d.root) {return color(d.group)} else { return 'black'}})

  // Create a drag handler and append it to the node object instead
  var drag_handler = d3.drag()
      .on("start", dragstarted)
      .on("drag", dragged)
      .on("end", dragended)

  drag_handler(node);
  
  node.on("click", clicked);

  simulation
      .nodes(graph.nodes)
      .on("tick", ticked);

  simulation.force("link")
      .links(graph.links);

  function ticked() {
    link
        .attr("x1", function(d) { return d.source.x; })
        .attr("y1", function(d) { return d.source.y; })
        .attr("x2", function(d) { return d.target.x; })
        .attr("y2", function(d) { return d.target.y; });

    radius = 15;
    node
        .attr("transform", (d) => {
          d.x = Math.max(radius, Math.min(width - radius, d.x))
          d.y = Math.max(radius, Math.min(height - radius, d.y))
          return "translate(" + d.x + "," + d.y + ")";
        })
  }

  function dragstarted(event, d) {
    if (!event.active) simulation.alphaTarget(0.3).restart();
    d.fx = d.x;
    d.fy = d.y;
  }

  function dragged(event, d) {
    d.fx = event.x;
    d.fy = event.y;
  }

  function dragended(event, d) {
    // if (!event.active) simulation.alphaTarget(0);
    d.fx = Math.max(0, d.fx);
    d.fx = Math.min(width, d.fx);

    d.fy = Math.max(0, d.fy);
    d.fy = Math.min(height, d.fy);
  }
  function clicked(event, d) {
    console.log(d)
  }

</script>
