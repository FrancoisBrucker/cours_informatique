import {template} from "./utils.js";

export default async function(eleventyConfig) {

  eleventyConfig.addPairedShortcode('attention2', (content, arg) => {

    return `
<div class="quote relative py-2 drop-shadow rounded rounded-tl-none rounded-bl-none border-solid border-l-8 border-red-700 bg-red-100">
<svg class="absolute w-7 h-7 pl-1 pt-0.5 pb-0.5 text-red-700" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="size-6">
  <path stroke-linecap="round" stroke-linejoin="round" d="m18.375 12.739-7.693 7.693a4.5 4.5 0 0 1-6.364-6.364l10.94-10.94A3 3 0 1 1 19.5 7.372L8.552 18.32m.009-.01-.01.01m5.699-9.941-7.81 7.81a1.5 1.5 0 0 0 2.112 2.13" />
</svg>
${template(content, arg)}
</div>
`
  })
};



