function nombre(chaîne) {
    let somme = 0
    for (let i=0; i < chaîne.length; i++) {
        somme += chaîne.charCodeAt(i)
    }
    return somme
}

function somme(nombre) {
    var somme = 0
    var chaîne = String(nombre)
    for (var i=0; i < chaîne.length ; i++) {
        somme += parseInt(chaîne.charAt(i))
    }
    return somme
}

function chiffreAssocie(chaîne) {
    var valeur = nombre(chaîne)

    while (valeur > 9) {
        valeur = somme(valeur)
    }
    return valeur
}

export default {
    chiffre: chiffreAssocie,
}