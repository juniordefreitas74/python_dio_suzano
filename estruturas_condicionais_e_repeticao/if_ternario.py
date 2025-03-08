saldo = 500
saque= 2900
status = 'Sucesso' if saldo>= saque else 'falha'

print (f'{status} em realizar o saque! ')

# o if ternário é um if em uma linha só para testar condições simples