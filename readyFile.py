'''
PEDRO ALEXANDRE SILVA TEIXEIRA PINTO
23/12/2021
DESENVOLVEDOR E ANALISTA DE DADOS - ITAÚ S/A
ESTAGIARIO DE INFRAESTRUTURA - TANAC S/A
ANÁLISE E DESENVOLVIMENTO DE SISTEMAS - IFRS
RIO GRANDE - RS
'''

import validTransitBoard
import validTimesTemp

countLine = 0
countDataOfThuck = 1
allInformationOfTruck = {}
# allInformationOfTruck = {
#     0: 
#         {
#         "data_entrada": "01/12/2021",
#         "hora_entrada": "21:40",
#         "data_saida": "01/12/2021",
#         "hora_saida": "23:00",
#         "placa": "AAA1B222"
#         }
       
# }


def readyTruckInfo():
    '''
    Função responsavel por fazer a leitura do arquivo importado no formato 'LST' e criar um json com todas as informações necessarias do projeto.
    Chamando ela é possivel fazer o relatorio completo:
    Data: Entrada e saida caso consta.
    Hora: entrada e saida caso consta.
    Placa: placa do caminhão. 
    '''
    # try:
    with open("arq.lst") as file:
        'Abre o arquivo com o nome indicado e valida se o mesmo é existente ele dentro do programa.'
        global countLine
        for line in file:
            'percorre linha a linha do arquivo'
            if (countLine == 0):
                for access in line.split():
                    'Quebra toda a linha em palavras e verifica se tem a uma palavra esperada.'
                    if (access == "ENTRADA"):
                        countLine = 1
                        print(f'contador de linha: {countLine}')

            elif (countLine == 1):
                for access in line.split():
                    'Outro verificador para segunda linha esperada'
                    if (access == "----------------"):
                        countLine = 2
                        print(f'contador de linha: {countLine}')
                        break
                print(f'saiu')
            elif (countLine > 1):
                for (indice, access) in enumerate(line.split()):
                    'Linha esperada contendo informações do caminhão'
                    verifyDate = validTimesTemp.checkDate(access)
                    if ((verifyDate['data'] == False and indice > 5) or (verifyDate['data'] == False and indice == 0)):
                        "Força o erro caso a primeira palavra não seja uma data."
                        break

                    if (indice == 0):
                        'Valor data de entrada'
                        criarDicionario({'info': 'd_e', 'data': access})
                        print(f'D_E: {access}')
                    if (indice == 1):
                        'valor hora de entrada'
                        criarDicionario({'info': 'h_e', 'data': access})
                        print(f'H_E: {access}')
                    if (indice == 2):
                        'valor sendo possivel ser hora de entrada caso em branco validar placa'
                        print (access)
                        #print((validTransitBoard.checkTransitBoard(access))['data'])
                        if ((validTimesTemp.checkDate(access))['data'] != False):
                            criarDicionario({'info': 'd_s', 'data': access})
                            print(f'D_S: {access}')
                        elif ((validTransitBoard.checkTransitBoard(access))['data'] != False):
                            criarDicionario({'info': 'd_s', 'data': ""})
                            criarDicionario({'info': 'h_s', 'data': ""})
                            criarDicionario({'info': 'placa', 'data': access})
                            print(f'PLACA: {line.split()[indice+1]}')
                            break
                        elif (((validTransitBoard.checkTransitBoard(access))['data'] == False)):
                            criarDicionario({'info': 'h_s', 'data': ""})
                            criarDicionario({'info': 'd_s', 'data': ""})
                            criarDicionario({'info': 'placa', 'data': line.split()[indice+1]})
                            print(f'PLACA: {line.split()[indice+1]}')
                            break                            
                        else:
                            break
                    if (indice == 3):
                        'valor hora de saida'
                        {'info': 'h_s', 'data': access}
                        print(f'H_S: {access}')
                    if (indice == 5):
                        'valor placa caminhão caso tenha entrada e saida registrada'
                        criarDicionario({'info': 'placa', 'data': access})
                        print(f'PLACA: {access}')

                countLine = countLine + 1
                pass
    # except:
    #     print("arquivo não encontrado")

def criarDicionario (data):
    print ('entrou')
    if (data['info'] == 'd_e'):
        allInformationOfTruck[countDataOfThuck] = {'data_entrada': data['data']}
    if (data['info'] == 'h_e'):
        allInformationOfTruck[countDataOfThuck] = {**allInformationOfTruck[countDataOfThuck], 'hora_entrada' : data['data']}
    if (data['info'] == 'd_s'):
        allInformationOfTruck[countDataOfThuck] = {**allInformationOfTruck[countDataOfThuck], 'data_saida' : data['data']}
    if (data['info'] == 'h_s'):
        allInformationOfTruck[countDataOfThuck] = {**allInformationOfTruck[countDataOfThuck], 'hora_saida' : data['data']}
    if (data['info'] == 'placa'):
        allInformationOfTruck[countDataOfThuck] = {**allInformationOfTruck[countDataOfThuck], 'placa' : data['data']}
        sumDataOfTruck()

def sumDataOfTruck ():
    """
    Função responsavel por somar um ao contador de cada linha salva.
    Essa função deve ser chamada apenas enviar a placa ao dicionario
    """
    global countDataOfThuck
    countDataOfThuck += 1



readyTruckInfo()
print (allInformationOfTruck)



dataEntrada = {'info': 'd_e', 'data': '01/01/1111'}
horaEntrada = {'info': 'h_e', 'data': '01:01'}
horaSaida = {'info': 'd_s', 'data': '02/02/2222'}
dataSaida = {'info': 'h_s', 'data': '02:02'}
placa = {'info': 'placa', 'data': 'ZZZ0A999'}

# criarDicionario(dataEntrada)
# criarDicionario(horaEntrada)
# criarDicionario(dataSaida)
# criarDicionario(horaSaida)
# criarDicionario(placa)
# criarDicionario(dataEntrada)
# criarDicionario(horaEntrada)
# criarDicionario(dataSaida)
# criarDicionario(horaSaida)
# criarDicionario(placa)

# print (countDataOfThuck)
# print (allInformationOfTruck)

"""
{
        "data_entrada": "01/12/2021",
        "hora_entrada": "21:40",
        "data_saida": "01/12/2021",
        "hora_saida": "23:00",
        "placa": "AAA1B222"
    }
"""

# ENTRADA: "12/12/2021"
# HORA: "21:40"
# SAIDA: "13/12/21"
# SAIDA: "00:16"
# PLACA: "JAW9A42"
