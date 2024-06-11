heure = float(input("Entrez votre nombre d'heure : "))

print ("Voici le nombre d'heure : " ,heure)

VariableHeure1 = heure + (0.05 * heure)
VariableHeure2 = heure + (0.02 * heure) 

print("Voici la variable heure 1 : " , VariableHeure1)
print("Voici la variable heure 2 : " ,VariableHeure2)

Operateur1 = 10 + float(VariableHeure1)

Operateur2 = 20 + float(VariableHeure2)

print("Voici le résultat de l'opérateur 1 : " ,Operateur1)
print("Voici le résultat de l'opérateur 2 : " , Operateur2)


if Operateur1 < Operateur2 :{
    print("L'opérateur 1 est + intéressant ")
}

elif Operateur1 == Operateur2 : {
    print("Les 2 se valent")
} 

else : {
    print ("l'opérateur 2 est + intéressant")
}



