---
layout: page
title:  "Théorie et pratiques algorithmique"
category: cours
---

> [Théorie et pratiques algorithmique]({% link cours/theorie-pratiques-algorithmique/index.md %})
{: .chemin}

Ce cours montrera l'informatique sous trois aspects complémentaires — théorie, code et algorithmes — que tout [honnête informaticien](https://fr.wikipedia.org/wiki/Honn%C3%AAte_homme) devrait connaître. Il s'adresse à des personnes ayant des connaissances minimales en informatiques mais voulant (ou étant obligé d' :-)) approfondir le sujet.

## prés-requis

Les connaissances et les outils que vous devez avoir pour commencer le cours. Ils sont minimaux.

### un ordinateur pour le développement

Pour développer, il faudra coder et exécuter du code. Il vous faut donc un ordinateur (portable ou tour) en état de marche. Il devra être sous un des trois systèmes d'exploitation suivant : windows 10, macos ou linux.

Vous devez dans l'idéal être administrateur de votre ordinateur et avoir fait [une installation fraîche de tout votre système]({% post_url tutos/systeme/2021-09-01-installation-ordinateur %}) pour éviter toute interférence lors de nos installations.

### connaissances système minimale

* pouvoir ouvrir un explorateur de fichier
* installer un programme avec un installeur

### base d'algorithmie

* savoir coder et exécuter de petits programmes en python :
  * savoir affecter des variables entières, réelles ou sous la forme de chaine de caractères
  * manipulation basique de conteneur comme les listes
  * savoir ce qu'est une fonction, ses paramètres, son code et son retour
* avoir une notion intuitive de ce qu'est un algorithme
  * pouvoir compter le nombre d'opération d'un algorithme simple
  * connaitre le principe de récursivité
* notion de base en mathématiques (niveau lycée)
  * les entiers
  * fonctions et bijections entre ensembles

## parties

Ce cours est composée de trois grandes parties qui s'enchevêtrent.

### algorithmie

1. [un algorithme ?]({% link cours/theorie-pratiques-algorithmique/algorithmie/algorithmes.md %})
2. [pseudo-code]({% link cours/theorie-pratiques-algorithmique/algorithmie/pseudo-code.md %})

### théorie

1. [calcul ?]({% link cours/theorie-pratiques-algorithmique/theorie/calcul.md %})
2. [machines de Turing]({% link cours/theorie-pratiques-algorithmique/theorie/machine-turing.md %})
3. [calculabilité]({% link cours/theorie-pratiques-algorithmique/theorie/calculabilite.md %})

### coder

1. [code]({% link cours/theorie-pratiques-algorithmique/coder/code.md %})

## TBD

* connaitre les bases d'un système d'exploitation, [les fichiers et les dossiers]({% post_url tutos/systeme/2021-08-24-fichiers-navigation %})
* avoir accès à un [terminal]({% post_url tutos/systeme/2021-08-24-terminal %})

## structure

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
  // data
var graph = {
  nodes: [],
  links: []
}

var groups = {
  theorie: 1,
  algorithmie: 2,
  code: 3,
  autre: 4,
}

graph.nodes.push({
  id: 'Algorithmie',
  link: "{% link cours/theorie-pratiques-algorithmique/algorithmie/index.md %}",
  group: groups.algorithmie,
  root: true,
  fx: 0.1 * width,
  fy: 0.1 * height,
})

graph.nodes.push({
  id: 'Coder',
  link: "{% link cours/theorie-pratiques-algorithmique/coder/index.md %}",
  group: groups.code,
  root: true,
  fx: 0.5 * width,
  fy: 0.1 * height,
})

graph.nodes.push({
  id: 'Théorie',
  link: "{% link cours/theorie-pratiques-algorithmique/theorie/index.md %}",
  group: groups.theorie,
  root: true,
  fx: 0.9 * width,
  fy: 0.1 * height,
})

graph.nodes.push({
  id: 'algorithme ?',
  link: "{% link cours/theorie-pratiques-algorithmique/algorithmie/algorithmes.md %}",
  group: groups.algorithmie
})
graph.links.push({
  source: 'Algorithmie',
  target: 'algorithme ?'
})

graph.nodes.push({
  id: 'pseudo-code',
  link: "{% link cours/theorie-pratiques-algorithmique/algorithmie/pseudo-code.md %}",
  group: groups.algorithmie
})
graph.links.push({
  source: 'algorithme ?',
  target: 'pseudo-code'
})

graph.nodes.push({
  id: 'code',
  link: "{% link cours/theorie-pratiques-algorithmique/coder/code.md %}",
  group: groups.code
})
graph.links.push({
  source: 'Coder',
  target: 'code'
})

graph.links.push({
  source: 'pseudo-code',
  target: 'code'
})

graph.nodes.push({
  id: 'calcul ?',
  link: "{% link cours/theorie-pratiques-algorithmique/theorie/calcul.md %}",
  group: groups.theorie
})
graph.links.push({
  source: 'Théorie',
  target: 'calcul ?'
})
graph.links.push({
  source: 'pseudo-code',
  target: 'calcul ?'
})

graph.nodes.push({
  id: 'machine de Turing',
  link: "{% link cours/theorie-pratiques-algorithmique/theorie/machine-turing.md %}",
  group: groups.theorie
})
graph.links.push({
  source: 'calcul ?',
  target: 'machine de Turing'
})

graph.nodes.push({
  id: 'projet informatique',
  link: "{% link cours/theorie-pratiques-algorithmique/coder/code-projet.md %}",
  group: groups.code
})
graph.links.push({
  source: 'code',
  target: 'projet informatique'
})

graph.nodes.push({
  id: 'vscode & python',
  link: "{% post_url tutos/editeur/vsc/2021-09-14-vsc-python %}",
  group: groups.autre
})
graph.links.push({
  source: 'vscode & python',
  target: 'projet informatique'
})

graph.nodes.push({
  id: 'installation vscode',
  link: "{% post_url tutos/editeur/vsc/2021-09-03-vsc-installation-et-prise-en-main %}",
  group: groups.autre
})
graph.nodes.push({
  id: 'installation python',
  link: "{% post_url tutos/python/2021-08-20-installation-de-python %}",
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
  id: 'naviguer dans un système de fichiers',
  link: "{% post_url tutos/systeme/2021-08-24-fichiers-navigation %}",
  group: groups.autre
})
graph.nodes.push({
  id: 'projet 1 : pourcentages',
  link: "{% link cours/theorie-pratiques-algorithmique/coder/projet-1-pourcentages.md %}",
  group: groups.code
})
graph.links.push({
  source: 'projet informatique',
  target: 'projet 1 : pourcentages'
})
graph.links.push({
  source: 'naviguer dans un système de fichiers',
  target: 'projet 1 : pourcentages'
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
