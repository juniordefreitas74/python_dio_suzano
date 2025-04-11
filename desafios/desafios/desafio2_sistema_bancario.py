def menu():
    menu_texto = """
\033[1;34m==================================\033[0m
\033[1;32m|          💰 MENU 💰           |\033[0m
\033[1;34m==================================\033[0m
\033[1;36m| [d] Depositar                  |\033[0m
\033[1;36m| [s] Sacar                      |\033[0m
\033[1;36m| [e] Extrato                    |\033[0m
\033[1;36m| [u] Novo usuário               |\033[0m
\033[1;36m| [c] Nova conta                 |\033[0m
\033[1;36m| [l] Listar contas              |\033[0m
\033[1;31m| [q] Sair                       |\033[0m
\033[1;34m==================================\033[0m
"""
    return input(menu_texto)


# a barra indica que tudo antes dela deve ser posicional
def depositar(saldo, valor, extrato, /):

    if valor > 0:  # se o valor for maior que 0
        saldo += valor  # adicione o valor ao saldo
        # adicione a operação ao extrtato
        extrato += f"\n(+) Depósito de: R${valor:.2f}"
        print(f"Depósito de: R$ {valor:.2f} realizado com sucesso!")
    else:
        print("\n❌❌❌❌  Valor inválido para depósito. ❌❌❌❌")
    return saldo, extrato


# o * indica que os argumentos são passados por chave=valor
def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):

    if numero_saques < limite_saques:

        # se o valor for maior que 0 e menor ou igual ao saldo
        if valor > 0 and valor <= saldo and valor < limite:
            saldo -= valor  # diminua o valor do saldo
            # adicione a operação ao extrtato
            extrato += f"\n(-) Saque de: R$-{valor:.2f}"

            print(f"Saque de: R${valor:.2f} feito com sucesso")
        else:
            # se o valor for maior que o limite,maior que o saldo emenor que 0
            print("\n❌❌❌❌  Valor inválido ou saldo insuficiente. ❌❌❌❌")

    else:
        # se o numero de saques for maior que o limite de saques
        print("Número de saques diários excedidos, volte amanhã!")
    return (saldo, extrato)


def cadastro_usuario(usuarios):  # Função para cadastrar um novo usuário na lista
    # Solicita o CPF do usuário
    cpf = input("Digite o CPF: (somente números): ")

    # Verifica se o CPF já existe na lista de usuários
    usuario = filtro_usuario(cpf, usuarios)
    if usuario:  # Se já existir um usuário com esse CPF
        # Exibe mensagem de erro
        print("\n❌❌❌❌  Usuário já cadastrado no banco de dados! ❌❌❌❌")
        return  # Encerra a função sem cadastrar um novo usuário

    else:  # Se o CPF não estiver cadastrado, continua o processo de cadastro
        # Solicita o nome completo do usuário
        nome = input("Digite o nome completo: ")
        # Solicita a data de nascimento
        data_nasc = input("Digite data de nascimento (dd-mm-aaaa): ")
        # Solicita o endereço
        endereco = input("Digite endereço (rua, número - bairro - cidade - ESTADO): ")

        # Adiciona o usuário à lista, armazenando suas informações em um dicionário
        usuarios.append(
            {
                "nome": nome,
                "cpf": cpf,
                "Data Nascimento": data_nasc,
                "Endereço": endereco,
            }
        )

        print("✅  Usuário cadastrado com sucesso! ✅")  # Mensagem de sucesso


def filtro_usuario(cpf, usuarios):  # Função para buscar um usuário na lista pelo CPF
    for usuario in usuarios:  # Percorre a lista de usuários
        if usuario["cpf"] == cpf:  # Se encontrar um usuário com o CPF informado
            return usuario  # Retorna o usuário encontrado


