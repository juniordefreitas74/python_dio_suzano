def calculo(podeSerQualquerNome):
    return sum(podeSerQualquerNome)

print (calculo([10, 20, 30, 40]))

def minhacabeca(teste):
    soma =[ x + 1 for x in teste]
    return sum(soma)
print(minhacabeca([10,20,30,40]))

'''
defini a função minhacabeca que recebe o parametro teste
defini uma variavel soma onde fiz um laço de repetição for
chamado de x onde x é cada elemento de teste e ele vai pegar
e somar 1 a cada elemento definido no print
pedi para a funcao retornar a soma

'''


def meujeito(aquario):
    somar = aquario +5
    subtrair = aquario -5
    return somar,subtrair
print(meujeito(220))

'''defini a função meu jeito
que recebe o parametro aquario
dentro da função coloquei duas variaveis
uma chamada somar pega o valor de aquario e soma 5
outra camada subtrair pega o valor de aquaria e subtrai 5 
pedi para printar a função meu jeito passando o parametro de aquario com 220'''