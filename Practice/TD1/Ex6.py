def NomDeJour(n):
    if n==1 : 
        print("C'est Lundi")
    elif n==2 : 
        print("C'est Mardi")
    elif n==3 : 
        print("C'est Mecredi")
    elif n==4 : 
        print("C'est Jeudi")
    elif n==5 : 
        print("C'est Vendredi")
    elif n==6 : 
        print("C'est Samedi")
    elif n==7 : 
        print("C'est Dimanche")
    else : 
        print("Ce numéro ne coorespond à aucun jour, veuillez saisir un numéro entre 1 et 7 ")
        
        
m = int(input("veuillez entrer le numéro de jour : "))
NomDeJour(m)

