note = int(input("Saisir une note : "))

match note : 
    case _ if note <= 5 :
        print("Lettre E")
    

    case _ if 5 < note <= 8: 
        print ("Lettre D")
    

    case _ if 8 < note <=11: 
        print("Lettre C ")
    

    case _ if  11< note <=14 : 
        print("Lettre B")
    

    case _ if 14 < note : 
        print("Lettre A")
    
