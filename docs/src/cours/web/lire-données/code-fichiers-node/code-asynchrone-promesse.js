import fs from 'fs/promises';

import path from 'path'
import {fileURLToPath} from 'url'

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

let localisation_fichier = path.join(__dirname,  "./fichier-texte.txt");
let promesse = fs.readFile(localisation_fichier, {encoding:'utf8'})

promesse.then(data => {
    console.log("tout s'est bien passé. Le contenu du fichier lu est :");
    console.log(data)
})

console.log("ici")

