import { Sequelize, DataTypes } from 'sequelize';

import { fileURLToPath } from 'url';
import path from 'path';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

import { logger } from './logger.js';

const sequelize = new Sequelize({
  dialect: 'sqlite',
  storage: path.join(__dirname, 'db.sqlite'),
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