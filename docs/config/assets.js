module.exports = function (eleventyConfig) {

  // préparer les module front 
  eleventyConfig.addPassthroughCopy("src/assets/package*.json");

  // ignorer les autres
  eleventyConfig.ignores.add("src/**/node_modules");

  // images 
  eleventyConfig.addPassthroughCopy("src/**/**/*.{jpg,png,ico,gif}");
  
  // data
  eleventyConfig.addPassthroughCopy("src/**/{cours,enseignements,tutoriels}/**/*.{txt,edi,csv,json,ipynb,zip,pdf,mat}");

  eleventyConfig.addPlugin(require("eleventy-postcss-extension"));

};

