#Afficher les mentions suivantes selon la valeur de la moyenne générale choisie par l'utilisateur 

moyenne=int(input("veuillez saisir la moyenne  "))
print("la moyenne est : ",moyenne)

if moyenne < 0 or moyenne > 20 : 
    print("veuillez saisir une moyenne correcte ")
    
elif moyenne >=16 : 
        print("Très Bien ")
elif moyenne >=14 : 
        print("Bien ")
elif moyenne >=12 : 
        print("Assez Bien")
        
      

     

    
