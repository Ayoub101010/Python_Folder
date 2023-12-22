#en utilisant un dictionnaire 

def Affiche(**dict):
    for key, value in dict.items():
        print(f"{key}: {value}")

Affiche(first_name="Ayoub", last_name="Dahdouh", city="Tangier")

# en utilisant une liste 
"""
    def Affiche_Liste(*Liste):
    for i in range(len(Liste)):
        print(f"{Liste[i]} " )
        
        
Affiche_Liste([[1, 4], [6, 9]])  
    """


#Retourner plusieur expression _ les variables globales _ Locales 

etudiant1 = {"first_name" :"Ayoub", "last_name": "Dahdouh", "city": "Tangier" }  
etudiant2 = {"first_name" :"Brahim", "last_name": "Bernoussi", "city": "Tangier" }  

def affiche (**etudiant1) : 
           global etudiant2
           etudiant2 = {"first_name" :"Ayoub", "last_name": "Dahdouh", "city": "Tetouan" }



