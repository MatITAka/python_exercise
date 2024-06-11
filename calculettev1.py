numberTotal = []
messageUser= ""
dialogUser = ""

while dialogUser != "stop" : 

    dialogUser = str(input("Ecrivez 'stop' pour arrêter, sinon appuyez sur entrée: "))

    if dialogUser == "stop" : 
        print("Voici le résultat final",numberTotal)
        break 

    number1 = int(input("Choisissez votre nombre : "))

    while True : 

        if messageUser != " + " or " - " or " * " or " / " :
            messageUser = str(input("Choisissez un type d'opération (+  -  *  /) : "))
            print("L'opération choisie n'existe pas")
            if messageUser ==  " + " or messageUser == " - " or messageUser == " * " or messageUser == " / " :
                break
            


        number2 = int(input("Choisissez un autre nombre : "))


        match messageUser : 
            case " + " : 
                numberTotal.append(number1 + number2)
                print(numberTotal)

            case " - " : 
                numberTotal.append(number1 - number2)
                print(numberTotal)

            case " * " : 
                numberTotal.append(number1 * number2)
                print(numberTotal)
            
            case " / " : 
                numberTotal.append(number1 / number2)
                print(numberTotal)
            
            case _ :
                print("Erreur")
        

