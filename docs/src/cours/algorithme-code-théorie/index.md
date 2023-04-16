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
      children: new Set(),
      next: new Set(),
      require: new Set(),
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
  pile = [tree]

  seen = new Set()
  while (pile.length > 0) {
    current = pile.pop()
    if (seen.has(current.url)) {
      continue
    }
    seen.add(current.url)
    g_node = G[current.url]
    for (node of current.children) {
      g_node.next.add(node.url)
      g_node.children.add(node.url)
      if (!seen.has(node.url)) {
        pile.push(node)
      }
    }

    if (current.hasOwnProperty('prerequis')) {
      for (x of current.prerequis) {
        url = decodeURI(new URL(x, new URL(current.url, "http://localhost/").href).toString()).substring(16)
        if (url in G) {
          G[url].next.add(current.url)
          g_node.require.add(url)
        }
      }
    }
    G[current.url] = g_node

  }
  return G
}

function complete_relation(G) {
  for (k in G) {
    for (x in G) {
      for (y in G) {
        if (G[x].next.has(k) && G[k].next.has(y)) {
          G[x].next.add(y)
        }
     }
    }
  }
}

function sparse_relation(gg) {
  to_del = []
  for (k in gg) {
    for (x in gg) {
      for (y in gg) {
        if (gg[x].next.has(k) && gg[k].next.has(y) && gg[x].next.has(y)) {
          to_del.push([x, y])
        }
     }
    }
  }
  for ([u, v] of to_del) {
    gg[u].next.delete(v)
  }
}
function copy_node(node) {
  return {
      title: node.title,
      children: new Set(node.children),
      next: new Set(node.next),
      require: new Set(node.require),
  }
}

function subgraph(root, G) {
  G2 = {}
  
  pile = [root]

  while (pile.length > 0) {
    current = pile.pop()
    if (current in G2) {
      continue
    }

    G2[current] = copy_node(G[current])

    for (node of G[current].children) {
      if (!(node in G2)) {
        pile.push(node)
      }
    }
    for (node of G2[current].require) {
      if (!(node in G2)) {
        G2[node] = copy_node(G[node])
        G2[node].group = "autre"
      }
    }
  }
  
  G2[root].group = "root"
  for (node of G2[root].children) {
    pile = [node]

    while (pile.length > 0) {
      current = pile.pop()

      G2[current].group = node

      for (x of G2[current].children) {
          pile.push(x)
      }
    }
  }
  for (x in G2) {
    z = new Set()
    for (y of G2[x].next) {
      if (y in G2) {
        z.add(y)
      }
    }
    G2[x].next = z
  }

  complete_relation(G2)
  sparse_relation(G2)

  groups = {
    root: 1,
    autre: 2,
  }
  i = 3
  for (x in G2[root].children) {
    groups[x] = i
    i += 1
  }

  return [G2, groups]

}

</script>  

<script>
tree = {{ collections.all | eleventyNavigation | dump | safe }}

graph_tree = create_graph(tree)

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

  var [G, groups] = subgraph(root, graph_tree)

  var graph = {
    nodes: [],
    links: [],  
  }

  all_nodes = new Set([root])
  graph.nodes.push({
    id: root,
    root: true,
    fx: 0.5*width,
    fy: 0.1*height,
  })

  i = 0
  for (tree of G[root].children) {
    all_nodes.add(tree)

    graph.nodes.push({
      id: tree,
      root: true,
      fx: 0.1*width + (i)*.8*width/Math.max(1, G[root].children.size - 1),
      fy: 0.2*height,
    })

    i += 1
  }
  for (x in G) {
    if (all_nodes.has(x)) {
      continue
    }
    all_nodes.add(x)

    graph.nodes.push({
      id: x,
    })
  }

  // edges
  for (node in G) {
    for (next of G[node].next) {
      graph.links.push({
        source: node,
        target: next
      })
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
    .attr("xlink:href", d => { return d.id})
    .append("circle")
    .attr("r", 5)
    .attr("fill", function(d) { return color(G[d.id].group); })

  node.append("a")
    .attr("xlink:href", d => { return d.id})
    .append("text")
      .text(function(d) {
        return G[d.id].title;
      })
      .attr('x', 6)
      .attr('y', 3)
      .style('fill', d => { if (d.root) {return color(G[d.id].group)} else { return 'black'}})

  var simulation = d3.forceSimulation()
      .force("link", d3.forceLink().id(d => { return d.id; }))
      .force("charge", d3.forceManyBody().strength(-200))
      .force("center", d3.forceCenter(.55*width, .5*height));

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
