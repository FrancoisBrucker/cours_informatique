class A:
    CTE = "un attribut de classe"

    def __init__(self, a):
        self.a = a

    def truc_que_fait_a(self):
        print("Truc défini dans la classe mère")

    def truc_que_fait_a(self):
        print("Autre truc dans la classe mère")

    def j_herite(self, x):
        print(x)


class B(A):
    def __init__(self, a, b):
        super().__init__(a)
        self.b = b

    def autre_truc(self):
        print("C'est mon autre truc à moi")

    def que_de_b(self):
        print("Méthode seulement de la classe fille")

    def j_herite(self, x):
        super().j_herite(x)
        print(x.upper())


if __name__ == "__main__":
    objet_a = A(10)
    objet_b = B(3, 7)

    print(objet_a.a)
    # print(objet_a.b)
    print(objet_b.a)
    print(objet_b.b)
    objet_a.truc_que_fait_a()
    # objet_a.autre_truc()
    # objet_a.que_de_b()
    objet_b.truc_que_fait_a()
    objet_b.autre_truc()
    objet_b.que_de_b()
    print(objet_b.CTE)
    print(A.CTE)
