import path from "path";
import {NodeCompiler} from "@myriaddreamin/typst-ts-node-compiler";

export default function (eleventyConfig) {

    eleventyConfig.addTemplateFormats("typ");
    eleventyConfig.addExtension("typ", {
        compile:async(inputContent, inputPath) => {
            const compiler = NodeCompiler.create({
                workspace:path.resolve(inputPath,".."),
            });
        //catch error, so that we can print it to the console
        try {
            const output = await compiler.svg({
                mainFileContent: inputContent,
                inputs: {
                    fill: "white",
                },
            });
            return async(data) => { return output;}
        } catch(error) {
            console.error("Error compiling typst file:", error);
            throw error;
        }
    }});

    eleventyConfig.addPairedShortcode('typst', async (rawContent, ...args) => {
      const typst = NodeCompiler.create();
      // const args = Array.prototype.slice.call(arguments, 1);
      
      // 
      const content = "#set page(width: auto,height:auto,fill: none)\n"+args.join("\n")+"\n"+rawContent
      
      try {
            const output = await typst.plainSvg({
                mainFileContent: content,
            });
            return `\n\n<center>${output}</center>\n\n`;
      } catch(error) {
            console.error("Error compiling typst file:", error);
            throw error;
        }
      
      
  });

      eleventyConfig.addPairedShortcode('algorithme', async (rawContent, ...args) => {
      const typst = NodeCompiler.create();
      // const args = Array.prototype.slice.call(arguments, 1);
      
      // 
      const content = "#set page(width: auto,height:auto,fill: none, margin:(top: 0.1cm,bottom: 0.1cm,x:0cm))\n#set text(size: 14pt)\n#import \"@preview/lovelace:0.3.0\": *"+args.join("\n")+"\n"+rawContent
      
      try {
            const output = await typst.plainSvg({
                mainFileContent: content,
            });
            return `\n\n<pre class="language-pseudocode">${output}</pre>\n\n`;
      } catch(error) {
            console.error("Error compiling typst file:", error);
            throw error;
        }
      
      
  });

}