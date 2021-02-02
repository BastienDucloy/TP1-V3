# Saisie du joueur et création de la liste de comparaison des caractères.
alphabet = tuple("abcdefghijklmnopqrstuvwxyz")
choix = input("\n\nVeuillez saisir une lettre : ")

# Vérification du choix du joueur.
def verification_choix(choix):
    while choix not in alphabet:
        print("Vous devez saisir une lettre!")
        choix = input("Veuillez saisir une lettre : ")