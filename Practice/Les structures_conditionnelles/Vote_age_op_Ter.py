print("Un Programme qui permet de demander l'âge d'un citoyen, puis affiche si le citoyen peut voter aux élections en utilisant l'opérateur ternaire (l'âge de vote est de 18ans).")


Age = int(input("Veuillez saisir votre age : "))

An = f"Votre âge est : {Age} ans "

print(An)


"""
    La première mèthode : !!!!!! 
    
    if Age < 0 :
    print ("Veuillez saisir une valeur d'age strictement positive")
elif Age < 18 : 
    print ("Vous êtes mineur, vous n'avez pas le droit de voter")
else:
    print("Oui, Vous pouvez voter")
    
    
    """
    
    #La mèthode ternaire 
    

Vote = f"vous avez le droit de voter"

NeVotePas = f"Vous n'avez pas le droit de voter"

affiche = NeVotePas if Age < 18 and Age > 0 else Vote 

print(affiche)



"""
    #La Troisième mèthode 

    msg = "Vous pouvez voter" if Age >= 18 else "Vous n'avez pas le droit de voter "

    """




    
    