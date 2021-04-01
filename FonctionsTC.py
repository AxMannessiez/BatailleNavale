#!/usr/bien/python3
# -*- coding: utf-8 -*-
"""
@author : Axel MANNESSIEZ & Benoit MARCILLAT

"""
#fichier : "FonctionsTC.py"
######################################################################################


############################
#BIBLIOTHÈQUES À IMPORTER :
import random as rd
############################


#On réimporte la fonction d'affichage des matrices pour tester le programme
def affichage(A) :
    """
    Fonction affichant plus esthétiquement les matrices données sous forme de 
    liste
    """
    chaine=""
    for x in A :                #On parcourt les lignes
        for y in x :
            chaine+=" "+str(y)       #On ajoute à chaine les éléments de la matrice séparés par un espace
        chaine+="\n"            #On ajoute un retour à la ligne entre chaque ligne de la matrice
    print(chaine)

def affichageEmoji(A) :
    """
    Fonction affichant plus esthétiquement les matrices données sous forme de 
    liste
    """
    chaine=""
    for x in A :                #On parcourt les lignes
        for y in x :
            chaine+=" "   #On sépare avec un espace
            if y==0 :           #Si on n'a pas d'information
                chaine+="⬜️"
            elif y==1 :         #S'il y a un bateau
                chaine+="⬛️"
            elif y==2 :         #S'il n'y a pas de bateau
                chaine+="❌"
            elif y==3 :         #Tir ennemi
                chaine+="🔵"
        chaine+="\n"            #On ajoute un retour à la ligne entre chaque ligne de la matrice
    print(chaine)  
    
    
def MatriceVide(matrice):
    """
    Fonction créant une matrice carrée vide de taille 10 en modifiant une 
    matrice donnée en argument
    """
    matrice[:]=[]           #On vide la matrice si jamais elle n'est pas vide de base
    for i in range (10) :   #Pour chaque ligne
        matrice.append([0,0,0,0,0,0,0,0,0,0])   #On remplit la ligne de 0


