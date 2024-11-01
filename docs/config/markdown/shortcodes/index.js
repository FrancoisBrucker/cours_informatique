import {template} from "./quotes/utils.js";
import quotes from "./quotes/index.js";

export default function setupShortcodes(eleventyConfig) {
    quotes(eleventyConfig);
}