nbPhoto = int(input("Entrez un nombre de photocopies : "))

prix = 0.0

if nbPhoto <10 : 
    prix = nbPhoto * 0.1

elif 11 <= nbPhoto <= 20: 
    prix = (10*0.1) + ( (nbPhoto - 10) *0.08)

elif 21 <= nbPhoto <= 50 :
    prix = (10*0.1) + (10*0.08) + ( (nbPhoto-20) *0.06) 

elif 50 < nbPhoto :
    prix = (10*0.1) + (10*0.08) + (30*0.06) + ( (nbPhoto-50) *0.03)


print("Voici le TTC : " ,prix, "$")