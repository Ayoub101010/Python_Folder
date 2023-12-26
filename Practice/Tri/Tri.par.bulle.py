List = [1, 4, 2, 67, 34, 100, 78]

Sorted_List=[]

for i in range(len(List)): 
    for j in range(i+1, len(List)): 
        if List[i] > List[j]:
            List[i],List[j]=List[j],List[i]
            '''temp = List[i]
            List[i]=List[j]
            List[j]=temp '''
            
    Sorted_List.append(List[i])
    
print(Sorted_List)    