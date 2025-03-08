for tabuada in range( 0 , 60 , 2):
    print(tabuada, end=' - ')
    # repita tabuada começando do 0 até 60 de 2 em 2
    
    # while (repita até...)
    
    sair = -1
    
while sair !=0:
    sair = int(input('\nDigite a opção desejada:\n[1] sacar \n[2] extrato \n[0] sair \n: '))
    
    if sair == 1:
        print(' sacando...')
    elif sair == 2 :
        print('exibindo extrato...')
    elif sair >= 3:
        print('ERRO digite opçao valida')
else:
    print ('obrigado por tudo')