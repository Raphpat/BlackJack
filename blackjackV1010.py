#BlackJack:
#Lancé X dés
# par le Joueur et l'ordi
# dés = [1;6] --> randint(a,b)
# somme > 21 perdu
# Les 2, > 21 nul
# Si inférieur à 21, choix de relancer pr le joueur

from random import *

def lancé(nb):
    des = [0 for i in range(nb)]
    for i in range(nb):
        des[i] = randint(1,6)
    #print(des)
    total = sum(des) #méthode sum() trouvée en ligne
    return(total)

def retourScores(j1, j2):
    print("Score joueur = ", j1)
    print("Score banque = ", j2)

#Premières comparaisons, pour voir si la partie n'est pas finie d'office
#(quelqu'un au dessus de 21)
def comparaisons1(j1, j2):
    if j1 > 21 and j2 > 21:
        retourScores(j1, j2)
        print("Partie Nulle")
        return True
    elif j1 > 21:
        retourScores(j1, j2)
        print("Vous avez perdu, la banque a gagné")
        #Possibilité compter score
        return True
    elif j2 > 21:
        retourScores(j1, j2)
        print("Vous avez gagné, la banque a perdu")
        return True
    else:
        return False

#Comparaisons entre j1 et j2 pr déterminer vainqueur
def comparaisons2(j1, j2):
    return 0

#Début, lancé de tout les dés, sortie du scoreJoueur
x = int(input('Nombre de dés lancés: '))
scoreJoueur = lancé(x)
print("Votre score: ", scoreJoueur)
scoreBanque = lancé(x)
#print(scoreBanque)
end = comparaisons1(scoreJoueur, scoreBanque)

if end == False:
    relance = str(input("Voulez vous relancer? (y/n): "))
    while relance == 'y':
        x = int(input('Nombre de dés lancés: '))
        scoreJoueur = lancé(x)
        print("Votre score: ", scoreJoueur)
        end = comparaisons1(scoreJoueur, scoreBanque)
        if end == True:
            break
        relance = str(input("Voulez vous relancer? (y/n): "))
else:
    print("Fin de la partie")
    #Ajouter impression compteur
