import request from 'supertest';


import { app } from '../app.js';
import db from "../db.js"

let user;
let server;

beforeAll(async () => {
    user = await request.agent(app);
    server = await app.listen(3001); // test en parallèle et parfois 3000 et 3001
});


afterAll(async () => {
    await server.close();
});


describe('prénoms', () => {
    beforeEach(async () => {
        await db.sequelize.sync({ force: true })
    });


    test('Prénom read', async () => {
        await db.model.Prénoms.create({
            prénom: "Carole"
        })

        await db.model.Signification.create({
            message: "Quatre",
            nombre: 4,
        })    
        await user
            .get(encodeURI('/prénom?valeur=Carole'))
            .expect(200)
            .expect('Content-Type', /json/)
            .expect(function (res) {
                expect(res.body).toEqual({"chiffre": 4, "message": "Quatre", "prénom": "Carole"})
            })
    })

})
