prixUT = int(input("Saisissez un prix : "))

if prixUT < 20 : 
    pourcentage = 10/100

elif 20 <= prixUT < 50 :
    pourcentage = 7.5/100

elif 50<= prixUT < 100 :
    pourcentage = 5/100

elif 100 <= prixUT : 
    pourcentage = 2.5/100

prixTTC =  prixUT + (prixUT * pourcentage)

print ("Voici votre prix TTC : " ,prixTTC)