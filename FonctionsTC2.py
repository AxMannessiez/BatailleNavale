#!/usr/bien/python3
# -*- coding: utf-8 -*-
"""
@author : Axel MANNESSIEZ & Benoit MARCILLAT

"""
#fichier : "FonctionsTC2.py"
######################################################################################


############################
#BIBLIOTHÈQUES À IMPORTER :
import pygame
from pygame import *
from pygame.locals import *
############################


def ReplacementB(x,y):
    """
    Fonction recadrant le bateau à l'emplacement exact sur la grille 
    correspondant
    """
    for i in range (560,1000,40):
        if x<i:
            x=i-40
            break
    for i in range (240,680,40):
        if y<i:
            y=i-40
            break
    return(x,y)

def ReplacementTir(cible):
    """
    Fonction recadrant le tir à l'emplacement exact sur la grille correspondant
    """
    x,y=cible
    for i in range (80,481,40):         #chaque case etant des carée de 40X40,on cherche l'arondi le plus proche pour la valeur de x
        if x<i:
            x=i-40
            break
    for i in range (80,481,40):         #et de Y
        if y<i:
            y=i-40
            break
    return(x,y)

def Tire(cible,image):
    """
    Fonction affichant une image sur la grille lorsque que l'utilisateur clique
    sur une case pour tirer
    """
    x,y=cible
    fenetre.blit(image,(x,y))
    pygame.display.flip()


def Affichage(Cas):
    """
    Fonction affichant soit les différentes bulles de texte et les différents
    caches en fonction de l'argument donnée
    """
    cacheR = pygame.image.load("Images/cacheR.jpg").convert()
    cachePB = pygame.image.load("Images/cachePB.jpg").convert()
    cacheTC = pygame.image.load("Images/cacheTC.jpg").convert()
    placement = pygame.image.load("Images/placement.jpg").convert()
    touchecoule = pygame.image.load("Images/touchecoule.jpg").convert()
    if Cas == "PB" :
        fenetre.blit(placement, (600,30))
        pygame.display.flip()
    elif Cas == "CachePB" :
        fenetre.blit(cachePB, (600,30))
        pygame.display.flip()
    elif Cas == "CacheR" :
        fenetre.blit(cacheR, (1025,569))
        pygame.display.flip()
    elif Cas == "TC" :
        fenetre.blit(touchecoule, (790,35))
        pygame.display.flip()
    elif Cas == "CacheTC" :
        fenetre.blit(cacheTC, (790,35))
        pygame.display.flip()
        

def PixTab(x,y) :
    """
    Fonction convertissant les positions en pixels en coordonnées de la grille
    de droite
    """
    X=int((x-560)/40)
    Y=int((y-240)/40)
    return(X,Y)
    
def PixTab2(x,y) :
    """
    Fonction convertissant les positions en pixels en coordonnées de la grille
    de gauche
    """
    X=int((x-80)/40)
    Y=int((y-80)/40)
    return(X,Y)
    
    
def TabPix(x,y):
    """
    Fonction convertissant les coordonnées de la grille de droite en positions
    en pixels 
    """
    X=int(x*40+560)
    Y=int(y*40+240)
    return(X,Y)
    
def TabPix2(x,y):
    """
    Fonction convertissant les coordonnées de la grille de gauche en positions
    en pixels 
    """
    X=int(x*40+80)
    Y=int(y*40+80)
    return(X,Y)

def RetourBateau(Matrice,ListeB,ListeC):
    """
    Fonction prenant en argument les données récupérées après les clics de
    l'utilisateur et mettant à jour la matrice des bateaux et la liste des
    bateaux
    """
    LT=[5,4,3,3,2]
    for i in range (5) : #pour chaque bateau
        taille=LT[i]
        x,y,r=ListeC[i]     #On sélectionne les données du bateau en cours
        x,y=PixTab(x,y)     #On convertit en tableau
        B=[]
        if r==0 :           #Si le bateau est horizontal
            for i in range (x,x+taille) :
                Matrice[y][i]=1
                B.append((i,y))
            ListeB.append(B)
        else :              #Si le bateau est vertical
            for i in range (y,y+taille) :
                Matrice[i][x]=1
                B.append((x,i))
            ListeB.append(B)
    

