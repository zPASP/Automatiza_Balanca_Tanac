'''
PEDRO ALEXANDRE SILVA TEIXEIRA PINTO
23/12/2021
ESTAGIARIO DE INFRAESTRUTURA - TANAC S/A
ANÁLISE E DESENVOLVIMENTO DE SISTEMAS - IFRS
RIO GRANDE - RS
'''

"""
CATALAGO DE ERROS:
INICIO 2 - Referente ao ERRO de placa
0001 - ERRO NO FORMATO DA PLACA.
"""
from os import error


def checkTransitBoard (board):
    '''
    Essa função checa a placa e verifica se o parametro recebido é uma placa valida ou não.
      Args:
        Recebe uma String no formato de placa e valida a mesma.
      Returns:
        Retorna um dicionario com as informações de erro ou com parametros da placa já verificada e o modelo da placa.
    '''
    counterLetter=0 
    counterNumber=0
    try:
        'Tratamento de erro para a placa'
        if len(board) == 7:
            'Condicional para a quantidade de caracteres informado na placa recebida'
            for (indice, value) in enumerate(board):
                "laço de repedição com valor e indice do caracter para validar dado-a-dado da placa."
                if ( value.isalpha() and (indice == 0 or indice == 1 or indice == 2 or indice == 4)):
                    counterLetter = counterLetter + 1
                elif ( value.isdigit() and (indice == 3 or indice == 4 or indice == 5 or indice == 6)):
                    counterNumber = counterNumber + 1
                else: 
                    break
            if (counterLetter == 4 and counterNumber == 3):
                'Com base no contador, informa o padrão da placa como mercosul'
                #print ("Padrão Mercosul")
                verifyBoard = {
                    "Model" : "Mercosul",
                    "data" : board
                    }
            elif (counterLetter == 3 and counterNumber == 4):
                'Com base no contador, informa o padrão da placa como brasil'
                #print ("Padrão Brasil")
                verifyBoard = {
                    "Model" : "Brasil - Antigo",
                    "data" : board
                    }
            return verifyBoard
        else:
            raise ValueError('ERRO DADOS INVALIDOS')
    except:
        'Exeção para possivel erro no formato ou dados da placa.'
        verifyBoard = {
          "Error" : "20001",
          "data" : False
          }
        return verifyBoard