import random
from time import sleep
NumComputador = random.randint(0,5)
NumJogador = int(input('Tente adivinhar o numero que o Computador pensou:'))
print('Processando...')
sleep(3)
if NumComputador == NumJogador:
    print('Você Acertou o numero!!!')
else:
    print('Você Errou o numero!!!,\n o numero era: {}'.format(NumComputador))


