#Le nombre de voyelles 

def NombreDeVoyelles(ch) : 
    nbr = 0 
    for i in range(len(ch)): 
        if ch[i] == 'a' or ch[i] == 'e' or ch[i] == 'o' or ch[i]=="i" or ch[i]=="u" :
            nbr += 1 
    print(f"le nombre de voyelles dans cette phrase est : {nbr}")
    
    
phrase = input("entrez une phrase: ")
print(f"votre phrase est : {phrase}")
NombreDeVoyelles(phrase)

    