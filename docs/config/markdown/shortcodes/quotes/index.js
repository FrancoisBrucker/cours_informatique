
module.exports = function (eleventyConfig) {

    require('./details')(eleventyConfig);
    require('./exercice')(eleventyConfig);
    require('./note')(eleventyConfig);
    require('./chemin')(eleventyConfig);
    require('./aller')(eleventyConfig);
    require('./lien')(eleventyConfig);
    require('./attention')(eleventyConfig);
    require('./prerequis')(eleventyConfig);
    require('./info')(eleventyConfig);
    require('./faire')(eleventyConfig);
};

