#BlackJack:
#Lancé de X dés
# par le Joueur et l'ordi
# dés = [1;6] --> randint(a,b) (lecture de la documentation random)
# somme > 21 perdu
# Les 2, > 21 nul
# Si inférieur à 21, choix de relancer pr le joueur

from random import *

#Fonction pour lancer les dés
def lance(nb):
    des = [0 for i in range(nb)]
    for i in range(nb):
        des[i] = randint(1,6)
    #print(des)
    total = sum(des) #méthode sum() trouvée en ligne
    return(total)

#Fonction pour imprimer les 2 scores
def retourScores(j1, j2):
    print("--") #Problème de lisibilitté, ici remédié par les "--"
    print("Score joueur: ", j1)
    print("Score banque: ", j2)

def retourResultats():
    print("--")
    print("Victoires joueur: ", resultats[0])
    print("Victoires banque: ", resultats[1])
    print("Parties nulles: ", resultats[2])
    print("--")

#Premières comparaisons, pour voir si la partie n'est pas finie d'office
#(quelqu'un au dessus de 21)
def comparaisons1(j1, j2):
    if j1 > 21 and j2 > 21:
        retourScores(j1, j2)
        print("Partie Nulle")
        resultats[2] += 1
        return True
    elif j1 > 21:
        retourScores(j1, j2)
        print("Vous avez perdu, la banque a gagné")
        resultats[1] += 1
        return True
    elif j2 > 21:
        retourScores(j1, j2)
        print("Vous avez gagné, la banque a perdu")
        resultats[0] += 1
        return True
    else:
        return False

#Comparaisons entre j1 et j2 pr déterminer vainqueur
def comparaisons2(j1, j2):
    retourScores(j1, j2)
    if j1 > j2:
        print("Vous avez gagné, la banque a perdu")
        resultats[0] += 1
    elif j2 > j1:
        print("Vous avez perdu, la banque a gagné")
        resultats[1] += 1
    else: #J'ai pensé au bug j1 == j2 que après avoir programmer comp2
        print("Partie Nulle")
        resultats[2] += 1

#Définition de la difficulté, qui augmente ou diminue le score de la banque de 1 ou 2
print("Définir la difficulté: Facile, Moyen, Difficile, Extreme")
print("Difficulté moyenne par défaut")
difficulte = str(input('Difficulté: '))
modif = 0
if difficulte == 'Facile':
    modif = -1
elif difficulte == 'Difficile':
    modif = 1
elif difficulte == 'Extreme':
    modif = 2
else:
    modif = 0

#Variable pour le while
rejouer = 'y'
#Variable des victoires du joueur, de la banque et nul
resultats =[0 for i in range(3)]
#print(resultats)

#Début, lancé de tout les dés, sortie du scoreJoueur
#Initialisation de la boucle de tour de jeu qui contient le code pour
#une manche
while rejouer == 'y':
    x = int(input('Nombre de dés lancés: '))
    print("--")
    scoreJoueur = lance(x)
    print("Votre score: ", scoreJoueur)
    print("--")
    scoreBanque = lance(x) + modif
    #print("Score banque: ", scoreBanque)
    end = comparaisons1(scoreJoueur, scoreBanque)
    #Si tout le monde <21 le jeu continue
    if end == False:
        relance = str(input("Voulez vous relancer? (y/n): "))
        #Boucle de relance des dés pour le joueur
        while relance == 'y':
            x = int(input('Nombre de dés lancés: '))
            print("--")
            scoreJoueur = lance(x)
            print("Votre score: ", scoreJoueur)
            print("--")
            end = comparaisons1(scoreJoueur, scoreBanque)
            if end == True:
                break
            relance = str(input("Voulez vous relancer? (y/n): "))
        comparaisons2(scoreJoueur, scoreBanque)
    else:
        print("Fin du tour")
    retourResultats()
    rejouer = str(input("Voulez vous rejouer? (y/n): "))
print("Fin de la partie")
retourResultats()

