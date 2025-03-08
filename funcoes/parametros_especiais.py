def somar(a,b):
    return a + b

def resultado_total(a,b, girafa):
    conta = girafa(a,b)
    print (f'o resultado é: {a} + {b} = {conta}')
resultado_total(12,13,somar)