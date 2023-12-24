#Résolution d'une équation de 2ème dégré 
import math 

def Equation_deuxieme_degre (a, b, c) : 
  if a==0 : 
      print ("L'équation n'est pas une équation de 2e dégré")
      print(f"La solution de cette équation est : {-c/b}")
  elif b==0 : 
      x1 = math.sqrt(c/a)
      x2 = - math.sqrt(c/a)
      print(f"L'équation admet deux solutions : \n{x1} et {x2}")
  elif c==0 : 
      print(f"x=0 ou x = {-b/a }")
  else : 
      
    delta = b**b -  4 * a * c 
    if delta < 0 : 
        print("cette équation n'admet pas de solution réels")
    elif delta == 0 : 
        x = -b / (2 * a)
        print(f"cette équation admet une seule solution : {x}")
    else : 
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        print(f"cette équation admet deux solutions : \n{x1} et\n{x2}")
        
        
a= float(input("veuillez entrer les valeur de a : "))
b= float(input("veuillez entrer les valeur de b : "))
c= float(input("veuillez entrer les valeur de c : "))

print(f"Soit l'équation suivante : \n {a} x² + {b} x + {c}")
Equation_deuxieme_degre(a,b,c)


        