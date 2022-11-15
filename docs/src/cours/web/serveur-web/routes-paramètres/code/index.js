const express = require('express')
const app = express()

const hostname = '127.0.0.1';
const port = 3000;

// app.get('/bonjour/', (req, res) => {
//     res.statusCode = 200;
//     res.setHeader('Content-Type', 'text/html; charset=utf-8');

//     res.end("bonjour");

// })

app.get('/bonjour', (req, res) => {
    res.statusCode = 200;
    res.setHeader('Content-Type', 'text/html; charset=utf-8');

    res.end(`bonjour ${req.query.prénom} ${req.query.nom} ! `);

})

app.get('/bonjour/:prenom', (req, res) => {
    res.statusCode = 200;
    res.setHeader('Content-Type', 'text/html; charset=utf-8');

    // res.end("bonjour " + req.params.prenom + " !");
    res.end(`bonjour ${req.params.prenom} ! `);

})

app.get('/bonjour/:prenom/:nom', (req, res) => {
    res.statusCode = 200;
    res.setHeader('Content-Type', 'text/html; charset=utf-8');

    // res.end("bonjour " + req.params.prenom + " !");
    res.end(`bonjour ${req.params.prenom} ${req.params.nom} ! `);

})


app.get('/aurevoir/Carole', (req, res) => {
    res.statusCode = 200;
    res.setHeader('Content-Type', 'text/html; charset=utf-8');

    res.end("au revoir Carole !");

})

// ...

app.get('/aurevoir/', (req, res) => {
    res.statusCode = 200;
    res.setHeader('Content-Type', 'text/html; charset=utf-8');

    res.end("au revoir");

})

app.use(function (req, res) {
    res.statusCode = 404;
    res.setHeader('Content-Type', 'text/html; charset=utf-8');

    res.end("N'existe pas");

})

app.listen(port, hostname);
console.log(`Server running at http://${hostname}:${port}/`);