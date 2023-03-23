import numérologie from "../back/numérologie.js"
// import db from "../db.js" // inutile. Juste pour voir le coverage


describe("Un chiffre associé à un prénom", () => {
    test("65 -> 6 + 5 = 11 -> 1 + 1 = 2", () => {
        expect(numérologie.somme(65)).toBe(6+5)
    })
    test("nombre associé au prénom d'une lettre", () => {
        expect(numérologie.nombre("A")).toBe(65)
    })
    test("nombre associé au prénom de plusieurs lettres", () => {
        expect(numérologie.chiffre("A")).toBe(2)
        expect(numérologie.chiffre("m")).toBe(1)
        expect(numérologie.chiffre("y")).toBe(4)
        expect(numérologie.chiffre("Amy")).toBe(2 + 1 + 4)
    })
    // test("nombre associé au prénom de plusieurs lettres", () => {
    //     expect(numérologie.chiffreAssocie("")).toBe(0)
    // })
    
})