Faturamento  = 1000
custo = 600

novas_vendas = 1200
Faturamento = Faturamento + novas_vendas
print ('faturamento', Faturamento)
print ('custo', custo)

imposto = 0.15 * Faturamento
lucro = Faturamento - custo - imposto

print ('imposto', imposto)
print('lucro', lucro)

mensagem = 'O faturamento da loja foi de 2100'
teve_lucro = True
margem_de_lucro = lucro / Faturamento
print ('Margem', margem_de_lucro)
print (10 % 4)