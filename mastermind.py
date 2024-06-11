import random

code = []

while len(code) <4 :
    code.append(random.choice(["J","B","V","R","N","O"]))

essaies = 8
essai = 1
gameOver = False


userCode = []
userCode_s = ""


while not gameOver :
    print("Essais : ", essai , "/8")
    userCode_s = str(input("Saisissez une combinaison de couleur avec un espace entre chaque: ")).strip()
    userCode = userCode_s .split(' ')

    if len(code) != 4 :
        print("Veuillez saisir exactement 4 couleurs")
        continue

    colorInPlace = 0
    colorInCode = 0

    for i in range(4) :
        if userCode[i] == code[i] : 
            colorInPlace +=1

    tempCode = code.copy()
    for i in range(4) :
        if userCode[i] in tempCode :
            colorInCode += 1 
            tempCode.remove(userCode[i])
    
    colorInCode += colorInPlace

    essai += 1 

    print(colorInPlace, "pions de couleur à la bonne place")
    print(colorInCode,"pions de couleur présent dans le code")

    if colorInPlace == 4 :
        gameOver = True 
        print("Vous avez gagné")
        
    
    
    if essai > essaies : 
        gameOver = True 
        print('Vous avez perdu, le code était' , code)
