import pyxel as px
from random import randint

#pyxel edit 2.pyxres

class EltGraphique:
    def __init__(self, x: float, y: float, u: int, v: int, w: int, h: int, dx: float = 0, dy: float = 0):
        self.x = x
        self.y = y
        self.u = u
        self.v = v
        self.w = w
        self.h = h
        self.dx = dx
        self.dy = dy

    def update(self):
        self.x += self.dx
        self.y += self.dy

    def draw(self):
        px.blt(self.x, self.y, 0, self.u, self.v, self.w, self.h)

    def collision(self, other: 'EltGraphique') -> bool:
        return not (
            (other.x >= self.x + self.w)
            or (other.x + other.w <= self.x)
            or (other.y >= self.y + self.h)
            or (other.y + other.h <= self.y)
        )




class Missiles(EltGraphique):
    pass
        



class Ennemis(EltGraphique):
    def __init__(self, x: float, y: float, u: int, v: int, w: int, h: int, dx: float = 0, dy: float = 0):
        super().__init__(x, y, u, v, w, h, dx, dy)
        self.missiles_ennemis: list[Missiles] = []
        self.PV = 50
 
    def tirer(self):
        self.missiles_ennemis.append(Missiles(self.x, self.y, 42, 34, 4, 4, 0, 4))

    def update(self):
        super().update()
        for m in self.missiles_ennemis:
            m.update()

    def draw(self):
        super().draw()
        for m in self.missiles_ennemis:
            m.draw()





class Vaisseaux(EltGraphique):
    def __init__(self, x: float, y: float, u: int, v: int, w: int, h: int):
        super().__init__(x, y, u, v, w, h)
        self.missiles_allier: list[Missiles] = []
        self.PV = 100

    def tirer(self):
        self.missiles_allier.append(Missiles(self.x + 4 * self.w / 10, self.y, 42, 34, 4, 4, 0, -7))

    def update(self): 
        self.x = (self.x + self.dx) % px.width
        self.y = (self.y + self.dy) % px.height
        for m in self.missiles_allier:
            m.update()

    def draw(self):
        super().draw()
        for m in self.missiles_allier:
            m.draw()





class Jeu:
    def __init__(self):
        self.vaisseau = Vaisseaux(px.width/2, px.height/2, 0, 40, 16, 16)
        self.ennemis: list[Ennemis] = [Ennemis(px.width/2, 0, 32, 40, 16, 16, 0, 1)]
        self.score = 0

    def check_collisions(self):
        for e in self.ennemis:
            for v in self.vaisseau.missiles_allier:
                if v.collision(e):
                    self.vaisseau.missiles_allier.remove(v)
                    e.PV -= 10 
                    if e.PV <= 0:
                        self.ennemis.remove(e)
                        self.score += 1

            for m in e.missiles_ennemis:
                if m.collision(self.vaisseau):
                    e.missiles_ennemis.remove(m)
                    self.vaisseau.PV -= 10
                    if self.vaisseau.PV <= 0:
                        print('game over')
                        px.quit()

    def print_score(self):
            
        return px.text(2, 2, f'SCORE : {self.score}', 2)
        """A = [0, 9, 17, 25, 33, 41, 49, 57, 65, 74]
        a = A[self.score]
        return px.blt(40, 2, 0, a, 74, 7, 11)"""
    

    def spawn_ennemis(self):
        self.ennemis.append(Ennemis(randint(0, px.width-15), 0, 32, 40, 16, 16, 0, 1))


    def update(self):
        """
        Gère les événements utilisateur pour déplacer le vaisseau.
        """
        # Modification du vecteur directeur selon les touches fléchées
        
        if px.btn(px.KEY_RIGHT):
            self.vaisseau.dx = 5
        elif px.btn(px.KEY_LEFT):
            self.vaisseau.dx = -5
        else :
            self.vaisseau.dx = 0
        if px.btn(px.KEY_DOWN):
            self.vaisseau.dy = 5
        elif px.btn(px.KEY_UP):
            self.vaisseau.dy = -5
        else :
            self.vaisseau.dy = 0
        
        if px.btnp(px.KEY_SPACE):
            self.vaisseau.tirer()
        for de in self.ennemis: 
            if randint(0, 35) == 1:
                de.tirer()
        
        self.check_collisions()

        if randint(0, 45) == 1:
            self.spawn_ennemis()

        self.vaisseau.update()
        for e in self.ennemis:
            e.update() 
        


    def draw(self):
        # Remplir l'écran en noir
        px.cls(0)
        self.print_score()
        self.vaisseau.draw()
        for e in self.ennemis:
            e.draw()    




if __name__ == "__main__":
    # Démarre l'application
    px.init(200, 200, title="Pixel en Mouvement", fps = 20)  #la taille de la feunetre est adapté pour que le pyxel soit carré
    appli = Jeu()
    px.load("2.pyxres")
    px.run(appli.update, appli.draw)