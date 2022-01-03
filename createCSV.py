numberVerify= 1
arrayTitle= {}
cont = 1
contadorDeLinha = 0
contadorDePalavras = 0
dados = ""


import date
import csv

with open("arq.lst") as file:
    for line in file:
        if (contadorDeLinha == 0):
            for access in line.split():
                if (access == "ENTRADA"):
                    contadorDeLinha = 1
                    dados = line
                    #print(f'contador de linha: {contadorDeLinha}')       
        elif (contadorDeLinha == 1):
            for access in line.split():
                if (access == "----------------"):
                    contadorDeLinha = 2
                    print(f'contador de linha: {contadorDeLinha}')
                    break
            print(f'saiu')
        elif (contadorDeLinha > 1):
            for (indice ,access) in enumerate(line.split()):           
                verifyDate = date.checkDate(access)
                if ((verifyDate['data'] == False and indice > 5) or (verifyDate['data'] == False and indice == 0)):
                    break
                if (indice == 0):
                    dados = dados + line
                    print (f'{contadorDeLinha}: {line}')
            contadorDeLinha = contadorDeLinha + 1

print (dados)