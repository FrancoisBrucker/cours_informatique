import express from 'express';

import numérologie from '../../back/numérologie.js'
import db from "../../db.js"

let router = express.Router();

router.get(encodeURI('/prénoms/read'), (req, res) => {
    db.model.Prénoms.findAll()
        .then((data) => {
            var liste = []
            for (let element of data) {
                liste.push({
                    prénom: element.prénom,
                    chiffre: numérologie.chiffre(element.prénom)
                })
            }
            res.json(liste)
        })
})


export {router};