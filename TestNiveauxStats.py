#!/usr/bien/python3
# -*- coding: utf-8 -*-
"""
@author : Axel MANNESSIEZ & Benoit MARCILLAT

"""
#fichier : "TestsNiveauxStats.py"
######################################################################################

############################
#BIBLIOTHÈQUES À IMPORTER 
import random as rd
import FonctionsTC as fn
import time
###########################

#PROGRAMME :

def Niveau0():
    """
    Fonction simulant une partie de bataille navale de niveau 0 où l'ordinateur
    est le seul à jouer, et renvoyant le nombre de coups qu'il a joué avant de 
    trouver et le temps qu'il a mis
    """
    #Initialisation :
    GrilleUser0=[]                  
    ListeBateauxUser1=[] 
    GrilleOrdi1=[]          #Grille de découverte de l'ordi
    ListeBateauxOrdi2=[1,1,1,1,1]     #Liste de découverte des bateaux ennemis, prenant la valeur 0 si le bateau est coulé
    fn.MatriceVide(GrilleUser0)
    fn.MatriceVide(GrilleOrdi1)

    #Placement des bateaux :
    fn.PlaceBateaux(GrilleUser0,ListeBateauxUser1)
    
    nbtours=0
    debut=time.time()
    
    #Boucle continue du jeu
    run=1
    while run == 1 :
        nbtours+=1
        cible=(rd.randint(0,9),rd.randint(0,9))
        if fn.Bateaula(GrilleUser0,cible) == True : #Si on a touché un bateau
            GrilleOrdi1[cible[1]][cible[0]]=1
            if fn.BateauCoule(GrilleOrdi1,ListeBateauxUser1,cible) == True :
                ListeBateauxOrdi2[fn.NumBateau(ListeBateauxUser1,cible)]=0  #On indique le bateau comme coulé
                if ListeBateauxOrdi2==[0,0,0,0,0] :
                    run=0
        else :
            GrilleOrdi1[cible[1]][cible[0]]=2

    fin=time.time()
    return((nbtours,fin-debut))

def Niveau1():
    """
    Fonction simulant une partie de bataille navale de niveau 1 où l'ordinateur
    est le seul à jouer, et renvoyant le nombre de coups qu'il a joué avant de 
    trouver et le temps qu'il a mis
    """
    #Initialisation :
    GrilleUser0=[]                  
    ListeBateauxUser1=[] 
    GrilleOrdi1=[]          #Grille de découverte de l'ordi
    ListeBateauxOrdi2=[1,1,1,1,1]     #Liste de découverte des bateaux ennemis, prenant la valeur 0 si le bateau est coulé
    fn.MatriceVide(GrilleUser0)
    fn.MatriceVide(GrilleOrdi1)
    ListeCases=[(x,y) for x in range (10) for y in range (10)]  #On crée la liste des cases de la grille pour ensuite "piocher" aléatoirement dedans

    #Placement des bateaux :
    fn.PlaceBateaux(GrilleUser0,ListeBateauxUser1)

    nbtours=0
    debut=time.time()
    
    #Boucle continue du jeu
    run=1
    while run == 1 :
        nbtours+=1
        NumCase=rd.randrange(len(ListeCases))       #On choisit une case au hasard dans celles que l'on n'a pas encore visé
        cible=ListeCases.pop(NumCase)
        if fn.Bateaula(GrilleUser0,cible) == True : #Si on a touché un bateau
            GrilleOrdi1[cible[1]][cible[0]]=1
            if fn.BateauCoule(GrilleOrdi1,ListeBateauxUser1,cible) == True :
                ListeBateauxOrdi2[fn.NumBateau(ListeBateauxUser1,cible)]=0  #On indique le bateau comme coulé
                if ListeBateauxOrdi2==[0,0,0,0,0] :
                    run=0
        else :
            GrilleOrdi1[cible[1]][cible[0]]=2

    fin=time.time()
    return((nbtours,fin-debut))


