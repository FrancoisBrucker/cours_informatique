import { EleventyRenderPlugin, EleventyHtmlBasePlugin } from "@11ty/eleventy";
import eleventyNavigationPlugin from "@11ty/eleventy-navigation";
import syntaxHighlight from "@11ty/eleventy-plugin-syntaxhighlight";
import setupMarkdown from './config/markdown/index.js';
import assetsConfig from "./config/assets.js";
import filtersConfig from "./config/filters.js";

import postCompilation from "./config/post-build.js";

export default function(eleventyConfig) {

  eleventyConfig.addPlugin(EleventyRenderPlugin);
  eleventyConfig.addPlugin(EleventyHtmlBasePlugin);
  eleventyConfig.addPlugin(eleventyNavigationPlugin);
  
  assetsConfig(eleventyConfig);
  setupMarkdown(eleventyConfig);
  filtersConfig(eleventyConfig);

  postCompilation(eleventyConfig); // tailwind

  eleventyConfig.addPlugin(syntaxHighlight, {
    
    alwaysWrapLineHighlights: false,
    // Line separator for line breaks
    lineSeparator: "\n",

    // Change which Eleventy template formats use syntax highlighters
    templateFormats: ["*"], // default

    // Use only a subset of template types (11ty.js added in v4.0.0)
    // templateFormats: ["liquid", "njk", "md", "11ty.js"],

    // init callback lets you customize Prism
    init: function({ Prism }) {
      Prism.languages.pseudocode =
        {
          'comment': {
            pattern: /(^|[^\\])#.*/,
            lookbehind: true,
            greedy: true
          },
          'string': {
            pattern: /(?:[rub]|br|rb)?(")(?:\\.|(?!\1)[^\\\r\n])*\1/i,
            greedy: true
          },
          'function': {
            pattern: /((?:^|\s)(algorithme|fonction|programme|méthode)[ \t]+)[a-zA-Z_]\w*(?=\s*\()/g,
            lookbehind: true
          },
          'class-name': {
		        pattern: /(\bstructure\s+)\w+/i,
		        lookbehind: true
	        },
          'keyword': /\b(?:_(?=\s*:)|et|ou|si|sinon si|sinon|pour chaque|pour|rendre|tant que|self)\b/,
          'builtin': /\b(?:entier|chiffre|booléen|bit|réel|caractère|chaîne|algorithme|fonction|structure|attributs|méthodes|création)\b/,
          'boolean': /\b(?:Faux|∅|Vrai)\b/,
          'number': / [ijn]([0-9])*(')*[\n ]|\b0(?:b(?:_?[01])+|o(?:_?[0-7])+|x(?:_?[a-f0-9])+)\b|(?:\b\d+(?:_\d+)*(?:\.(?:\d+(?:_\d+)*)?)?|\B\.\d+(?:_\d+)*)(?:e[+-]?\d+(?:_\d+)*)?j?(?!\w)/i,
          'operator': /[-+%=]=?|←|→|!=|≠|≤|≥|:=|\*\*?=?|\/\/?=?|<[<=>]?|>[=>]?|[&|^~]/,
          'punctuation': /[{}[\];(),.:]/
        };
    },

    // Added in 3.1.1, add HTML attributes to the <pre> or <code> tags
    preAttributes: {
      tabindex: 0,

      // Added in 4.1.0 you can use callback functions too
      "data-language": function({ language, content, options }) {
        return language;
      }
    },
    codeAttributes: {},

    // Added in 5.0.0, throw errors on invalid language names
    errorOnInvalidLanguage: false,
  });

  return {
    dir: {
      input: "src",
      output: "dist"
    },
    markdownTemplateEngine: "njk",
  }

};