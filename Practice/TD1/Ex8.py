
def is_prime(n):

  for i in range(2,n):
    if (n%i) == 0:
     print(f"{n} n'est pas premier ")
     break
    else : 
     print(f"{n} est pas premier ")
     break 
    
  


N = int(input("veuillez entrer votre nombre : "))

is_prime(N) 