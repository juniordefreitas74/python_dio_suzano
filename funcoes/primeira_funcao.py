#DEF REFERE A UMA FUNÇÃO ENTAO VC 
# PRECISA DECLARA UMA FUNCAO DAR O NOME E COLOCAR
# OU NÃO UM PARAMETRO DENTRO DOS PARENTESES

def mensagem():
    print('Olá mundo')
    #  NESTE CASO EU NÃO PASSO NADA 
    #  E QDO CHAMAR ELE VAI PRINTAR O QUE FOI PEDIDO
''
def mensagem2(nome):
    print(f'seja bem vindo {nome}')
    # AQUI EU DEFINI QUE A FUNÇAO PRECISA DE UM NOME
    # ENTÃO QDO EU CHAMAR ELA PRECISO INDICAR QUAL O 
    # NOME PARA ELA FUNCIONAR
    '''Olá mundo'''

def mensagem3(nome='anonimo'):
    print (f'bom dia {nome}')
    # AQUI EU DEFINI QUE A FUNCAO PRECISA DE UM NOMA 
    # MAS SE EU NÃO PASSAR NADA ELA VAI PREENCHER COMO ANONIMO
    '''seja bem vindo junior'''
 
#  APÓS DEFINIR A FUNÇÃO VC PRECISA
#  CHAMA-LA PARA PODER FUNCIONAR
'''bom dia anonimo''' #SE EU NAO PASSAR NADA
'''bom dia LARA''' # SE EU DEFINIR O NOME
    
mensagem()
mensagem2(nome = 'junior')
mensagem3()
mensagem3(nome='LARA')