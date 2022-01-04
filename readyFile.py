numberVerify= 1
arrayTitle= {}
cont = 1
contadorDeLinha = 0
contadorDePalavras = 0
import validTimesTemp
import validTransitBoard
with open("arq.lst") as file:
    for line in file:
        if (contadorDeLinha == 0):
            for access in line.split():
                if (access == "ENTRADA"):
                    contadorDeLinha = 1
                    print(f'contador de linha: {contadorDeLinha}')
        elif (contadorDeLinha == 1):
            for access in line.split():
                if (access == "----------------"):
                    contadorDeLinha = 2
                    print(f'contador de linha: {contadorDeLinha}')
                    break
            print(f'saiu')
        elif (contadorDeLinha > 1):
            for (indice ,access) in enumerate(line.split()):
                verifyDate = validTimesTemp.checkDate(access)
                if ((verifyDate['data'] == False and indice > 5) or (verifyDate['data'] == False and indice == 0)):
                    break

                if (indice == 0):
                    print(f'D_E: {access}')
                if (indice == 1):
                    print(f'H_E: {access}')
                if (indice == 2):
                    print ((validTransitBoard.checkTransitBoard(access))['data'])
                    if ((validTimesTemp.checkDate(access))['data'] != False):
                        print(f'D_S: {access}')
                    elif ((validTransitBoard.checkTransitBoard(access))['data'] != False):
                        print(f'PLACA: {access}')
                        break
                    else:
                        break        
                if (indice == 3):
                    print(f'H_S: {access}')
                if (indice == 5):
                    print(f'PLACA: {access}')



            contadorDeLinha = contadorDeLinha + 1






"""             if (access == "ENTRADA"):
                #print (f'VERIFICANDO: {numberVerify}')
                for lineAccess in line.split():
                    if (lineAccess == "M."):
                        #print (f'final da linha {lineAccess}')
                        break
                    else:
                        #print (f'{lineAccess}')
                        a = 'a'
                numberVerify= numberVerify+1  """


# ENTRADA: "12/12/2021"
# HORA: "21:40"
# SAIDA: "13/12/21"
# SAIDA: "00:16"
# PLACA: "JAW9A42"


def receiveData (data):
    print ("")




