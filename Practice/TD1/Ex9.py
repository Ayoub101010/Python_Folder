#Factorielle 

def Fact(n): 
    if n>0 : 
     P=1
     for i in range(1, n+1):
        P *= i 
     print (f"fact({n}) = {P}")
    else : 
        print("Il faut saisir un entier positif")
        
m = int(input("veuillez entrer votre nombre : "))
Fact(m) 


    
        