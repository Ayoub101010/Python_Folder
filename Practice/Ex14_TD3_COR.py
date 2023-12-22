liste=[8,3,12.5,45,25.5,52,1]
sorted_liste=[]

#Tri par selection
while len(liste)>0:#Une boucle while s'exécute tant que la liste liste n'est pas vide (c'est-à-dire tant qu'il y a encore des éléments à trier)
    nbr=min(liste)#À chaque itération de la boucle, il recherche le plus petit élément de la liste non triée à l'aide de la fonction min()
    sorted_liste.append(nbr)#À chaque itération de la boucle, il recherche le plus petit élément de la liste non triée à l'aide de la fonction min(),
    liste.remove(nbr)#Ensuite, il supprime l'élément le plus petit de la liste initiale en utilisant liste.remove(nbr)
print(sorted_liste)


#Tri par Bulle
for i in range(len(liste)-1):#Il parcourt la liste liste avec une boucle for allant de 0 à la longueur de la liste moins 1 (len(liste) - 1)
    index=i #Dans cette boucle externe, une variable index est initialisée avec la valeur de i.

    for j in range(i+1,len(liste)): #À l'intérieur de la boucle interne, il compare les éléments liste[i] et liste[j] (l'élément actuel et l'élément suivant).
        if liste[i]>liste[j]:#Si liste[i] est plus grand que liste[j], il met à jour la variable index pour contenir la valeur de j, ce qui signifie que l'élément à l'indice j est le plus petit de la sous-liste non triée.
            index=j
    liste[i],liste[index]=liste[index],liste[i] #Enfin, il effectue un échange (swap) des éléments à l'indice i et index en utilisant liste[i], liste[index] = liste[index], liste[i]. Cela place le plus petit élément à l'indice i.

print(liste) #Après l'exécution de ce deuxième bloc de code, la liste liste contient les éléments triés en ordre croissant.