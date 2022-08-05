const { EleventyRenderPlugin } = require("@11ty/eleventy");

const markdownConfig = require("./config/markdown")
const assetsConfig = require("./config/assets")

module.exports = function (eleventyConfig) {

  eleventyConfig.setFrontMatterParsingOptions({
    excerpt: true,
    // Optional, default is "---"
    // excerpt_separator: "<!-- résumé -->"
  });

  eleventyConfig.addPlugin(EleventyRenderPlugin);
  
  markdownConfig(eleventyConfig);
  assetsConfig(eleventyConfig);

  return {
    pathPrefix: "/cours_informatique/",
    dir: {
      input: "src",
      output: "dist"
    },
  }

};