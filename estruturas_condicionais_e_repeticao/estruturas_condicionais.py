saldo = 2000
saque = float(input('Informe o valor do saque: '))

if saldo >= saque:
    print('Saque realizado!')
if saldo < saque:
    print('Saldo Insulficiente')
    
if saldo >= saque:
    print('Saque realizado!')
else:
    print('não dá pra sacar esse valor')
    
    
opcao = int(input('Informe uma opção: [1] Sacar \n [2] Extrato: '))
if opcao == 1:
    valor = float(input('Informe a quantia para saque:'))
    #..
elif opcao == 2:
    print('exibindo extrato...')
else:
    