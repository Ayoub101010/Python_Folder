print("Un Programme qui permet de demander à l'utilisateur de saisir un entier entre 1 et 7 au clavier, et afficher le nom du jour correspondant")

n = int(input("veuillez saisir un nombre entre 1 et 7 : "))

if  n<=0 or n>=8 : 
    print ("le nombre est invalide")
elif n == 1:
    print("le jour est:  LUNDI")
elif n == 2:
    print("le jour est:  MARDI")

elif n == 3:
    print("le jour est:  MERCREDI")

elif n == 4:
    print("le jour est:  JEUDI")

elif n == 5:
     print("le jour est:  VENDREDI")

elif n == 6:
    print("le jour est:  SAMEDI")

elif n == 7:
    print("le jour est:  DIMANCHE")

    
