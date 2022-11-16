const { Sequelize, DataTypes } = require('sequelize');
path = require('path')

const sequelize = new Sequelize({
  dialect: 'sqlite',
  storage: path.join(__dirname, 'db.sqlite')
});

const MonModèle = sequelize.define('MonModèle', {
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

module.exports = {
    sequelize: sequelize,
    model: {
        MonModèle: MonModèle,
    }
}