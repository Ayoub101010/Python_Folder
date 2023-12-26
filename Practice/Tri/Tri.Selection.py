List = [1, 4, 2, 67, 34, 100, 78]

Sorted_List = []

for i in range(len(List)):
    min_index = i
    for j in range(i + 1, len(List)):
        if List[j] < List[min_index]:
            min_index = j

    List[i], List[min_index] = List[min_index], List[i]

    Sorted_List.append(List[i])

print(Sorted_List)

