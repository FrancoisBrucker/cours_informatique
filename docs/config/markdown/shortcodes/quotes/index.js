
module.exports = function (eleventyConfig) {

    require('./details')(eleventyConfig);
    require('./exercice')(eleventyConfig);
    require('./note')(eleventyConfig);
    require('./chemin')(eleventyConfig);
    require('./attention')(eleventyConfig);
    require('./pres-requis')(eleventyConfig);
    require('./info')(eleventyConfig);
};

