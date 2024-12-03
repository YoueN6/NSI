import pyxel as px
import random
from random import randint

#pyxel edit 2.pyxres

class Pixel:
    def __init__(self, x:float, y: float, dx: float=0, dy:float=0, color:float=0):
        """
        Initialise un pixel avec une position (x, y), un vecteur directeur (dx, dy) et une couleur.
        """
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.color = color

    def update(self):
        """
        Le pyxel se déplace toujours de son vecteur directeur
        """
        self.x = (self.x + self.dx) % px.width
        self.y = (self.y + self.dy) % px.height

    def draw(self):
        """
        Dessine le pixel sur l'écran.
        """
        #px.pset(int(self.x), int(self.y), self.color)
        px.blt(self.x, self.y, 0, 0, 0, 40, 40)


class vaisseaux:
    def __init__(self, x:float, y: float, dx: float=0, dy:float=0, color:float=0):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.color = color
        
    def update(self):
        """
        Le pyxel se déplace toujours de son vecteur directeur
        """
        self.x = (self.x + self.dx) % px.width
        self.y = (self.y + self.dy) % px.height

    def draw(self):
        """
        Dessine le pixel sur l'écran.
        """
        px.blt(self.x, self.y, 0, 0, 0, 40, 40)
        

class missiles:
    def __init__(self, x:float, y: float, dy:float=0, color:float=0):
        self.x = x
        self.y = y
        self.dy = dy
        self.color = color

    def update(self):
        self.y -= self.dy

    def draw(self):
        px.blt(self.x, self.y, 0, 0, 0, 40, 40)
        
        

        
class Jeu:
    def __init__(self):
        """
        Un jeu gère un Pixel.
        """

        self.pixel: list[Pixel] = [Pixel(px.width/2, px.height/2, color = 5)]
        

    def update(self):
        """
        Gère les événements utilisateur pour déplacer le pixel.
        """
        if px.btn(px.KEY_SPACE):
            self.spawn_pixel()
        if px.btn(px.KEY_P):
            if len(self.pixel) > 0 :
                random.shuffle(self.pixel)
                self.pixel.pop()
        # Modification du vecteur directeur selon les touches fléchées
        
        if px.btn(px.KEY_RIGHT):
            for p in self.pixel:
                p.dx = 1
        elif px.btn(px.KEY_LEFT):
            for p in self.pixel:
                p.dx = -1
        else :
            for p in self.pixel:
                p.dx = 0
        
        if px.btn(px.KEY_DOWN):
            for p in self.pixel:
                p.dy = 1
        elif px.btn(px.KEY_UP):
            for p in self.pixel:
                p.dy = -1
        else :
            for p in self.pixel:
                p.dy = 0
        

        # Le jeu demande au pixel de se mettre à jour
        
        
        for pixels in self.pixel:
            pixels.update()
        

    def draw(self):
        """
        Efface l'écran et dessine le pixel.
        """
        # Remplir l'écran en noir
        px.cls(0)
        # Le jeu demande au pixel de se dessiner
        for pixels in self.pixel:
            pixels.draw()

    def spawn_pixel(self):
        """
        Fais apparaitre un nouveau pixel aléatoirement
        """
        self.pixel.append(Pixel(randint(0, px.width-1), randint(0, px.height-1), color = randint(1, 16)))

if __name__ == "__main__":
    # Démarre l'application
    px.init(300, 300, title="Pixel en Mouvement", fps = 200)  #la taille de la feunetre est adapté pour que le pyxel soit carré
    appli = Jeu()
    px.load("2.pyxres")
    px.run(appli.update, appli.draw)
    
    
    
    
    
