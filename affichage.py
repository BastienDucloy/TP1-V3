# Importation des modules.
import main
import tirage

# Déclaration des condition et leurs valeurs d'origines.
essais = 0
erreur = False

# Fonction pour gérer l'affichage du pendu.
def affichage_pendu(erreur,essais):

    if erreur == True and essais == 1:
        print("________")
        print(" |/    |")
        print(" |")
        print(" |")
        print(" |")
        print("-#-")
        essais = main.chance
    elif erreur == True and essais == 2:
        print("________")
        print(" |/    |")
        print(" |     O")
        print(" |")
        print(" |")
        print("-#-")
        essais = main.chance
    elif erreur == True and essais == 3:
        print("________")
        print(" |/    |")
        print(" |     O")
        print(" |     |")
        print(" |")
        print("-#-")
        essais = main.chance
    elif erreur == True and essais == 4:
        print("________")
        print(" |/    |")
        print(" |     O")
        print(" |    /|")
        print(" |")
        print("-#-")
        essais = main.chance
    elif erreur == True and essais == 5:
        print("________")
        print(" |/    |")
        print(" |     O")
        print(" |    /|\ ")
        print(" |")
        print("-#-")
        essais = main.chance
    elif erreur == True and essais == 6:
        print("________")
        print(" |/    |")
        print(" |     O")
        print(" |    /|\ ")
        print(" |    / ")
        print("-#-")
        essais = main.chance
    elif erreur == True and essais == 7:
        print("________")
        print(" |/    |")
        print(" |     O")
        print(" |    /|\ ")
        print(" |    / \ ")
        print("-#-")
        essais = main.chance
    elif erreur == True and essais == 8:
        print("\n!!! DOMMAGE, VOUS AVEZ PERDU !!!")
        print("\n:(")
        print("Le mot que vous cherchiez était", tirage.mot)