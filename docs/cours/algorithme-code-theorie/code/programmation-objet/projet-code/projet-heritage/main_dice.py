from dice import StatDice


def chi2(valeurs):
    N = sum(valeurs)

    chi2 = 0
    for o in valeurs:
        chi2 += (o - N / 6) ** 2 / (N / 6)

    return chi2


dice = StatDice()

for i in range(1000):
    dice.roll()

print('1000 lancers :', dice.stats())
print('chi2 = ', chi2(dice.stats()))
