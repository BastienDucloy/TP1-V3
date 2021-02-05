# Importation des modules.
import random

# Liste avec la bibliothèque de mots du jeu.
bibliotheque = ["matrice", u"crédit", "lego", "exercice", "lundi", "dimanche", "mardi", "moteur", u"aggrégation", u"noël"]

# Choix du mot de façon aléatoire.
nb = random.randint(0,len(bibliotheque) - 1)
mot = bibliotheque[nb]
longueur = len(mot)