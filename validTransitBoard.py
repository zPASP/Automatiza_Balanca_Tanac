
def checkTransitBoard (board):
    counterLetter=0 
    counterNumber=0
    try:
        if len(board) == 7:
            for (indice, value) in enumerate(board):
                if ( value.isalpha() and (indice == 0 or indice == 1 or indice == 2 or indice == 4)):
                    counterLetter = counterLetter + 1
                elif ( value.isdigit() and (indice == 3 or indice == 4 or indice == 5 or indice == 6)):
                    counterNumber = counterNumber + 1
                else: 
                    break
            if (counterLetter == 4 and counterNumber == 3):
                print ("Padrão Mercosul")
                verifyBoard = {
                    "Model" : "Mercosul",
                    "data" : board
                    }
            elif (counterLetter == 3 and counterNumber == 4):
                print ("Padrão Brasil")
                verifyBoard = {
                    "Model" : "Brasil - Antigo",
                    "data" : board
                    }
            return verifyBoard
    except:
        verifyBoard = {
          "Error" : "20001",
          "data" : False
          }
        return verifyBoard


