import pygame
from random import*

class TimerBarres:
    def __init__(self):
        self.delay=85
        self.compteur=500
        self.val=85

    def actualiserTimerBarre(self):
        self.delay-=1
        self.compteur-=1

        if self.compteur==0:
            self.val=randint(70, 100)
            self.compteur=500

        if self.delay==0:
            self.delay=self.val
            return True
        return False