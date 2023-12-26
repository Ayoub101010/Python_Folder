# Calculer le nombre d'occurence d'un caractère 

def NbrOccurence (ch, c ):
    
    nbr=0 
    for i in range(len(ch)):
        if ch[i] == c :
            nbr +=1
    print(f"Le nombre d'occurence de caractere {c} est : {nbr}")
    
text = str(input("veuillez entrer votre texte:  "))
caractere = str(input("veuillez entrer votre caractere:  "))
NbrOccurence(text,caractere)


