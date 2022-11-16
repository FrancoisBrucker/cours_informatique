const db = require("./db")

async function initDB() {
    await db.sequelize.sync({force: true})
    
    var data = await db.model.MonModèle.create({
        message: "mon premier message",
        nombre: 7,
    })

    data = await db.model.MonModèle.create({
        message: "un autre massage",
        nombre: 3,
    })

}

initDB()
    .then(() => {
        console.log("base initialisée")
    })