def menu():
    opcoes = '''\n
    ==================== MENU ====================
    
    \t[d]  Depositar
    \t[s]  Sacar
    \t[e]  Extrato
    \t[nc] Nova Conta
    \t[lc] Listar Contas
    \t[nu] Novo Usuário
    \t[q]  Sair
    
    ==>'''
    return input(opcoes).strip().lower()


# essa barra sindica que os parâmetros antes dela só podem ser passados por posição
def depositar(saldo, valor, extrato, /):
    if valor > 0:  # se o valor ffor maior que 0
        saldo += valor  # adiciona esse valor em saldo
        # adiciona em extrato a fstring
        extrato += f'Depósito: R$ {valor:.2f}\n'
        print('\n ====Depósito realizado com sucesso! ====')  # printa msg
    else:
        print('\n@@@ Operação Falhou! O valor informado é Inválido. @@@')
    return saldo, extrato


def sacar (*,saldo, valor, extrato, limite,, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saque = numero_saques >= limite_saques
    if excedeu_saldo:
        print('\n@@@@ Operação falhou! Você não tem saldo suficiente. @@@@')









opcao = menu()  # Chama a função e armazena a opção escolhida
print(f"Você escolheu a opção: {opcao}")
