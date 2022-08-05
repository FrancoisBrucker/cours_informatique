const markdownIt = require("markdown-it");

const shortcode = require("./shortcodes")

module.exports = function (eleventyConfig) {

  markdownItLibrary = markdownIt({
    html: true,
    breaks: true,
    linkify: true
  })

  markdownItLibrary
    .use(require('markdown-it-attrs'))
    .use(require('markdown-it-multimd-table'), {
      multiline: true,
      rowspan: true,
      headerless: true,
      multibody: true,
      aotolabel: true,
    });


  eleventyConfig.setLibrary("md", markdownItLibrary)

  eleventyConfig.addPlugin(require('@pborenstein/eleventy-md-syntax-highlight'),
    { showLineNumbers: false }
  )
  eleventyConfig.addPlugin(require("eleventy-plugin-mathjax"));

  eleventyConfig.addFilter("md", function (content = "") {
    return markdownItLibrary.render(content);
  });

  shortcode(markdownItLibrary, eleventyConfig);

};

