const { DataTypes } = require('sequelize');

module.exports = (sequelize) => {

    return sequelize.define('Prénoms', {
        prénom: {
            type: DataTypes.STRING,
            allowNull: false
        },
    }, {
        // Other model options go here
    });
    
}