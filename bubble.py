tableau = [10,35,26,8,90,67,34,65,78,28,19]

tableauSort = []

print(tableau)

while tableau :
    valeurMini = tableau[0]
    for valeur in tableau :
        if valeur < valeurMini :
            valeurMini = valeur
    tableauSort.append(valeurMini)
    tableau.remove(valeurMini)

print(tableauSort)


        

