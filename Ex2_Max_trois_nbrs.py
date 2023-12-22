a = float(input("veuillez saisir le premier nombre :"))
b = float(input("veuillez saisir le deuxième nombre :"))
c = float(input("veuillez saisir le Troisiéme nombre :"))


a1 = f"le premier nombre est : {a}" 
a2 = f"le deuxiéme nombre est : {b}" 
a3 = f"le Troisiéme nombre est : {c}" 

print(a1)
print(a2)
print(a3)

if a<b : 
    if c<b :
        print("Le maximum est : ", b )
    else : 
            print("Le maximum est : ", c)
else : 
    if c<a:
        print("Le maximum est : ", a)
    else :
        print("Le maximum est : ", c)

        

        
