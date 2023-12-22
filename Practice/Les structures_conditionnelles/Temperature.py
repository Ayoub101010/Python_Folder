print("Un Programme qui permet de lire la valeur de la température de l'eau et d'afficher son état")
T = float(input("veuillez saisir le Température de l'eau : "))

"""if T < 0 : 
    print ("L'eau est glacé.")
elif  T > 100 : 
    print ("L'eau est Vapeur.")
else : 
    print ("L'eau est Liquide .")"""
    
if T < 0 : 
    print ("L'eau est glacé.")
elif  T >= 0 and T <= 100:
     print ("L'eau est Liquide .")
else : 
        print ("L'eau est Vapeur.")
        

    
    
    
    