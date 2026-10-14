import {template} from "./utils.js";

function escapeHtml(code) {
    return "\n\n" + code + "\n\n";
}

export default async function(eleventyConfig) {

  eleventyConfig.addPairedShortcode('definition', (content, arg) => {
    let val
    
    if (arg) {
      val = ''
    }
    else {
      val = '<div class="pl-8 mb-2 mr-8"><strong>Définition</strong></div>'
      
    }

    return `
<div class="quote relative drop-shadow  py-2 pr-2 rounded rounded-tl-none rounded-bl-none border-solid border-l-8 border-amber-600 bg-amber-100">
<svg class="absolute w-7 h-7 pl-1 pt-0.5 pb-0.5 text-amber-600" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="size-6">
  <path stroke-linecap="round" stroke-linejoin="round" d="M8.625 12a.375.375 0 1 1-.75 0 .375.375 0 0 1 .75 0Zm0 0H8.25m4.125 0a.375.375 0 1 1-.75 0 .375.375 0 0 1 .75 0Zm0 0H12m4.125 0a.375.375 0 1 1-.75 0 .375.375 0 0 1 .75 0Zm0 0h-.375M21 12a9 9 0 1 1-18 0 9 9 0 0 1 18 0Z" />
</svg>
${val}
${template(content, arg)}
</div>
`
  })
};