def PlaceBateaux(Matrice,ListeB,TaillesB=[5,4,3,3,2]) :
    """
    Fonction prenant en argument une matrice vide et y plaçant aléatoirement
    des bateaux (représentés par des 1) - les tailles des bateaux étant laissées
    en argument ([5,4,3,3,2] par défaut) - et notant leurs emplacement dans la
    liste donnée en argument
    """
    for x in TaillesB :       #Pour chaque bateau
        orientation = rd.randint(0,1)   #On détermine au hasard l'orientation du bateau (horizontale si 0, verticale si 1)
        
        #####################
        
        if orientation == 0 :           #Si le bateau est à l'horizontale :
            positionx=rd.randint(0,10-x)       #On choisit où positionner la gauche du bateau pour que le bateau ne dépasse pas
            
            Toutparfait=False
            it1=0
            while Toutparfait==False and it1<10 :
                it1+=1
                positiony=rd.randint(0,9)          #Les lignes sont comptées en Python de 0 à 9
                #On va vérifier si la position déterminée est sélectionnable ou non :
                Toutbonneposition=False             #On n'a pas encore vérifié
                
                if x==5 :                   #Si c'est le premier bateau, on n'a pas besoin de vérifier l'emplacement
                    Toutparfait=True
                    Toutbonneposition=True
                
                it2=0                                #On compte le nombre d'itérations pour ne pas avoir de boucle infinie
                while Toutbonneposition==False and it2<10 :    #Tant que l'emplacement n'est pas correct
                    it2+=1                               #On met à jour le compteur d'itération
                    bonneposition=True                  #Pour rentrer dans la boucle

                    for i in range(positionx,positionx+x) :       #On vérifie sur la longueur du bateau
                        if Matrice[positiony][i]==0 :           #S'il n'y a rien à cet emplacement
                            try :
                                if Matrice[positiony-1][i]==0 :         #Rien au dessus
                                    try :
                                        if Matrice[positiony+1][i]==0 :         #Rien en dessous
                                            bonneposition=True                      #On continue et on vérifie la place suivante
                                        else:
                                            bonneposition=False
                                    except IndexError :             #Dans le cas où le bateau est tout en bas, il n'y a forcément pas de bateau en dessous
                                        pass
                                else:
                                    bonneposition=False
                            except IndexError :                     #Dans le cas où le bateau est tout en haut, il n'y a forcément pas de bateau au dessus
                                pass
                        else:                                      #S'il y a déjà un bateau
                            bonneposition=False                         #Ça ne va pas et on s'arrête
                        if bonneposition==False :       #On sort de la boucle dès qu'il y a une erreur
                            break

                    if bonneposition == True :          #Si tout est bon
                        #On effectue le dernier test, à savoir aucun bateau à gauche ni à droite
                        if positionx!=0 and Matrice[positiony][positionx-1]!=0 :
                            bonneposition=False
                        if positionx+x-1!=9 and Matrice[positiony][positionx+x]!=0 :
                            bonneposition=False
                            
                    if bonneposition == True :          #Si on sort de la boucle avec True
                        Toutbonneposition=True              #Tout est correct et on sort de la boucle
                    else :                              #Si la boucle a été interrompue parce qu'un enmplacement ne convenait pas
                        if positiony < 9 :                  #Si on n'est pas en bas
                            positiony+=1                        #On essaye la ligne suivante
                        else :                          #Si on est en bas
                            positiony=0                     #On repart en haut
                
                if Toutbonneposition == True :
                    B=[]                                    #On crée une liste contenant les emplacements correspondant au bateau
                    for i in range(positionx,positionx+x):  #Pour chaque place
                        Matrice[positiony][i]=1                 #On pose un "bout" de bateau
                        B.append((i,positiony))
                    ListeB.append(B)
                    Toutparfait=True                           #On a fini
                else :  #Si aucune position n'est envisageable à cette colonne,
                    if positionx+x-1 < 9 :                  #Si on n'est pas à droite
                        positionx+=1                        #On essaye la colonne suivante
                    else :                          #Si on est à droite
                        positionx=0                     #On repart à gauche
        
        ########################
        
        else :      #Si le bateau est à la verticale, le code est identique en inversant x et y`
            positiony=rd.randint(0,10-x)       #On choisit où positionner le haut du bateau pour que le bateau ne dépasse pas
            
            Toutparfait=False
            it1=0
            while Toutparfait==False and it1<10 :
                it1+=1
                positionx=rd.randint(0,9)          #Les colonnes sont comptées en Python de 0 à 9
                #On va vérifier si la position déterminée est sélectionnable ou non :
                Toutbonneposition=False             #On n'a pas encore vérifié
                
                if x==5 :                   #Si c'est le premier bateau, on n'a pas besoin de vérifier l'emplacement
                    Toutparfait=True
                    Toutbonneposition=True
                
                it2=0                                #On compte le nombre d'itérations pour ne pas avoir de boucle infinie
                while Toutbonneposition==False and it2<10 :    #Tant que l'emplacement n'est pas correct
                    it2+=1                               #On met à jour le compteur d'itération
                    bonneposition=True                  #Pour rentrer dans la boucle
                    
                    for i in range(positiony,positiony+x) :       #On vérifie sur la longueur du bateau
                        if Matrice[i][positionx]==0 :           #S'il n'y a rien à cet emplacement
                            try :
                                if Matrice[i][positionx-1]==0 :         #Rien à gauche
                                    try :
                                        if Matrice[i][positionx+1]==0 :         #Rien à droite
                                            bonneposition=True                      #On continue et on vérifie la place suivante
                                        else:
                                            bonneposition=False
                                    except IndexError :             #Dans le cas où le bateau est tout à droite, il n'y a forcément pas de bateau à droite
                                        pass
                                else:
                                    bonneposition=False
                            except IndexError :                     #Dans le cas où le bateau est tout à gauche, il n'y a forcément pas de bateau à gauche
                                pass
                        else:                                      #S'il y a déjà un bateau
                            bonneposition=False                         #Ça ne va pas et on s'arrête
                        if bonneposition==False :       #On sort de la boucle dès qu'il y a une erreur
                            break
                    
                    if bonneposition == True :          #Si tout est bon
                        #On effectue le dernier test, à savoir aucun bateau en haut ni en bas
                        if positiony!=0 and Matrice[positiony-1][positionx]!=0 :
                            bonneposition=False
                        if positiony+x-1!=9 and Matrice[positiony+x][positionx]!=0 :
                            bonneposition=False
                            
                    if bonneposition == True :          #Si on sort de la boucle avec True
                        Toutbonneposition=True              #Tout est correct et on sort de la boucle
                    else :                              #Si la boucle a été interrompue parce qu'un enmplacement ne convenait pas
                        if positionx < 9 :                  #Si on n'est pas à droite
                            positionx+=1                        #On essaye la colonne suivante
                        else :                          #Si on est à droite
                            positionx=0                     #On repart à gauche
                
                if Toutbonneposition == True :
                    B=[]
                    for i in range(positiony,positiony+x):  #Pour chaque place
                        Matrice[i][positionx]=1                 #On pose un "bout" de bateau
                        B.append((positionx,i))
                    ListeB.append(B)
                    Toutparfait=True                           #On a fini
                else :      #Si aucune position ne convient à cette ligne
                        if positiony+x-1 < 9 :                  #Si on n'est pas en bas
                            positiony+=1                        #On essaye la ligne suivante
                        else :                          #Si on est en bas
                            positiony=0                     #On repart en haut


