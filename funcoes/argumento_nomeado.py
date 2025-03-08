'''Argumento nomeado é aquela função onde devemos passar chave e valor'''

def TiposDeCarro (marca,modelo,ano,placa):
    # salva carro no banco de dados
    print(f'\nCarro inserido com sucesso! {marca} /{modelo} /{ano} / {placa}\n')
    
    
    
TiposDeCarro('fiat', 'Idea', '2014','DTG6524')
TiposDeCarro(marca='Ford',modelo='Fiesta',ano=2018,placa='RFY6512')

TiposDeCarro(**{'marca': 'Wolks', 'modelo': ' T-Cross', 'ano': 2025, 'placa':'FRD3A548'})
