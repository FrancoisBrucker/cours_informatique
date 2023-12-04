import fs from 'fs';

import path from 'path'
import {fileURLToPath} from 'url'

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

let localisation_fichier = path.join(__dirname,  "./fichier-texte.txt");
let contenu = fs.readFileSync(localisation_fichier, {encoding:'utf8'})
console.log(contenu)
