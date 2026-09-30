'''Declaração de variaveis e entrada do tipo real'''
vlrReais = float(input('Quantos Reais você tem na carteira?'))
dolar = float(input('Quanto está o dolar atualmente?'))
'''Conversão de reais para dolar'''
vlrDolar = vlrReais / dolar

print('O valor convertido para dolar é: {}'.format(vlrDolar))
