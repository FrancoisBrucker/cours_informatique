# Corrigé — Examen terminal Programmation L1 MPCI 2026
#
# Le sujet s'articule autour d'une application de gestion de bibliothèque
# personnelle et vise à évaluer deux compétences :
#
#   1. Programmation orientée objet — conception et implémentation de classes
#      Python (attributs, encapsulation, méthodes) à travers les classes
#      Livre et Bibliothèque.
#
#   2. Pattern MVC (Modèle-Vue-Contrôleur) — comprendre la séparation des
#      responsabilités (exercice 2) puis l'implémenter concrètement avec
#      VueTerminal et Contrôleur (exercice 3), de façon à ce que la vue
#      soit interchangeable sans toucher au reste.

# ============================================================
# Exercice 1 — Programmation orientée objet
# ============================================================

class Livre:
    def __init__(self, titre: str, auteur: str):
        self.titre = titre
        self.auteur = auteur
        self._disponible = True

    # Q1.1.2 — accesseur
    def est_disponible(self) -> bool:
        return self._disponible

    # Q1.1.3
    def emprunter(self) -> bool:
        if self._disponible:
            self._disponible = False
            return True
        return False

    # Q1.1.3 (suite implicite) — retourner
    def retourner(self):
        self._disponible = True

    # Q1.1.4
    def __str__(self) -> str:
        etat = "disponible" if self._disponible else "emprunté"
        return f"{self.titre} ({self.auteur}) [{etat}]"


class Bibliothèque:
    def __init__(self):
        self._livres: list = []

    # Q1.2.1
    def ajouter(self, livre: Livre):
        self._livres.append(livre)

    def livres_disponibles(self) -> list:
        return [l for l in self._livres if l.est_disponible()]

    # Q1.2.2
    def chercher(self, titre: str):
        for livre in self._livres:
            if livre.titre == titre:
                return livre
        return None

    def emprunter(self, titre: str) -> bool:
        livre = self.chercher(titre)
        if livre is None:
            return False
        return livre.emprunter()

    def retourner(self, titre: str) -> bool:
        livre = self.chercher(titre)
        if livre is None:
            return False
        livre.retourner()
        return True


# ============================================================
# Exercice 2 — Refactoring partiel (Q2.2.1)
# Réécriture du bloc "elif choix == '2'" en utilisant Bibliothèque
# ============================================================
#
#   elif choix == "2":
#       titre = vue.demander_titre()          # (d) → Vue
#       succes = modele.emprunter(titre)      # (e)(f) → Modèle
#       if succes:
#           vue.afficher_message("Emprunté.")
#       else:
#           vue.afficher_message("Indisponible ou introuvable.")


# ============================================================
# Exercice 3 — Implémentation du patron MVC
# ============================================================

class VueTerminal:
    # Q3.1.1
    def afficher_livres(self, livres: list):
        if not livres:
            print("Aucun livre disponible.")
        else:
            for livre in livres:
                print(str(livre))

    def afficher_message(self, message: str):
        print(message)

    def demander_titre(self) -> str:
        return input("Titre : ")

    def afficher_menu(self):
        print("1. Livres disponibles  2. Emprunter  0. Quitter")

    def demander_choix(self) -> str:
        return input("Votre choix : ")


class Contrôleur:
    # Q3.2.1
    def __init__(self, modele: Bibliothèque, vue: VueTerminal):
        self._modele = modele
        self._vue = vue

    def afficher_disponibles(self):
        livres = self._modele.livres_disponibles()
        self._vue.afficher_livres(livres)

    def emprunter(self):
        titre = self._vue.demander_titre()
        succes = self._modele.emprunter(titre)
        if succes:
            self._vue.afficher_message("Emprunté avec succès.")
        else:
            self._vue.afficher_message("Indisponible ou introuvable.")

    # Q3.2.2
    def lancer(self):
        while True:
            self._vue.afficher_menu()
            choix = self._vue.demander_choix()
            if choix == "1":
                self.afficher_disponibles()
            elif choix == "2":
                self.emprunter()
            elif choix == "0":
                break


# Q3.3.2 — Lancement de l'application
if __name__ == "__main__":
    modele = Bibliothèque()
    modele.ajouter(Livre("Le Petit Prince", "Antoine de Saint-Exupéry"))
    modele.ajouter(Livre("1984", "George Orwell"))

    vue = VueTerminal()
    controleur = Contrôleur(modele, vue)
    controleur.lancer()
