const sass = require("sass");
const pluginCSS = require("eleventy-postcss-extension");

module.exports = function (eleventyConfig) {

  // eleventyConfig.addPassthroughCopy("src/assets/stylesheets/**/*.css");

  eleventyConfig.addPlugin(pluginCSS);

  eleventyConfig.addTemplateFormats("scss");

  // Creates the extension for use
  eleventyConfig.addExtension("scss", {
    outputFileExtension: "css", // optional, default: "html"

    // `compile` is called once per .scss file in the input directory
    compile: async function(inputContent) {
      let result = sass.compileString(inputContent);

      // This is the render function, `data` is the full data cascade
      return async (data) => {
        return result.css;
      };
    }
  });
};

