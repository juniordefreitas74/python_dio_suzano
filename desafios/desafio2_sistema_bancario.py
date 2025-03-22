def menu():
   menu_texto= '''
   ========== MENU ==========
   
        [d]  Depositar
        [s]  sacar
        [e]  Extrato
        [nu] Novo usuário
        [nc] Nova conta
        [q]  Sair
        
   ==========================
   '''
   return input(menu_texto)

def depositar(saldo, valor, extrato,/): # a barra indica que tudo antes dela deve ser posicional
   
   if valor > 0: # se o valor for maior que 0
      saldo += valor # adicione o valor ao saldo
      extrato += f'\n(+) Depósito de: R${valor:.2f}' # adicione a operação ao extrtato
      print (f'Depósito de: R$ {valor:.2f} realizado com sucesso!')
   else:
      print("\n@@@Valor inválido para depósito.@@@")
   return saldo,extrato
      
def sacar(*,saldo, valor, extrato, limite, numero_saques, limite_saques): # o * indica que os argumentos são passados por chave=valor

   if numero_saques <limite_saques:
      
      if valor > 0 and valor <= saldo and valor < limite: #se o valor for maior que 0 e menor ou igual ao saldo
         saldo -= valor #diminua o valor do saldo
         extrato += f'\n(-) Saque de: R$-{valor:.2f}' # adicione a operação ao extrtato
         
         print (f'Saque de: R${valor} feito com sucesso')
      else:
         print("\n@@@ Valor inválido ou saldo insuficiente. @@@")#se o valor for maior que o limite,maior que o saldo emenor que 0
   
   else:print('Número de saques diários excedidos, volte amanhã!') #se o numero de saques for maior que o limite de saques
   return(saldo,extrato)

def cadastro_usuario(usuarios):  # Função para cadastrar um novo usuário na lista
    cpf = input('Digite o CPF: (somente números): ')  # Solicita o CPF do usuário

    usuario = filtro_usuario(cpf, usuarios)  # Verifica se o CPF já existe na lista de usuários
    if usuario:  # Se já existir um usuário com esse CPF
        print('\n@@@ Usuário já cadastrado no banco de dados! @@@')  # Exibe mensagem de erro
        return  # Encerra a função sem cadastrar um novo usuário

    else:  # Se o CPF não estiver cadastrado, continua o processo de cadastro
        nome = input('Digite o nome completo: ')  # Solicita o nome completo do usuário
        data_nasc = input('Digite data de nascimento (dd-mm-aaaa): ')  # Solicita a data de nascimento
        endereco = input('Digite endereço (rua, número - bairro - cidade - ESTADO): ')  # Solicita o endereço

        # Adiciona o usuário à lista, armazenando suas informações em um dicionário
        usuarios.append({
            'nome': nome,
            'cpf': cpf,
            'Data Nascimento': data_nasc,
            'Endereço': endereco
        })

        print('✅ Usuário cadastrado com sucesso! ✅')  # Mensagem de sucesso

def filtro_usuario(cpf, usuarios):  # Função para buscar um usuário na lista pelo CPF
    for usuario in usuarios:  # Percorre a lista de usuários
        if usuario['cpf'] == cpf:  # Se encontrar um usuário com o CPF informado
            return usuario  # Retorna o usuário encontrado
    
  

   

   

def exibir_extrato(saldo,/,*,extrato):
   print("\n====== EXTRATO ======")
   
   print(extrato)
   
   print (f'\n⩸⩸⩸⩸ seu saldo atual é de: R$ {saldo:.2f} ⩸⩸⩸⩸')
   
   print("======================")
   return(saldo,extrato)




def mestre():
   LIMITE_SAQUES= 3
   AGENCIA= '0001'
   
   saldo = 0
   limite = 500
   extrato = ''
   saques_info = []
   numero_saques = 0
   usuarios =[]
   contas = []
   
   while True:
      opcao = menu()
      if opcao == 'd':
         valor = float(input('\nDgite o valor do Depósito: R$ '))
         saldo,extrato = depositar(saldo,valor,extrato)
         print (f'\n⩸⩸⩸⩸ seu saldo atual é de: R$ {saldo:.2f} ⩸⩸⩸⩸')
         
      elif opcao == 's':
         valor = float(input('\nDgite o valor do Saque: R$ '))
         saldo, extrato = sacar(saldo=saldo, valor=valor, extrato=extrato,limite=limite,numero_saques=numero_saques,limite_saques=LIMITE_SAQUES)
         print (f'\n⩸⩸⩸⩸ seu saldo atual é de: R$ {saldo:.2f} ⩸⩸⩸⩸')
         numero_saques += 1
         
      elif opcao == 'e':
         saldo,extrato = exibir_extrato(saldo, extrato=extrato,)
         
      elif opcao== 'nu':
         cadastro_usuario(usuarios)
         
         
      
      elif opcao == 'q':
         break
      
      else:
        print('@@@@ Operação inválida, por favor selecione novamente a opção desejada @@@@')

         
      
mestre()