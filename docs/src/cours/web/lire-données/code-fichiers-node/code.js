import fs from 'fs';

let contenu = fs.readFileSync("./fichier-texte.txt", {encoding:'utf8'})
console.log(contenu)
