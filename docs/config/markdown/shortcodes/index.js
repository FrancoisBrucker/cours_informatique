
module.exports = function (eleventyConfig) {

    require('./quotes')(eleventyConfig);
    require('./resume')(eleventyConfig);
};