def Niveau2():
    """
    Fonction simulant une partie de bataille navale de niveau 2 où l'ordinateur
    est le seul à jouer, et renvoyant le nombre de coups qu'il a joué avant de 
    trouver et le temps qu'il a mis
    """
    #Initialisation :
    GrilleUser0=[]          #Grille des bateaux de l'utilisateur
    ListeBateauxUser1=[]    #Liste des emplacements des bateaux de l'utilisateur
    GrilleOrdi1=[]          #Grille de découverte de l'ordi
    ListeBateauxOrdi2=[1,1,1,1,1]       #Liste de découverte des bateaux ennemis, prenant la valeur 0 si le bateau est coulé
    fn.MatriceVide(GrilleUser0)         #On transforme les listes en vraies grilles 10x10
    fn.MatriceVide(GrilleOrdi1)
    ListeCases=[(x,y) for x in range (10) for y in range (10)]  #On crée la liste des cases de la grille pour ensuite "piocher" aléatoirement dedans
    sauvcible=0,0
    recherche,direction,compteur_tir,compte_faux=0,0,0,0
    choix_direction,direction_bonne,inverse=True,False,False

    #Placement des bateaux :
    fn.PlaceBateaux(GrilleUser0,ListeBateauxUser1)

    newtour=True
    nbtours=0
    debut=time.time()
    
    #Boucle continue du jeu
    run=1
    while run == 1 and nbtours<150:
        nbtours+=1
        
        #Si on n'a pas de bateau à couler, on cherche à en toucher un nouveau (code similaire à celui du niveau 1)
        if recherche==0 :
            NumCase=rd.randrange(len(ListeCases))       #On choisit une case au hasard dans celles que l'on n'a pas encore visé
            cible=ListeCases.pop(NumCase)
            sauvcible=cible
            if fn.Bateaula(GrilleUser0,cible) == True : #Si on a touché un bateau
                GrilleOrdi1[cible[1]][cible[0]]=1           #On met à jour la matrice
                recherche=1                                 #On passera au tour suivant en mode recherche
                if fn.BateauCoule(GrilleOrdi1,ListeBateauxUser1,cible) == True :    #Si on a coulé un bateau
                    ListeBateauxOrdi2[fn.NumBateau(ListeBateauxUser1,cible)]=0          #On indique le bateau comme coulé
                    if ListeBateauxOrdi2==[0,0,0,0,0] :                                 #Et si tous les bateaux sont coulés
                        run=0
            else :
                GrilleOrdi1[cible[1]][cible[0]]=2
            newtour=False
            
            
        #Si on a déja touché un bateau, on cherche à le couler
        if recherche==1 and newtour==True:

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
                    if fn.Bateaula(GrilleUser0,cible) == True :                         #Si on a touché un bateau :
                        GrilleOrdi1[cible[1]][cible[0]]=1                                   #On met à jour la matrice
                        choix_direction,direction_bonne=False,True                          #On ne modifie plus la direction
                        compte_faux=0
                        if fn.BateauCoule(GrilleOrdi1,ListeBateauxUser1,cible) == True :    #Si on a coulé un bateau
                            ListeBateauxOrdi2[fn.NumBateau(ListeBateauxUser1,cible)]=0          #On indique le bateau comme coulé dans la matrice
                            recherche=0                                                         #Et on réinitialise toutes les  
                            compteur_tir,compte_faux=0,0                                        # variables pour trouver un autre
                            choix_direction,direction_bonne,inverse=True,False,False            # bateau au tour suivant
                            if ListeBateauxOrdi2==[0,0,0,0,0] :                                 #Et si tous les bateaux sont coulés
                                run=0
                    else:                                                               #Si on a tiré dans l'eau :
                        GrilleOrdi1[cible[1]][cible[0]]=2                                   #On met à jour la matrice
                        if direction_bonne==False:                                          #Si on n'est pas dans la bonne direction :
                            direction=1                                                         #On se déplace verticalement
                            compte_faux+=1
                            compteur_tir=0
                        else:                                                               #Et si on est dans la bonne direction :
                            inverse=True                                                        #On tire en marche arrière
                            compteur_tir=0                                                      #On réinitialise le nombre de tirs
                    newtour=False

                #Si le déplacement se fait verticalement
                if direction==1 and newtour==True :
                    compteur_tir+=1                                                     #On va se déplacer d'une case
                    cible=sauvcible[0],sauvcible[1]+compteur_tir                        #On tire sur la cible suivante
                    try :
                        ListeCases.remove(cible)                                            #On empêche à l'ordinateur de tirer ensuite à nouveau dessus
                    except ValueError :
                        pass                                            #On empêche à l'ordinateur de tirer ensuite à nouveau dessus
                    if fn.Bateaula(GrilleUser0,cible) == True :                         #Si on a touché un bateau :
                        GrilleOrdi1[cible[1]][cible[0]]=1                                   #On met à jour la matrice
                        choix_direction,direction_bonne=False,True                          #On ne modifie plus la direction
                        compte_faux=0
                        if fn.BateauCoule(GrilleOrdi1,ListeBateauxUser1,cible) == True :    #Si on a coulé un bateau
                            ListeBateauxOrdi2[fn.NumBateau(ListeBateauxUser1,cible)]=0          #On indique le bateau comme coulé dans la matrice
                            recherche=0                                                         #Et on réinitialise toutes les  
                            compteur_tir,compte_faux=0,0                                        # variables pour trouver un autre
                            choix_direction,direction_bonne,inverse=True,False,False            # bateau au tour suivant
                            if ListeBateauxOrdi2==[0,0,0,0,0] :                                 #Et si tous les bateaux sont coulés
                                run=0
                    else:
                        GrilleOrdi1[cible[1]][cible[0]]=2                                   #On met à jour la matrice
                        if direction_bonne==False:                                          #Si on n'est pas dans la bonne direction :
                            direction=0                                                         #On se déplace horizontalement
                            compte_faux+=1
                            compteur_tir=0
                        else:                                                               #Et si on est dans la bonne direction :
                            inverse=True                                                        #On tire en marche arrière
                            compteur_tir=0                                                      #On réinitialise le nombre de tirs
                    newtour=False
            
            
            #Si on tire dans le sens inverse :
            if inverse == True and newtour==True :
                
                #Si le déplacement se fait horizontalement
                if direction==0 :                                      
                    compteur_tir-=1                                                         #On va se déplacer d'une case
                    cible=sauvcible[0]+compteur_tir,sauvcible[1]                            #On tire sur la cible suivante
                    try :
                        ListeCases.remove(cible)                                            #On empêche à l'ordinateur de tirer ensuite à nouveau dessus
                    except ValueError :
                        pass                                                #On empêche à l'ordinateur de tirer ensuite à nouveau dessus
                    if fn.Bateaula(GrilleUser0,cible) == True :                             #Si on a touché un bateau
                        GrilleOrdi1[cible[1]][cible[0]]=1                                       #On met à jour la matrice
                        if fn.BateauCoule(GrilleOrdi1,ListeBateauxUser1,cible) == True :        #Si on a coulé un bateau
                            ListeBateauxOrdi2[fn.NumBateau(ListeBateauxUser1,cible)]=0              #On indique le bateau comme coulé dans la matrice
                            recherche=0                                                             #Et on réinitialise toutes les  
                            compteur_tir,compte_faux=0,0                                            # variables pour trouver un autre
                            choix_direction,direction_bonne,inverse=True,False,False                # bateau au tour suivant
                            if ListeBateauxOrdi2==[0,0,0,0,0] :                                     #Et si tous les bateaux sont coulés
                                run=0
                    else:
                        GrilleOrdi1[cible[1]][cible[0]]=2                                       #On met à jour la matrice
                        compteur_tir=0                                                          #On réinitialise le nombre de tirs
                        if direction_bonne==False:                                              #Si on n'est pas dans la bonne direction :
                            direction=1                                                             #On se déplace verticalement
                            compteur_tir=0
                    newtour=False

                #Si le déplacement se fait verticalement
                if direction==1 and newtour==True :
                    compteur_tir-=1                                                         #On va se déplacer d'une case
                    cible=sauvcible[0],sauvcible[1]+compteur_tir                            #On tire sur la cible suivante
                    try :
                        ListeCases.remove(cible)                                            #On empêche à l'ordinateur de tirer ensuite à nouveau dessus
                    except ValueError :
                        pass                                               #On empêche à l'ordinateur de tirer ensuite à nouveau dessus
                    if fn.Bateaula(GrilleUser0,cible) == True :                             #Si on a touché un bateau
                        GrilleOrdi1[cible[1]][cible[0]]=1                                       #On met à jour la matrice
                        if fn.BateauCoule(GrilleOrdi1,ListeBateauxUser1,cible) == True :        #Si on a coulé un bateau
                            ListeBateauxOrdi2[fn.NumBateau(ListeBateauxUser1,cible)]=0              #On indique le bateau comme coulé dans la matrice
                            recherche=0                                                             #Et on réinitialise toutes les  
                            compteur_tir,compte_faux=0,0                                            # variables pour trouver un autre
                            choix_direction,direction_bonne,inverse=True,False,False                # bateau au tour suivant
                            if ListeBateauxOrdi2==[0,0,0,0,0] :                                     #Et si tous les bateaux sont coulés
                                run=0
        
        #Fin du tour de l'ordinateur, on repasse à l'utilisateur
        newtour=True

    fin=time.time()
    if nbtours>=150 :
        return("Erreur")
    else:
        return((nbtours,fin-debut))