def Bateaula(Grille,Tuple) :
    """
    Fonction prenant en argument un tuple correspondant à la position tirée et
    renvoyant True ou False si un bateau est touché ou non sur la grille donnée
    en argument
    """
    x,y=Tuple
    if x >=0 and y>=0 :
        if Grille[y][x]==1 :
            return True
        elif Grille[y][x]==3 :  #S'il retape au même endroit
            return True
        else :
            return False
    else :
        #print ("Erreur de tir")
        return False


def NumBateau(ListeBateau,Tuple) :
    """
    Fonction prenant en argument le tuple de coordonnées correspondant à la
    position du bateau touché et renvoyant le numéro de ce bateau (en Python,
    donc le premier bateau est le numéro 0)
    """
    i=0
    for bateau in ListeBateau :  #Pour chaque bateau
        for couple in bateau :       #Pour chaque tuple de coordonnées de point du bateau
            if couple==Tuple :           #Si c'est cet endroit qui a éte touché
                return i                    #On renvoie le numéro du bateau
        i+=1

def BateauCoule(Grille,ListeBateau,Tuple):
    """
    Fonction prenant en argument la grille de découverte et le tuple de
    coordonnées correspondant à la position du bateau touché et renvoyant True
    ou False si le bateau est coulé ou non
    """
    numbateau=NumBateau(ListeBateau,Tuple)
    bateau=ListeBateau[numbateau]    #On récupère uniquement les coordonnées du bateau touché
    for couple in bateau :
        if Grille[couple[1]][couple[0]] !=1 :   #Si on n'a pas touché une partie du bateau
            return False                            #Alors on ne l'a pas coulé
    return True                                 #Si on n'est pas sorti du programme, c'est que toutes les cases sont touchées

#A4=[]
#ListeB=[]
#MatriceVide(A4)
#affichageEmoji(A4)
#PlaceBateaux(A4,ListeB)
#print(A4)
#affichageEmoji(A4)
#print(ListeB,"\n")
#
#A5=[[0, 0, 0, 1, 1, 1, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 1, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 1, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
#affichageEmoji(A5)
#print(Bateaula(A5,(3,0)))
#print(Bateaula(A5,(9,9)))
#print()
#ListeBA5=[[(1,8),(2,8),(3,8),(4,8),(5,8)],[(3,3),(4,3),(5,3),(6,3)],[(3,0),(4,0),(5,0)],[(6,5),(7,5),(8,5)],[(1,2),(2,2)]]
#print(NumBateau(ListeBA5,(5,3)))
#
#print()
#GrilleA51=[[0, 0, 0, 1, 1, 1, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
#affichageEmoji(GrilleA51)
#print(BateauCoule(GrilleA51,ListeBA5,(5,3)))
#print(BateauCoule(GrilleA51,ListeBA5,(4,0)))
#
#
#




