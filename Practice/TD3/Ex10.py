def Pair_Impair_List(List): 
    List_Pair = []
    List_Impair = []
    
    for i in range(len(List)):
        
        if (List[i] % 2 == 0) : 
            List_Pair.append(List[i])
        else:              
             List_Impair.append(List[i])
    print(f"voice la liste pair : {List_Pair}")
    print(f"voice la liste impair : {List_Impair}")
             
Liste = [int(x) for x in input("veuillez entrer votre liste : ").split() ]
Pair_Impair_List(Liste)

      