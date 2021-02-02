# Importation des modules.
import random

# Liste avec la bibliothèque de mots du jeu.
bibliotheque = ["Matrice", "credit", "Lego", "exercice", "Lundi", "Dimanche", "Mardi", "moteur", "aggregation"]

# Choix du mot de façon aléatoire.
nb = random.randint(0,len(bibliotheque))
mot = bibliotheque[nb]
longueur = len(mot)