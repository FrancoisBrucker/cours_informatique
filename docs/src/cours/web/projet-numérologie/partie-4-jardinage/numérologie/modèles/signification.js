const { DataTypes } = require('sequelize');

module.exports = (sequelize) => {

    return sequelize.define('Signification', {
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

}