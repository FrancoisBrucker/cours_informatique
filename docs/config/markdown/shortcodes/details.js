
const outdent = require('outdent');

module.exports = function (markdownItLibrary, eleventyConfig) {

    eleventyConfig.addPairedShortcode('details', (content, arg) => {
        
        summary = `<summary>${arg}</summary>`
        content = "<div>" + outdent`${markdownItLibrary.render(content)}` + "</div>"

        return '<details>' + summary + content + '</details>'
    });
};

