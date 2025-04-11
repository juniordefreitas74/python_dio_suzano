import textwrap
from abc import ABC, abstractmethod
from datetime import datetime


# Classe Cliente: Representa um cliente do banco
class Cliente:
    def __init__(self, endereco):
        # Inicializa o cliente com um endereço e uma lista vazia de contas
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self, conta, transacao):
        # Realiza uma transação em uma conta específica
        # A lógica de sucesso/falha e registro no histórico é feita dentro de transacao.registrar
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        # Adiciona uma conta à lista de contas do cliente
        self.contas.append(conta)


# Classe PessoaFisica: Herda de Cliente, representa um cliente pessoa física
class PessoaFisica(
    Cliente
):  # Corrigido: Nome da classe segue padrão CamelCase (Pessoa_fisica -> PessoaFisica)
    def __init__(self, nome, cpf, data_nasc, endereco):
        # Inicializa a pessoa física com nome, CPF, data de nascimento e endereço
        super().__init__(endereco)  # Chama o construtor da classe pai (Cliente)
        self.nome = nome
        self.cpf = cpf
        self.data_nasc = data_nasc


# Classe Conta: Representa uma conta bancária genérica
class Conta:
    def __init__(self, numero_conta, cliente):
        # Inicializa os atributos básicos da conta
        self._saldo = 0  # Atributo protegido por convenção (_)
        self._numero_conta = numero_conta
        self._agencia = "0001"  # Agência padrão
        self._cliente = cliente
        self._historico = Historico()  # Cria um histórico para a conta

    # Getters usando @property para acesso mais Pythonico
    @property
    def saldo(self):
        return self._saldo

    @property
    def numero_conta(self):
        return self._numero_conta

    @property
    def agencia(self):
        return self._agencia

    @property
    def cliente(self):
        return self._cliente

    @property
    def historico(self):
        return self._historico

    # Método de classe para criar nova conta (embora não usado diretamente no fluxo principal)
    @classmethod
    def nova_conta(cls, cliente, numero_conta):
        # Retorna uma nova instância da classe Conta (ou subclasses, se chamado a partir delas)
        return cls(numero_conta, cliente)

    def sacar(self, valor):
        # Lógica de saque básico
        saldo = self.saldo  # Usa o getter @property
        excedeu_saldo = valor > saldo

        if excedeu_saldo:
            print("\n@@@ Operação falhou! Saldo insuficiente. @@@")
        elif valor > 0:
            self._saldo -= valor  # Modifica o atributo protegido
            print("\n=== Saque realizado com sucesso! ===")
            return True  # Indica sucesso
        else:
            print("\n@@@ Operação falhou! O valor informado é inválido. @@@")

        return False  # Indica falha

    def depositar(self, valor):
        # Lógica de depósito básico
        if valor > 0:
            self._saldo += valor  # Modifica o atributo protegido
            print("\n=== Depósito realizado com sucesso! ===")
            return True  # Indica sucesso
        else:
            print("\n@@@ Operação falhou! O valor informado é inválido. @@@")
            return False  # Indica falha


# Classe ContaCorrente: Herda de Conta, com regras específicas de conta corrente
class ContaCorrente(Conta):
    def __init__(self, numero_conta, cliente, limite=500, limite_saques=3):
        # Inicializa a conta corrente, chamando o construtor da classe pai
        super().__init__(numero_conta, cliente)
        self._limite = limite  # Atributo protegido
        self._limite_saques = limite_saques  # Atributo protegido

    # Getters para atributos específicos de ContaCorrente
    @property
    def limite(self):
        return self._limite

    @property
    def limite_saques(self):
        return self._limite_saques

    def sacar(self, valor):
        # Lógica de saque específica para conta corrente (limites)
        # Conta transações de saque no histórico
        numero_saques = len(
            [
                transacao
                for transacao in self.historico.transacoes  # Acessa a lista de transações do histórico
                if transacao["tipo"]
                == Saque.__name__  # Compara com o nome da classe Saque
            ]
        )

        excedeu_limite_valor = valor > self.limite
        excedeu_limite_saques = numero_saques >= self.limite_saques

        if excedeu_limite_valor:
            print(
                f"\n@@@ Operação falhou! O valor do saque (R$ {valor:.2f}) excede o limite de R$ {self.limite:.2f}. @@@"
            )
        elif excedeu_limite_saques:
            print(
                f"\n@@@ Operação falhou! Número máximo de saques ({self.limite_saques}) excedido. @@@"
            )
        else:
            # Se não excedeu os limites específicos, tenta o saque da classe pai (Conta)
            return super().sacar(valor)

        return False  # Indica falha se algum limite foi excedido

    def __str__(self):
        # Representação em string da conta corrente
        return f"""\
            Agência:\t{self.agencia}
            C/C:\t\t{self.numero_conta}
            Titular:\t{self.cliente.nome}
        """


