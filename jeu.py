from donkeykong import DonkeyKong
from presentation import *
from mario import *
from timerbarre import *
from barre import *
from constantes import *
from grue import *
from tonneau import *

class Jeu:
    def __init__(self):
        self.presentation = Presentation() 
        self.mario = Mario()
        self.timerBarre=TimerBarres()
        self.barres=[]
        self.echec=0
        self.donkeykong=DonkeyKong()
        self.grue=Grue()
        self.nbCrochets=4
        self.score=0
        self.listeTonneaux=[]
    # ----------------------------------------------------------------------------
    # Méthode contenant la boucle principale du jeu

    def demarrer(self):
        while True: 
            # récupérer l'événement du joueur et changer l'état de Mario

            val=self.timerBarre.actualiserTimerBarre()

            if val==True:
                barre=Barre()
                self.barres.append(barre)

            if len(self.barres) !=0 and self.barres[0].etat==Constantes.TERMINE:
                del self.barres[0]


            if len(self.barres) !=0 and self.mario.ligne==2 and self.barres[0].position==0:
                self.echec+=1
                time.sleep(1.5)
                self.RetourMarioDepart()
                self.mario.ligne=4
                self.mario.position=0

            if len(self.barres) != 0 and self.mario.ligne == 3 and self.mario.etat==Constantes.SAUT and \
                    (self.mario.position==4 or self.mario.position==5 or self.mario.position==6) and \
                    (self.barres[0].position == 4 or self.barres[0].position == 5 or self.barres[0].position == 6):
                self.echec += 1
                time.sleep(1.5)
                self.RetourMarioDepart()
                self.mario.ligne = 4
                self.mario.position=0

            '''si Mario à la ligne 2 et si y'a la premiere barre en position 0
            --> incrementer le nomnbre d'echec, attendre un certain temps et remettre mario à la ligne 4 en position 0'''


            if self.mario.ligne==0 and self.mario.position==0 and self.mario.etat==Constantes.LEVIER:
                self.grue.etatGrue=Constantes.NORMAL
                self.grue.delaiGrue=100


            if self.mario.ligne==0 and self.mario.position==2 and self.mario.etat==Constantes.SAUT:
                if self.grue.etatGrue==Constantes.NORMAL and self.grue.posCrochet==0:
                    self.nbCrochets-=1

                    if self.nbCrochets!=0:
                        for i in range (1, 4):
                            self.presentation.effacerImageInterne()
                            self.presentation.afficherMarioSucces(i)
                            self.presentation.actualiserFenetreGraphique()

                            time.sleep(0.8)
                        self.score+=5
                    else:
                        for i in range (1, 6):
                            self.presentation.effacerImageInterne()
                            self.presentation.afficherMarioSuccesDK(i)
                            self.presentation.actualiserFenetreGraphique()

                            time.sleep(0.8)
                        self.score += 10
                        self.nbCrochets=4
                    self.mario.etat=Constantes.NORMAL
                    self.RetourMarioDepart()
                    self.mario.ligne=4
                    self.mario.position=0
                else:
                    for i in range(1, 4):
                        self.presentation.effacerImageInterne()
                        self.presentation.afficherMarioEchec(i)
                        self.presentation.actualiserFenetreGraphique()
                    self.echec+=1
                    self.mario.etat = Constantes.NORMAL
                    self.RetourMarioDepart()
                    self.mario.ligne = 4
                    self.mario.position = 0

            if self.donkeykong.lancerTonneau==1:
                tonneau=Tonneau(self.donkeykong.position)
                self.listeTonneaux.append(tonneau)
                self.donkeykong.lancerTonneau=0

            '''Supprimer de la liste des tonneaux'''
            i=0
            while i <len(self.listeTonneaux):
                tonneau = self.listeTonneaux[i]
                if tonneau.etat == Constantes.TERMINE:
                    self.listeTonneaux.pop(i)
                else:
                    i += 1

            for tonneau in self.listeTonneaux:
                if self.mario.ligne==0 and tonneau.ligne==1:
                    if self.mario.position==tonneau.position:
                        self.echec += 1
                        self.RetourMarioDepart()
                        self.mario.ligne = 4
                        self.mario.position = 0

                elif self.mario.ligne==1 and tonneau.ligne==3 and tonneau.position==1:
                        self.echec += 1
                        self.RetourMarioDepart()
                        self.mario.ligne = 4
                        self.mario.position = 0
                elif self.mario.ligne==3 and tonneau.ligne==5:
                    if self.mario.position==0 and tonneau.position==1:
                        self.echec += 1
                        self.RetourMarioDepart()
                        self.mario.ligne = 4
                        self.mario.position = 0
                    elif self.mario.position==1 and tonneau.position==2 :
                        self.echec += 1
                        self.mario.ligne = 4
                        self.RetourMarioDepart()
                        self.mario.position = 0
                    elif self.mario.position == 2 and tonneau.position == 3:
                        self.echec += 1
                        self.RetourMarioDepart()
                        self.mario.ligne = 4
                        self.mario.position = 0
                    elif self.mario.position == 3 and tonneau.position == 4:
                        self.echec += 1
                        self.RetourMarioDepart()
                        self.mario.ligne = 4
                        self.mario.position = 0
                    elif self.mario.position==4 and tonneau.position==5:
                        if self.mario.etat!=Constantes.SAUT:
                            self.echec += 1
                            self.RetourMarioDepart()
                            self.mario.ligne=4
                            self.mario.position=0
                        elif self.mario.etat==Constantes.SAUT and tonneau.delaiTonneau==1:
                            self.score+=1
                    elif self.mario.position==5 and tonneau.position==6:
                        if self.mario.etat != Constantes.SAUT:
                            self.echec += 1
                            self.RetourMarioDepart()
                            self.mario.ligne = 4
                            self.mario.position = 0
                        elif self.mario.etat == Constantes.SAUT and tonneau.delaiTonneau==1:
                            self.score += 1
                    elif self.mario.position == 6 and tonneau.position == 7:
                        if self.mario.etat != Constantes.SAUT:
                            self.echec += 1
                            self.RetourMarioDepart()
                            self.mario.ligne = 4
                            self.mario.position = 0
                        elif self.mario.etat == Constantes.SAUT and tonneau.delaiTonneau==1:
                            self.score += 1
                    elif self.mario.position==7 and tonneau.position==8:
                        self.echec += 1
                        self.RetourMarioDepart()
                        self.mario.ligne = 4
                        self.mario.position = 0
                    elif self.mario.position==8 and tonneau.position==9:
                        self.echec += 1
                        self.RetourMarioDepart()
                        self.mario.ligne = 4
                        self.mario.position = 0

                elif self.mario.ligne==4 and tonneau.ligne==6:
                    if self.mario.position==0 and tonneau.position==1:
                        if self.mario.etat != Constantes.SAUT:
                            self.echec += 1
                            self.RetourMarioDepart()
                            self.mario.ligne = 4
                            self.mario.position = 0
                        elif self.mario.etat == Constantes.SAUT and tonneau.delaiTonneau==1:
                            self.score += 1
                    elif self.mario.position==1 and tonneau.position==2 :
                        self.echec += 1
                        self.RetourMarioDepart()
                        self.mario.ligne = 4
                        self.mario.position = 0
                    elif self.mario.position == 2 and tonneau.position == 3:
                        self.echec += 1
                        self.RetourMarioDepart()
                        self.mario.ligne = 4
                        self.mario.position = 0
                    elif self.mario.position == 3 and tonneau.position == 4:
                        self.echec += 1
                        self.RetourMarioDepart()
                        self.mario.ligne = 4
                        self.mario.position = 0
                    elif self.mario.position==4 and tonneau.position==5:
                        self.echec += 1
                        self.RetourMarioDepart()
                        self.mario.ligne=4
                        self.mario.position=0
                    elif self.mario.position==5 and tonneau.position==6:
                        self.echec += 1
                        self.RetourMarioDepart()
                        self.mario.ligne = 4
                        self.mario.position = 0
                    elif self.mario.position == 6 and tonneau.position == 7:
                        if self.mario.etat != Constantes.SAUT:
                            self.echec += 1
                            self.RetourMarioDepart()
                            self.mario.ligne = 4
                            self.mario.position = 0
                        elif self.mario.etat == Constantes.SAUT and tonneau.delaiTonneau==1:
                            self.score += 1
                    elif self.mario.position==7 and tonneau.position==8:
                        self.echec += 1
                        self.RetourMarioDepart()
                        self.mario.ligne = 4
                        self.mario.position = 0
                    elif self.mario.position==8 and tonneau.position==9:
                        self.echec += 1
                        self.RetourMarioDepart()
                        self.mario.ligne = 4
                        self.mario.position = 0

            i=0
            while i<len(self.listeTonneaux):
                j=i+1
                while j<len(self.listeTonneaux):
                    if self.listeTonneaux[i]==self.listeTonneaux[j]:
                        self.listeTonneaux.pop(i)
                    j+=1
                i+=1

            #Mettre tout à jour
            for barre in self.barres:
                barre.actualiserBarre()

            self.donkeykong.actualiserDonkeyKong()

            self.grue.actualiserGrue()

            for tonneau in self.listeTonneaux:
                tonneau.actualiserTonneau()

            self.mario.actualiser(self.presentation.lireEvenement())

            # Mettre à jour l'image à l'écran
            self.actualiserEcran()

            if self.echec == 3:
                self.presentation.attendreFermetureFenetre()

            # attendre 100 millisecondes (délai de référence)

            time.sleep(0.1)

    # ----------------------------------------------------------------------------
    # mettre à jour l'image à l'écran

    def actualiserEcran(self):
        self.presentation.effacerImageInterne()

        self.presentation.afficherMario(self.mario.ligne, self.mario.position,
                                        self.mario.etat)
        '''for barre in self.barres:
            self.presentation.afficherBarre(barre.position)'''
        for i in range (len(self.barres)):
            self.presentation.afficherBarre(self.barres[i].position)

        self.presentation.afficherEchecs(self.echec)
        self.presentation.afficherDonkeyKong(self.donkeykong.position, self.donkeykong.etat)
        self.presentation.afficherLevier(self.grue.etatGrue)
        self.presentation.afficherGrue(self.grue.posCrochet, self.grue.etatGrue)
        self.presentation.afficherEchafaudage(self.nbCrochets)

        for tonneau in self.listeTonneaux:
            self.presentation.afficherTonneau(tonneau.ligne, tonneau.position)


        self.presentation.afficherScore(self.score)

        self.presentation.actualiserFenetreGraphique()

    def RetourMarioDepart(self):
        i=0
        sup=0
        while i<len(self.listeTonneaux):
            if self.listeTonneaux[i].ligne==6:
                if self.listeTonneaux[i].position==1:
                    self.listeTonneaux.pop(i)
                    sup=1
                elif self.listeTonneaux[i].position == 2:
                    self.listeTonneaux.pop(i)
                    sup=1
                elif self.listeTonneaux[i].position==3:
                    self.listeTonneaux.pop(i)
                    sup=1

            if sup==1:
                sup=0
            else:
                i+=1


