const http = require('http');
const fs = require('fs');

const hostname = '127.0.0.1';
const port = 3000;

const server = http.createServer((req, res) => {
    console.log(req.url)
    if (req.url === "/") {
        console.log("index")
        res.statusCode = 200;
        res.setHeader('Content-Type', 'text/html');
    
        fichier = fs.readFileSync("./index.html", {encoding:'utf8'})
        res.end(fichier);
    }
    else if (req.url === "/favicon.ico") {
        console.log("fav")
        res.statusCode = 200;
        res.setHeader('Content-Type', 'image/x-icon');
    
        fichier = fs.readFileSync("./favicon.ico")
        res.end(fichier);
    }
    else {
    res.statusCode = 404;
    res.setHeader('Content-Type', 'text/plain');
    res.end();
    }    
});

server.listen(port, hostname, () => {
    console.log(`Server running at http://${hostname}:${port}/`);
});
