#Un programme qui prend une phrase en entrée et convertit la première lettre de chaque mot en majuscule 

def Majuscule(ch): 
    print(ch.capitalize())
    
text = str(input("veuillez entrer votre texte : "))
Majuscule(text)
    