
const { template } = require("./utils")

module.exports = function (eleventyConfig) {

  eleventyConfig.addPairedShortcode('chemin', (content, arg) => {

    return `
<div class="quote relative  py-2 drop-shadow rounded rounded-tl-none rounded-bl-none border-solid border-l-8 border-purple-500 bg-purple-100">
<svg class="absolute w-7 h-7 pl-1 pt-0.5 pb-0.5 text-purple-500" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
  <path stroke-linecap="round" stroke-linejoin="round" d="M5 19a2 2 0 01-2-2V7a2 2 0 012-2h4l2 2h4a2 2 0 012 2v1M5 19h14a2 2 0 002-2v-5a2 2 0 00-2-2H9a2 2 0 00-2 2v5a2 2 0 01-2 2z" />
</svg>
${template(content, arg)}
`
  })
};



