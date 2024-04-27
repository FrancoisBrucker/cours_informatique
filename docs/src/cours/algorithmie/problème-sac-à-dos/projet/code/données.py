EXEMPLE = [
    {
        "nom": "poudre 1",
        "kg": 15,
        "prix_kg": 9,
    },
    {
        "nom": "poudre 2",
        "kg": 2,
        "prix_kg": 15,
    },
    {
        "nom": "poudre 3",
        "kg": 4,
        "prix_kg": 8,
    },
    {
        "nom": "poudre 4",
        "kg": 1,
        "prix_kg": 6,
    },
    {
        "nom": "poudre 5",
        "kg": 6,
        "prix_kg": 3,
    },
    {
        "nom": "poudre 6",
        "kg": 80,
        "prix_kg": 10,
    },
]


def prix(produit):
    return produit["kg"] * produit["prix_kg"]
