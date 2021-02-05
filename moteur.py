# Importation des modules.
import affichage

# État du jeu.
enJeu = True

# État du jeu si la partie est perdu.
def Perdu():
    affichage.erreur = True
    affichage.essais = 8
