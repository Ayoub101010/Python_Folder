Livre = {"titre": "Gossip", "auteur":"Alan ", "année":"2010", "genre":"Novel" }

def Imprime (**Livre):
    for key, value in Livre.items():
        print (f"{key}: {value}")

        
Imprime (**Livre)