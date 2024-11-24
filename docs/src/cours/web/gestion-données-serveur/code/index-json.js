import express from 'express'

const app = express()

const hostname = '127.0.0.1';
const port = 3000;

let donnée = {
	valeur: 42
}

app.use(express.json())

app.get('/', (req, res) => {
    res.json(donnée);

})


app.post('/', (req, res) => {
	console.log(req.body)
    donnée.valeur = req.body.valeur;
    res.redirect('/');

})


app.listen(port, hostname);
console.log(`Server running at http://${hostname}:${port}/`);