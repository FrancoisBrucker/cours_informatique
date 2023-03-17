import { fileURLToPath } from 'url';
import path from 'path';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);


import express from 'express';
const app = express()

import {router as routes} from "./routes/index.js";

const hostname = '127.0.0.1';
const port = 3000;

app.use(function (req, res, next) {
    const date = new Date(Date.now())
    console.log('Time:', date.toLocaleDateString(), date.toLocaleTimeString(), "; url :", req.url);
    next(); // sans cette ligne on ne pourra pas poursuivre.
})

app.use("/static", express.static(path.join(__dirname, '/static')))

app.get('/', (req, res) => {
    res.redirect(301, '/static/index.html')
})

app.use('/', routes)

app.use(function (req, res) {
    console.log("et c'est le 404 : " + req.url);

    res.statusCode = 404;
    res.setHeader('Content-Type', 'text/html');

    res.end("<html><head><title>le quatre cent quatre</title></head><body><h1>Et c'est le 404.</h1></body></html>");

})

app.listen(port, hostname);
console.log(`Server running at http://${hostname}:${port}/`);