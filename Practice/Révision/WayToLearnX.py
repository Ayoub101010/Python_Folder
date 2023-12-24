#Partie1
#Ex8 
#Créez une fonction qui prend une liste et renvoie la somme de tous les nombres de la liste.


def Somme(L) : 
    
   S= 0 
   for i in range(len(L)): 
    S = S + L[i]
   print(f"La somme est : {S}")    
  
  
n = int(input("veuillez entrer la taille de la liste"))
L = [0]*n
for i in range(len(L)) :
   L[i]=(int(input()))
print(f"Voici votre liste : {L}")
Somme(L)
    






       