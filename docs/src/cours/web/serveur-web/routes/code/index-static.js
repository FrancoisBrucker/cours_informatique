const http = require('http');
const fs = require('fs');
const path = require('path')

const hostname = '127.0.0.1';
const port = 3000;

const server = http.createServer((req, res) => {
    console.log(req.url)

    if (req.url === "/") {
        res.writeHead(301,{Location: "http://" + req.headers['host'] + '/static/index.html'});
        res.end();
        return;
    } else  if (req.url.startsWith("/static/")) {
        fichier = path.join(__dirname,  req.url.substring(7))
    } else {
        fichier = ""
    }
    console.log("fichier : " + fichier)
    
    if (fs.existsSync(fichier)) {
        res.writeHead(200,  {'Content-Type': 'text/html'})
    
        fichier = fs.readFileSync(fichier, {encoding:'utf8'})
        res.end(fichier);
    }
    else {
    res.writeHead(404,  {'Content-Type': 'text/plain'})
    res.end();
    }
});

server.listen(port, hostname, () => {
    console.log(`Server running at http://${hostname}:${port}/`);
});
