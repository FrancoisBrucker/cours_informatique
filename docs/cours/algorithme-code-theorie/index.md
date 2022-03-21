---
layout: page
title:  "Algorithme, code et théorie"
category: cours
---

> [Algorithme, code et théorie]({% link cours/algorithme-code-theorie/index.md %})
{: .chemin}

Ce cours montrera l'informatique sous trois aspects complémentaires — théorie, code et algorithmes — que tout [honnête informaticien](https://fr.wikipedia.org/wiki/Honn%C3%AAte_homme) devrait connaître. Il s'adresse à des personnes ayant des connaissances minimales en informatiques mais voulant (ou étant obligé d' :-)) approfondir le sujet.

## prés-requis

Les connaissances et les outils que vous devez avoir pour commencer le cours. Ils sont minimaux.

### un ordinateur pour le développement

Pour développer, il faudra coder et exécuter du code. Il vous faut donc un ordinateur (portable ou tour) en état de marche. Il devra être sous un des trois systèmes d'exploitation suivant : windows 10, macos ou linux.

Vous devez dans l'idéal être administrateur de votre ordinateur et avoir fait [une installation fraîche de tout votre système]({% link _tutoriels/systeme/2021-09-01-installation-ordinateur.md %}) pour éviter toute interférence lors de nos installations.

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

1. [un algorithme ?]({% link cours/algorithme-code-theorie/algorithme/algorithmes.md %})
2. [pseudo-code]({% link cours/algorithme-code-theorie/algorithme/pseudo-code.md %})
3. [complexité max/min]({% link cours/algorithme-code-theorie/algorithme/complexite-max-min.md %})
4. [preuve d'algorithme]({% link cours/algorithme-code-theorie/algorithme/preuve-algorithme.md %})
5. [étude de cas : l'exponentiation]({% link cours/algorithme-code-theorie/algorithme/etude-exponentiation.md %})
6. [complexité en moyenne]({% link cours/algorithme-code-theorie/algorithme/complexite-moyenne.md %})
7. [complexité d'un problème]({% link cours/algorithme-code-theorie/algorithme/complexite-probleme.md %})
8. [étude : mélanger un tableau]({% link cours/algorithme-code-theorie/algorithme/etude-melange.md %})
9. [étude : trier un tableau]({% link cours/algorithme-code-theorie/algorithme/etude-tris.md %})
10. [structure : dictionnaire]({% link cours/algorithme-code-theorie/algorithme/structure-dictionnaire.md %})
11. [structure : liste]({% link cours/algorithme-code-theorie/algorithme/structure-liste.md %})
12. [algorithmes gloutons]({% link cours/algorithme-code-theorie/algorithme/methode-gloutons.md %})
13. [étude : heuristiques gloutonnes]({% link cours/algorithme-code-theorie/algorithme/etude-voyageur-de-commerce.md %})
14. [structure : chaine de caractères]({% link cours/algorithme-code-theorie/algorithme/structure-chaine-de-caracteres.md %})

### théorie

1. [fonctions]({% link cours/algorithme-code-theorie/theorie/fonctions.md %})
2. [Algorithmes, fonctions et pseudo-code]({% link cours/algorithme-code-theorie/theorie/algorithmes-fonctions-pseudo-code.md %})
3. [machines de Turing]({% link cours/algorithme-code-theorie/theorie/machine-turing.md %})
4. [décidabilité]({% link cours/algorithme-code-theorie/theorie/decidabilite.md %})
5. [calculabilité]({% link cours/algorithme-code-theorie/theorie/calculabilite.md %})
6. [fonctions de hash]({% link cours/algorithme-code-theorie/theorie/fonctions-hash.md %})

### code

1. [coder]({% link cours/algorithme-code-theorie/code/coder.md %})
2. [projet informatique]({% link cours/algorithme-code-theorie/code/projet-hello-dev.md %})
3. [projet : pourcentages]({% link cours/algorithme-code-theorie/code/projet-pourcentages.md %})
4. [projet : exponentiation]({% link cours/algorithme-code-theorie/code/projet-exponentiation.md %})
5. [projet : tris]({% link cours/algorithme-code-theorie/code/projet-tris.md %})
6. [mémoire et espace de noms]({% link cours/algorithme-code-theorie/code/memoire-et-espace-noms.md %})
7. [classes et objets]({% link cours/algorithme-code-theorie/code/programmation-objet/classes-et-objets.md %})
8. [composition et agrégation]({% link cours/algorithme-code-theorie/code/programmation-objet/composition-agregation.md %})
9. [projet : composition et agrégation]({% link cours/algorithme-code-theorie/code/programmation-objet/projet-composition-agregation.md %})
10. [héritage]({% link cours/algorithme-code-theorie/code/programmation-objet/heritage.md %})
11. [projet : héritage]({% link cours/algorithme-code-theorie/code/programmation-objet/projet-heritage.md %})
12. [projet : TDD]({% link cours/algorithme-code-theorie/code/programmation-objet/projet-tdd.md %})
13. [projet : programmation événementielle]({% link cours/algorithme-code-theorie/code/projet-programmation-evenementielle.md %})
14. [fichiers]({% link cours/algorithme-code-theorie/code/fichiers.md %})
15. [projet : fichiers]({% link cours/algorithme-code-theorie/code/projet-fichiers.md %})

### autre

Outils, concepts et méthodes utiles pour comprendre le cours

1. [naviguer dans un système de fichiers]({% link _tutoriels/systeme/fichiers-navigation.md %})
2. [installation vscode]({% link _tutoriels/editeur/vsc/vsc-installation-et-prise-en-main.md %}), [installation python]({% link _tutoriels/python/2021-08-20-installation-de-python.md %}) et [vscode & python]({% link _tutoriels/editeur/vsc/2021-09-14-vsc-python.md %})
3. [terminal]({%link _tutoriels/systeme/2021-08-24-terminal.md %}) et [utilisation du terminal]({% link _tutoriels/systeme/2021-12-02-terminal-utilisation.md %})

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
  link: "{% link cours/algorithme-code-theorie/algorithme/index.md %}",
  group: groups.algorithmie,
  root: true,
  fx: 0.1 * width,
  fy: 0.1 * height,
})

graph.nodes.push({
  id: 'Code',
  link: "{% link cours/algorithme-code-theorie/code/index.md %}",
  group: groups.code,
  root: true,
  fx: 0.5 * width,
  fy: 0.1 * height,
})

graph.nodes.push({
  id: 'Théorie',
  link: "{% link cours/algorithme-code-theorie/theorie/index.md %}",
  group: groups.theorie,
  root: true,
  fx: 0.9 * width,
  fy: 0.1 * height,
})

graph.nodes.push({
  id: 'algorithme ?',
  link: "{% link cours/algorithme-code-theorie/algorithme/algorithmes.md %}",
  group: groups.algorithmie
})
graph.links.push({
  source: 'Algorithmie',
  target: 'algorithme ?'
})

graph.nodes.push({
  id: 'pseudo-code',
  link: "{% link cours/algorithme-code-theorie/algorithme/pseudo-code.md %}",
  group: groups.algorithmie
})
graph.links.push({
  source: 'algorithme ?',
  target: 'pseudo-code'
})

graph.nodes.push({
  id: 'coder',
  link: "{% link cours/algorithme-code-theorie/code/coder.md %}",
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
  link: "{% link cours/algorithme-code-theorie/theorie/fonctions.md %}",
  group: groups.theorie
})

graph.links.push({
  source: 'Théorie',
  target: 'fonctions'
})

graph.links.push({
  source: 'algorithme ?',
  target: 'fonctions'
})

graph.nodes.push({
  id: 'Algorithmes, fonctions et pseudo-code',
  link: "{% link cours/algorithme-code-theorie/theorie/algorithmes-fonctions-pseudo-code.md %}",
  group: groups.theorie
})
graph.links.push({
  source: 'fonctions',
  target: 'Algorithmes, fonctions et pseudo-code'
})
graph.links.push({
  source: 'pseudo-code',
  target: 'Algorithmes, fonctions et pseudo-code'
})

graph.nodes.push({
  id: 'machine de Turing',
  link: "{% link cours/algorithme-code-theorie/theorie/machine-turing.md %}",
  group: groups.theorie
})
graph.links.push({
  source: 'fonctions',
  target: 'machine de Turing'
})

graph.nodes.push({
  id: 'décidabilité',
  link: "{% link cours/algorithme-code-theorie/theorie/decidabilite.md %}",
  group: groups.theorie
})

graph.links.push({
  source: 'Algorithmes, fonctions et pseudo-code',
  target: 'décidabilité'
})

graph.nodes.push({
  id: 'calculabilité',
  link: "{% link cours/algorithme-code-theorie/theorie/calculabilite.md %}",
  group: groups.theorie
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
  link: "{% link cours/algorithme-code-theorie/code/projet-hello-dev.md %}",
  group: groups.code
})

graph.links.push({
  source: 'coder',
  target: 'projet informatique'
})

graph.nodes.push({
  id: 'naviguer dans un système de fichiers',
  link: "{% link _tutoriels/systeme/fichiers-navigation.md %}",
  group: groups.autre
})
graph.nodes.push({
  id: 'vscode & python',
  link: "{% link _tutoriels/editeur/vsc/2021-09-14-vsc-python.md %}",
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
  link: "{% link _tutoriels/editeur/vsc/vsc-installation-et-prise-en-main.md %}",
  group: groups.autre
})
graph.nodes.push({
  id: 'installation python',
  link: "{% link _tutoriels/python/2021-08-20-installation-de-python.md %}",
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
  link: "{% link _tutoriels/systeme/2021-08-24-terminal.md %}",
  group: groups.autre
})
graph.nodes.push({
  id: 'utilisation du terminal',
  link: "{% link _tutoriels/systeme/2021-12-02-terminal-utilisation.md %}",
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
  link: "{% link cours/algorithme-code-theorie/code/projet-pourcentages.md %}",
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
  link: "{% link cours/algorithme-code-theorie/algorithme/complexite-max-min.md %}",
  group: groups.algorithmie
})
graph.links.push({
  source: 'pseudo-code',
  target: 'complexité max/min'
})

graph.nodes.push({
  id: "preuve d'algorithme",
  link: "{% link cours/algorithme-code-theorie/algorithme/preuve-algorithme.md %}",
  group: groups.algorithmie
})
graph.links.push({
  source: 'pseudo-code',
  target: "preuve d'algorithme"
})

graph.nodes.push({
  id: "étude : l'exponentiation",
  link: "{% link cours/algorithme-code-theorie/algorithme/etude-exponentiation.md %}",
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
  link: "{% link cours/algorithme-code-theorie/code/projet-exponentiation.md %}",
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
  link: "{% link cours/algorithme-code-theorie/algorithme/complexite-moyenne.md %}",
  group: groups.algorithmie
})

graph.links.push({
  source: 'complexité max/min',
  target: "complexité en moyenne"
})

graph.nodes.push({
  id: "complexité d'un problème",
  link: "{% link cours/algorithme-code-theorie/algorithme/complexite-probleme.md %}",
  group: groups.algorithmie
})

graph.links.push({
  source: "étude : l'exponentiation",
  target: "complexité d'un problème"

})

graph.nodes.push({
  id: "étude : mélanger un tableau",
  link: "{% link cours/algorithme-code-theorie/algorithme/etude-melange.md %}",
  group: groups.algorithmie
})

graph.links.push({
  source: "étude : l'exponentiation",
  target: "étude : mélanger un tableau"

})

graph.nodes.push({
  id: "étude : trier un tableau",
  link: "{% link cours/algorithme-code-theorie/algorithme/etude-tris.md %}",
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
  link: "{% link cours/algorithme-code-theorie/code/projet-tris.md %}",
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
  link: "{% link cours/algorithme-code-theorie/code/memoire-et-espace-noms.md %}",
  group: groups.code
})
graph.links.push({
  source: 'coder',
  target: 'mémoire et espace de noms'
})

graph.nodes.push({
id: "classes et objets",
  link: "{% link cours/algorithme-code-theorie/code/programmation-objet/classes-et-objets.md %}",
  group: groups.code
})

graph.links.push({
  source: "mémoire et espace de noms",
  target: "classes et objets"
})

graph.nodes.push({
id: "composition et agrégation",
  link: "{% link cours/algorithme-code-theorie/code/programmation-objet/composition-agregation.md %}",
  group: groups.code
})

graph.links.push({
  source: "mémoire et espace de noms",
  target: "composition et agrégation"
})

graph.nodes.push({
id: "projet : composition et agrégation",
  link: "{% link cours/algorithme-code-theorie/code/programmation-objet/projet-composition-agregation.md %}",
  group: groups.code
})

graph.links.push({
  source: "composition et agrégation",
  target: "projet : composition et agrégation"
})

graph.nodes.push({
id: "héritage",
  link: "{% link cours/algorithme-code-theorie/code/programmation-objet/heritage.md %}",
  group: groups.code
})

graph.links.push({
  source: "composition et agrégation",
  target: "héritage"
})

graph.nodes.push({
id: "projet : héritage",
  link: "{% link cours/algorithme-code-theorie/code/programmation-objet/projet-heritage.md %}",
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
  link: "{% link cours/algorithme-code-theorie/code/programmation-objet/projet-tdd.md %}",
  group: groups.code
})

graph.links.push({
  source: "projet : héritage",
  target: "projet : TDD"
})

graph.nodes.push({
id: "fonctions de hash",
  link: "{% link cours/algorithme-code-theorie/theorie/fonctions-hash.md %}",
  group: groups.theorie
})

graph.links.push({
  source: 'fonctions',
  target: "fonctions de hash"
})

graph.nodes.push({
id: "structure : dictionnaire",
  link: "{% link cours/algorithme-code-theorie/algorithme/structure-dictionnaire.md %}",
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
  link: "{% link cours/algorithme-code-theorie/algorithme/structure-liste.md %}",
  group: groups.algorithmie
})

graph.links.push({
  source: "complexité en moyenne",
  target: "structure : liste"
})

graph.nodes.push({
id: "structure : chaine de caractères",
  link: "{% link cours/algorithme-code-theorie/algorithme/structure-chaine-de-caracteres.md %}",
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
  link: "{% link cours/algorithme-code-theorie/code/fichiers.md %}",
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
  link: "{% link cours/algorithme-code-theorie/code/projet-programmation-evenementielle.md %}",
  group: groups.code
})

graph.links.push({
  source: "projet : héritage",
  target: "projet : programmation événementielle"
})

graph.nodes.push({
id: "projet : fichiers",
  link: "{% link cours/algorithme-code-theorie/code/projet-fichiers.md %}",
  group: groups.code
})

graph.links.push({
  source: "fichiers",
  target: "projet : fichiers"
})

graph.nodes.push({
id: "algorithmes gloutons",
  link: "{% link cours/algorithme-code-theorie/algorithme/methode-gloutons.md %}",
  group: groups.algorithmie
})

graph.links.push({
  source: "complexité max/min",
  target: "algorithmes gloutons"

})

graph.nodes.push({
id: "étude : voyageur de commerce",
  link: "{% link cours/algorithme-code-theorie/algorithme/etude-voyageur-de-commerce.md %}",
  group: groups.algorithmie
})

graph.links.push({
  source: "algorithmes gloutons",
  target: "étude : voyageur de commerce"
  
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
