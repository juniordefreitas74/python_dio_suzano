
menu = f'''
   ======= SISTEMA BANCÁRIO ======
   =                             =
   =        [d] Depositar        =
   =        [s] Sacar            =
   =        [e] Extrato          =
   =        [q] Sair             =
   =                             =
   ===============================
      DIGITE A OPÇÃO DESEJADA!
'''


saldo = 0
limite = 500
extrato = []
saques_info = []
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(f'{menu}\n> ')

    if opcao == 'd':
        deposito = float(input('\nDgite o valor de Depósito:'))
        if deposito > 0:
            saldo += deposito

            extrato.append(deposito)
            print(f'\nFoi depositado: R$ {deposito:.2f}')

        else:
            print("\nValor inválido para depósito.")

    elif opcao == 's':
        if numero_saques < LIMITE_SAQUES:

            total_extrato1 = sum(extrato)

            saque = float(input('Digite o valor que deseja sacar: '))
            if saque <= total_extrato1 and saque <= 500 and saque > 0:

                if sum(saques_info) + saque > total_extrato1:

                    sacado = total_extrato1 - total_saques1
                    print('\nSaldo insuficiente, tente outro valor!')
                    print(f'Seu saldo atual é de: R${sacado:.2f}')

                else:
                    saques_info.append(saque)
                    total_saques1 = sum(saques_info)
                    sacado2 = total_extrato1 - total_saques1
                    print(f'\nSaque de: R${saque:.2f} efetuado com sucesso.\n')
                    print(f'Seu saldo atual é de: R${sacado2:.2f}')
                    numero_saques += 1

            else:
                total_saques2 = sum(saques_info)
                sacado3 = total_extrato1 - total_saques2
                print(
                    '\nValor inválido para saque. O saque deve ser de até R$500,00 e dentro do saldo disponível.')
                print(f'Seu saldo atual é de: R${sacado3:.2f}')

        else:
            print('Numero de saques diários excedido, tente novamente amanhã!')

    elif opcao == 'e':
        print("\n====== EXTRATO ======")

        extrato_formatado = ''.join(
            [f"Depósito de R$ {valor:.2f}\n" for valor in extrato])
        extrato_formatado2 = ''.join(
            [f"Saque de R$ {valor:.2f}\n" for valor in saques_info])
        print(extrato_formatado)
        print(extrato_formatado2)
        total_extrato2 = sum(extrato)-sum(saques_info)
        print(f'Saldo total de: R${total_extrato2:.2f}')

        if total_extrato2 < 0:
            print('Não houve movimentações.')

        print("======================")

    elif opcao == 'q':
        break

    else:
        print('Operação inválida, por favor selecione novamente a opção desejada')
