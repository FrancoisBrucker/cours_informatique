import db from "./db.js";

async function initDB() {
    await db.sequelize.sync({force: true})
    
    await db.model.Signification.create({
        message: "Une main de fer dans un gant de velours... Votre caractère bien trempé vous cause parfois du tort, mais pas question de vous adoucir : vous êtes comme vous êtes, que ça plaise ou non ! Au moins, vous avez le mérite de jouer cartes sur table. Vos amis savent qu'ils peuvent compter sur votre loyauté.",
        nombre: 1,
    })

    await db.model.Signification.create({
        message: "Au premier abord, on vous juge froide, distante. Mais c'est mal vous connaître car sous votre carapace glaciale, vous êtes ultrasensible ! Le sarcasme et l'ironie vous protègent des déceptions... Combien de fois avez-vous accordé votre confiance à des gens qui ne la méritaient pas ?",
        nombre: 2,
    })

    await db.model.Signification.create({
        message: "Vous avez l'âme d'une artiste ! Dessin, chant, danse... Vous vous épanouissez dans les activités créatives, et vous avez une imagination débordante.",
        nombre: 3,
    })

    await db.model.Signification.create({
        message: "La spontanéité, ce n'est pas votre truc. Dans votre vie, tout doit être rangé, organisé, planifié, sinon c'est la panique ! Au travail, les responsabilités vous font peur : vous préférez vous mettre au service d'un supérieur plutôt que de prendre les commandes. Votre prudence naturelle vous pousse à ne pas vous aventurer en terrain inconnu...",
        nombre: 4,
    })

    await db.model.Signification.create({
        message: "Le changement, l'imprévu, la nouveauté, vous adorez ! Ultra curieuse, vous êtes bien décidée à tout essayer, et les expériences extrêmes ne vous font pas peur.",
        nombre: 5,
    })

    await db.model.Signification.create({
        message: "Vous attendez le prince charmant !",
        nombre: 6,
    })

    await db.model.Signification.create({
        message: "Sous votre petit air mystérieux, vous cachez des capacités d'observation et d'analyse incroyables. D'ailleurs, lorsque vous leur donnez des conseils, vos proches les suivent à la lettre !",
        nombre: 7,
    })

    await db.model.Signification.create({
        message: "Des projets, vous en avez toujours en pagaille ! Visionnaire, vous avez l'âme d'un chef : vous commandez, et les autres vous obéissent sans discuter. Et à l'arrivée, on reconnaît vos mérites.",
        nombre: 8,
    })

    await db.model.Signification.create({
        message: "Vous rêvez d'un monde paisible et harmonieux... L'idéaliste de la famille, c'est vous ! Vous êtes vulnérable face au mensonge et à la trahison. Pourtant, lorsque les choses se corsent, vous êtes capable de vous démener pour résoudre les problèmes au plus vite. Pas question de rester passive face aux situations difficiles !",
        nombre: 9,
    })

}

initDB()
    .then(() => {
        console.log("base initialisée")
    })