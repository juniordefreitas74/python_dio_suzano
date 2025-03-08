# Sistema Bancário em Python

Este é um simples sistema bancário desenvolvido em Python, que permite ao usuário realizar operações de **depósito, saque e consulta de extrato**.

## Funcionalidades
- **Depósito**: O usuário pode adicionar valores ao saldo da conta.
- **Saque**: O usuário pode sacar valores da conta, respeitando um limite de R$500,00 por transação e até 3 saques diários.
- **Extrato**: Exibe todas as transações realizadas, incluindo depósitos e saques.
- **Sair**: Encerra o programa.

## Como Utilizar
1. Execute o script Python.
2. Escolha uma das opções no menu:
   - `[d]` Depositar
   - `[s]` Sacar
   - `[e]` Extrato
   - `[q]` Sair
3. Insira os valores conforme solicitado pelo sistema.
4. O programa continuará em execução até que o usuário escolha a opção `[q]` para sair.

## Exemplo de Uso
```bash
======= SISTEMA BANCÁRIO ======
=                             =
=        [d] Depositar        =
=        [s] Sacar            =
=        [e] Extrato          =
=        [q] Sair             =
=                             =
===============================
   DIGITE A OPÇÃO DESEJADA!
> d
Digite o valor de Depósito: 1000
Foi depositado: R$ 1000.00

> s
Digite o valor que deseja sacar: 500
Saque de: R$500.00 efetuado com sucesso.
Seu saldo atual é de: R$500.00

> e
====== EXTRATO ======
Depósito de R$ 1000.00
Saque de R$ 500.00
Saldo total de: R$500.00
=====================

> q
```

## Requisitos
- Python 3 instalado

## Melhorias Futuras
- Implementar autenticação de usuários
- Criar interface gráfica
- Armazenar transações em banco de dados

## Autor
Desenvolvido por **Junior de Freitas**. Qualquer sugestão ou melhoria é bem-vinda!

---

Este README fornece uma visão geral do funcionamento do sistema bancário, ajudando novos usuários a compreender como utilizá-lo. Caso precise de alguma alteração, me avise! 🚀

