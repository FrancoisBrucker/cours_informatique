// import postcssPlugin from "eleventy-postcss-extension"

export default function (eleventyConfig) {

  // eleventyConfig.addPlugin(postCSSConfig);

  // garder le node_modules des assets, ignorer les autres
  eleventyConfig.addPassthroughCopy("src/assets/node_modules");
  eleventyConfig.ignores.add("src/!(assets)/**/node_modules");

  // images 
  eleventyConfig.addPassthroughCopy("src/**/!(node_modules)/**/*.{jpg,png,ico,pdf,svg,gif}");

  // videos
  eleventyConfig.addPassthroughCopy("src/**/!(node_modules)/**/*.{webm,mov,mp4,ogv}");
  
  // data
  eleventyConfig.addPassthroughCopy("src/**/!(node_modules)/**/*.{txt,edi,csv,json,ipynb,zip,pdf,mat}");

};

// export default function (eleventyConfig) {

//   // préparer les module front 
//   eleventyConfig.addPassthroughCopy("src/assets/package*.json");

//   // ignorer les autres
//   eleventyConfig.ignores.add("src/**/node_modules");

//   // images 
//   eleventyConfig.addPassthroughCopy("src/**/**/*.{jpg,png,ico,gif}");
  
//   // data
//   eleventyConfig.addPassthroughCopy("src/**/{cours,enseignements,tutoriels}/**/*.{txt,edi,csv,json,ipynb,zip,pdf,mat}");

//   eleventyConfig.addPlugin(postcssPlugin);

// };

