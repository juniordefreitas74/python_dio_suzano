from datetime import (
    datetime,
)  ## Importa a classe datetime para manipulação de datas e horas
from abc import (
    ABC,
    abstractmethod,
)  ## Importa as classes ABC e abstractmethod para definir classes abstratas


class Cliente:  ## Representa um cliente do banco
    def __init__(self, endereco):  ## Inicializa o cliente com um endereço
        self.endereco = endereco  ## Atributo de endereço do cliente
        self.contas = []  ## Lista de contas do cliente

    def realizar_transacao(
        self, conta, transacao
    ):  # ## Realiza uma transação em uma conta
        transacao.registrar(conta)  ## Registra a transação na conta

    def adicionar_conta(
        self, conta
    ):  ## Adiciona uma conta à lista de contas do cliente
        self.contas.append(conta)  ## Adiciona a conta à lista de contas do cliente


class Pessoa_fisica(Cliente):

    def __init__(
        self, nome, cpf, data_nasc, endereco
    ):  ## Inicializa a pessoa física com nome, CPF, data de nascimento e endereço
        super().__init__(endereco)  ## Chama o construtor da classe pai (Cliente)
        self.nome = nome
        self.cpf = cpf
        self.data_nasc = data_nasc


class Conta:  ## Representa uma conta bancária
    def __init__(self, numero_conta, cliente):
        self.saldo = 0  ## Inicializa o saldo da conta como 0
        self.numero_conta = numero_conta  ## Atributo de número da conta
        self.agencia = "0001"  ## Atributo de agência da conta
        self.cliente = cliente  ## Atributo de cliente associado à conta
        self.historico = Historico()  ## Inicializa o histórico de transações da conta

    def nova_conta(self, cliente, numero_conta):
        return Conta(
            numero_conta, cliente
        )  ## Cria uma nova conta para o cliente com um número de conta específico

    def saldo(self):
        return self.saldo  ## Retorna o saldo da conta

    def agencia(self):  ## Retorna o número da agência da conta
        return self.agencia

    def cliente(self):
        return self.cliente  ## Retorna o cliente associado à conta

    def numero_conta(self):  ## Retorna o número da conta
        return self.numero_conta  ## Retorna o número da conta

    def historico(self):
        return self.historico  ## Retorna o histórico de transações da conta

    def sacar(self, valor):
        saldo = self.saldo  ## Obtém o saldo atual da conta
        excedeu_saldo = (
            valor > saldo
        )  ## Verifica se o valor a ser sacado excede o saldo
        if excedeu_saldo:
            print(
                "Saldo insuficiente, tente outro valor."
            )  ## Exibe mensagem de erro se o saldo for insuficiente
        elif valor > 0:  ## Verifica se o valor a ser sacado é positivo
            self.saldo -= valor  ## Subtrai o valor do saldo da conta
            print(
                f"Saque de R$ {valor} realizado com sucesso!"
            )  ## Exibe mensagem de sucesso
            return True  ## Retorna True indicando que o saque foi realizado com sucesso
        else:
            print("Valor inválido para saque.")
            return False  ## Exibe mensagem de erro se o valor for inválido

    def depositar(self, valor):
        if valor > 0:  ## Verifica se o valor a ser depositado é positivo
            self.saldo += valor
            print(
                f"Depósito de R$ {valor} realizado com sucesso!"
            )  ## Exibe mensagem de sucesso
            return (
                True  ## Retorna True indicando que o depósito foi realizado com sucesso
            )
        else:
            print(
                "Valor inválido para depósito."
            )  ## Exibe mensagem de erro se o valor for inválido
            return False  ## Retorna False indicando que o depósito não foi realizado com sucesso


class ContaCorrente(Conta):  ## Representa uma conta corrente
    def __init__(self, numero_conta, cliente, limite=500, limite_saques=3):
        super().__init__(numero_conta, cliente)
        self.limite = limite
        self.limite_saques = limite_saques

    def sacar(self, valor):
        numero_saques = len(
            [
                transacao
                for transacao in self.historico.transacoes
                if transacao["tipo"] == "saque"
            ]  # Verifica o número de saques realizados
        )
        excdeu_limite = (
            valor > self.limite
        )  # Verifica se o valor a ser sacado excede o limite
        excedeu_saques = numero_saques >= self.limite_saques
        if excedeu_limite:
            print("Valor excede o limite de saque.")
            return False  # Exibe mensagem de erro se o valor exceder o limite
        elif excedeu_saques:
            print("Número máximo de saques diários atingido.")
            return False  # Exibe mensagem de erro se o número máximo de saques diários for atingido
        else:
            return super().sacar(valor)
        return False  # Retorna False se o saque não for realizado com sucesso

    def __str__(self):
        return f"""
        Agência: {self.agencia}
        C/C: {self.numero_conta}           
        Titular: {self.cliente.nome}
        """


class Historico:

    def __init__(self):
        self.transacoes = []
        ## Inicializa o histórico de transações como uma lista vazia

    def transacoes(self):
        return self.transacoes

    ## Retorna a lista de transações
    def adicionarTransacao(self, transacao):
        self.transacoes.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
                "data": datetime.now().strftime(
                    "%d/%m/%Y %H:%M:%S"
                ),  ## Adiciona a data e hora atual à transação
            }
        )
        ## Adiciona uma nova transação ao histórico


class Transacao(ABC):  ## Classe abstrata para transações

    @abstractmethod
    def valor(self):
        pass

    ## Método abstrato para obter o valor da transação
    @abstractmethod
    def registrar(self, conta):
        pass

    ## Método abstrato para registrar a transação em uma conta


class Saque(Transacao):  ## Classe para transação de saque

    def __init__(self, valor):
        self.valor = valor  ## Inicializa o valor do saque

    def registrar(self, conta):
        conta.sacar(self.valor)  ## Registra o saque na conta
        conta.historico.adicionarTransacao(
            self
        )  ## Adiciona a transação ao histórico da conta
        ## Adiciona a transação ao histórico da conta

    def valor(self):
        return self.valor

    ## Retorna o valor do saque


class Deposito(Transacao):  ## Classe para transação de depósito

    def __init__(self, valor):
        self.valor = valor  ## Inicializa o valor do depósito

    def registrar(self, conta):
        conta.depositar(self.valor)  ## Registra o depósito na conta
        conta.historico.adicionarTransacao(
            self
        )  ## Adiciona a transação ao histórico da conta

    def valor(self):
        return self.valor

    ## Retorna o valor do depósito
