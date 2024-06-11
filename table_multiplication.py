multiplcation = []

for i in range(1, 11):
    tableau = []
    for a in range(1, 11) :
        number = f'{a} x {i} = {i*a}'
        tableau.append(number)

    multiplcation.append(f"Tableau de {i} : {tableau}")


for i in multiplcation :
    print("")
    print(i)
    print("")
