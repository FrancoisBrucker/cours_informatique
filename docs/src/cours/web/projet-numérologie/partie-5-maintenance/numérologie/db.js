import { Sequelize, DataTypes } from 'sequelize';

import { fileURLToPath } from 'url';
import path from 'path';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

import { logger } from './logger.js';

let env = process.env.NODE_ENV || 'development';

let storage;

if (env === "test") {
  storage = ":memory:"
} else {
  storage = path.join(__dirname, 'db.sqlite')
}
const sequelize = new Sequelize({
  dialect: 'sqlite',
  storage: storage,
  logging: (msg) => logger.info(msg),
});

import signification from "./modèles/signification.js"
import prénoms from "./modèles/prénoms.js"

if (env === "test") {
  await sequelize.sync({force: true})
  await signification(sequelize).sync({force: true})
  await prénoms(sequelize).sync({force: true})

  await signification(sequelize).create({
    message: "La spontanéité, ce n'est pas votre truc. Dans votre vie, tout doit être rangé, organisé, planifié, sinon c'est la panique ! Au travail, les responsabilités vous font peur : vous préférez vous mettre au service d'un supérieur plutôt que de prendre les commandes. Votre prudence naturelle vous pousse à ne pas vous aventurer en terrain inconnu...",
    nombre: 4,
  })
}

export default {
  sequelize: sequelize,
  model: {
    Signification: signification(sequelize),
    Prénoms: prénoms(sequelize),
  }
}