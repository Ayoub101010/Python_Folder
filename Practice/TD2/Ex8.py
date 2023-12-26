#Trouver la dernière position d'une sous-chaine "Bon" dans une chaine donnée

'''def TrouverBon(ch): 
    
    nbr_Mots = 0 
    for i in range(len(ch)): 
        if (ch[i:i+3] == 'Bon'):
            nbr_Mots +=1
            
            print(f"Bon est apparait dans la position : {i}")
    
text = str(input("veuillez entrer votre texte : "))
TrouverBon(text)'''
    
#Méthode 2 _ essayer de donner le numéro du mot 

def TrouverBon(ch): 
    phrase = ch.split()  
    nbr_Mots = 0 
    for i, mot in enumerate(phrase):
        if mot == 'Bon':
            nbr_Mots += 1
            print(f"Le mot 'Bon' est apparu à la position du mot : {i + 1}")

text = input("Veuillez entrer votre texte : ")

TrouverBon(text)
