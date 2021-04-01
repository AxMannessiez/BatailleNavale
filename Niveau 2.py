#!/usr/bien/python3
# -*- coding: utf-8 -*-
"""
@author : Axel MANNESSIEZ & Benoit MARCILLAT

"""
#fichier : "Niveau2.py"
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
sauvcible=0,0
recherche,direction,compteur_tir,compte_faux=0,0,0,0
choix_direction,direction_bonne,inverse=True,False,False

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


        if Tour == 0 :      #Si c'est à l'ordinateur de jouer
            
            if cachetexte==0 :                          #On affiche ou non l'inscription "Touché Coulé"
                fn2.Affichage("CacheTC")
            else :
                cachetexte-=1
            
            #Si on n'a pas de bateau à couler, on cherche à en toucher un nouveau (code similaire à celui du niveau 1)
            if recherche==0 :
                NumCase=rd.randrange(len(ListeCases))       #On choisit une case au hasard dans celles que l'on n'a pas encore visé
                cible=ListeCases.pop(NumCase)
                sauvcible=cible
                ciblegrph=fn2.TabPix(cible[0],cible[1])     #On convertit en coordonnées en pixels
                if fn.Bateaula(GrilleUser0,cible) == True : #Si on a touché un bateau
                    GrilleOrdi1[cible[1]][cible[0]]=1           #On met à jour la matrice
                    fn2.Tire(ciblegrph,boutbateaucoule)         #On met à jour l'interface graphique
                    recherche=1                                 #On passera au tour suivant en mode recherche
                    if fn.BateauCoule(GrilleOrdi1,ListeBateauxUser1,cible) == True :    #Si on a coulé un bateau
                        ListeBateauxOrdi2[fn.NumBateau(ListeBateauxUser1,cible)]=0          #On indique le bateau comme coulé
                        if ListeBateauxOrdi2==[0,0,0,0,0] :                                 #Et si tous les bateaux sont coulés
                            print("L'ordinateur a gagné !")                                     #C'est la fin de la partie
                            run=0
                            pygame.quit()
                else :
                    GrilleOrdi1[cible[1]][cible[0]]=2
                    fn2.Tire(ciblegrph,croix)
                Tour=1
            
            
            #Si on a déja touché un bateau, on cherche à le couler
            if recherche==1 and Tour==0:

                #Choix initial de la direction des tirs :
                if choix_direction==True:                                           #Si ça n'a pas encore été fait
                    direction=rd.randint(0,1)                                           #On choisit si l'on tire horizontalement ou verticalement
                    choix_direction=False
                    
                #On vérifie au début si la position suivante n'est pas en dehors des limites
                exterieurx = sauvcible[0]+compteur_tir+1
                exterieury = sauvcible[1]+compteur_tir+1
                if inverse == False :
                    if choix_direction==False and direction_bonne==False:                                           #Si on est au début 
                        if exterieurx==10 and exterieury==10 :
                            direction=1
                            inverse=True
                            compte_faux+=2
                        elif exterieurx==10 and direction==0 :                                               #Si on dépasse horizontalement
                            direction=1                                                         #On se déplace verticalement
                            compte_faux+=1
                        elif exterieury==10 and direction==1 :                                               #Si on dépasse verticalement
                            direction=0                                                         #On se déplace horizontalement
                            compte_faux+=1
                    if direction_bonne==True :                                          #Si on est dans le jeu
                        if exterieurx==10 and direction==0 :                                                 #Si on dépasse horizontalement
                            inverse=True                                                        #On se déplace en marche arrière
                        if exterieury==10 and direction==1 :                                             #Si on dépasse verticalement
                            inverse=True                                                        #On se déplace en marche arrière


                #Si le reste du bateau n'est ni en bas, ni à droite, il faut partir en arrière (donc à gauche)
                if compte_faux==2 and inverse==False:
                    inverse=True
                    direction=0
                    if choix_direction==False and direction_bonne==False and sauvcible[0]-1==-1:
                        direction=1
                
                
                #Si on tire dans le sens normal :
                if inverse == False :
                    
                    #Si le déplacement se fait horizontalement
                    if direction==0 :
                        compteur_tir+=1                                                     #On va se déplacer d'une case
                        cible=sauvcible[0]+compteur_tir,sauvcible[1]                        #On tire sur la cible suivante
                        try :
                            ListeCases.remove(cible)                                            #On empêche à l'ordinateur de tirer ensuite à nouveau dessus
                        except ValueError :
                            pass
                        ciblegrph=fn2.TabPix(cible[0],cible[1])                             #On convertit en coordonnées en pixels
                        if fn.Bateaula(GrilleUser0,cible) == True :                         #Si on a touché un bateau :
                            GrilleOrdi1[cible[1]][cible[0]]=1                                   #On met à jour la matrice
                            fn2.Tire(ciblegrph,boutbateaucoule)                                 #On met à jour l'interface graphique
                            choix_direction,direction_bonne=False,True                          #On ne modifie plus la direction
                            compte_faux=0
                            if fn.BateauCoule(GrilleOrdi1,ListeBateauxUser1,cible) == True :    #Si on a coulé un bateau
                                ListeBateauxOrdi2[fn.NumBateau(ListeBateauxUser1,cible)]=0          #On indique le bateau comme coulé dans la matrice
                                recherche=0                                                         #Et on réinitialise toutes les  
                                compteur_tir,compte_faux=0,0                                        # variables pour trouver un autre
                                choix_direction,direction_bonne,inverse=True,False,False            # bateau au tour suivant
                                if ListeBateauxOrdi2==[0,0,0,0,0] :                                 #Et si tous les bateaux sont coulés
                                    print("L'ordinateur a gagné !")                                     #C'est la fin de la partie
                                    fn.affichageEmoji(GrilleUser1)
                                    fn.affichageEmoji(GrilleOrdi0)                                      #On affiche la grille des bateaux de l'ordinateur
                                    run=0
                                    pygame.quit()
                        else:                                                               #Si on a tiré dans l'eau :
                            GrilleOrdi1[cible[1]][cible[0]]=2                                   #On met à jour la matrice
                            fn2.Tire(ciblegrph,croix)                                           #On met à jour l'interface graphique
                            if direction_bonne==False:                                          #Si on n'est pas dans la bonne direction :
                                direction=1                                                         #On se déplace verticalement
                                compte_faux+=1
                                compteur_tir=0
                            else:                                                               #Et si on est dans la bonne direction :
                                inverse=True                                                        #On tire en marche arrière
                                compteur_tir=0                                                      #On réinitialise le nombre de tirs
                        Tour=1
    
                    #Si le déplacement se fait verticalement
                    if direction==1 and Tour==0 :
                        compteur_tir+=1                                                     #On va se déplacer d'une case
                        cible=sauvcible[0],sauvcible[1]+compteur_tir                        #On tire sur la cible suivante
                        try :
                            ListeCases.remove(cible)                                            #On empêche à l'ordinateur de tirer ensuite à nouveau dessus
                        except ValueError :
                            pass                                            #On empêche à l'ordinateur de tirer ensuite à nouveau dessus
                        ciblegrph=fn2.TabPix(cible[0],cible[1])                             #On convertit en coordonnées en pixels
                        if fn.Bateaula(GrilleUser0,cible) == True :                         #Si on a touché un bateau :
                            GrilleOrdi1[cible[1]][cible[0]]=1                                   #On met à jour la matrice
                            fn2.Tire(ciblegrph,boutbateaucoule)                                 #On met à jour l'interface graphique
                            choix_direction,direction_bonne=False,True                          #On ne modifie plus la direction
                            compte_faux=0
                            if fn.BateauCoule(GrilleOrdi1,ListeBateauxUser1,cible) == True :    #Si on a coulé un bateau
                                ListeBateauxOrdi2[fn.NumBateau(ListeBateauxUser1,cible)]=0          #On indique le bateau comme coulé dans la matrice
                                recherche=0                                                         #Et on réinitialise toutes les  
                                compteur_tir,compte_faux=0,0                                        # variables pour trouver un autre
                                choix_direction,direction_bonne,inverse=True,False,False            # bateau au tour suivant
                                if ListeBateauxOrdi2==[0,0,0,0,0] :                                 #Et si tous les bateaux sont coulés
                                    print("L'ordinateur a gagné !")                                     #C'est la fin de la partie
                                    fn.affichageEmoji(GrilleUser1)
                                    fn.affichageEmoji(GrilleOrdi0)                                      #On affiche la grille des bateaux de l'ordinateur
                                    run=0
                                    pygame.quit()
                        else:
                            GrilleOrdi1[cible[1]][cible[0]]=2                                   #On met à jour la matrice
                            fn2.Tire(ciblegrph,croix)                                           #On met à jour l'interface graphique
                            if direction_bonne==False:                                          #Si on n'est pas dans la bonne direction :
                                direction=0                                                         #On se déplace horizontalement
                                compte_faux+=1
                                compteur_tir=0
                            else:                                                               #Et si on est dans la bonne direction :
                                inverse=True                                                        #On tire en marche arrière
                                compteur_tir=0                                                      #On réinitialise le nombre de tirs
                        Tour=1
                
                
                #Si on tire dans le sens inverse :
                if inverse == True and Tour ==0:
                    
                    #Si le déplacement se fait horizontalement
                    if direction==0 :                                      
                        compteur_tir-=1                                                         #On va se déplacer d'une case
                        cible=sauvcible[0]+compteur_tir,sauvcible[1]                            #On tire sur la cible suivante
                        try :
                            ListeCases.remove(cible)                                            #On empêche à l'ordinateur de tirer ensuite à nouveau dessus
                        except ValueError :
                            pass                                                #On empêche à l'ordinateur de tirer ensuite à nouveau dessus
                        ciblegrph=fn2.TabPix(cible[0],cible[1])                                 #On convertit en coordonnées en pixels
                        if fn.Bateaula(GrilleUser0,cible) == True :                             #Si on a touché un bateau
                            GrilleOrdi1[cible[1]][cible[0]]=1                                       #On met à jour la matrice
                            fn2.Tire(ciblegrph,boutbateaucoule)                                     #On met à jour l'interface graphique
                            if fn.BateauCoule(GrilleOrdi1,ListeBateauxUser1,cible) == True :        #Si on a coulé un bateau
                                ListeBateauxOrdi2[fn.NumBateau(ListeBateauxUser1,cible)]=0              #On indique le bateau comme coulé dans la matrice
                                recherche=0                                                             #Et on réinitialise toutes les  
                                compteur_tir,compte_faux=0,0                                            # variables pour trouver un autre
                                choix_direction,direction_bonne,inverse=True,False,False                # bateau au tour suivant
                                if ListeBateauxOrdi2==[0,0,0,0,0] :                                     #Et si tous les bateaux sont coulés
                                    print("L'ordinateur a gagné !")                                         #C'est la fin de la partie
                                    fn.affichageEmoji(GrilleUser1)
                                    fn.affichageEmoji(GrilleOrdi0)                                      #On affiche la grille des bateaux de l'ordinateur
                                    run=0
                                    pygame.quit()
                        else:
                            GrilleOrdi1[cible[1]][cible[0]]=2                                       #On met à jour la matrice
                            fn2.Tire(ciblegrph,croix)                                               #On met à jour l'interface graphique
                            compteur_tir=0                                                          #On réinitialise le nombre de tirs
                            if direction_bonne==False:                                              #Si on n'est pas dans la bonne direction :
                                direction=1                                                             #On se déplace verticalement
                                compteur_tir=0
                        Tour=1
    
                    #Si le déplacement se fait verticalement
                    if direction==1 and Tour==0 :
                        compteur_tir-=1                                                         #On va se déplacer d'une case
                        cible=sauvcible[0],sauvcible[1]+compteur_tir                            #On tire sur la cible suivante
                        try :
                            ListeCases.remove(cible)                                            #On empêche à l'ordinateur de tirer ensuite à nouveau dessus
                        except ValueError :
                            pass                                               #On empêche à l'ordinateur de tirer ensuite à nouveau dessus
                        ciblegrph=fn2.TabPix(cible[0],cible[1])                                 #On convertit en coordonnées en pixels
                        if fn.Bateaula(GrilleUser0,cible) == True :                             #Si on a touché un bateau
                            GrilleOrdi1[cible[1]][cible[0]]=1                                       #On met à jour la matrice
                            fn2.Tire(ciblegrph,boutbateaucoule)                                     #On met à jour l'interface graphique
                            if fn.BateauCoule(GrilleOrdi1,ListeBateauxUser1,cible) == True :        #Si on a coulé un bateau
                                ListeBateauxOrdi2[fn.NumBateau(ListeBateauxUser1,cible)]=0              #On indique le bateau comme coulé dans la matrice
                                recherche=0                                                             #Et on réinitialise toutes les  
                                compteur_tir,compte_faux=0,0                                            # variables pour trouver un autre
                                choix_direction,direction_bonne,inverse=True,False,False                # bateau au tour suivant
                                if ListeBateauxOrdi2==[0,0,0,0,0] :                                     #Et si tous les bateaux sont coulés
                                    print("L'ordinateur a gagné !")                                     #C'est la fin de la partie
                                    fn.affichageEmoji(GrilleUser1)
                                    fn.affichageEmoji(GrilleOrdi0)                                      #On affiche la grille des bateaux de l'ordinateur
                                    run=0
                                    pygame.quit()
            
            
            #Fin du tour de l'ordinateur, on repasse à l'utilisateur
            Tour=1

    

  

