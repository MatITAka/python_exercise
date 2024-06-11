print("Calcul de TVA")

montant = int(input("Saisir votre montant à calculer : "))

tauxTVA = int(input("Saisir votre montant de TVA : "))

montantTaxe = montant * tauxTVA/100

print (montantTaxe)

montantTTC = montant - montantTaxe

print (montantTTC)

