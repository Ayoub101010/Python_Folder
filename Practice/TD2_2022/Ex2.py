#même signe ou Non 

def Check_Signe(n, m ) : 
    if n*m > 0 : 
        print(f"{n} et {m} ont le même signe ")
    elif n*m < 0 : 
         
        print(f"{n} et {m} n'ont pas  le même signe ")
    else : 
        print(f"l'un des deux nombres ou les deux nombre sont nuls ")
        
        
n  = int(input("veuillez entrer le premier nombre "))
m  = int(input("veuillez entrer le deuxiéme nombre "))
Check_Signe(n, m)
