List = [1, 4, 2, 67, 34, 100, 78]
Sorted_List = []

for i in range(len(List)):
    Sorted_List.append(List[i])
    for j in range(i, 0, -1):
        if Sorted_List[j] < Sorted_List[j - 1]:
            Sorted_List[j], Sorted_List[j - 1] = Sorted_List[j - 1], Sorted_List[j]

print(Sorted_List)
