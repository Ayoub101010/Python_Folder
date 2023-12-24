#Ex2
#Créez une fonction qui accepte une liste et renvoie le dernier élément de la liste.

def getLast(L): 
    
   print(f"votre dernier élément de votre  liste est : {L[-1]}")


n=int(input("veuillez entrer votre liste : "))
L=[0]*n
for i in range(len(L)): 
    L[i] = (input())
print(f"voici votre liste principale : {L}")
getLast(L)
    
       
            