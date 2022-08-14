
const { escapeHtml } = require("./utils")

module.exports = function (eleventyConfig) {

    eleventyConfig.addPairedShortcode('details', (content, arg) => {
        
        return `

<div class="relative drop-shadow rounded rounded-tl-none rounded-bl-none border-solid border-l-8 border-indigo-500 bg-indigo-100">
<details class="group">
<summary class="list-none py-0.5">
<svg class="group-open:hidden absolute w-7 h-7 pl-1 pt-0.5 text-indigo-500" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
  <path stroke-linecap="round" stroke-linejoin="round" d="M9 5l7 7-7 7" />
</svg>
<svg class="group-open:block hidden absolute w-7 h-7 pl-1 pt-0.5 text-indigo-500" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
  <path stroke-linecap="round" stroke-linejoin="round" d="M19 9l-7 7-7-7" />
</svg>
<div class="pl-8 font-bold inline-block">
${escapeHtml(arg)}
</div>
<svg class="group-open:hidden inline-block pl-3 w-10 text-indigo-500" xmlns="http://www.w3.org/2000/svg"  fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
  <path stroke-linecap="round" stroke-linejoin="round" d="M5 12h.01M12 12h.01M19 12h.01M6 12a1 1 0 11-2 0 1 1 0 012 0zm7 0a1 1 0 11-2 0 1 1 0 012 0zm7 0a1 1 0 11-2 0 1 1 0 012 0z" />
</svg>
</summary>
<div class="mx-8 pb-2">
${escapeHtml(content)}
</div>

</details>     
</div>
`        
    });
};