# Classe Historico: Armazena o histórico de transações de uma conta
class Historico:
    def __init__(self):
        # Inicializa a lista de transações (atributo protegido)
        self._transacoes = []

    # Getter para as transações
    @property
    def transacoes(self):
        return self._transacoes

    def adicionar_transacao(self, transacao):
        # Adiciona uma transação formatada ao histórico
        self._transacoes.append(
            {
                "tipo": transacao.__class__.__name__,  # Nome da classe da transação (Saque, Deposito)
                "valor": transacao.valor,
                "data": datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
            }
        )


# Classe Abstrata Transacao: Define a interface para transações
class Transacao(ABC):
    # Propriedade abstrata para o valor da transação
    @property
    @abstractmethod
    def valor(self):
        pass

    # Método abstrato para registrar a transação na conta
    @abstractmethod
    def registrar(self, conta):
        pass


# Classe Saque: Herda de Transacao, representa um saque
class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor  # Atributo protegido

    # Implementa a propriedade abstrata valor
    @property
    def valor(self):
        return self._valor

    # Implementa o método abstrato registrar
    def registrar(self, conta):
        # Tenta realizar o saque na conta
        sucesso_transacao = conta.sacar(self.valor)

        # Se o saque foi bem-sucedido, registra no histórico
        if sucesso_transacao:
            conta.historico.adicionar_transacao(
                self
            )  # Chama o método correto do histórico


# Classe Deposito: Herda de Transacao, representa um depósito
class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor  # Atributo protegido

    # Implementa a propriedade abstrata valor
    @property
    def valor(self):
        return self._valor

    # Implementa o método abstrato registrar
    def registrar(self, conta):
        # Tenta realizar o depósito na conta
        sucesso_transacao = conta.depositar(self.valor)

        # Se o depósito foi bem-sucedido, registra no histórico
        if sucesso_transacao:
            conta.historico.adicionar_transacao(
                self
            )  # Chama o método correto do histórico


# --- Funções Auxiliares ---


def menu():
    # Exibe o menu e retorna a opção do usuário em minúsculo
    menu_texto = """
    ================ MENU ================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova Conta
    [lc]\tListar Contas
    [nu]\tNovo Usuário
    [q]\tSair
    => """
    return input(textwrap.dedent(menu_texto)).lower()


def filtrar_cliente(cpf, clientes):
    # Busca um cliente na lista pelo CPF
    clientes_filtrados = [cliente for cliente in clientes if cliente.cpf == cpf]
    return clientes_filtrados[0] if clientes_filtrados else None


def recuperar_conta_cliente(cliente):
    # Recupera a *primeira* conta do cliente (pode precisar de lógica mais complexa se houver múltiplas contas)
    if not cliente.contas:
        print("\n@@@ Cliente não possui conta! @@@")
        return None
    # FIXME: Assume que o cliente tem apenas uma conta ou opera sempre na primeira.
    return cliente.contas[0]


