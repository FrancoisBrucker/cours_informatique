import fs from 'fs/promises';

import path from 'path'
import {fileURLToPath} from 'url'

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

async function lire(localisation_fichier) {
    return await fs.readFile(localisation_fichier, {encoding:'utf8'});
}

let localisation_fichier = path.join(__dirname,  "./fichier-texte.txt");
fs.readFile(localisation_fichier, {encoding:'utf8'}).then(data => {
    console.log(data)
})
console.log("ici")

