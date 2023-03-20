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

export default {
  sequelize: sequelize,
  model: {
    Signification: signification(sequelize),
    Prénoms: prénoms(sequelize),
  }
}