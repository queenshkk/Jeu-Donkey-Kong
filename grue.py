import pygame
from constantes import *

class Grue:
    def __init__(self):
        self.etatGrue=Constantes.TERMINE
        self.delaiCrochet=6
        self.sens='c'
        self.posCrochet=0
        self.delaiGrue=100


    def actualiserGrue(self):
        if self.etatGrue==Constantes.NORMAL:
            self.delaiCrochet-=1
            self.delaiGrue-=1

            if self.delaiCrochet==0:
                print("ok")

                print(self.delaiCrochet)
                if self.sens=='c':
                    if self.posCrochet<4:
                        self.posCrochet+=1
                    elif self.posCrochet==4:
                        self.sens='d'
                elif self.sens=='d':
                    if self.posCrochet>0:
                        self.posCrochet-=1
                    elif self.posCrochet==0:
                        self.sens='c'

                self.delaiCrochet=6

            if self.delaiGrue==0:
                self.etatGrue=Constantes.TERMINE
                self.posCrochet=0
                self.sens='c'




