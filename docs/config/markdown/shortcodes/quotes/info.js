const { template } = require("./utils")

module.exports = function (eleventyConfig) {

  eleventyConfig.addPairedShortcode('info', (content, arg) => {

    return `
<div class="quote relative  py-2 drop-shadow rounded rounded-tl-none rounded-bl-none border-solid border-l-8 border-cyan-500 bg-cyan-100">
<svg class="absolute w-7 h-7 pl-1 pt-0.5 pb-0.5 text-cyan-500" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
  <path stroke-linecap="round" stroke-linejoin="round" d="M9.663 17h4.673M12 3v1m6.364 1.636l-.707.707M21 12h-1M4 12H3m3.343-5.657l-.707-.707m2.828 9.9a5 5 0 117.072 0l-.548.547A3.374 3.374 0 0014 18.469V19a2 2 0 11-4 0v-.531c0-.895-.356-1.754-.988-2.386l-.548-.547z" />
</svg>
${template(content, arg)}
`
  })
};


