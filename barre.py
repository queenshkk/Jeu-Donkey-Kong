import pygame
from constantes import *
class Barre:
    def __init__ (self):
        self.delay=6
        self.position=8
        self.etat=Constantes.NORMAL

    def actualiserBarre(self):
        self.delay -= 1

        if self.delay == 0:
            if self.position >= 1:
                self.position-=1
                self.delay=6

            else:
                self.etat= Constantes.TERMINE



