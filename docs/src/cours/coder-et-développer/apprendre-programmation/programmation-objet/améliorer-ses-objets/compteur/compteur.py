class Compteur:
    def __init__(self, pas=1, valeur=0):
        assert pas != 0

        self._pas = pas
        self.valeur = valeur

    def _get_pas(self):
        return self._pas

    def _set_pas(self, pas):
        assert pas != 0

        self._pas = pas

    pas = property(_get_pas, _set_pas)
    
    def incrémente(self):
        self.valeur = self.valeur + self.pas

    def __str__(self):
        return "Le compteur vaut " + str(self.valeur)

    def __repr__(self):
        return f"Compteur(pas={self.pas}, valeur={self.valeur})"

    def __lt__(self, other):
        return self.valeur < other.valeur

    def __le__(self, other):
        return self.valeur <= other.valeur

    def __eq__(self, other):
        return other.valeur == self.valeur
