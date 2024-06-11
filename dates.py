a1 = int(input("Saisissez l'année de référence 1 :"))
m1 = int(input("Saisissez le mois de référence 1 :"))
j1= int(input("Saisissez le jour de référence 1 : "))

a2 = int(input("Saisissez l'année de référence 2 : "))
m2 = int(input("Saisissez le mois de référence 2 : "))
j2 = int(input("Saisissez le jour de référence 2 : "))


if a1 > a2 : 
    print("la date 1 est supérieur à la date 2")
elif a1 < a2 : 
    print("la date 2 est supérieur à la date 1")
else :
        if m1 > m2 : 
            print('la date 1 est supérieur a la date 2')
        if m1 < m2 : 
            print("La date 2 est supérieur à la date 1")
        else : 
                if j1 > j2 : 
                    print('la date 1 est supérieure à la date 2')
                if j1 < j2 : 
                    print("la date 2 est supérieur à la date 1")
                else :
                        print ("il s'agit du même jour")
