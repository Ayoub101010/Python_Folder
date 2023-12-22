#Un programme qui permet de calculer la somme des 20 premiers entiers positifs
s = 0   
for i in range(21): 
    s = s + i
    
print("La somme est : ",s)    
#print ("La somme est : ", sum([i for i in range(21)]))