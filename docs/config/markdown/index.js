module.exports = function (eleventyConfig) {

  markdownItLibrary = require("markdown-it")({
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


  eleventyConfig.addPlugin(require('@pborenstein/eleventy-md-syntax-highlight'),
    { showLineNumbers: false }
  )
  
  eleventyConfig.addPlugin(require("eleventy-plugin-mathjax"));

  eleventyConfig.addFilter("md", function (content = "") {
    
    return markdownItLibrary.render(content);
  });

  eleventyConfig.setLibrary("md", markdownItLibrary)

  require("./shortcodes")(eleventyConfig);

};

