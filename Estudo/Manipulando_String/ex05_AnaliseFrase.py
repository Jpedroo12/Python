frase = str(input('Digite uma frase: \n')).strip().upper()
letra = str(input('Digite a letra que quer analisar: \n')).strip().upper()

print('A letra {} aparece {} vezes na frase.'.format(letra, frase.count(letra)))

print('A primeira ocorrência da letra {} foi na posição {}.'.format(letra, frase.find(letra) + 1))

print('A última ocorrência da letra {} foi na posição {}.'.format(letra, frase.rfind(letra) + 1))