def depositar(clientes):
    # Função para orquestrar a operação de depósito
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\n@@@ Cliente não encontrado! @@@")
        return

    try:
        valor = float(input("Informe o valor do depósito: "))
    except ValueError:
        print("\n@@@ Valor inválido! Digite um número. @@@")
        return

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return  # Mensagem de erro já foi dada em recuperar_conta_cliente

    transacao = Deposito(valor)
    cliente.realizar_transacao(conta, transacao)


def sacar(clientes):
    # Função para orquestrar a operação de saque
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\n@@@ Cliente não encontrado! @@@")
        return

    try:
        valor = float(input("Informe o valor do saque: "))
    except ValueError:
        print("\n@@@ Valor inválido! Digite um número. @@@")
        return

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return  # Mensagem de erro já foi dada em recuperar_conta_cliente

    transacao = Saque(valor)
    cliente.realizar_transacao(
        conta, transacao
    )  # A lógica de limites e registro está encapsulada


def exibir_extrato(clientes):
    # Função para exibir o extrato de um cliente
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\n@@@ Cliente não encontrado! @@@")
        return

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return

    print("\n================ EXTRATO ================")
    transacoes = conta.historico.transacoes  # Usa o getter @property

    if not transacoes:
        print("Não foram realizadas movimentações.")
    else:
        for transacao in transacoes:
            # Formata a saída de cada transação
            print(
                f"{transacao['data']}\t{transacao['tipo']:<10}\tR$ {transacao['valor']:.2f}"
            )  # {:<10} alinha o tipo à esquerda

    print(f"\nSaldo:\t\tR$ {conta.saldo:.2f}")  # Usa o getter @property
    print("==========================================")


def criar_cliente(
    clientes,
):  # Renomeado de criar_usuario para criar_cliente para consistência
    # Função para criar um novo cliente (PessoaFisica)
    cpf = input("Informe o CPF (somente número): ")
    cliente = filtrar_cliente(cpf, clientes)

    if cliente:
        print("\n@@@ Já existe cliente com esse CPF! @@@")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input(
        "Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): "
    )

    novo_cliente = PessoaFisica(
        nome=nome, cpf=cpf, data_nasc=data_nascimento, endereco=endereco
    )
    clientes.append(novo_cliente)

    print("\n=== Cliente criado com sucesso! ===")


def criar_conta(numero_conta, clientes, contas):
    # Função para criar uma nova conta corrente
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\n@@@ Cliente não encontrado, fluxo encerrado! @@@")
        return

    # Cria a conta corrente e associa ao cliente
    conta = ContaCorrente.nova_conta(
        cliente=cliente, numero_conta=numero_conta
    )  # Usa o método de classe
    contas.append(conta)
    cliente.adicionar_conta(conta)  # Adiciona a referência da conta no cliente

    print("\n=== Conta criada com sucesso! ===")
    print(f"Agência: {conta.agencia}, Conta: {conta.numero_conta}")


def listar_contas(contas):
    # Função para listar todas as contas criadas
    if not contas:
        print("\n@@@ Nenhuma conta cadastrada. @@@")
        return

    print("\n================ LISTA DE CONTAS ================")
    for conta in contas:
        print(textwrap.indent(str(conta), " " * 4))  # Usa o __str__ da conta e indenta
    print("=================================================")


# --- Função Principal ---


def main():
    clientes = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "d":
            depositar(clientes)
        elif opcao == "s":
            sacar(clientes)
        elif opcao == "e":
            exibir_extrato(clientes)
        elif opcao == "nu":
            criar_cliente(clientes)  # Chama a função renomeada
        elif opcao == "nc":
            # Gera um número de conta sequencial simples
            numero_conta = len(contas) + 1
            criar_conta(numero_conta, clientes, contas)
        elif opcao == "lc":
            listar_contas(contas)
        elif opcao == "q":
            print("\nSaindo do sistema... Obrigado por usar nossos serviços!")
            break
        else:
            print(
                "\n@@@ Operação inválida, por favor selecione novamente a operação desejada. @@@"
            )


# Executa o programa principal
if __name__ == "__main__":
    main()
