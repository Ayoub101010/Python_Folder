#EX 11 : 

personne = {"nom":"Dahdouh","age":28,"ville":"Tanger"}
print(personne)

#EX12 : 

for valeur in personne.values() : 
    print (valeur)
    
#Ex 13 :  

personne["age"]="30"

print(personne)

#Ex14 : 

personne["email"] = "ayoub.dahdouh2@etu.uae.ac.ma"
print(personne)


#Ex 15 : 

del personne["ville"]
print(personne)

#Ex 16 : 

if "nom" in personne:
    print("nom existe")
else : 
    print("nom n'existe pas ")




     
    