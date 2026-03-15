import pygame
from constantes import *
from random import*

class DonkeyKong:
    def __init__(self):
        self.position=0
        self.delai=6
        self.etat=Constantes.NORMAL
        self.delaiAttente=42
        self.delaiEtatTonneau=0
        self.lancerTonneau=0

    def actualiserDonkeyKong(self):
        self.delai -= 1
        if self.delai == 0:
            self.delai = 6
            self.val=randint(0, 2)

            if self.val==1:
                if self.position>0:
                    self.position-=1
            elif self.val==2:
                if self.position<2:
                    self.position+=1

        self.delaiAttente -= 1
        if self.delaiAttente == 0:
            self.etat=Constantes.TONNEAU
            self.delaiAttente = randint(70,90)
            self.delaiEtatTonneau=6

        if self.etat==Constantes.TONNEAU:
            self.delaiEtatTonneau-=1
            if self.delaiEtatTonneau==0:
                self.lancerTonneau=1
                self.etat=Constantes.NORMAL


