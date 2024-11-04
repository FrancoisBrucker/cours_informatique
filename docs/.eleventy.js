import { EleventyRenderPlugin, EleventyHtmlBasePlugin } from "@11ty/eleventy";
import eleventyNavigationPlugin from "@11ty/eleventy-navigation";

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

  return {
    dir: {
      input: "src",
      output: "dist"
    },
    markdownTemplateEngine: "njk",
  }

};