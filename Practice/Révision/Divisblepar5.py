#Créez une fonction qui renvoie True si un entier est divisible par 5, sinon renvoie False

def isDivisibleBy5(n) :
    
    if n%5 == 0 : 
        
        print(f"{n} est divisible par 5 ")
    else :
        print(f"{n} n'est pas divible par 5 ")
 
    
n = int(input("Veuillez entrer votre entier : "))
isDivisibleBy5(n)
 
    
    
    
    