import random

MIN_VALEUR = 1
MAX_VALEUR = 6


class Dé:
    def __init__(self, position=1):
        self._positon = 1  # init
        self.position = position  # utilisation du mutateur

    def lancer(self):
        self.position = random.randrange(MIN_VALEUR, MAX_VALEUR + 1)

        return self

    def __str__(self):
        if self.position == 1:
            return "⚀"
        elif self.position == 2:            
            return "⚁"
        elif self.position == 3:            
            return "⚂"
        elif self.position == 4:            
            return "⚃"
        elif self.position == 5:            
            return "⚄"
        else:
            return "⚅"


    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, nouvelle_position):
        if nouvelle_position < MIN_VALEUR:
            nouvelle_position = MIN_VALEUR
        elif nouvelle_position > MAX_VALEUR:
            nouvelle_position = MAX_VALEUR

        self._position = nouvelle_position

class TapisVert:
    def __init__(self):
        temp = []
        for i in range(5):
            temp.append(Dé())

        self._dés = tuple(temp)

    def __str__(self):
        return " - ".join([str(x) for x in self.dés])
        
    @property
    def dés(self):
        return self._dés

    def lancer(self):
        for dé in self.dés:
            dé.lancer()

    # def _positions(self):
    #     count = [0] * 7
    #     for dice in self.dés:
    #         count[dice.get_position()] += 1
    #     return count

    # def nb_des_identiques(self, nb_times):
    #     count = self._positions()

    #     for i in range(len(count)):
    #         if count[i] >= nb_times:
    #             return True
    #     return False

    # def a_une_pair(self):
    #     return self.nb_des_identiques(2)

    # def a_un_brelan(self):
    #     return self.nb_des_identiques(3)

    # def a_un_carre(self):
    #     return self.nb_des_identiques(4)

    # def a_une_double_paire(self):
    #     count = self._positions()
    #     nb_2 = 0
    #     for x in count:
    #         if x > 1:
    #             nb_2 += 1
    #     return nb_2 > 1

    # def a_un_full(self):
    #     count = self._positions()
    #     nb_2 = 0
    #     nb_3 = 0
    #     for x in count:
    #         if x == 2:
    #             nb_2 += 1
    #         elif x == 3:
    #             nb_3 += 1
    #     return (nb_2 > 0) and (nb_3 > 0)