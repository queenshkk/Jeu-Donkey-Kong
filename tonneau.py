import pygame
from  constantes import *

class Tonneau:
    def __init__(self, position):
        self.position=position
        self.delaiTonneau=6
        self.etat=Constantes.NORMAL
        self.ligne=0

    def actualiserTonneau(self):
        self.delaiTonneau-=1
        if self.delaiTonneau == 0:
            self.delaiTonneau=6

            if self.ligne == 0 or self.ligne==1:
                    self.ligne+=1
            elif self.ligne==2:
                self.ligne=3
                if self.position == 2:
                    self.position = 6
                elif self.position==1:
                    self.position = 4
                elif self.position==0:
                    self.position = 2
            elif self.ligne==3:
                self.position-=1
                if self.position==0:
                    self.ligne=4
            elif self.ligne==4:
                self.ligne = 5
            elif self.ligne==5:
                if self.position <10:
                    self.position+=1
                elif self.position==10:
                    self.ligne=6
            elif self.ligne==6:
                self.position-=1
                if self.position==0:
                    self.etat = Constantes.TERMINE


