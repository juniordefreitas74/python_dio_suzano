maior_idade = 18
idade_treinee = 16

idade = int(input('Informe sua idade: '))

if idade >= maior_idade:
    print ('maior de idade, pode tirar CNH')
    
if idade < maior_idade:
    print ('Ainda não pode tirar CNH')
    
    
if idade >= maior_idade:
    print ('maior de idade, pode tirar CNH')
else:
    print ('Ainda não pode tirar CNH de novo')
    
if idade >= maior_idade:
    print ('maior de idade, pode tirar CNH')
elif idade>= idade_treinee and idade < maior_idade:
    print(" liberado para aulas teóricas")   

else:
    print ('Ainda não pode tirar CNH de novo3')