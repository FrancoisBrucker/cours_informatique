module.exports = function (eleventyConfig) {

  eleventyConfig.addPassthroughCopy("src/assets/node_modules");

  eleventyConfig.addPassthroughCopy("src/**/!(node_modules)/**/*.{jpg,png}");
  eleventyConfig.addPassthroughCopy("src/**/!(node_modules)/**/*.{txt,edi}");

  eleventyConfig.addPlugin(require("eleventy-postcss-extension"));

};

