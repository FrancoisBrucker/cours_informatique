VIDE = "-"


class Alignement:
    def __init__(self, a_star, b_star):
        self.a_star = a_star
        self.b_star = b_star

    def _supprime_vide(self, chaine):
        s = ""

        for x in chaine:
            if x != VIDE:
                s += x
        return s

    def a(self):
        return self._supprime_vide(self.a_star)

    def b(self):
        return self._supprime_vide(self.b_star)

    def affiche(self):
        ligne_intermédiaire = ""

        for x, y in zip(self.a_star, self.b_star):
            if x != y:
                ligne_intermédiaire += " "
            else:
                ligne_intermédiaire += "|"

        print(self.a_star)
        print(ligne_intermédiaire)
        print(self.b_star)

    def evolution(self):
        chaines = [self.a()]
        debut = ""
        fin = self.a()

        for x, y in zip(self.a_star, self.b_star):
            print(x, y)
            if x == VIDE:
                chaines.append(debut + y + fin)
                debut = debut + y
            elif y == VIDE:
                chaines.append(debut + fin[1:])
                debut = debut
                fin = fin[1:]
            else:
                chaines.append(debut + y + fin[1:])
                debut = debut + y
                fin = fin[1:]
        return chaines


class DistanceElem:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self._matrice = self._calcul_matrice()
        self._alignement = self._calcul_alignement()

    def _calcul_matrice(self):
        M = []
        for i in range(len(self.b) + 1):
            M.append([0] * (len(self.a) + 1))

        for j in range(1, len(self.a) + 1):
            M[0][j] = j
        for i in range(1, len(self.b) + 1):
            M[i][0] = i

        for j in range(len(self.a)):
            for i in range(len(self.b)):
                if self.a[j] == self.b[i]:
                    x = 0
                else:
                    x = 1
                M[i + 1][j + 1] = min(M[i][j] + x, M[i + 1][j] + 1, M[i][j + 1] + 1)

        return M

    def _calcul_alignement(self):
        pass

    def matrice(self):
        return self._matrice

    def dist(self):
        return self._matrice[-1][-1]

    def _calcul_alignement(self):
        i = -1
        j = -1
        a_star = ""
        b_star = ""

        while (i >= -len(self.b)) and (j >= -len(self.a)):
            if self.a[j] == self.b[i]:
                cas_1 = self._matrice[i - 1][j - 1]
            else:
                cas_1 = self._matrice[i - 1][j - 1] + 1

            cas_2 = self._matrice[i - 1][j] + 1
            c = self._matrice[i][j - 1] + 1

            if cas_1 <= min(cas_2, c):
                a_star = self.a[j] + a_star
                b_star = self.b[i] + b_star

                i = i - 1
                j = j - 1
            elif cas_2 <= min(cas_1, c):
                a_star = VIDE + a_star
                b_star = self.b[i] + b_star

                i = i - 1
            else:
                a_star = self.a[j] + a_star
                b_star = VIDE + b_star

                j = j - 1

        if j >= -len(self.a):
            b_star = VIDE * (len(self.a) + j + 1) + b_star
            a_star = self.a[: len(self.a) + j + 1] + a_star
        if i >= -len(self.b):
            a_star = VIDE * (len(self.b) + i + 1) + a_star
            b_star = self.b[: len(self.b) + i + 1] + b_star

        return Alignement(a_star, b_star)

    def alignement(self):
        return self._alignement


class Distance(DistanceElem):
    def __init__(self, a, b, f):
        self.f = f
        super().__init__(a, b)

    def _calcul_matrice(self):
        M = []
        for i in range(len(self.b) + 1):
            M.append([0] * (len(self.a) + 1))

        for j in range(1, len(self.a) + 1):
            M[0][j] = M[0][j - 1] + self.f(self.a[j - 1])
        for i in range(1, len(self.b) + 1):
            M[i][0] = M[i - 1][0] + self.f(self.b[i - 1])

        for j in range(len(self.a)):
            for i in range(len(self.b)):
                M[i + 1][j + 1] = min(
                    M[i][j] + self.f(self.a[j], self.b[i]),
                    M[i + 1][j] + self.f(self.a[j]),
                    M[i][j + 1] + self.f(self.b[i]),
                )

        return M


def cout(x, y=None):
    if y is None:
        return 1
    elif x != y:
        return 2
    else:
        return 0


def main_alignement():
    alignement = Alignement("MER-OUS", "MARLOU-")

    print(alignement.a(), alignement.b())
    alignement.affiche()
    print("=" * 40)
    for x in alignement.evolution():
        print(x)


def main_distance_elem():
    dist = DistanceElem("ACTGATT", "GCTAATCG")

    for ligne in dist.matrice():
        print(ligne)
    print("distance : ", dist.dist())

    print(dist.a, dist.b)
    dist.alignement().affiche()

    print("=" * 40)
    DistanceElem("ACTGATT", "").alignement().affiche()
    print("=" * 40)
    DistanceElem("", "GCTAATCG").alignement().affiche()


def main_distance_general():
    dist = Distance("ACTGATT", "GCTAATCG", cout)

    for ligne in dist.matrice():
        print(ligne)


# main_alignement()
# main_distance_elem
main_distance_general()
exit()


def crer_fonction(dist):
    def f(x, y=None):
        if y is None:
            return dist[x]
        elif x < y:
            return dist[(x, y)]
        else:
            return dist[(y, x)]

    return f


def calcul_matrice(a, b, f):
    M = [[0] * len(a) for i in len(b)]
    M[0][0] = 0
    for j in range(len(a)):
        M[0][j] = M[0][j + 1] + f(a[j])
    for i in range(len(b)):
        M[i][0] = M[j + 1][0] + f(b[i])

    for i in range(len(b)):
        for j in range(len(a)):
            M[i + 1][j + 1] = min(
                M[i][j] + f(a[j], b[i]), M[i + 1][j] + f(b[i]), M[i][j + 1] + f(a[j])
            )

    return M
