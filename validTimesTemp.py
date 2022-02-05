'''
PEDRO ALEXANDRE SILVA TEIXEIRA PINTO
23/12/2021
DESENVOLVEDOR E ANALISTA DE DADOS - ITAÚ S/A
ESTAGIARIO DE INFRAESTRUTURA - TANAC S/A
ANÁLISE E DESENVOLVIMENTO DE SISTEMAS - IFRS
RIO GRANDE - RS
'''

from datetime import datetime

'''
CATALAGO DE ERROS:
INICIO 1 - Referente ao ERRO de TIMESTEMP
0001 - ERRO NO FORMATO DA DATA.
0002 - ERRO NO FORMATO DA HORA.
'''


def checkDate(data):
    '''
    Essa função checa a data e verifica se o parametro recebido é uma data valida ou não.
      Args:
        Recebe uma String no formato de data e valida a mesma.
      Returns:
        Retorna um dicionario com as informações de erro ou com um "Data" com o valor verificado.
    '''
    try:
        "Tratamento de erro no formato da data"
        dataVerify = datetime.strptime(data, '%d/%m/%Y').date()
        return {"data": dataVerify}
    except ValueError as err:
        "Exeção para possivel erro no formato ou data informado no atributo"
        dataVerify = {
            "Error": "10001",
            "data": False
        }
        return dataVerify


def checkHour(data):
    '''
    Essa função checa o parametro recebido e retorna um dicionario contendo um erro ou o dado verificado.
      Args:
        Recebe uma String no formato de hroa e valida a mesma.
      Returns:
        Retorna um dicionario com as informações de erro ou com um "Data" com o valor verificado.
    '''
    try:
        "Tratamento de possiveis erros no formato da data."
        if (len(data) != 5):
          'Verifica se a esta no tamanho esperado, se não força o erro'
          None

        if (len(data) == 5):
            for (indice, time) in enumerate(data):
                'Laço de repetição para validar a hora informada'

                if (indice == 0):
                    if (type(int(time))):
                        if(int(time) > -1 and int(time) <= 2):
                            pass
                        else:
                            break

                if (indice == 1):
                    if (time.isdigit()):
                        if(int(time) > -1 and int(data[0]) < 2):
                            pass
                        elif (int(time) <= 3 and int(data[0]) == 2):
                            pass
                        else:
                            break

                if (indice == 2):
                    if (time == ":"):
                        pass
                    else:
                        break

                if (indice == 3):
                    if (time.isdigit()):
                        if(int(time) > -1 and int(time) < 6):
                            pass
                        else:
                            break

                if (indice == 4):
                    if (time.isdigit()):
                        if(int(time) > -1):
                            hourVerify = {"data": data}

        return hourVerify
    except:
        "Exeção para possivel erro no formato ou hora informado no atributo"
        hourVerify = {
            "Error": "10002",
            "data": False
        }
        return hourVerify