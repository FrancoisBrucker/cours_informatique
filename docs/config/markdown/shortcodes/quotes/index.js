import info from "./info.js";
import attention from "./attention.js";
import attention2 from "./attention2.js";
import note from "./note.js";
import note2 from "./note2.js";
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
    note2(eleventyConfig);
    chemin(eleventyConfig);
    lien(eleventyConfig);
    attention(eleventyConfig);
    attention2(eleventyConfig);
    prerequis(eleventyConfig);
    info(eleventyConfig);
    faire(eleventyConfig);
    aller(eleventyConfig);

};
