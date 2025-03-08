faturamento = 1000
custo = 600
lucro = faturamento - custo

print ('O lucro foi de', lucro, ' e o faturamento foi de', faturamento)
texto = f'O lucro foi de R$ {lucro}  e o faturamento foi de R$ {faturamento}'
print (texto)

email = 'eMaIl_falso@gmail.com '



print(email.lower()) # letra minuscula
print(email.strip()) # retira espaços antes e depois do texto

email = email.lower() #colocar em letra minuscula
email = email.strip() # # retira espaços antes e depois do texto

print(email)
print ('o  email tem',len(email),'caracteres') #len tamanho no caso do email

#posição de alguma letra ou numero
posicao = email.find('@')
print (posicao)