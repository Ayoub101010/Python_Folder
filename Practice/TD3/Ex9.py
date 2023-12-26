#mèthode 1 : 

'''t1 = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
t2 = ['Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin', 'Juillet', 'Août', 'Septembre', 'Octobre', 'Novembre', 'Décembre']

t3 = []  


for month, days in zip(t2, t1):
    t3.append(month)
    t3.append(days)

print(t3)'''

#Mèthode 2 : 


t1 = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
t2 = ['Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin', 'Juillet', 'Août', 'Septembre', 'Octobre', 'Novembre', 'Décembre']

t3 = []  

for i in range(len(t1)):
    t3.append(t2[i])
    t3.append(t1[i])

print(t3)


