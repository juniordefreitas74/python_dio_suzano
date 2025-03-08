nome = 'Junior'
idade = 50
profissao = 'programador'
linguagem = 'python'
# estilo antigo % (%s para string %f para float %d para numeros inteiros)
print ('olá, meu nome é %s. Eu tenho %d anos, trabalho como %s e faço um curso de %s.'% (nome, idade,profissao, linguagem))

print('- - - - - - - - - - - - - - -  - - - ')

# f (format) chama a variavel dentro de chaves
print(f'Olá, me chamo {nome}, tenho {idade} anos, sou {profissao} e estou matrculado no curso de {linguagem}.')

print('- - - - - - - - - - - - - - -  - - - ')

pi = 3.14159

print(f'valor de pi : {pi: .2f}') # quebra o numero para 2 casas decimais

print(f'valor de pi : {pi: 10.3f}') # coloca 10 casas (espaços ) antes do ponto e tres casa decimais apos o ponto