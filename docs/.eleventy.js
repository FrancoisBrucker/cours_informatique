const { EleventyRenderPlugin } = require("@11ty/eleventy");
const { EleventyHtmlBasePlugin } = require("@11ty/eleventy");

const embedYouTube = require("eleventy-plugin-youtube-embed");
const eleventyNavigationPlugin = require("@11ty/eleventy-navigation");

const markdownConfig = require("./config/markdown")
const assetsConfig = require("./config/assets")
const filtersConfig = require("./config/filters")

module.exports = function (eleventyConfig) {

  eleventyConfig.addPlugin(EleventyRenderPlugin);
  eleventyConfig.addPlugin(EleventyHtmlBasePlugin);


  eleventyConfig.addPlugin(embedYouTube);
  eleventyConfig.addPlugin(eleventyNavigationPlugin);
  
  markdownConfig(eleventyConfig);
  assetsConfig(eleventyConfig);
  filtersConfig(eleventyConfig);

  return {
    // pathPrefix: "/cours_informatique/",
    dir: {
      input: "src",
      output: "dist"
    },
    markdownTemplateEngine: "njk",
  }

};