
def verification(choix):
    # Saisie du joueur et création de la liste de comparaison des caractères.
    alphabet = tuple("abcdefghijklmnopqrstuvwxyz")
    accents = tuple(u"éèêûöë")
    indice = "indice"

    # Vérification du choix du joueur.
    while choix not in alphabet and choix not in accents and choix not in indice:
        print("Vous devez saisir une lettre!")
        choix = input("Veuillez saisir une lettre : ")