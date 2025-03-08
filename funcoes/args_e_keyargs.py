def mini_carta(data,*texto_carta,**ass_agradecimento):
    texto = '\n'.join(texto_carta)
    meta_dados= '\n'.join ([f'{chave.title()}:{valor.title()}' for chave,valor in ass_agradecimento.items()])
    mensagem= f'\n\n{data}\n\n{texto}\n\n{meta_dados}\n\n'
    print(mensagem) 

'''
Defini a funçao mini_carta passei 3 parametros  1 normal 2 um args 3 kwargs
onde o 1 é normal o segundo vai até chegar o kwargs que precisa de chave e valor para rodar
a vriavel texto recebe um quebralinha o .join junta palavras ou textos separados por virgula
nesse caso a cada virgula após final da string do texto_carta ele quebra linha

'''
mini_carta(
    'Sexta, 07 de março de 2025',
    'Boa noite',
    'espero que todos estejam bem,',
    'venho por meio dessa carta,',
    'desejar à todos um ótimo fim de semana.',
    ps= 'Obrigado',
    pss= 'Obrigado',
    ass= 'junior de freitas',
    asss= 'junior de freitas',
)