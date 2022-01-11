vetTeste = { 1 : { 'nome' : 'pedro'}}

print (vetTeste)

vetTeste[2] = {'nome' : 'arthur'}

print (vetTeste)

vetTeste[2] = {**vetTeste[2],'idade': 12}

print(vetTeste)
print(type(vetTeste))
