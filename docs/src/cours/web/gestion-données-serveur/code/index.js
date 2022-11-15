const express = require('express')
const app = express()

const hostname = '127.0.0.1';
const port = 3000;

donnée = 42

app.get('/', (req, res) => {
    res.statusCode = 200;
    res.setHeader('Content-Type', 'text/html; charset=utf-8');

    res.end(donnée.toString());

})


app.post('/', (req, res) => {

    donnée = req.query.valeur;
    res.redirect('/');

})


app.listen(port, hostname);
console.log(`Server running at http://${hostname}:${port}/`);