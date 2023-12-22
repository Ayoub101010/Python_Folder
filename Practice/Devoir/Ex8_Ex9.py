#Ex8 : sous-ensemble

Legumes = {"carotte", "brocoli"}
fruits = {'pomme', 'banane', 'orange'}
aliments = Legumes|fruits 
print(aliments)
"""
if fruits.issubset(aliments):
    print("Oui, fruits est un sous-ensemble de l'ensemble aliments")
else : 
    print("Non, fruits n'est pas un sous-ensemble de l'ensemble aliments ")
"""

for element in fruits:
  if element in aliments:
      a = 1 
  else : 
      a = 0 
if a == 1 : 
  print("fruits est un sous ensemble des aliments")    
  

  
  #Ex9   

fruits.clear()
aliments = Legumes|fruits 

Aliments=f"voici la nouvelle ensemble des aliments : {aliments}" 
print(Aliments)
  
  
