
module.exports = function (markdownItLibrary, eleventyConfig) {

    require('./details')(markdownItLibrary, eleventyConfig);
    require('./exercice')(markdownItLibrary, eleventyConfig);

};

