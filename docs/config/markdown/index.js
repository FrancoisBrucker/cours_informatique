import markdownIt from "markdown-it"
import markdownItAttrs from "markdown-it-attrs"
import markdownItMultimdTable from "markdown-it-multimd-table"
import eleventyMdSyntaxHighlight from "@pborenstein/eleventy-md-syntax-highlight"

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
      });


  eleventyConfig.addPlugin(eleventyMdSyntaxHighlight,
      {showLineNumbers: false}
  )

  // eleventyConfig.addPlugin(require("eleventy-plugin-mathjax"));

  eleventyConfig.addFilter("md", function (content = "") {
      return markdownItLibrary.render(content);
  });

  eleventyConfig.setLibrary("md", markdownItLibrary)

  shortcodes(eleventyConfig);
};

