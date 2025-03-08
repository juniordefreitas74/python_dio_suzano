curso = '  pYthOn jUnOr'

print(curso.upper()) # Transforma todo texto em maiusculo
print(curso.lower()) # Transforma todo texto em minusculo
print(curso.title()) # Transforma a primeira letra de cada palavra em maisculo

print(' - - - - - - - - - - - - - - - - - - - -')

print(curso.strip()) # remove os espaços em branco do inicio e do fim da palavra ou frase
print(curso.lstrip()) #remove os espaços em branco do inicio da palavra
print(curso.rstrip()) # remove os espaços em branco do fim da palavra

print(' - - - - - - - - - - - - - - - - - - - -')
curso = 'Junior'

print(curso.center(10, '@')) # centraliza o texto dentro da area que vc definiu no caso 10 e se quiser colocar algo ao lado seria a segunda opção
print('-'.join(curso)) #separa letra por letra com o caracter que vc pedir

print(' - - - - - - - - - - - - - - - - - - - -')