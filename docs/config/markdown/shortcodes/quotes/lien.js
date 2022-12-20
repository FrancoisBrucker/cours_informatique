
const { template } = require("./utils")

module.exports = function (eleventyConfig) {

  eleventyConfig.addPairedShortcode('lien', (content, arg) => {

    return `
<div class="quote relative py-2 drop-shadow rounded rounded-tl-none rounded-bl-none border-solid border-l-8 border-emerald-500 bg-emerald-100">
  <svg class="absolute w-7 h-7 pl-1 pt-0.5 pb-0.5 text-emerald-500" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
    <path stroke-linecap="round" stroke-linejoin="round" d="M5.25 5.653c0-.856.917-1.398 1.667-.986l11.54 6.348a1.125 1.125 0 010 1.971l-11.54 6.347a1.125 1.125 0 01-1.667-.985V5.653z" />
  </svg>
${template(content, arg)}
</div>
`
  })
};



