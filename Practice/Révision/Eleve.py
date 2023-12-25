def Eleve(n): 
    eleves = {}
    for i in range(n): 
        nom = input("veuillez entrer le nom de l'élève : ")
        age = input("veuillez entrer son âge : ")
        taille = input("veuillez entrer sa Taille : ")
        eleves[nom] = (age, taille)
    return eleves

n = int(input("veuillez entrer le nombre des élèves : "))
eleves = Eleve(n)

def Afficher(eleves, nom): 
    if nom in eleves:
        print("nom: ", nom, "- âge : ", eleves[nom][0], "- taille", eleves[nom][1], "m")  
    else: 
        print("cet élève n'existe pas ")

x = input("veuillez entrer le nom d'élève : ")
Afficher(eleves, x)
