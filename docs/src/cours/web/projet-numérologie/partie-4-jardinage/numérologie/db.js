const { Sequelize, DataTypes } = require('sequelize');
path = require('path')

const sequelize = new Sequelize({
  dialect: 'sqlite',
  storage: path.join(__dirname, 'db.sqlite')
});

signification = require("./modèles/signification")
prénoms = require("./modèles/prénoms")

module.exports = {
    sequelize: sequelize,
    model: {
        Signification: signification(sequelize),
        Prénoms: prénoms(sequelize),
    }
}