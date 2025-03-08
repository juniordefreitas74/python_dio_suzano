# Criando um menu para exibir as opções disponíveis para o usuário
menu = f'''
    ***** SISTEMA BANCÁRIO ******
    *                           *
    *       [d] Depositar       *
    *       [s] Sacar           *
    *       [e] Extrato         *
    *       [q] Sair            *
    *                           *
    *****************************
      DIGITE A OPÇÃO DESEJADA!
'''

# Definição das variáveis iniciais do sistema bancário
saldo = 0  # Saldo inicial da conta
limite = 500  # Limite máximo permitido por saque
extrato = []  # Lista que armazenará os depósitos realizados
saques_info = []  # Lista que armazenará os saques realizados
numero_saques = 0  # Contador do número de saques diários efetuados
LIMITE_SAQUES = 3  # Constante que define o limite de saques por dia

# Loop infinito para manter o programa rodando até que o usuário escolha sair
while True:  
    opcao = input(f'{menu}\n> ')  # Exibe o menu e solicita a opção do usuário

    if opcao == 'd':  # Verifica se a opção escolhida é 'd' (Depósito)
        deposito = float(input('\nDigite o valor de Depósito: '))  # Solicita o valor do depósito

        if deposito > 0:  # Verifica se o valor do depósito é positivo
            saldo += deposito  # Atualiza o saldo, somando o valor depositado
            extrato.append(deposito)  # Registra o depósito na lista de extrato
            print(f'\nFoi depositado: R$ {deposito:.2f}')  # Confirmação do depósito
            
        else:
            print("\nValor inválido para depósito.")  # Mensagem de erro para depósitos inválidos

    elif opcao == 's':  # Verifica se a opção escolhida é 's' (Saque)
        if numero_saques < LIMITE_SAQUES:  # Verifica se o limite diário de saques não foi atingido
            total_extrato1 = sum(extrato)  # Calcula o saldo total considerando os depósitos

            saque = float(input('Digite o valor que deseja sacar: '))  # Solicita o valor do saque

            # Verifica se o saque está dentro do saldo disponível e do limite de R$500 por saque
            if saque <= total_extrato1 and saque <= 500:
                # Verifica se o saque não ultrapassa o saldo disponível
                if sum(saques_info) + saque > total_extrato1:
                    sacado = total_extrato1 - total_saques1  # Erro: total_saques1 não foi definido antes
                    print('\nSaldo insuficiente, tente outro valor!')
                    print(f'Seu saldo atual é de: R${sacado:.2f}')

                else:
                    saques_info.append(saque)  # Registra o saque na lista de saques
                    total_saques1 = sum(saques_info)  # Atualiza o total de saques realizados
                    sacado2 = total_extrato1 - total_saques1  # Atualiza o saldo após o saque
                    print(f'\nSaque de: R${saque:.2f} efetuado com sucesso.\n')
                    print(f'Seu saldo atual é de: R${sacado2:.2f}')
                    numero_saques += 1  # Incrementa o contador de saques efetuados

            else:
                total_saques2 = sum(saques_info)  # Soma total dos saques realizados
                sacado3 = total_extrato1 - total_saques2  # Atualiza saldo após os saques
                print('\nValor inválido para saque. O saque deve ser de até R$500 e dentro do saldo disponível.')
                print(f'Seu saldo atual é de: R${sacado3:.2f}')
                
        else:
            print('Número de saques diários excedido, tente novamente amanhã!')  # Mensagem ao ultrapassar limite de saques

    elif opcao == 'e':  # Verifica se a opção escolhida é 'e' (Extrato)
        print("\n====== EXTRATO ======")  # Exibe o cabeçalho do extrato

        # Formata a exibição dos depósitos registrados no extrato
        extrato_formatado = ''.join([f"Depósito de R$ {valor:.2f}\n" for valor in extrato])
        # Formata a exibição dos saques registrados no extrato
        extrato_formatado2 = ''.join([f"Saque de R$ {valor:.2f}\n" for valor in saques_info])

        print(extrato_formatado)  # Exibe os depósitos
        print(extrato_formatado2)  # Exibe os saques

        total_extrato2 = sum(extrato) - sum(saques_info)  # Calcula o saldo final
        print(f'Saldo total de: R${total_extrato2:.2f}')  # Exibe o saldo atualizado

        # Se o saldo for zero ou negativo, exibe uma mensagem de ausência de movimentações
        if total_extrato2 <= 0:
            print('Não houve movimentações.')

        print("======================")  # Rodapé do extrato

    elif opcao == 'q':  # Verifica se a opção escolhida é 'q' (Sair)
        break  # Encerra o loop e finaliza o programa

    else:
        print('Operação inválida, por favor selecione novamente a opção desejada')  # Mensagem para opções inválidas
