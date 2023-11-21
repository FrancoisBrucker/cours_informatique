import http from 'http';
import fs from 'fs';
import path from 'path';

import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const hostname = '127.0.0.1';
const port = 3000;

const server = http.createServer((req, res) => {
    console.log(req.url)

    if (req.url === "/") {
        console.log("redirection");

        res.writeHead(301, {Location: "http://" + req.headers['host'] + '/static/index.html'});
        res.end();
    } else  if (req.url.startsWith("/static/")) {
        console.log("fichier statique");
        let fichier = path.join(__dirname,  req.url);
        
        res.writeHead(200,  {'Content-Type': 'text/html'});
        fichier = fs.readFileSync(fichier, {encoding:'utf8'});
        res.end(fichier);
    }
    else if (req.url.startsWith("/API/hasard")) {
        console.log("API");
        
        res.writeHead(200,  {'Content-Type': 'text/plain'});
        res.end(String(Math.random()));
    }
    else {
    res.writeHead(404,  {'Content-Type': 'text/plain'})
    res.end();
    }
});

server.listen(port, hostname, () => {
    console.log(`Server running at http://${hostname}:${port}/`);
});
