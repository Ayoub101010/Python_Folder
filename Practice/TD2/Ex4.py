#Calculer le nombre des mots dans une phrase 

def NbrMots(ch): 
    
    n=0
    for i in range(len(ch)):
        if ch[i] == ' ':
            n += 1
    print(f"le nombre de mots de cette chaine de caractère est : {n}")
    
    
text = str(input("veuillez entrer votre texte : "))
NbrMots(text)

