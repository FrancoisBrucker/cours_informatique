import { Sequelize, DataTypes } from 'sequelize';

import { fileURLToPath } from 'url';
import path from 'path';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);


const sequelize = new Sequelize({
  dialect: 'sqlite',
  storage: path.join(__dirname, 'db.sqlite')
});

const Signification = sequelize.define('Signification', {
    message: {
        type: DataTypes.STRING,
        allowNull: false
    },
    nombre: {
        type: DataTypes.INTEGER,
        allowNull: false
    },
}, {
    // Other model options go here
});

const Prénoms = sequelize.define('Prénoms', {
    prénom: {
        type: DataTypes.STRING,
        allowNull: false
    },
}, {
    // Other model options go here
});

export default {
    sequelize: sequelize,
    model: {
        Signification: Signification,
        Prénoms: Prénoms,
    }
}