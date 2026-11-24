// Index de recherche Pagefind (https://pagefind.app/), généré après chaque build.
//
// On n'indexe pas les fichiers de dist/ tels quels : on passe à Pagefind le HTML
// de chaque page produite par Eleventy, débarrassé du code et des formules LaTeX.
// Les pages publiées ne sont pas modifiées.
//
// Seul le contenu marqué data-pagefind-body (l'article de layout/post.njk) est indexé,
// et les éléments marqués data-pagefind-ignore en sont exclus.

import * as pagefind from "pagefind";

// blocs de code et SVG (Typst, icônes) : retirés avant de chercher les formules,
// pour qu'un `$` dans du code ne soit pas pris pour un délimiteur.
const NON_TEXTE = /<(pre|code|svg|script|style)\b[\s\S]*?<\/\1>/gi;

// Formules : $$…$$, \[…\], \(…\) puis $…$ (sans traverser un bloc de texte).
const BLOC = String.raw`(?!<\/?(?:p|li|h[1-6]|div|td|th|tr|table|ul|ol|blockquote|details|summary)\b)`;
const FORMULES = [
  /\$\$[\s\S]*?\$\$/g,
  /\\\[[\s\S]*?\\\]/g,
  /\\\([\s\S]*?\\\)/g,
  new RegExp(String.raw`(?<!\\)\$(?:${BLOC}[^$]){1,1000}?(?<!\\)\$`, "g"),
];

export function nettoyer(html) {
  let texte = html.replace(NON_TEXTE, " ");
  for (const re of FORMULES) texte = texte.replace(re, " ");
  return texte;
}

export default function (eleventyConfig) {
  eleventyConfig.on("eleventy.after", async ({ dir, results }) => {
    const debut = Date.now();
    const prefixe = (eleventyConfig.pathPrefix || "/").replace(/^\/*/, "/").replace(/\/*$/, "/");

    const { index, errors } = await pagefind.createIndex({ forceLanguage: "fr" });
    if (errors.length) {
      console.error("[pagefind]", errors);
      return;
    }

    let pages = 0;
    for (const { url, outputPath, content } of results) {
      if (!url || !outputPath?.endsWith(".html") || typeof content !== "string") continue;
      if (!content.includes("data-pagefind-body") || url === "/recherche/") continue;
      const r = await index.addHTMLFile({
        url: prefixe + url.replace(/^\//, ""),
        content: nettoyer(content),
      });
      if (r.errors.length) console.error("[pagefind]", url, r.errors);
      else pages++;
    }

    await index.writeFiles({ outputPath: `${dir.output}/pagefind` });
    await pagefind.close();
    console.log(`[pagefind] ${pages} pages indexées en ${((Date.now() - debut) / 1000).toFixed(1)}s`);
  });
}
