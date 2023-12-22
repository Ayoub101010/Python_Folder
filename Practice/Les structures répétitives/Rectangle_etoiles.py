#Un programme permettent de prendre un nombre L de ligne et un nombre C do colonnes, puis de réaliser un << rectangle d'étoiles >> de L lignes par C colonnes. 
#On commence par demander au utilisateur le nombre de lignes (L) et le nombre de colonnes (C).
L =int(input("veuillez saisir le nombre de lignes : "))
C = int(input("veuillez saisir le nombre de colones : "))

for i in range(L): 
    for j in range (C): 
        
       print ("*",end=" ")
    print()
    
