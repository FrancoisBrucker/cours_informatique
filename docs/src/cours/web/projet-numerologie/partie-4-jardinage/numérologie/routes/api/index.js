let express = require('express');

const numérologie = require('../../back/numérologie')
const db = require("../../db")

let router = express.Router();

router.get(encodeURI('/prénoms/read'), (req, res) => {
    db.model.Prénoms.findAll()
        .then((data) => {
            var liste = []
            for (element of data) {
                liste.push({
                    prénom: element.prénom,
                    chiffre: numérologie.chiffre(element.prénom)
                })
            }
            res.json(liste)
        })
})


module.exports = router