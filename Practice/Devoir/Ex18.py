# Ex 18 : 

Liste = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]

occurrences = {}

for i in Liste:
    if i in occurrences:
        occurrences[i] += 1
    else:
        occurrences[i] = 1

print(occurrences)