from datetime import datetime

"""
CATALAGO DE ERROS:
INICIO 1 - Referente ao ERRO de data
0001 - ERRO NO FORMATO DA DATA.
0002 - ERRO NO FORMATO DA HORA.
"""

def checkDate (data):
    try:
        dataVerify = datetime.strptime(data, '%d/%m/%Y').date()
        return {"data" : dataVerify}
    except ValueError as err:
        #print (f'Error: 10001')
        dataVerify = {
          "Error" : "10001",
          "data" : False
          }
        return dataVerify

def checkHour (data):
    try:
        if (len(data) != 5):
            None
        
        if (len(data) == 5):
          for (indice, time) in enumerate(data):
            
            if (indice == 0):
              if (type(int(time))):
                  if(int(time) > -1 and int(time) <= 2):
                      pass
                  else:
                      break
            
            if (indice == 1):
              if (type(int(time))):
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
              if (type(int(time))):
                  if(int(time) > -1 and int(time) < 6):
                      pass
                  else:
                      break

            if (indice == 4):
              if (type(int(time))):
                  if(int(time) > -1):
                      hourVerify = { "data" : data }
                      
        return hourVerify
    except:
        hourVerify = {
          "Error" : "10002",
          "data" : False
          }
        return hourVerify

print (checkHour("23:59"))      




def formatDate (data):
    data = checkDate(data)
    print (data["data"])
    
#print (formatDate("30/11/2018"))




"""
str_date = '11/07/2018'
date = datetime.strptime(str_date, '%d/%m/%Y').date()
print(date, type(date))
str_date = '2018-20-11'
try:
    date = datetime.strptime(str_date, '%Y-%m-%d').date()
except ValueError as err:
    print(f'ValueError : {err} ')
    pass
finally:
    print ("FINALIZADO")


try:
  print(date, type(date))
except NameError:
  print("Variable x is not defined")
except ValueError as err:
  print(f'ValueError {err} ')
  pass
except:
  print("ERRO GLOBAL")
finally:
    print("FINALIZADO")
"""

    
