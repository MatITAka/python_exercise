quantity = int(input("Saisissez une quantité de produits :"))

modeLivraison = ""

while modeLivraison != "rapide" or "normal" : 
    modeLivraison = str(input("Choissisez votre mode de livraison (rapide/normal) :"))
    if modeLivraison == "rapide" or  modeLivraison == "normal" : 
        break 



match modeLivraison :

    case "rapide" :
       if quantity < 50 :
           print('2 jours de livraison')
       elif 50 <= quantity < 100 :
           print('3 jours de livraison')
       else : 
           print('5 jours de livraison')


    
    case "normal" : 
        if quantity < 50 : 
            print('4 jours de livraison')
        elif 50 <= quantity < 100 :
            print('5 jours de livraison')
        else : 
            print('7 jours de livraison')
    

    

