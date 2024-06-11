produits = float(input("Saisissez le nombre de produits : "))
print("Voici le nombre de produits :", produits)

prix = float(input("Saisissez le prix : "))
print("Voici le prix de chaque article : " ,prix)

montantHT = produits * prix
print("Voici le montant total hors taxe : " ,montantHT)

match montantHT :

    case _ if montantHT < 200 : 
        taux = 2,5/100
    
    case _ if 200 <= montantHT < 400 :
        taux = 5/100
    
    case _ if 400 <= montantHT < 700 : 
        taux = 7,5/100
    
    case _ if 700 <= montantHT :
        taux = 10/100

print("Voici le taux : " ,taux)

montantRemise = montantHT - (montantHT * taux)

print ("Voici le prix remisé : ", montantRemise)

montantTaxe = montantRemise * 20/100 

print("Voici la taxe TVA : " ,montantTaxe)

montantTTC = montantRemise - montantTaxe 

print ("Voici le prix TTC : " ,montantTTC)

