# fazer repetição usando o comando for

texto = input('Informe o nome:')
vogais = 'AEIOU'

for teste in texto:
    if teste.upper() in vogais:
        print(teste, end='')
print()