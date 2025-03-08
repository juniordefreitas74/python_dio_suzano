# recebe um numero de teclado e exibe os 2 numeros seguintes
# forma simples para poucas vezes
# a = int(input('Informe um numero inteiro: '))
# print(a)

# a += 1
# print(a)

# a += 1
# print(a)
texto = input('informe um texto:')
vogais ='AEIOU'
for letra in texto:
    if letra.upper() in vogais:
        print(letra, end='')
else:
    print()
    print('oi') # adiciona um quebrawsw