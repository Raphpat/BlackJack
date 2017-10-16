from random import *
victoire_joueur=0                                   #r correspond au nbr de parties gagnées par le joueur
victoire_banque=0                                   #e correspond au nbr de parties gagnées par la banque

def nbrdelancés():
    global victoire_joueur                          #permet de faire appel et de modifier une variable en dehors de l'espace de la fonction
    global victoire_banque
    h=0                                             #h correspond au score du joueur
    g=0                                             #g correspond au score de la banque
    relance="y"                                     #permet de lancer au moins une fois
    while relance=="y":
        x=int(input("Combien de lancés voulez vous effectuer ? "))
        for i in range(x):
            j=randint(1,6)                          #j correspond aux lancés du joueur
            b=randint(1,6)                          #b correspond aux lancés de la banque
            print("lancé",i+1,":",j)
            h=h+j
            g=g+b
        if g>21 and h>21:
            relance="n"
            print("La banque est à ",g," et vous êtes à ",h,", la partie est nulle.")
        elif g>21:
            relance="n"
            print("La banque est à ",g," et vous êtes à ",h,", la banque a perdu.")
        elif h>21:
            relance="n"
            print("La banque est à ",g," et vous êtes à ",h,", vous avez perdu.")
        elif g==21 and h!=21:
            relance="n"
            victoire_banque=victoire_banque+1       #pour comptabiliser les parties gagnées
            print("La banque est à 21 et vous êtes à ",h,"la banque a gagnée. Le score est à ",victoire_banque," pour la banque contre ",victoire_joueur," pour vous.")
        elif g!=21 and h==21:
            relance="n"
            victoire_joueur=victoire_joueur+1       #pour comptabiliser les parties gagnées
            print("La banque est à ",g," et vous êtes à 21, vous avez gagné. Le score est à",victoire_banque," pour la banque contre ",victoire_joueur," pour vous.")
        elif g==21 and h==21:
            relance="n"
            victoire_banque=victoire_banque+1
            victoire_joueur=victoire_joueur+1
            print("Vous avez tous les deux atteints 21, vous avez tous les deux gagné.")
        else:
            print("Vous êtes à ",h)
            relance=str(input("Voulez vous relancer les dés y/n ?"))
    return()

reponse="y"
while reponse=="y":
    nbrdelancés()
    reponse=str(input("Voulez vous rejouer y/n ?" ))
