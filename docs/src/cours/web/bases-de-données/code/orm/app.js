const db = require("./db")

async function utilisation() {
    console.log("Lecture id = 1 :")
    data = await db.model.MonModèle.findByPk(1);
    console.log(data.toJSON())

    console.log("---------")
    console.log("clé primaire : ", data.id)
    console.log("message : ", data.message)
    console.log("nombre : ", data.nombre)
    console.log("date de création création : ", data.createdAt)
    console.log("dernière modification : ", data.updatedAt)
    console.log("---------")

    console.log("Lecture id qui n'existe pas :")
    data = await db.model.MonModèle.findByPk(42);
    console.log(data) // n'existe pas

    console.log("Lecture tous les éléments :")
    data = await db.model.MonModèle.findAll();
    for (element of data) {
        console.log(element.toJSON())
    }

    console.log("Lecture requête :")
    data = await db.model.MonModèle.findAll({
        where: {
            nombre: 3
        }
    });
    for (element of data) {
        console.log(element.toJSON())
    }
}

utilisation()