#Ex10

Legumes = {"carotte", "brocoli"}
Legumes_copies = Legumes.copy()

Legumes_copies.add('épinard')
legumes=f"L'ensemble Legumes est : {Legumes}"
#print(legumes)
legumes_copies=f"L'ensemble Legumes copie est : {Legumes_copies}"
print(legumes_copies)
#La modification de la copie ne modifie pas l'original, mais ajoute un élément à la copie