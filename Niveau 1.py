#!/usr/bien/python3
# -*- coding: utf-8 -*-
"""
@author : Axel MANNESSIEZ & Benoit MARCILLAT

"""
#fichier : "Niveau1.py"
######################################################################################


############################
#BIBLIOTHÈQUES À IMPORTER 
import random as rd
import FonctionsTC as fn
import FonctionsTC2 as fn2
import pygame
from pygame import *
from pygame.locals import *
###########################

#PROGRAMME :


#Initialisation :
GrilleOrdi0=[]          #Grille des bateaux de l'ordi
GrilleOrdi1=[]          #Grille de découverte de l'ordi
ListeBateauxOrdi1=[]     #Liste des emplacements des bateaux de l'ordi
ListeBateauxOrdi2=[1,1,1,1,1]     #Liste de découverte des bateaux ennemis, prenant la valeur 0 si le bateau est coulé
GrilleUser0=[]          #Grille des bateaux de l'utilisateur
GrilleUser1=[]          #Grille de découverte de l'utilisateur
ListeBateauxUser1=[]    #Liste des emplacements des bateaux de l'utilisateur
ListeBateauxUser2=[1,1,1,1,1]   #Liste de découverte des bateaux ennemis  
fn.MatriceVide(GrilleOrdi0)     #On transforme les listes en vraies grilles 10x10
fn.MatriceVide(GrilleOrdi1)
fn.MatriceVide(GrilleUser0)
fn.MatriceVide(GrilleUser1)
ListeCases=[(x,y) for x in range (10) for y in range (10)]  #On crée la liste des cases de la grille pour ensuite "piocher" aléatoirement dedans

#Placement des bateaux :
fn.PlaceBateaux(GrilleOrdi0,ListeBateauxOrdi1)   #On place les bateaux de l'ordi et on note leurs coordonnées
fn2.PlaceBateaux2(GrilleUser0,ListeBateauxUser1)   #On ouvre l'interface graphique pour l'utilisateur
#fn.PlaceBateaux(GrilleUser0,ListeBateauxUser1)

croix = pygame.image.load("Images/croix.gif").convert() 
boutbateau = pygame.image.load("Images/boutbateau.jpg").convert()
boutbateaucoule = pygame.image.load("Images/boutbateaucoule.jpg").convert() 
cachetexte=0
Tour=0

#Boucle continue du jeu
run=1
while run == 1 :
    
    for event in pygame.event.get():
        if event.type == QUIT:
            run = 0
            pygame.quit()
                
        if Tour==1 and event.type == MOUSEBUTTONDOWN and event.button==1 : #Si c'est à l'utilisateur de jouer
            ciblegrph=pygame.mouse.get_pos()
            x,y=ciblegrph
            if x>=80 and x<=480 and y>=80 and y<=480 :      #Si l'utilisateur clique dans la bonne zone
                ciblegrph=fn2.ReplacementTir(ciblegrph)         #On replace parfaitement le tir
                cible=fn2.PixTab2(ciblegrph[0],ciblegrph[1])    #On convertirt en case du tableau
                #cible=eval(input("Donner le tuple correspondant à l'endroit visé : "))  (SANS INTERFACE GRAPHIQUE)
                if fn.Bateaula(GrilleOrdi0,cible) == True :     #Si on a touché un bateau
                    GrilleUser1[cible[1]][cible[0]]=1               #On actualise la matrice
                    fn2.Tire(ciblegrph,boutbateau)                  #On actualise l'affichage
                    if fn.BateauCoule(GrilleUser1,ListeBateauxOrdi1,cible) == True :    #Si le bateau entier est coulé
                        fn2.Affichage("TC")                                                 #On l'affiche
                        cachetexte=2
                        ListeBateauxUser2[fn.NumBateau(ListeBateauxOrdi1,cible)]=0          #On indique le bateau comme coulé
                        if ListeBateauxUser2==[0,0,0,0,0] :                                 #Et si tous les bateaux sont coulés
                            print("Vous avez gagné !")
                            run=0
                            pygame.quit()
                else :
                    GrilleUser1[cible[1]][cible[0]]=2               #On actualise la matrice
                    fn2.Tire(ciblegrph,croix)                       #On actualise l'affichage
                Tour=0
            
        if Tour == 0 :      #C'est à l'ordinateur de jouer
            
            if cachetexte==0 :                          #On affiche ou non l'inscription "Touché Coulé"
                fn2.Affichage("CacheTC")
            else :
                cachetexte-=1
            
            NumCase=rd.randrange(len(ListeCases))       #On choisit une case au hasard dans celles que l'on n'a pas encore visé
            cible=ListeCases.pop(NumCase)
            ciblegrph=fn2.TabPix(cible[0],cible[1])     #On convertit en coordonnées en pixels
            if fn.Bateaula(GrilleUser0,cible) == True : #Si on a touché un bateau :
                GrilleOrdi1[cible[1]][cible[0]]=1           #On met à jour la matrice
                #GrilleUser0[cible[1]][cible[0]]=3          (POUR VERSION SANS INTERFACE GRAPHIQUE)
                fn2.Tire(ciblegrph,boutbateaucoule)         #On met à jour l'interface graphique
                if fn.BateauCoule(GrilleOrdi1,ListeBateauxUser1,cible) == True :    #Si l'ordinateur a coulé un bateau
                    ListeBateauxOrdi2[fn.NumBateau(ListeBateauxUser1,cible)]=0          #On indique le bateau comme coulé dans la matrice
                    if ListeBateauxOrdi2==[0,0,0,0,0] :                                 #Et si tous les bateaux sont coulés
                        print("L'ordinateur a gagné !")                                     #C'est la fin de la partie
                        fn.affichageEmoji(GrilleOrdi0)                                      #On affiche la grille des bateaux de l'ordinateur
                        run=0
                        pygame.quit()
            else :
                GrilleOrdi1[cible[1]][cible[0]]=2
                fn2.Tire(ciblegrph,croix)
            Tour=1
    
#Diagonales Niveau 3
#[(0,0),(9,9),(1,1),(8,8),(2,2),(7,7),(3,3),(6,6),(4,4),(5,5),(4,0),(5,9),(5,1),(4,8),(6,2),(3,7),(7,3),(2,6),(8,4),(1,5),(9,5),(0,4),(8,0),(1,9),(9,1),(0,8),(2,0),(7,9),(3,1),(6,8),(4,2),(5,7),(5,3),(4,6),(6,4),(3,5),(7,5),(2,4),(8,6),(1,3),(9,7),(0,2),(6,0),(3,9),(7,1),(2,8),(8,2),(1,7),(9,3),(0,6)]
