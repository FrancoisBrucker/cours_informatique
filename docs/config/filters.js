module.exports = function (eleventyConfig) {

  eleventyConfig.addFilter("siteUrl", function (url, base="/") {
    try {
      return decodeURI(new URL(url, new URL(base, "http://localhost/").href).toString()).substring(16);
    } catch (err) {
      console.error(err);
      return url;
    }
  });

};

