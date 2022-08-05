

const stylesheetsConfig = require("./stylesheets")

module.exports = function (eleventyConfig) {

  eleventyConfig.addPassthroughCopy("src/assets/node_modules");

  eleventyConfig.addPassthroughCopy("src/**/!(node_modules)/**/*.jpg");

  stylesheetsConfig(eleventyConfig)

};

