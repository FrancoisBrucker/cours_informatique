---
layout: layout/post.njk

title: Algorithme, code et théorie
tags: ['cours', 'algorithmie', 'code', 'théorie']
authors:
    - François Brucker

eleventyNavigation:
    prerequis:
        - "/cours/coder-en-python/"

eleventyComputed:
    eleventyNavigation:
        key: "{{ page.url }}"
        title: "{{ title | safe }}"
        parent: Cours

---

<!-- début résumé -->

Ce cours montrera l'informatique sous trois aspects complémentaires — théorie, code et algorithmes — que tout [honnête informaticien](https://fr.wikipedia.org/wiki/Honn%C3%AAte_homme) devrait connaître. Il s'adresse à des personnes ayant des connaissances minimales en informatiques mais voulant (ou étant obligé d' :-)) approfondir le sujet.

<!-- fin résumé -->

## Prérequis

Les connaissances et les outils que vous devez avoir pour commencer le cours. Ils sont minimaux :

* vous allez coder. Et beaucoup. Pour cela, il faut que vous ayez un ordinateur configuré pour le faire.
* connaissances système :
  * pouvoir ouvrir un explorateur de fichier
  * installer un programme avec un installeur

{% faire "**indispensable !**" %}
Faites une installation fraîche de votre système en suivant ce tutoriel : [Nouvelle installation de son système]({{ "/tutoriels/installation-système"  }}).
{% endfaire %}

## Parties

Ce cours est composé de trois grandes parties qui s'enchevêtrent.

{{ collections.all | eleventyNavigation(eleventyNavigation.key) | eleventyNavigationToMarkdown() | safe }}

## Structure

<script>

function create_graph(tree) {
  G = {}
  for (root of tree) {
    add_nodes(G, root)
  }

  for (root of tree) {
    add_edges(G, root)
  }

  return G;
}

function add_nodes(G, tree) {
  pile = [tree]

  while (pile.length > 0) {
    current = pile.pop()
    if (current.url in G) {
      continue
    }

    G[current.url] = {
      title: current.title,
      children: [],
      require: [],
      needed: [],
      father: undefined,
    }

    for (node of current.children) {
      if (!(node in G)) {
        pile.push(node)
      }
    }
  }
  return G
}

function add_edges(G, tree) {
  console.log(tree)
  pile = [tree]

  seen = {}
  while (pile.length > 0) {
    current = pile.pop()
    if (current.url in seen) {
      continue
    }
    seen[current.url] = true;
    g_node = G[current.url]
    for (node of current.children) {
      g_node.children.push(node.url)

      G[node.url].father = current.url
      if (!(node.url in seen)) {
        pile.push(node)
      }
    }

    if (current.hasOwnProperty('prerequis')) {
    for (x of current.prerequis) {
      url = decodeURI(new URL(x, new URL(current.url, "http://localhost/").href).toString()).substring(16)

      if (url in G) {
        g_node.require.push(url);
        G[url].needed.push(current.url)
      }
    }

    }
    G[current.url] = g_node

  }
  return G
}

</script>  

<script>
tree = {{ collections.all | eleventyNavigation | dump | safe }}

G = create_graph(tree)

root = {{page.url | dump | safe}}

</script>  
  
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
  
  var graph = {
    nodes: [],
    links: []
  }

  groups = {
    autre: 1
  }
  
  all_nodes = {}
  i = 2
  for (tree of G[root].children) {
      all_nodes[tree] = true;
      groups[tree] = i
      graph.nodes.push({
        id: G[tree].title,
        link: tree,
        group: tree,
        root: true,
        fx: 0.1*width + (i-2)*.8*width/Math.max(1, G[root].children.length - 1),
        fy: 0.1*height,
      })

      i += 1
  }

  // tree
  for (tree of G[root].children) {
      pile = []
      for (node of G[tree].children) {
        pile.push(node)
      }

      while (pile.length > 0) {
        node = pile.pop()
        if (node in all_nodes) {
          continue
        }
        all_nodes[node] = true;

        for (next of G[node].children) {
          graph.links.push({
            source: node,
            target: next
          })

          if (!(next in seen)) {
            pile.push(next)
          }
        }

        graph.nodes.push({
          id: G[node].title,
          link: node,
          group: tree,
        })
      }
  }

  //require
  for (tree of G[root].children) {
      pile = [tree]
      for (node of G[tree].children) {
        pile.push(node)
      }

      seen = {}
      while (pile.length > 0) {
        node = pile.pop()
        if (node in seen) {
          continue
        }
        seen[node] = true;

        for (next of G[node].children) {
          if (!(next in seen)) {
            pile.push(next)
          }
        }

        for (req of G[node].require) {
          if (!(req in all_nodes)) {
            all_nodes[req] = true;

            graph.nodes.push({
              id: G[req].title,
              link: req,
              group: "autre",
            })
          }
            graph.links.push({
              source: req,
              target: node
          })
        }
      }
  }
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

var link = svg.append("g")
    .attr("class", "links")
    .selectAll("line")
    .data(graph.links)
    .enter().append("line")
    .style('stroke', d => { return "#000"})

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

  var simulation = d3.forceSimulation()
      .force("link", d3.forceLink().id(d => { return d.link; }))
      .force("charge", d3.forceManyBody().strength(-100))
      .force("center", d3.forceCenter(width / 2, height / 2));

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
