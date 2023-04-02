from pyglet import shapes

import utils

class Grille:
    def __init__(self, x, y, nombre_lignes, nombre_colonnes, dimension_case, couleur):
        self.x = x
        self.y = y
        self.nombre_lignes = nombre_lignes
        self.nombre_colonnes = nombre_colonnes
        self.dimension_case = dimension_case

        self.cases = []
        for i in range(nombre_lignes):
            ligne = []
            for j in range(nombre_colonnes):
                ligne.append(None)
            self.cases.append(ligne)

        self.quadrillage = []
        for j in range(nombre_colonnes + 1):
            self.quadrillage.append(
                shapes.Line(
                    self.x + j * dimension_case,
                    self.y,
                    self.x + j * dimension_case,
                    self.y + nombre_lignes * dimension_case,
                    color=couleur,
                )
            )
        for i in range(nombre_lignes + 1):
            self.quadrillage.append(
                shapes.Line(
                    self.x,
                    self.y + i * dimension_case,
                    self.x + nombre_colonnes * dimension_case,
                    self.y + i * dimension_case,
                    color=couleur,
                )
            )

    def draw(self):
        for line in self.quadrillage:
            line.draw()

        for i in range(self.nombre_lignes):
            for j in range(self.nombre_colonnes):
                if self.cases[i][j] != None:
                    self.cases[i][j].draw()

    def déplace(self, dl, dc):
        dx = dc * self.dimension_case
        dy = -dl * self.dimension_case

        self.x += dx
        self.y += dy

        for line in self.quadrillage:
            line.x += dx
            line.y += dy

        for i in range(self.nombre_lignes):
            for j in range(self.nombre_colonnes):
                if self.cases[i][j] != None:
                    self.cases[i][j].x += dx
                    self.cases[i][j].y += dy

    def xy_vers_lc(self, x, y):
        return utils.xy_vers_lc(x, y, self.x, self.y, self.dimension_case, self.nombre_lignes)

    def lc_vers_xy(self, l, c):
        return utils.lc_vers_xy(l, c, self.x, self.y, self.dimension_case, self.nombre_lignes)

    def rotation(self):
        self.cases = utils.rotation(self.cases)

        for i in range(self.nombre_lignes):
            for j in range(self.nombre_colonnes):
                x, y = self.lc_vers_xy(i, j)
                if self.cases[i][j] != None:
                    self.cases[i][j].x = x
                    self.cases[i][j].y = y

    def supprime_ligne(self):
        for i in range(self.nombre_lignes):
            a_supprimer = True
            while a_supprimer:
                for j in range(self.nombre_colonnes):
                    if self.cases[i][j] == None:
                        a_supprimer = False
                
                if a_supprimer:            
                    for k in range(i, 0, -1):
                        for j in range(self.nombre_colonnes):                        
                            self.cases[k][j] = self.cases[k-1][j]
                            if self.cases[k][j] != None:
                                x, y = self.lc_vers_xy(k, j)
                                self.cases[k][j].x = x
                                self.cases[k][j].y = y
                    
                    for j in range(self.nombre_colonnes):                        
                        self.cases[0][j] = None


                