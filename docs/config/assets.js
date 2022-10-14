module.exports = function (eleventyConfig) {

  eleventyConfig.addPassthroughCopy("src/assets/node_modules");

  // images 
  eleventyConfig.addPassthroughCopy("src/**/!(node_modules)/**/*.{jpg,png,ico}");
  
  // data
  eleventyConfig.addPassthroughCopy("src/**/{cours,enseignements,tutoriels}/**/*.{txt,edi,csv,json}");

  eleventyConfig.addPlugin(require("eleventy-postcss-extension"));

};

