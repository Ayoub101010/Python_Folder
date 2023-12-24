#Ex9 
#Créez une fonction qui prend une liste de nombres et renvoie le plus petit nombre de la liste.


def getMin (L) : 
 min = L[0]
 for i in range(1,len(L)):
     if L[i]<min : 
         min=L[i]
 print(f"le minimum est : {min}")
 
 
 
n=int(input("veuillez entrer la taille de votre liste"))
L=[0]*n
for i in range(len(L)):
  L[i]=int(input())
print(f"voici votre liste : {L}")
getMin(L)
      
     
        