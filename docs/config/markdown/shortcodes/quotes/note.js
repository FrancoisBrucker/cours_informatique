
const { template } = require("./utils")

module.exports = function (eleventyConfig) {

  eleventyConfig.addPairedShortcode('note', (content, arg) => {

    return `
<div class="quote relative drop-shadow  py-2 pr-2 rounded rounded-tl-none rounded-bl-none border-solid border-l-8 border-amber-800 bg-amber-100">
<svg class="absolute w-7 h-7 pl-1 pt-0.5 pb-0.5 text-amber-800" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
  <path stroke-linecap="round" stroke-linejoin="round" d="M12 8v4m0 4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
</svg>
${template(content, arg)}
`
  })
};
