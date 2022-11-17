function nombre(chaîne) {
    var somme = 0
    for (var i=0; i < chaîne.length; i++) {
        somme += chaîne.charCodeAt(i)
    }
    return somme
}

// test de nombre(chaîne)

// // est-ce 2x plus ?
// console.log(nombre("cou"))
// console.log(nombre("coucou"))

// // chaque caractère :la somme est-elle correcte ?
// for (c of "cou") { 
//     console.log(c + " : " + nombre(c))
// }
// console.log('----------------')
// // fin de test de nombre(chaîne)

function somme(nombre) {
    var somme = 0
    chaîne = String(nombre)
    for (var i=0; i < chaîne.length ; i++) {
        somme += parseInt(chaîne.charAt(i))
    }
    return somme
}

// test de somme(nombre)
// console.log(somme(132))

// // avec un chiffre : charAt != charCodeAt
// console.log(somme(4))
// console.log("4".charCodeAt(0))
// console.log("4".charAt(0))

// // conversion chaîne de caractères et nombre
// console.log(typeof "4".charAt(0))
// console.log(parseInt("4".charAt(0)))
// console.log(typeof parseInt("4".charAt(0)))

// console.log('----------------')
// // fin de test de somme(nombre)

function chiffreAssocie(chaîne) {
    valeur = nombre(chaîne)

    while (valeur > 9) {
        valeur = somme(valeur)
    }
    return valeur
}

// test de chiffreAssocie(chaîne)

// //test valeur somme des chiffres
// console.log(nombre("coucou"))
// console.log(chiffreAssocie("coucou"))

// console.log('----------------')
// // fin de test de chiffreAssocie(chaîne)

module.exports = {
    chiffre: chiffreAssocie,
}