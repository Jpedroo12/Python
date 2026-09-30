'''Declaração da unida de medida(Metro)'''
medida = int(input('Digite a medida em metros:'))
'''Tranforma metros em centímetros'''
cent = medida * 100
'''Transforma metros em milimetros'''
mili = medida * 1000
'''apresenta o valor de metro em milímetros e centímetros, '''
print('a conversão para centímetros é: {}\n a conversão para milímetros é: {}'. format(cent, mili))
'''\n quebra a linha de apresentação'''