import markdownIt from "markdown-it"
import markdownItAttrs from "markdown-it-attrs"
import markdownItAnchor from "markdown-it-anchor"
import markdownItMultimdTable from "markdown-it-multimd-table"

import shortcodes from "./shortcodes/index.js"

export default async function(eleventyConfig) {

  let markdownItLibrary = markdownIt({
      html: true,
      breaks: false,
      linkify: true
  })

  markdownItLibrary
      .use(markdownItAttrs)
      .use(markdownItMultimdTable, {
          multiline: true,
          rowspan: true,
          headerless: true,
          multibody: true,
          aotolabel: true,
      })
      // id sur les titres (sommaire flottant, liens directs, recherche).
      // Un id donné explicitement avec {#mon-id} est conservé.
      .use(markdownItAnchor, {
          level: 2,
          tabIndex: false,
          slugify: (s) => s.normalize("NFD").replace(/[\u0300-\u036f]/g, "")
              .toLowerCase().replace(/[^a-z0-9]+/g, "-").replace(/^-+|-+$/g, "") || "section",
      });

  // eleventyConfig.addPlugin(require("eleventy-plugin-mathjax"));

  eleventyConfig.addFilter("md", function (content = "") {
      return markdownItLibrary.render(content);
  });

  eleventyConfig.setLibrary("md", markdownItLibrary)

  shortcodes(eleventyConfig);
};

