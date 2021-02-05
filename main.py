# Importation des modules.
import tirage
import saisie
import affichage
import moteur
import random

# Présentation des consignes du jeu du pendu.
print("     ----- LE PENDU ----- \n")
print("Bienvenue dans le jeu du pendu !!! \n")
print("Le but de ce jeu est de deviner le mot choisi... avant que votre personnage ne se retrouve entièrement sur l'échaffaud.")
print("Lors de chaque partie vous aurez le droit à un indice pour vous éviter la potence...")
print(" !!! Pour faire appel à cet indice écrivez le mot : 'indice', vous pourrez ainsi découvrir l'une des lettres composant le mot. !!!")
print("Vous avez tout bien compris...")
print("... alors commençons! \n")


# Mise en variable des informations sur le mot de la liste choisit.
mot_selectionne = tuple(tirage.mot)
longueur = tirage.longueur

# Création du mot vide
mot_vide = ["_"] * len(mot_selectionne)

# initialisation des variables du jeu
nb_tour = 0
aide_utilisee = False
position = 0
lettre_lue =['_']
utilise = False
nb_indice = 0
lettre_indice = ""

# --- BlOC PRINCIPAL DU JEU --- #
while moteur.enJeu:

# Utilisation de la fonction pour le choix d'une lettre.
    lettre = input("\n\nVeuillez saisir une lettre : ")
    saisie.verification(lettre)
    if lettre == "indice" and aide_utilisee == True:
        print ("Vous avez déjà utilisé votre indice, désolé...")

# Choix aléatoire d'une lettre dans le mot pour l'indice. La comparé aux lettres du mot et lettres déjà sorties.
    def choix_lettre_indice():
        nb_indice = random.randint(0, len(mot_selectionne) - 1)
        lettre_indice = mot_selectionne[nb_indice]
        return lettre_indice

# Permet d'afficher help quand un indice est demandé. Là où mettre le code de l'aide.
    if lettre == "indice" and aide_utilisee == False:

        lettre_indice = choix_lettre_indice()

        while lettre_indice in mot_vide:
            lettre_indice = choix_lettre_indice()

        if lettre_indice in tuple(mot_selectionne):
            while position < len(mot_selectionne):
                lettre_si = mot_selectionne[position]
                if lettre_indice == lettre_si:
                    mot_vide[position] = lettre_indice
                position = position + 1
            position = 0
            print("La lettre '" + lettre_indice + "' se trouve dans le mot : " + ''.join(map(str, mot_vide)))
            print("Vous avez utilisé votre indice...")
            aide_utilisee = True

# Permet de gérer les erreurs du joueur et d'afficher le pendu
    if lettre not in mot_selectionne and lettre != "indice":

# Incrémentation du compteur nb_tour
        nb_tour = nb_tour + 1
        print("Erreur : la lettre '" + lettre + "' ne se trouve pas dans le mot.")
        affichage.erreur = True
        affichage.affichage_pendu(affichage.erreur, affichage.essais+nb_tour)

# Permet d'afficher les lettres trouvées par le joueur dans le mot
    if lettre in mot_selectionne and lettre != "indice":
    #Remplissage du mot vide avec la lettre trouvée
        while position < len(mot_selectionne):
                lettre_lue = mot_selectionne[position]
                if lettre_lue == lettre:
                    mot_vide[position] = lettre
                position = position + 1
        print("La lettre '" + lettre +"' se trouve dans le mot : " + ''.join(map(str, mot_vide)))
        position = 0



# Vérification si la partie est gagnée ou perdue.
    if tuple(mot_vide) == tuple(mot_selectionne):
        print("\nBRAVO vous avez trouvé!... Le mot était : " + ''.join(map(str, mot_vide)))
        moteur.enJeu = False
    elif nb_tour == 8:
        moteur.Perdu()
        moteur.enJeu = False