def Moyenne(Liste):
    """
    Fonction retournant la moyenne d'une liste donnée en argument
    """
    return (sum(Liste)/len(Liste))

def Variance(Liste,Moyenne):
    """
    Fonction retournant la variance d'une liste
    """
    Liste2=[]
    for x in Liste :
        Liste2.append((x-Moyenne)**2)
    return (sum(Liste2)/len(Liste2))

def It(Niveau,n):
    """
    Fonction effectuant n parties successives de bataille navale et renvoyant
    les statistiques de ses parties
    """
    LTours=[]
    LTemps=[]
    nberreurs=0
    for i in range(n) :
        if i in [int(n*0.1),int(n*0.2),int(n*0.3),int(n*0.4),int(n*0.5),int(n*0.6),int(n*0.7),int(n*0.8),int(n*0.9)] :
            print(int(i*100/n),"%")
        retour=Niveau()
        if retour == "Erreur" :
            nberreurs+=1
        else :
            tours,temps=retour
            LTours.append(tours)
            LTemps.append(temps)
    #Moyennes :
    MoyTours=Moyenne(LTours)
    MoyTemps=sum(LTemps)/len(LTemps)
    #Écarts-types:
    ETTours=(Variance(LTours,MoyTours))**0.5
    ETTemps=(Variance(LTemps,MoyTemps))**0.5
    #Minimums:
    MinTours=min(LTours)
    MinTemps=min(LTemps)
    #Maximums:
    MaxTours=max(LTours)
    MaxTemps=max(LTemps)
    #Étendue :
    EtTours=MaxTours-MinTours
    EtTemps=MaxTemps-MinTemps
    print("Pour n =",n,":\n")
    print("Nombre d'erreurs :",nberreurs)
    print("Tours :\n")
    print("Moyenne : ",round(MoyTours,5))
    print("Écart-type : ",round(ETTours,5))
    print("Minimum : ",round(MinTours,5))
    print("Maximum : ",round(MaxTours,5))
    print("Étendue : ",round(EtTours,5))
    print("\nTemps :\n")
    print("Moyenne : ","%e"%(MoyTemps))
    print("Écart-type : ","%e"%(ETTemps))
    print("Minimum : ","%e"%(MinTemps))
    print("Maximum : ","%e"%(MaxTemps))
    print("Étendue : ","%e"%(EtTemps))

print("Niveau 0 :\n")
It(Niveau0,1000000)
print("\n------------------\nNiveau 1 :\n")
It(Niveau1,1000000)
print("\n------------------\nNiveau 2 :\n")
It(Niveau2,1000000)

#
#X=np.linspace(0,99,100)
#plt.plot(X,L1,'r',label="Nombre de tours")
#plt.show()
#plt.plot(X,L2,'r',label="Temps de résolution")
#plt.show()
