def ChangerCaratere(ch, n, m ):
    nouv = "" 
    for c in ch : 
        if c ==  n : 
            nouv += m 
        else : 
            nouv += c
    print(f"Voici votre nouvelle chaine de caratere : {nouv}")        
  
chaine =str(input("veuillez entrer votre Phrase : "))
x= str(input("veuillez entrer votre caractere : "))
y = str(input("veuillez entrer le nouveau caratere : "))
ChangerCaratere(chaine, x, y )
       