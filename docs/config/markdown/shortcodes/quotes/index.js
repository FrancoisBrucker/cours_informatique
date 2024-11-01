import info from "./info.js";
import attention from "./attention.js";
import note from "./note.js";
import faire from "./faire.js";
import details from "./details.js";
import exercice from "./exercice.js";
import chemin from "./chemin.js";
import prerequis from "./prerequis.js";
import lien from "./lien.js";
import aller from "./aller.js";

export default async function(eleventyConfig) {

    details(eleventyConfig);
    exercice(eleventyConfig);
    note(eleventyConfig);
    chemin(eleventyConfig);
    lien(eleventyConfig);
    attention(eleventyConfig);
    prerequis(eleventyConfig);
    info(eleventyConfig);
    faire(eleventyConfig);
    aller(eleventyConfig);

};
