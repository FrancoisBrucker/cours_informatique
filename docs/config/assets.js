// import postcssPlugin from "eleventy-postcss-extension"
import fs from "fs";
import path from "path";

export default function (eleventyConfig) {

  // eleventyConfig.addPlugin(postCSSConfig);

  // garder le node_modules des assets, ignorer les autres
  eleventyConfig.addPassthroughCopy("src/assets/node_modules");
  eleventyConfig.ignores.add("src/!(assets)/**/node_modules");

  // caches créés en local (tests python, jupyter) : pas de pages
  eleventyConfig.ignores.add("src/**/.pytest_cache/**");
  eleventyConfig.ignores.add("src/**/.ipynb_checkpoints/**");

  // images 
  eleventyConfig.addPassthroughCopy("src/**/!(node_modules)/**/*.{jpg,png,ico,pdf,svg,gif}");

  // html
  eleventyConfig.addPassthroughCopy("src/**/!(node_modules)/**/*.{html}");

  // videos
  eleventyConfig.addPassthroughCopy("src/**/!(node_modules)/**/*.{webm,mov,mp4,ogv}");
  
  // data
  eleventyConfig.addPassthroughCopy("src/**/!(node_modules)/**/*.{txt,edi,csv,json,zip,pdf,mat,geojson,sh}");
  // notebooks, sans les sauvegardes de jupyter (.ipynb_checkpoints)
  eleventyConfig.addPassthroughCopy("src/**/!(.ipynb_checkpoints)/*.ipynb");

  // Les motifs « !(node_modules) » ci-dessus n'excluent pas un node_modules
  // situé plus bas dans l'arborescence : on retire donc après copie les
  // node_modules et .vscode locaux des exemples (jamais commités).
  // dist/assets (MathJax, Prism) n'est pas concerné.
  eleventyConfig.on("eleventy.after", ({ dir }) => {
    const assets = path.resolve(dir.output, "assets");
    const nettoyer = (d) => {
      for (const e of fs.readdirSync(d, { withFileTypes: true })) {
        if (!e.isDirectory()) continue;
        const p = path.join(d, e.name);
        if (path.resolve(p) === assets) continue;
        if (e.name === "node_modules" || e.name === ".vscode") fs.rmSync(p, { recursive: true, force: true });
        else nettoyer(p);
      }
    };
    if (fs.existsSync(dir.output)) nettoyer(dir.output);
  });
};



