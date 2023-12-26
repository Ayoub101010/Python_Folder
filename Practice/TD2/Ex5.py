#Calculer le nombre des caracteres d'une chaine sauf l'espace 

def NbrCaractere(ch): 
    
    n=0
    for i in range(len(ch)):
        if ch[i] != ' ':
            n += 1
    print(f"le nombre de mots de cette chaine de caractère est : {n}")
    
    
text = str(input("veuillez entrer votre texte : "))
NbrCaractere(text)

