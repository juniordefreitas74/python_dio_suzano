saldo = 1000
saque = 200
limite = 100
conta_especial = True


tela= saldo >= saque and saque <= limite
print(tela) 
tela= saldo >= saque or saque <= limite
print(tela) 
tela= saldo >= saque and saque <= limite
print(not tela) 