def PlaceBateaux2(Matrice,ListeB):
    """
    Fonction affichant l'interface graphique pour permettre à l'utilisateur de
    placer ses bateaux, en mettant à jour la matrice des bateaux, la liste des
    bateaux et les orientations des bateaux
    """
    pygame.init()
    global fenetre
    fenetre = pygame.display.set_mode((1280, 720))   
    
                ###ouverture :###
    
    fond = pygame.image.load("Images/fond_bateau.jpg").convert()
    bateau1=pygame.image.load("Images/bateau_5x5.jpg").convert()
    bateau2=pygame.image.load("Images/bateau_4x4.jpg").convert()
    bateau3=pygame.image.load("Images/bateau_3x3.jpg").convert()
    bateau4=pygame.image.load("Images/bateau_3x3_copie.jpg").convert()
    bateau5=pygame.image.load("Images/bateau_2x2.jpg").convert()
    bateau=bateau1     
    fenetre.blit(fond, (0,0))
    fenetre.blit(bateau, (1070,250))
    pygame.display.flip()
    
    continuer = 1           ##initialisation
    position=0   
    c=0
    rotation=0
    numbateau=1             #compteur pour savoir quel bateau on affiche
    rotbateau1=0            #on par du principe que tout les bateau sont horizontal au départ     
    rotbateau2=0
    rotbateau3=0
    rotbateau4=0
    rotbateau5=0
    mode_de_jeu=0

    while continuer:
        for event in pygame.event.get():        #on récupère les différentes actions réalisé par l'utilisateur
            if event.type == QUIT:
                continuer = 0
                pygame.quit()
                

            Affichage("PB")                     #On affiche "Placement des bateaux"                                   
                
            x,y=mouse.get_pos()                                             #récupèration de la position de la souris
            if x>1000 and x<1120 and y>250 and y<290 and mode_de_jeu==0:   #on vérifie si elle se trouve à l'emplacement d'un bateau
                position=1
            
            b=mouse.get_pressed()
            if event.type == MOUSEBUTTONDOWN  and mode_de_jeu==0:          #Drag and Drop
                if event.button == 1:
                    screencopy=fenetre.copy()
                    
            
            if b[0] ==0 and c==1 and position==1 and numbateau==1 and mode_de_jeu==0:  #on verifie que le bateau peut bien etre posé
                if rotation==1:             #on garde une trace de la rotation ou non
                    rotbateau1=1
                position=0
                c=0
                rotation=0
                numbateau+=1                #on affiche en nouveau bateau
                x1,y1=ReplacementB(x,y)     #on replace bien le bateau
                fenetre.blit(fond, (0,0))
                fenetre.blit(bateau, (x1,y1))
                fenetre.blit(bateau2, (1070,250))
                bateau=bateau2
                pygame.display.flip()
            
            if b[0] ==0 and c==1 and position==1 and numbateau==2 and mode_de_jeu==0:  #même procédé
                if rotation==1:
                    rotbateau2=1
                position=0
                c=0
                rotation=0
                numbateau+=1                                                                #on garde un compteur pour suivre l'instalation des bateaux
                x2,y2=ReplacementB(x,y)
                if rotbateau1==1:                                                           #réalise ou non la rotation du bateau précèdent
                    bateau1=pygame.transform.rotate(bateau1, -90)                           #et on affiche les bateau précédement installé
                fenetre.blit(fond, (0,0))
                fenetre.blit(bateau1, (x1,y1))
                fenetre.blit(bateau, (x2,y2))
                fenetre.blit(bateau3, (1070,250))
                bateau=bateau3
                pygame.display.flip()                                                      #on ouvre un nouvelle fenetre pour cacher le bateau installé 
    
            if b[0] ==0 and c==1 and position==1 and numbateau==3 and mode_de_jeu==0:      #on répete l'oppérarion jusqu'a ce que tout le bateau soient installé
                if rotation==1:
                    rotbateau3=1
                position=0
                c=0
                rotation=0
                numbateau+=1
                x3,y3=ReplacementB(x,y)
                if rotbateau2==1:
                    bateau2=pygame.transform.rotate(bateau2, -90)
                fenetre.blit(fond, (0,0))
                fenetre.blit(bateau1, (x1,y1))
                fenetre.blit(bateau2, (x2,y2))
                fenetre.blit(bateau, (x3,y3))
                fenetre.blit(bateau4, (1070,250))
                bateau=bateau4
                pygame.display.flip()
    
            if b[0] ==0 and c==1 and position==1 and numbateau==4 and mode_de_jeu==0:
                if rotation==1:
                    rotbateau4=1
                position=0
                c=0
                rotation=0
                numbateau+=1
                x4,y4=ReplacementB(x,y)
                if rotbateau3==1:
                    bateau3=pygame.transform.rotate(bateau3, -90)
                fenetre.blit(fond, (0,0))
                fenetre.blit(bateau1, (x1,y1))
                fenetre.blit(bateau2, (x2,y2))
                fenetre.blit(bateau3, (x3,y3))
                fenetre.blit(bateau, (x4,y4))
                fenetre.blit(bateau5, (1070,250))
                bateau=bateau5
                pygame.display.flip()
    
            if b[0] ==0 and c==1 and position==1 and numbateau==5 and mode_de_jeu==0:
                if rotation==1:
                    rotbateau5=1
                position=0
                c=0
                rotation=0
                numbateau+=1
                x5,y5=ReplacementB(x,y)
                if rotbateau4==1:
                    bateau4=pygame.transform.rotate(bateau4, -90)
                fenetre.blit(fond, (0,0))
                fenetre.blit(bateau1, (x1,y1))
                fenetre.blit(bateau2, (x2,y2))
                fenetre.blit(bateau3, (x3,y3))
                fenetre.blit(bateau4, (x4,y4))
                if rotbateau5==1:                                               
                    bateau5=pygame.transform.rotate(bateau5, -90)   
                fenetre.blit(bateau, (x5,y5))
                pygame.display.flip()
                mode_de_jeu=1                                                  #on change le mode de jeux une fois tout les bateau installé afin de mettre fin a la fonction et renvoyer les bateaux
    
    
            if x>1040 and y>600 and x<1080 and y<640 and rotation==0 and mode_de_jeu==0:   #définition de la zone de rotation
                bateau=pygame.transform.rotate(bateau, 90)
                b=bateau.get_rect(center=(x, y))                #modification réalisé par la fonction interne a pygame
                fenetre.blit(bateau,b)
                rotation=1
    
            if x>1120 and y>600 and x<1160 and y<640 and rotation==1 and mode_de_jeu==0:   #définition de la zone de rotation inverse
                bateau=pygame.transform.rotate(bateau, -90)
                b=bateau.get_rect(center=(x, y))
                fenetre.blit(bateau,b)
                rotation=0
                
                
            if b[0] == 1 and position==1 and mode_de_jeu==0:   #deuxième partie du drag and drop
                c=1                
                fenetre.blit(screencopy,(0,0))
                fenetre.blit(bateau, (x-20,y-20))
                pygame.display.flip()
            
            if mode_de_jeu==1:                                 #une fois que tous les bateaux sont installés, on revoie leurs positions ainsi que leurs rotations
                ListeCoord=[(x1,y1,rotbateau1),(x2,y2,rotbateau2),(x3,y3,rotbateau3),(x4,y4,rotbateau4),(x5,y5,rotbateau5)]
                RetourBateau(Matrice,ListeB,ListeCoord)
                Affichage("CacheR")
                Affichage("CachePB")
                continuer=0


    
#
#import FonctionsTC as fn
#A4=[]
#ListeB=[]
#ListeRotation=[]
#fn.MatriceVide(A4)
#placement_bateau(A4,ListeB,ListeRotation)
#fn.affichageEmoji(A4)
#print(ListeB)