def nova_conta(numero_conta, usuarios):
    # Define a agência padrão
    AGENCIA = "0001"

    # Solicita o CPF do usuário
    cpf = input("Digite o CPF (somente números): ")

    # Verifica se o CPF já existe na lista de usuários
    usuario = filtro_usuario(cpf, usuarios)

    numero = numero_conta

    if usuario:

        print(f"Conta cadastrada com sucesso: Agência: {AGENCIA} Conta nº: {numero}")

        nova_conta = {
            "nome": usuario["nome"],
            # Assumindo que "usuario" tem um dicionário com "nome"
            "cpf": cpf,
            "Data Nascimento": usuario.get("Data Nascimento"),
            # Ajuste conforme a estrutura do usuário
            "Endereço": usuario["Endereço"],  # Ajuste conforme necessário
            "Agência": AGENCIA,
            "Conta": numero,
        }

        print(nova_conta)

        return nova_conta
    else:
        print("\n❌❌❌❌  Usuário não encontrado! ❌❌❌❌")
    return None


def exibir_extrato(saldo, /, *, extrato):
    print("\n🟰🟰🟰🟰🟰🟰🟰🟰🟰🟰  EXTRATO 🟰🟰🟰🟰🟰🟰🟰🟰🟰🟰")

    print(extrato)

    print(f"\n🟰🟰🟰🟰  seu saldo atual é de: R$ {saldo:.2f} 🟰🟰🟰🟰")

    print("======================")
    return (saldo, extrato)


def mestre():
    LIMITE_SAQUES = 3
    numero_conta = 1000
    saldo = 0
    limite = 500
    extrato = ""
    usuarios = []  # Lista vazia para armazenar os usuários
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()
        if opcao == "d":
            cpf = input("Digite o CPF do titular da conta: (somente números): ")
            # Verifica se o CPF já existe na lista de usuários
            titular = filtro_usuario(cpf, usuarios)
            if titular:
                valor = float(input("\nDgite o valor do Depósito: R$ "))
                saldo, extrato = depositar(saldo, valor, extrato)
                print(f"\n🟰🟰🟰🟰  seu saldo atual é de: R$ {saldo:.2f} 🟰🟰🟰🟰")
            else:
                print("❌❌❌❌ Conta não encontrada, digite um CPF válido! ❌❌❌❌")

        elif opcao == "s":
            cpf = input("Digite o CPF do titular da conta: (somente números): ")
            # Verifica se o CPF já existe na lista de usuários
            titular = filtro_usuario(cpf, usuarios)
            if titular:
                valor = float(input("\nDgite o valor do Saque: R$ "))
                saldo, extrato = sacar(
                    saldo=saldo,
                    valor=valor,
                    extrato=extrato,
                    limite=limite,
                    numero_saques=numero_saques,
                    limite_saques=LIMITE_SAQUES,
                )
                print(f"\n🟰🟰🟰🟰  seu saldo atual é de: R$ {saldo:.2f} 🟰🟰🟰🟰")
                numero_saques += 1
            else:
                print("❌❌❌❌ Conta não encontrada, digite um CPF válido! ❌❌❌❌")

        elif opcao == "e":
            saldo, extrato = exibir_extrato(
                saldo,
                extrato=extrato,
            )
        elif opcao == "l":

            if contas:
                for ueu in contas:
                    lista = """
\033[1;31m==================================\033[0m
\033[1;32m|         Lista Contas           |\033[0m
\033[1;31m==================================\033[0m
"""
                    print(lista)

                    print(
                        f"Nome: {ueu['nome']},\nCPF: {ueu['cpf']},\nAgência: {ueu['Agência']},\nConta: {ueu['Conta']}"
                    )
                    print("¤" * 20)  # Depuração
        elif opcao == "u":
            cadastro_usuario(usuarios)

        elif opcao == "c":
            conta = nova_conta(numero_conta=numero_conta, usuarios=usuarios)
            contas.append(conta)
            numero_conta += 1

        elif opcao == "q":
            break

        else:
            print(
                "❌❌❌❌   Operação inválida, por favor selecione novamente a opção desejada ❌❌❌❌"
            )


mestre()
