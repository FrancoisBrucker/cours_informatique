import { DataTypes } from 'sequelize';

export default (sequelize) => {

    return sequelize.define('Prénoms', {
        prénom: {
            type: DataTypes.STRING,
            allowNull: false
        },
    }, {
        // Other model options go here
    });

}
