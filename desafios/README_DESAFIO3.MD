# Sistema Bancário Simples em Python

Este projeto é uma simulação de um sistema bancário básico desenvolvido em Python. Ele utiliza conceitos de Programação Orientada a Objetos (POO) para modelar clientes, contas (corrente) e transações (depósito, saque). A interação com o sistema é feita através de um menu de texto no console.

## Funcionalidades

O sistema oferece as seguintes operações através de um menu interativo:

*   **[d] Depositar:** Realizar depósitos em contas existentes de clientes.
*   **[s] Sacar:** Realizar saques de contas existentes, respeitando:
    *   Saldo disponível na conta.
    *   Limite de valor por saque (R$ 500,00 para Conta Corrente).
    *   Limite de quantidade de saques diários (3 saques para Conta Corrente).
*   **[e] Extrato:** Exibir o histórico de transações (depósitos e saques) e o saldo atual da conta de um cliente.
*   **[nc] Nova Conta:** Criar uma nova conta corrente para um cliente já cadastrado no sistema. O número da conta é gerado sequencialmente.
*   **[lc] Listar Contas:** Exibir uma lista de todas as contas correntes criadas no sistema, mostrando agência, número da conta e nome do titular.
*   **[nu] Novo Usuário:** Cadastrar um novo cliente (Pessoa Física) no sistema, solicitando nome, CPF, data de nascimento e endereço. O sistema valida se o CPF já existe.
*   **[q] Sair:** Encerrar a execução do programa.

## Tecnologias Utilizadas

*   Python 3.x
*   Módulos Python padrão: `textwrap`, `abc`, `datetime`.

## Como Executar

1.  **Pré-requisitos:** Certifique-se de ter o Python 3 instalado em seu sistema.
2.  **Salvar o Código:** Salve o código Python fornecido em um arquivo com a extensão `.py` (por exemplo, `sistema_bancario.py`).
3.  **Abrir Terminal:** Abra um terminal ou prompt de comando.
4.  **Navegar até o Diretório:** Use o comando `cd` para navegar até o diretório onde você salvou o arquivo `sistema_bancario.py`.
5.  **Executar:** Execute o script Python com o comando:
    ```bash
    python sistema_bancario.py
    ```
6.  **Interagir:** O menu principal será exibido no terminal. Siga as instruções e digite a letra correspondente à opção desejada para interagir com o sistema.

## Estrutura do Projeto (Classes Principais)

*   **`Cliente`**: Classe base para clientes, armazena endereço e uma lista das contas associadas. Contém métodos para adicionar contas e realizar transações.
*   **`PessoaFisica(Cliente)`**: Representa um cliente pessoa física, herdando de `Cliente` e adicionando atributos como nome, CPF e data de nascimento.
*   **`Conta`**: Classe base para contas bancárias. Possui atributos como saldo, número da conta, agência (fixa "0001"), cliente associado e um objeto `Historico`. Implementa a lógica básica de `sacar` e `depositar`. Utiliza propriedades (`@property`) para acesso controlado aos atributos.
*   **`ContaCorrente(Conta)`**: Especialização de `Conta` para contas correntes. Adiciona atributos de `limite` por saque e `limite_saques` diários. Sobrescreve o método `sacar` para implementar essas regras específicas antes de chamar o método da classe pai.
*   **`Historico`**: Armazena uma lista (`_transacoes`) de todas as transações realizadas em uma conta. Possui um método `adicionar_transacao`.
*   **`Transacao` (ABC)**: Classe abstrata que define a interface para todas as transações, exigindo a implementação da propriedade `valor` e do método `registrar`.
*   **`Saque(Transacao)`**: Classe concreta para transações de saque.
*   **`Deposito(Transacao)`**: Classe concreta para transações de depósito.
*   **Funções Auxiliares**: Funções como `menu()`, `filtrar_cliente()`, `depositar()`, `sacar()`, `exibir_extrato()`, `criar_cliente()`, `criar_conta()`, `listar_contas()` e `main()` orquestram a lógica do programa e a interação com o usuário.

## Possíveis Melhorias Futuras

*   Persistência de dados (salvar e carregar informações de clientes e contas em arquivos ou banco de dados).
*   Suporte a diferentes tipos de conta (ex: Conta Poupança) com regras distintas.
*   Autenticação de usuário (login/senha).
*   Tratamento de erros mais robusto e validação de entradas aprimorada (ex: formato de data, CPF).
*   Permitir que um cliente possua múltiplas contas e possa escolher em qual operar.
*   Implementação de outras operações bancárias (transferências, etc.).
*   Interface gráfica (GUI) em vez de linha de comando.