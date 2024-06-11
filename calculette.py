numberTotal = int()
dialogUser = ""
number1 = int()
while dialogUser != "stop":
    dialogUser = input("Ecrivez 'stop' pour arrêter, sinon appuyez sur entrée: ").strip()
    if dialogUser == "stop":
        print("Voici le résultat final : ", numberTotal)
        break

    if number1 is not int() : 
            print("Il ne s'agit pas d'un chiffre")
    else : 
        if not numberTotal :
            number1 = int(input("Choisissez votre nombre : "))
        else :
            print("Vous avez déjà un nombre enregistré") 

    while True:
        messageUser = input("Choisissez un type d'opération (+ - * /) : ").strip()
        if messageUser in ("+", "-", "*", "/"):
            break
        else:
            print("L'opération choisie n'existe pas")
    number2 = int(input("Choisissez un autre nombre : "))
    match messageUser:
        case "+":
            if not numberTotal :
                numberTotal = (number1 + number2)
            else : 
                numberTotal = (numberTotal+ number2)
        case "-":
            if not numberTotal :
                numberTotal = (number1 - number2)
            else : 
                numberTotal = (numberTotal- number2)
        case "*":
            if not numberTotal :
                numberTotal = (number1 * number2)
            else : 
                numberTotal = (numberTotal* number2)
        case "/":
            if not numberTotal  : 
                 if number1 == 0  or number2 == 0 :
                    print('On ne peux pas diviser par 0')
                 else :
                    numberTotal = (number1 / number2)
            else : 
                numberTotal = (numberTotal / number2)
        case _:
            print("Erreur")
    print(numberTotal)

