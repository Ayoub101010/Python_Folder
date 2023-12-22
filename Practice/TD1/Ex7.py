Poids = int(input("veuillez saisir le poids "))

if Poids < 0 : 
    print("Ce poids n'existe pas ")
    
elif Poids <=2 : 
    print ("le coût d'expédition est : 5$")
elif Poids <=5 :
    print ("le coût d'expédition est : 10$")
elif Poids <=10 : 
    print ("le coût d'expédition est : 20$")
elif Poids > 10 : 
    print ("le coût d'expédition est : 30$")
    

    